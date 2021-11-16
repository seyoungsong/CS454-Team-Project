# CS454 Team Project

- [Maven](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
- [OpenClover](https://openclover.org/doc/manual/latest/maven--user-guide.html): code coverage
- [sloc](https://github.com/flosse/sloc): simple tool to count SLOC (source lines of code)
- [PIT](http://pitest.org/): generate mutation faults
- [Java Uuid Generator (JUG)](https://github.com/cowtowncoder/java-uuid-generator)

## Prerequisites

- `yarn`

## Install

```bash
# install OpenJDK 11
brew install openjdk@11
sudo ln -sfn $(brew --prefix)/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
java -version # openjdk version "11.0.12"

# install Maven
echo "export JAVA_HOME=$(/usr/libexec/java_home)" >> ~/.zshrc
brew install --ignore-dependencies maven
mvn --version # Apache Maven 3.8.3

# install sloc
yarn global add sloc
sloc --version # 0.2.1
```

- [Configuring Clover's short name in `.m2/settings.xml`](https://openclover.org/doc/manual/latest/maven--basic-usage.html)

If `.m2/settings.xml` file doesn't exist in user home, copy it from maven home.

```bash
mvn --version  # Maven home: /opt/homebrew/Cellar/maven/3.8.3/libexec
cp /opt/homebrew/Cellar/maven/3.8.3/libexec/conf/settings.xml ~/.m2/
```

Open your `.m2/settings.xml` file in vscode.

```
code ~/.m2/settings.xml
```

Before you get started, add this to your `.m2/settings.xml` file so you can reference Clover by its short name `clover`.

```xml
<pluginGroups>
  <pluginGroup>org.openclover</pluginGroup>
</pluginGroups>
```

## Example

```bash
# download example project from github (java-uuid-generator)
git clone --depth 1 --branch java-uuid-generator-4.0.1 https://github.com/cowtowncoder/java-uuid-generator.git
rm -rf java-uuid-generator/.git
cd java-uuid-generator
git init . && git add . && git commit -m "init"

# check maven
mvn clean
mvn test # you may have to remove some lines from the source to disable false alarms.

# check maven single test
mvn -Dtest=EthernetAddressTest#testAsByteArray test

# check java
mvn package
java -cp target/java-uuid-generator-4.0.1.jar com.fasterxml.uuid.Jug r

# check sloc
sloc src/main # SLOC
sloc src/test # TLOC
```

[Installing Clover in pom.xml](https://openclover.org/doc/manual/latest/maven--basic-usage.html)

[Clover Maven Plugin Version](https://search.maven.org/artifact/org.openclover/clover-maven-plugin)

```xml
<plugin>
    <groupId>org.openclover</groupId>
    <artifactId>clover-maven-plugin</artifactId>
    <version>4.4.1</version>
</plugin>
```

```bash
# run clover (you will have to run it twice for the first time)
mvn clean clover:setup test clover:aggregate clover:clover

# copy the folder
cp -R target/site/clover ./clover

# open report in web browser (you can check the time duration of each test)
open target/site/clover/index.html
open clover/index.html  # cd ~/java-uuid-generator
code clover/clover.xml

# run clover for 1 unit test
mvn clean clover:setup -Dtest=UUIDGeneratorTest#testGenerateNameBasedUUIDNameSpaceAndName test clover:aggregate clover:clover

# copy
cp target/site/clover/clover.xml clover_unit.xml
```

## References

[1] Z. Li, M. Harman, and R. M. Hierons, “Search Algorithms for Regression Test Case Prioritization,” IIEEE Trans. Software Eng., vol. 33, no. 4, pp. 225–237, Apr. 2007, doi: 10.1109/TSE.2007.38.

[2] Q. Luo, K. Moran, L. Zhang, and D. Poshyvanyk, “How Do Static and Dynamic Test Case Prioritization Techniques Perform on Modern Software Systems? An Extensive Study on GitHub Projects,” IIEEE Trans. Software Eng., vol. 45, no. 11, pp. 1054–1080, Nov. 2019, doi: 10.1109/TSE.2018.2822270.

[3] J. Zhou, J. Chen, and D. Hao, “Parallel Test Prioritization,” ACM Trans. Softw. Eng. Methodol., vol. 31, no. 1, Sep. 2021, doi: 10.1145/3471906.
