# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return (dict[target - x], i)
            dict[x] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    S = Solution()
    result = S.twoSum(nums, target)
    for index in range(len(result)):
        print(result[index])
