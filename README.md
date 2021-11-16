# CS454 Team Project

- [Maven](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
- [JUnit](https://junit.org/junit5/): testing framework
- [PIT](http://pitest.org/): generate mutation faults
- [Clover](https://bitbucket.org/atlassian/clover/src/master/): dynamic coverage
- [bcel](http://commons.apache.org/proper/commons-bcel/): static coverage
- [sloc](https://github.com/flosse/sloc): basic information

https://github.com/cowtowncoder/java-uuid-generator

```
brew install openjdk@11
brew install --ignore-dependencies maven
export JAVA_HOME=`/usr/libexec/java_home`
yarn global add sloc

git clone https://github.com/cowtowncoder/java-uuid-generator.git
git checkout tags/java-uuid-generator-4.0.1
mvn clean
mvn test
mvn package
java -cp target/java-uuid-generator-4.0.1.jar com.fasterxml.uuid.Jug r

sloc src/main # SLOC
sloc src/test # TLOC

mvn test
```

https://search.maven.org/search?q=g:org.jacoco%20a:jacoco-maven-plugin
https://www.eclemma.org/jacoco/trunk/doc/maven.html

## References

[1] Z. Li, M. Harman, and R. M. Hierons, “Search Algorithms for Regression Test Case Prioritization,” IIEEE Trans. Software Eng., vol. 33, no. 4, pp. 225–237, Apr. 2007, doi: 10.1109/TSE.2007.38.

[2] Q. Luo, K. Moran, L. Zhang, and D. Poshyvanyk, “How Do Static and Dynamic Test Case Prioritization Techniques Perform on Modern Software Systems? An Extensive Study on GitHub Projects,” IIEEE Trans. Software Eng., vol. 45, no. 11, pp. 1054–1080, Nov. 2019, doi: 10.1109/TSE.2018.2822270.

[3] J. Zhou, J. Chen, and D. Hao, “Parallel Test Prioritization,” ACM Trans. Softw. Eng. Methodol., vol. 31, no. 1, Sep. 2021, doi: 10.1145/3471906.
