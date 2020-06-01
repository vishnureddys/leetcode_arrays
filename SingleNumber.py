'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = dict()
        for i in nums:
            if i not in temp:
                temp[i] = 1
            elif i in temp:
                temp[i] += 1
        for i in temp:
            if temp[i] == 1:
                return i
