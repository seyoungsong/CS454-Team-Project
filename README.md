# CS454 Team Project

- Search Algorithms for Regression Test Case Prioritization

  - Print_tokens, Print_tokens2, Schedule, Schedule2, Space, Sed
  - The programs and test suites were from an infrastructure [4] that is designed to support controlled experimentation with software testing and regression testing techniques.
  - Cantata++
  - [4] H. Do, S.G. Elbaum, and G. Rothermel, “Supporting Controlled Experimentation with Testing Techniques: An Infrastructure and Its Potential Impact,” Empirical Software Eng.: An Int’l J., vol. 10, no. 4, pp. 405-435, 2005.
  - [10] M. Hutchins, H. Foster, T. Goradia, and T. Ostrand, “Experiments on the Effectiveness of Dataflow- and Control-Flow-Based Test Adequacy Criteria,” Proc. 16th Int’l Conf. Software Eng., pp. 191- 200, May 1994.

- Parallel Test Prioritization
  - To investigate the performance of these adapted parallel test prioritization techniques, we con- ducted the first extensive study based on 54 open-source Java projects from GitHub, whose total number of lines of source code is 895,728 and total number of tests is 30,783. These projects have been widely used by many existing software-testing studies [8, 45].
  - [8] Chen, Junjie, et al. "Optimizing test prioritization via test distribution analysis." Proceedings of the 2018 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering. 2018.
  - [45] Luo, Qi, et al. "How do static and dynamic test case prioritization techniques perform on modern software systems? An extensive study on GitHub projects." IEEE Transactions on Software Engineering 45.11 (2018): 1054-1080.
  - In this study, we used 54 open-source Java projects from GitHub, which have been widely used in many existing studies [7, 8, 45]. All projects are built on Maven, and are suited with tests in the JUnit testing framework.
  - we used PIT to generate mutation faults
  - More specifically, we used the actual execution time reported by maven (i.e., executing command “mvn test”).
  - For each open-source subject, we used Clover6 to collect its dynamic coverage, used bcel7 to col- lect its static coverage, used SLOC8 to collect its basic information (i.e., lines of source code and lines of test code), and used Pitest (PIT) to generate mutation faults.

https://github.com/cowtowncoder/java-uuid-generator

## How do static and dynamic test case prioritization techniques perform on modern software systems? An extensive study on GitHub projects.

geojson-jackson
statsd-jvm-profiler
stateless4j
jarchivelib
JSONassert
java-faker
jackson-datatype-joda
Java-apns
pusher-websocket-java
gson-fire
jackson-datatype-guava
dictomaton
jackson-uuid-generator
JAdventure
exp4j
jumblr
efflux
metrics-core
low-gc-membuffers
xembly
scribe-java
jpush-api-java-client
gdx-artemis
protoparser
commons-cli
mp3agic
webbit
RestFixture
LastCalc
jackson-dataformat-csv
skype-java-api
lambdaj
jackson-dataformat-xml
jopt-simple
jline2
javapoet
Liqp
cassandra-reaper
JSqlParser
raml-java-parser
redline-smalltalk
user-agent-utils
javaewah
jsoup-learning
wsc
rome
JActor
RoaringBitmap
JavaFastPFOR
jprotobuf
worldguard
commons-jxpath
commons-io
nodebox
asterisk-java
ews-java-api
commons-lang
joda-time

## Parallel Test Prioritization

assertj-core
asterisk-java
blueflood
camel-core
chukwa
commons-dbcp
commons-io
commons-math
commons-pool
disklrucache
ews-java-api
gdx-artemis-master
gson-fire
hbase
hivemall
jackson-core
jackson-datatype-guava
jactor
jasmine-maven-plugin
java-apns
java-uuid-generator
javapoet
jopt-simple
joss
jsprit
jumblr
la4j
lambdaj-master
languagetool
lanterna
lastcalc
low-gc-membuffers
mapdb-mapdb
metrics-core
nv-websocket-client
opentripplanner-otp
protoparser
raml-java-parser
raml-java-parser-master
redline-smalltalk
redline-smalltalk-master
restcountries
roaringbitmap
rome
scribe-java
spring-retry
stream-lib
streamex
vraptor-archive
webbit

## Optimizing Test Prioritization via Test Distribution Analysis

assertj-core
asterisk-java
Camel-Core
Chukwa
Commons-Pool
gson-fire
HBase
jasmine-maven-plugin
java-apns
LastCalc
MapDB
OpenTripPlanner
PHP
vraptor-archive
blueflood
cloudhopper-smpp
commons-dbcp
commons-email
commons-math
commons-io
cucumber-reporting
ddd-cqrs-sample
dictomaton
DotCi
ews-java-api
exp4j
gdx-artemis
geo
geohash-java
hivemall
HTTP-Proxy-Servlet
jackson-core
jackson-datatype-guava
jopt-simple
joss
jsprit
la4j
lambdaj
languagetool
metrics-core
raml-java-parser
redline-smalltalk
RoaringBitmap
rome
scribe-java
spring-data-solr
spring-retry
stream-lib
tamper
webbit

## References

[1] Z. Li, M. Harman, and R. M. Hierons, “Search Algorithms for Regression Test Case Prioritization,” IIEEE Trans. Software Eng., vol. 33, no. 4, pp. 225–237, Apr. 2007, doi: 10.1109/TSE.2007.38.

[2] J. Zhou, J. Chen, and D. Hao, “Parallel Test Prioritization,” ACM Trans. Softw. Eng. Methodol., vol. 31, no. 1, Sep. 2021, doi: 10.1145/3471906.
