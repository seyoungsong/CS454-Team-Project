# CS454 Team Project - Data Collection by Seyoung Song

## Dependencies: OpenJDK, Maven, sloc, OpenClover

- [OpenJDK 11](https://adoptium.net/releases.html?variant=openjdk11&jvmVariant=hotspot)
- [Maven](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
  - [Running a Single Test](https://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html)
- [sloc](https://github.com/flosse/sloc)

```bash
# install OpenJDK 11
brew install openjdk@11
sudo ln -sfn $(brew --prefix)/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
java -version # openjdk version "11.0.12"

# install Maven
echo "export JAVA_HOME=$(/usr/libexec/java_home)" >> ~/.zshrc
brew install --ignore-dependencies maven
mvn --version # Apache Maven 3.8.4

# install sloc (and yarn)
brew install yarn
yarn --version # 1.22.17
yarn global add sloc
sloc --version # 0.2.1
```

- [OpenClover for Maven: User's Guide](https://openclover.org/doc/manual/latest/maven--user-guide.html)
  - [Configuring Clover's short name in `.m2/settings.xml`](https://openclover.org/doc/manual/latest/maven--basic-usage.html)

```bash
# copy settings.xml from maven home to user home
mvn --version  # Maven home: /opt/homebrew/Cellar/maven/3.8.4/libexec
mkdir -p ~/.m2
cp /opt/homebrew/Cellar/maven/3.8.4/libexec/conf/settings.xml ~/.m2/

# open `~/.m2/settings.xml` file in vscode.
code ~/.m2/settings.xml
```

```xml
<pluginGroups>
  <pluginGroup>org.openclover</pluginGroup>
</pluginGroups>
```

## Clone the subject repository from GitHub

- [Search GitHub](https://github.com/search)

TODO: git clone latest tag

```bash
# download a java program from github
rm -rf repo
git clone --depth 1 --recursive https://github.com/cowtowncoder/java-uuid-generator repo
rm -rf repo/.git

# make sure maven works
mvn --file repo/pom.xml --fail-never clean test

# run sloc
sloc --format cli-table repo > sloc.txt # SLOC
```

## Run OpenClover

```bash
# run clover, ignoring failures, without generating HTML
mvn --file repo/pom.xml --fail-never -Dmaven.clover.generateHtml=false clean clover:setup test clover:aggregate clover:clover

# copy clover.xml to root
cp repo/target/site/clover/clover.xml ./clover.xml

# identify unit tests from clover.xml and make commands.sh
python identify_tests.py

# run clover for single tests
rm -rf clover
mkdir -p clover
bash commands.sh

# parse xml files to make data.json
python parse_data.py
```

## Extra

```bash
git clone --depth 1 --recursive https://github.com/rometools/rome repo

# full clover
mvn --file repo/pom.xml --fail-never clean clover:setup test clover:aggregate clover:clover

# (option) open report in web browser
open repo/target/site/clover/index.html
code repo/target/site/clover/clover.xml

# to run clover for 1 unit test
mvn --file repo/pom.xml clean clover:setup -Dtest=com.rometools.certiorem.hub.ControllerTest#testSubscribe test clover:aggregate clover:clover -Dmaven.clover.generateHtml=false --fail-never

# copy (unit) clover.xml to clover dir
mkdir -p ./clover
cp repo/target/site/clover/clover.xml ./clover/clover#com.rometools.certiorem.hub#ControllerTest#testSubscribe.xml
```
