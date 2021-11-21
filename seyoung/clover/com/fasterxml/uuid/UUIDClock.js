var clover = new Object();

// JSON: {classes : [{name, id, sl, el,  methods : [{sl, el}, ...]}, ...]}
clover.pageData = {"classes":[{"el":36,"id":513,"methods":[{"el":35,"sc":5,"sl":32}],"name":"UUIDClock","sl":27}]}

// JSON: {test_ID : {"methods": [ID1, ID2, ID3...], "name" : "testXXX() void"}, ...};
clover.testTargets = {"test_14":{"methods":[{"sl":32}],"name":"testGetTimestamp","pass":true,"statements":[{"sl":34}]},"test_24":{"methods":[{"sl":32}],"name":"testGenerateTimeBasedUUID","pass":true,"statements":[{"sl":34}]},"test_43":{"methods":[{"sl":32}],"name":"testSecureRandomUUIDTimerConstructor","pass":true,"statements":[{"sl":34}]},"test_6":{"methods":[{"sl":32}],"name":"testGenerateTimeBasedUUIDWithEthernetAddress","pass":true,"statements":[{"sl":34}]}}

// JSON: { lines : [{tests : [testid1, testid2, testid3, ...]}, ...]};
clover.srcFileLines = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [6, 24, 14, 43], [], [6, 24, 14, 43], [], []]
