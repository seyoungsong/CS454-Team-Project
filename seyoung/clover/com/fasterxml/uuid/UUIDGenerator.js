var clover = new Object();

// JSON: {classes : [{name, id, sl, el,  methods : [{sl, el}, ...]}, ...]}
clover.pageData = {"classes":[{"el":49,"id":555,"methods":[{"el":36,"sc":5,"sl":36}],"name":"UUIDGenerator","sl":25}]}

// JSON: {test_ID : {"methods": [ID1, ID2, ID3...], "name" : "testXXX() void"}, ...};
clover.testTargets = {"test_0":{"methods":[{"sl":36}],"name":"testGenerateNameBasedUUIDNameSpaceAndName","pass":true,"statements":[]},"test_24":{"methods":[{"sl":36}],"name":"testGenerateTimeBasedUUID","pass":true,"statements":[]},"test_30":{"methods":[{"sl":36}],"name":"testIssue5","pass":true,"statements":[]},"test_31":{"methods":[{"sl":36}],"name":"testGenerateRandomBasedUUID","pass":true,"statements":[]},"test_34":{"methods":[{"sl":36}],"name":"testGenerateNameBasedUUIDNameSpaceNameAndMessageDigest","pass":true,"statements":[]},"test_6":{"methods":[{"sl":36}],"name":"testGenerateTimeBasedUUIDWithEthernetAddress","pass":true,"statements":[]}}

// JSON: { lines : [{tests : [testid1, testid2, testid3, ...]}, ...]};
clover.srcFileLines = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [6, 31, 24, 34, 0, 30], [], [], [], [], [], [], [], [], [], [], [], [], []]
