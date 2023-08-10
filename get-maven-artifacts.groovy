import org.joda.time.DateTime
import org.sonatype.nexus.common.collect.DetachingMap
import org.sonatype.nexus.repository.storage.Asset
import org.sonatype.nexus.repository.storage.Query
import org.sonatype.nexus.repository.storage.StorageFacet
import org.sonatype.nexus.repository.storage.StorageTx

import groovy.json.JsonBuilder
import groovy.json.JsonSlurper

class MavenArtifact {
	String group
	String id
	String specificVersion
	String baseVersion
	DateTime lastUpdated
	List<MavenArtifactAsset> assets = new ArrayList<MavenArtifactAsset>()
	
	String specificGav() {
		"${group}:${id}:${specificVersion}"
	}
	String baseGav() {
		"${group}:${id}:${baseVersion}"
	}
}
class MavenArtifactAsset {
	String path
	String fileExtension
	String classifier
}

def request = new JsonSlurper().parseText(args)
assert request.repoName: 'repoName parameter is required'
assert request.groupId: 'groupId parameter is required'
assert request.artifactId: 'artifactId parameter is required'
assert request.startDate: 'startDate parameter is required, format: yyyy-mm-dd'

log.info("Asset query: repoName=${request.repoName}, groupId=${request.groupId}, artifactId=${request.artifactId}, startDate=${request.startDate}")

def repo = repository.repositoryManager.get(request.repoName)
StorageFacet storageFacet = repo.facet(StorageFacet)
StorageTx tx = storageFacet.txSupplier().get()


List<Asset> allAssets = new ArrayList<Asset>()
try {
    tx.begin()
	
	// the following URL was extremely helpful for query building: https://github.com/sonatype/nexus-public/blob/a6a8abcdcba3fd1947884f05f913d0da6939261c/plugins/nexus-repository-maven/src/main/java/org/sonatype/nexus/repository/maven/internal/MavenIndexPublisher.java#L100
    Iterable<Asset> results = tx.findAssets(
		Query.builder()
			.where('component.group').eq(request.groupId)
			.and('component.name').eq(request.artifactId)
			.and('blob_created > ').param(request.startDate)
		.build(), [repo])
	
	results.each {
		allAssets.add(it)
	}
} finally {
    tx.close()
}

Map<String, MavenArtifact> artifactsBySpecificVersion = new HashMap<String, MavenArtifact>()
log.info("${allAssets.size()} total assets found")

allAssets.each {
	def mavenProps = it.attributes().get("maven2")
	if (mavenProps) {
		log.debug("${it.name()}")
		DetachingMap mavenPropMap = mavenProps.asType(DetachingMap)
		/*
		mavenPropMap.each { mavenProp ->
			log.info("\t${mavenProp.getKey()}: ${mavenProp.getValue()} (${mavenProp.getValue().getClass().getSimpleName()})")
		}
		*/
		
		MavenArtifact ma = new MavenArtifact()
		ma.group = mavenPropMap.get("groupId")
		ma.id = mavenPropMap.get("artifactId")
		ma.specificVersion = mavenPropMap.get("version")
		ma.baseVersion = mavenPropMap.get("baseVersion")
		ma.lastUpdated = it.blobCreated()
		if (!artifactsBySpecificVersion.containsKey(ma.specificGav())) {
			artifactsBySpecificVersion.put(ma.specificGav(), ma)
		}
		List<MavenArtifactAsset> artifactAssets = artifactsBySpecificVersion.get(ma.specificGav()).assets
		MavenArtifactAsset maa = new MavenArtifactAsset()
		maa.path = "/repository/${repo.name}/${it.name()}"
		maa.fileExtension = mavenPropMap.get("extension")
		maa.classifier = mavenPropMap.get("classifier")
		artifactAssets.add(maa)
	} else {
		log.warn("no maven props found for ${it.name()}")
	}
}

List<MavenArtifact> specificVersionArtifacts = new ArrayList<MavenArtifact>(artifactsBySpecificVersion.values())
log.info("${specificVersionArtifacts.size()} total artifacts found")

specificVersionArtifacts.each {
	log.debug("\t${it.specificGav()} has ${it.assets.size()} assets")
}

specificVersionArtifacts.sort { a, b -> b.lastUpdated <=> a.lastUpdated } // sort by last updated descending

log.debug("after sorting:")
specificVersionArtifacts.each {
	log.debug("\t${it.specificGav()} has ${it.assets.size()} assets")
}

log.debug("removing snapshot artifacts")
Map<String, MavenArtifact> artifactsByBaseVersion = new HashMap<String, MavenArtifact>()
specificVersionArtifacts.each {
	// since list is ordered, only keep first (AKA most recent) artifact for same base version. this removes any old 'snapshot' artifacts
	if (!artifactsByBaseVersion.containsKey(it.baseGav())) {
		artifactsByBaseVersion.put(it.baseGav(), it)
	}
}

List<MavenArtifact> baseVersionArtifacts = new ArrayList<MavenArtifact>(artifactsByBaseVersion.values())
baseVersionArtifacts.sort { a, b -> b.lastUpdated <=> a.lastUpdated } // sort by last updated descending
log.info("${baseVersionArtifacts.size()} unique artifacts found")

baseVersionArtifacts.each {
	log.debug("\t${it.specificGav()} has ${it.assets.size()} assets")
}

JsonBuilder jsonBuilder = new JsonBuilder()

jsonBuilder(
	baseVersionArtifacts.collect {
		[
			groupId: it.group,
			artifactId: it.id,
			version: it.baseVersion,
			updated: it.lastUpdated.toString(),
			files: it.assets
		]
	}
)

return jsonBuilder.toString()
