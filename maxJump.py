import logging
'''
Leet Code problem 55: https://leetcode.com/problems/jump-game/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    i = 0
    maxjumpPosition = nums[0]
    while i <= maxjumpPosition:
        if (nums[i] + i) > maxjumpPosition:
            maxjumpPosition = nums[i] + i
        if maxjumpPosition >= (len(nums) - 1):
            return True
        i = i + 1
    return False


def test():
    testCases = [([2, 3, 1, 1, 4], True),
                 ([3, 2, 1, 0, 4], False)]

    passfaillist = []
    for pair in testCases:
        this_testcase = pair[0]
        expected_result = pair[1]
        calculated_result = canJump(this_testcase)
        passfaillist.append(expected_result == calculated_result)
    print(passfaillist)
    print("Number of failed cases = " + str(passfaillist.count(False)))
    return passfaillist

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

    test()
