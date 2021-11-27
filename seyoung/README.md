# CS454 Team Project - Data Collection by Seyoung Song

TODO: sort lines with zero padding
TODO: minimum duration: 0.001 / 2

## Linux (Debian)

```bash
# install python (mambaforge)
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh

# install python libs
mamba install pytz slugify tqdm -y

# openjdk 8
# https://adoptium.net/installation.html?variant=openjdk8#x64_linux-jdk
wget https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u312-b07/OpenJDK8U-jdk_x64_linux_hotspot_8u312b07.tar.gz
tar xzf OpenJDK8U-jdk_x64_linux_hotspot_8u312b07.tar.gz
echo 'export PATH="/root/jdk8u312-b07/bin:$PATH"' >> ~/.zshrc
source .zshrc
java -version

# maven
# https://maven.apache.org/download.cgi#files
# https://maven.apache.org/install.html
wget https://dlcdn.apache.org/maven/maven-3/3.8.4/binaries/apache-maven-3.8.4-bin.tar.gz
tar xzvf apache-maven-3.8.4-bin.tar.gz
echo 'export PATH="/root/apache-maven-3.8.4/bin:$PATH"' >> ~/.zshrc
source .zshrc
mvn --version

# yarn
# https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt install yarn -y

# sloc
yarn global add sloc

# screen
apt install screen -y
```

## Dependencies: OpenJDK, Maven, sloc, OpenClover

- [OpenJDK 11](https://adoptium.net/releases.html?variant=openjdk11&jvmVariant=hotspot)
- [Maven](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
  - [Running a Single Test](https://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html)
- [sloc](https://github.com/flosse/sloc)

```bash
# install OpenJDK 8
brew install openjdk@8
sudo ln -sfn $(brew --prefix)/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
java -version # openjdk version "1.8.0_312"

# install Maven
echo "export JAVA_HOME=$(/usr/libexec/java_home)" >> ~/.zshrc
brew install --ignore-dependencies maven
mvn --version # Apache Maven 3.8.4

# install sloc (and yarn)
brew install yarn
yarn --version # 1.22.17
yarn global add sloc
sloc --version # 0.2.1

# copy settings.xml from maven home to user home
mvn --version  # Maven home: /root/apache-maven-3.8.4
mkdir -p ~/.m2
cp /root/apache-maven-3.8.4/conf/settings.xml ~/.m2/
code ~/.m2/settings.xml
# <pluginGroup>org.openclover</pluginGroup>


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

```bash
# download a java program from github
rm -rf repo
git clone --depth 1 --recursive https://github.com/cowtowncoder/java-uuid-generator repo

# make sure maven works
mvn --file repo/pom.xml --fail-never clean test
```

## Run OpenClover

```bash
# run clover, ignoring failures, without generating HTML
mvn --file repo/pom.xml --fail-never -Dmaven.clover.generateHtml=false clean clover:setup test clover:aggregate clover:clover

# copy clover.xml to root
cp repo/target/site/clover/clover.xml ./clover.xml

# identify unit tests from clover.xml and make tests.sh
python identify_tests.py

# run clover for single tests
rm -rf clover
mkdir -p clover
bash tests.sh

# log github url, timestamp, hash
git --git-dir repo/.git config --get remote.origin.url > git.log
git --git-dir repo/.git log -n 1 --format=%ct%n%H >> git.log

# run sloc
sloc --format csv repo > sloc.csv # SLOC

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

## Run

Change `--idx` with respect to [`github_result_sloc.json](./github_result_sloc.json)

```bash
python main.py --idx 22
zsh run.sh

# one line
python main.py --idx 22; clear; zsh run.sh

# all
zsh all.sh
```

```bash
# Start a new named screen session
screen -S aa

# run
zsh all.sh

# Detach
# Ctrl + A, D

screen -ls

# Reattach to an open screen:
screen -r aa

# Kill
# Ctrl + A, K
```
