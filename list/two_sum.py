#!/usr/bin/python
# coding=utf-8

import sys
#输出python 版本
#print(sys.version)
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order
example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
def twoSum(nums, target):
    """fetch two element from the list and the sum of the two element equal target
    Args:
        nums: the list
        target: the sum
    Returns:
        a list of the index of two element
    """
    for index in range(len(nums)):
        for index2 in range(len(nums) - 1):
            if (nums[index] + nums[index2+1] == target):
                return [index, index2+1]
            else:
                index2 = index2 + 1
        index = index + 1

#nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
