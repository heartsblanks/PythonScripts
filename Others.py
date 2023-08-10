<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-project</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <!-- Other properties -->
        <os.detected>${os.detected.classifier}</os.detected>
        <JCN_HOME_WINDOWS>C:\path\to\ACE\library</JCN_HOME_WINDOWS>
        <JCN_HOME_LINUX>/path/to/ACE/library</JCN_HOME_LINUX>

        <JCN_HOME>
            <if>
                <condition>
                    <equals arg1="${os.detected}" arg2="windows"/>
                </condition>
                <then>${JCN_HOME_WINDOWS}</then>
                <else>${JCN_HOME_LINUX}</else>
            </if>
        </JCN_HOME>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>kr.motd.maven</groupId>
                <artifactId>os-maven-plugin</artifactId>
                <version>1.6.2</version>
                <executions>
                    <execution>
                        <phase>initialize</phase>
                        <goals>
                            <goal>detect</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <dependencies>
        <!-- Other dependencies -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>your-ace-related-artifact</artifactId>
            <version>1.0</version>
            <scope>system</scope>
            <systemPath>${JCN_HOME}/your-ace-library.jar</systemPath>
        </dependency>
    </dependencies>
</project>