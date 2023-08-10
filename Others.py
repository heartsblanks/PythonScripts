import requests
from datetime import datetime
import json

class MavenArtifact:
    def __init__(self):
        self.group = None
        self.id = None
        self.specificVersion = None
        self.baseVersion = None
        self.lastUpdated = None
        self.assets = []

class MavenArtifactAsset:
    def __init__(self):
        self.path = None
        self.fileExtension = None
        self.classifier = None

def fetch_artifacts(repo_name, group_id, artifact_id, start_date):
    url = f"https://your.repository.url/api/v1/components?repository={repo_name}&group={group_id}&name={artifact_id}&version=&format=maven2"

    response = requests.get(url)
    response_json = response.json()

    artifacts = {}
    for asset in response_json:
        if "maven2" in asset["format"]:
            maven_props = asset["format"]["maven2"]
            artifact = MavenArtifact()
            artifact.group = maven_props.get("groupId")
            artifact.id = maven_props.get("artifactId")
            artifact.specificVersion = maven_props.get("version")
            artifact.baseVersion = maven_props.get("baseVersion")
            artifact.lastUpdated = datetime.strptime(asset["created"], "%Y-%m-%dT%H:%M:%S.%fZ")

            artifact_asset = MavenArtifactAsset()
            artifact_asset.path = f"/repository/{repo_name}/{asset['name']}"
            artifact_asset.fileExtension = maven_props.get("extension")
            artifact_asset.classifier = maven_props.get("classifier")
            artifact.assets.append(artifact_asset)

            artifacts[artifact.specificVersion] = artifact

    sorted_artifacts = sorted(artifacts.values(), key=lambda x: x.lastUpdated, reverse=True)
    return sorted_artifacts

repo_name = "your_repo_name"
group_id = "your_group_id"
artifact_id = "your_artifact_id"
start_date = "yyyy-mm-dd"

specific_version_artifacts = fetch_artifacts(repo_name, group_id, artifact_id, start_date)

result = []
for artifact in specific_version_artifacts:
    result.append({
        "groupId": artifact.group,
        "artifactId": artifact.id,
        "version": artifact.baseVersion,
        "updated": artifact.lastUpdated.isoformat(),
        "files": [{
            "path": asset.path,
            "fileExtension": asset.fileExtension,
            "classifier": asset.classifier
        } for asset in artifact.assets]
    })

json_output = json.dumps(result, indent=4)
print(json_output)