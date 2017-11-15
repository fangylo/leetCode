'''
Leet Code problem 55: https://leetcode.com/problems/jump-game/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

import logging


def testCase():
    """Test cases"""
    testCases = [("()", "()"),
                 ("(", None),
                 ("(()", "()"),
                 ("())", "()"),
                 ("(())", "(())"),
                 (")(())", "(())"),
                 (")(())(", "(())"),
                 ("(())", "(())"),
                 (")(())", "(())"),
                 (")(())(", "(())"),
                 ("(()()()()()))))", "(()()()()())"),
                 ("()()()", "()()()"),
                 ("))()()()", "()()()"),
                 (")()()()((", "()()()")]

    passfaillist = []
    for pair in testCases:
        this_testcase = pair[0]
        expected_result = pair[1]
        calculated_result = getMaxSubStr(this_testcase)
        passfaillist.append(expected_result == calculated_result)
    print(passfaillist)
    print("Number of failed cases = " + str(passfaillist.count(False)))
    return passfaillist


def getMaxSubStr(string):
    maxSubStr_fwd = getMaxSubStrFwd(string)
    maxSubStr_rev = getMaxSubStrRev(string)
    # logging.debug("maxSubStr_fwd="+maxSubStr_fwd)
    # logging.debug("maxSubStr_rev="+maxSubStr_rev)
    if maxSubStr_fwd is None and maxSubStr_rev is None:
        result = None
    elif maxSubStr_fwd is None and maxSubStr_rev is not None:
        result = maxSubStr_rev
    elif maxSubStr_fwd is not None and maxSubStr_rev is None:
        result = maxSubStr_fwd
    elif maxSubStr_fwd is not None and maxSubStr_rev is not None:
        if len(maxSubStr_fwd) > len(maxSubStr_rev):
            result = maxSubStr_fwd
        else:
            result = maxSubStr_rev
    return result


def getMaxSubStrFwd(string):
    testlist = list(string)
    # Go through item each from the left

    depthlevelList = []
    currentDepthLevel = 0
    maxSubstringStartIndex = 0
    maxSubstringStopIndex = 0
    maxSubstringLength = 0
    maxSubstring = None
    thisSubstringStopIndex = 0
    thisSubstringStartIndex = 0

    for i in range(0, len(testlist)):
        if testlist[i] == ")":
            currentDepthLevel = currentDepthLevel - 1
        if testlist[i] == "(":
            currentDepthLevel = currentDepthLevel + 1
        depthlevelList.append(currentDepthLevel)

        if currentDepthLevel < 0:
            # Reset depthlevel AFTER current negative depthlevel
            # is appended to the depthlevelList.
            currentDepthLevel = 0
            # Check to see the depthlevel of the (i-1)th item.
            if i > 0:
                if depthlevelList[i - 1] == 0:  # previous depth level is 0
                    logging.debug("test met, i=" + str(i))
                    thisSubstringStopIndex = (i - 1)
                    thisSubstringLength = thisSubstringStopIndex - thisSubstringStartIndex
                    # Compare with current max valid substring:
                    if thisSubstringLength > maxSubstringLength:
                        maxSubstringLength = thisSubstringLength
                        maxSubstringStartIndex = thisSubstringStartIndex
                        maxSubstringStopIndex = thisSubstringStopIndex
                        # Reset start index:
                        thisSubstringStartIndex = i + 1
                elif depthlevelList[i - 1] < 0:  # previous depth is also negative
                    thisSubstringStartIndex = i + 1
                    thisSubstringStopIndex = i + 1
            elif i == 0:  # if this is the first item of the list
                thisSubstringStartIndex = i + 1
                thisSubstringStopIndex = i + 1

        if currentDepthLevel > 0:
            # When it's the first item on the list:
            if i == 0:
                thisSubstringStartIndex = 0
            elif i == (len(testlist) - 1):
                if depthlevelList[(i - currentDepthLevel)] == 0:
                    thisSubstringStopIndex = (i - currentDepthLevel)
                    thisSubstringLength = thisSubstringStopIndex - thisSubstringStartIndex
                    # Compare with current max valid substring:
                    if thisSubstringLength > maxSubstringLength:
                        maxSubstringLength = thisSubstringLength
                        maxSubstringStartIndex = thisSubstringStartIndex
                        maxSubstringStopIndex = thisSubstringStopIndex

        if currentDepthLevel == 0 and i == (len(testlist) - 1):
            if depthlevelList[i - 1] > 0:
                thisSubstringStopIndex = i
                thisSubstringLength = thisSubstringStopIndex - thisSubstringStartIndex
                # Compare with current max valid substring:
                if thisSubstringLength > maxSubstringLength:
                    maxSubstringLength = thisSubstringLength
                    maxSubstringStartIndex = thisSubstringStartIndex
                    maxSubstringStopIndex = thisSubstringStopIndex

        # logging.debug("i=" + str(i))
        # logging.debug(depthlevelList)
        # logging.debug("thisSubstringStartIndex=" +
        #               str(thisSubstringStartIndex))
        # logging.debug("thisSubstringStopIndex=" + str(thisSubstringStopIndex))
        # logging.debug("maxSubstringStartIndex=" + str(maxSubstringStartIndex))
        # logging.debug("maxSubstringStopIndex=" + str(maxSubstringStopIndex))

    if maxSubstringStopIndex > 0:
        maxSubstring = testlist[
            maxSubstringStartIndex:maxSubstringStopIndex + 1]
        maxSubstring = "".join(maxSubstring)
        logging.debug("max valid substring=" + maxSubstring)
    return(maxSubstring)


def getMaxSubStrRev(string):
    string = string[::-1]
    tmp_str = string.replace("(", "t")
    tmp_str = tmp_str.replace(")", "(")
    rev_string = tmp_str.replace("t", ")")
    logging.debug(rev_string)

    rev_maxSubString = getMaxSubStrFwd(rev_string)
    if rev_maxSubString is not None:
        tmp_str = rev_maxSubString.replace("(", "t")
        tmp_str = tmp_str.replace(")", "(")
        rev_maxSubString = tmp_str.replace("t", ")")
        return rev_maxSubString[::-1]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

    testCase()
