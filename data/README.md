# Data

In OpenClover, the minimum unit of time measurement is `0.001` seconds. Therefore, if the testing time is shorter than that, `duration` is marked as `0.0` seconds. However, using this value as it is can cause unnecessary confusion in the algorithm. Therefore, we will not use `0.0` seconds as it is, but use the value of `0.0005` seconds.

```json
{
  "info": {
    // information about this file and project
    "project": "Java UUID Generator 4.0.2-SNAPSHOT", // project name
    "filename": "cowtowncoder_java-uuid-generator.json", // json file name
    "github": {
      "url": "https://github.com/cowtowncoder/java-uuid-generator", // github url of the project
      "dev": "cowtowncoder", // developer name
      "repo": "java-uuid-generator" // repository name
    },
    "env": {
      "platform": "macOS-11.6-arm64-arm-64bit", // platform name by `platform.platform()`
      "java": "openjdk version \"1.8.0_312\"", // java version
      "maven": "Apache Maven 3.8.4 (9b656c72d54e5bacbed989b64718c159fe39b537)" // maven version
    },
    "commit": {
      "datetime": "2021-11-21T13:30:47+09:00", // ISO 8601 date of the latest commit
      "url": "https://github.com/cowtowncoder/java-uuid-generator/tree/a28b65dc2d862e6aa3ac7b16584d0e9eb8dd8ff9", // github url of latest branch
      "hash": "a28b65dc2d862e6aa3ac7b16584d0e9eb8dd8ff9", // hash of the latest commit
      "timestamp": 1637469047 // unix timestamp of the latest commit
    },
    "metrics": {
      // metrics from clover.xml
      "project": {
        // project metrics
        "coveredelements": "549",
        "complexity": "321",
        "loc": "3198", // Lines Of Code (including comment lines).
        "methods": "110",
        "classes": "21",
        "statements": "829",
        "packages": "5",
        "coveredconditionals": "120",
        "coveredmethods": "69",
        "elements": "1235",
        "ncloc": "1577", // Non-Commented Lines Of Code
        "files": "20",
        "conditionals": "296",
        "coveredstatements": "360"
      },
      "testproject": {
        // test project metrics
        "coveredelements": "1124",
        "complexity": "221",
        "loc": "3684",
        "methods": "93",
        "classes": "8",
        "statements": "1016",
        "packages": "1",
        "coveredconditionals": "105",
        "coveredmethods": "87",
        "elements": "1221",
        "ncloc": "2396",
        "files": "6",
        "conditionals": "112",
        "coveredstatements": "932"
      }
    }
  },
  "data": [
    // code coverage per test case (method)
    {
      "name": "com.fasterxml.uuid.EthernetAddressTest#testAsByteArray", // unique name of the test. format: f"{package}.{class}#{method}".
      "package": "com.fasterxml.uuid", // package of this test
      "class": "EthernetAddressTest", // class of this test
      "method": "testAsByteArray", // name of this test method
      "success": true, // pass/fail of this test
      "duration": 0.004, // testing time (sec).
      "coverage": [
        // code coverage of this single test
        {
          "package": "com.fasterxml.uuid", // package
          "class": "EthernetAddress", // filename
          "lines": [
            // statement coverage by lines
            "168M", // Method
            "169", // Statement
            "341M",
            "343",
            "344",
            "345",
            "355M",
            "356",
            "356F", // conditional branch: False
            "359",
            "362M",
            "364",
            "364T", // conditional branch: True
            "367",
            "368",
            "369",
            "370",
            "371",
            "372",
            "373",
            "374"
          ]
        }
      ]
    }
  ]
}
```
