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
```

## Usage

```bash
git clone --depth 1 --branch java-uuid-generator-4.0.1 https://github.com/cowtowncoder/java-uuid-generator.git
mvn clean
mvn test
mvn package
java -cp target/java-uuid-generator-4.0.1.jar com.fasterxml.uuid.Jug r

sloc src/main # SLOC
sloc src/test # TLOC

cp /opt/homebrew/Cellar/maven/3.8.3/libexec/conf/settings.xml ~/.m2/
code ~/.m2/settings.xml
mvn clean clover:setup test clover:aggregate clover:clover
mvn -Dtest=EthernetAddressTest test
mvn -Dtest=EthernetAddressTest#testAsByteArray test

mvn clean clover:setup -Dtest=EthernetAddressTest#testAsByteArray test clover:aggregate clover:clover
```

```xml
<plugin>
  <groupId>com.atlassian.maven.plugins</groupId>
  <artifactId>clover-maven-plugin</artifactId>
  <version>4.1.2</version>
</plugin>
```

## References

[1] Z. Li, M. Harman, and R. M. Hierons, “Search Algorithms for Regression Test Case Prioritization,” IIEEE Trans. Software Eng., vol. 33, no. 4, pp. 225–237, Apr. 2007, doi: 10.1109/TSE.2007.38.

[2] Q. Luo, K. Moran, L. Zhang, and D. Poshyvanyk, “How Do Static and Dynamic Test Case Prioritization Techniques Perform on Modern Software Systems? An Extensive Study on GitHub Projects,” IIEEE Trans. Software Eng., vol. 45, no. 11, pp. 1054–1080, Nov. 2019, doi: 10.1109/TSE.2018.2822270.

[3] J. Zhou, J. Chen, and D. Hao, “Parallel Test Prioritization,” ACM Trans. Softw. Eng. Methodol., vol. 31, no. 1, Sep. 2021, doi: 10.1145/3471906.
