from unittest import TestCase
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""


class Solution(object):
    def two_sum(self, nums: list, target: int):
        hash_m = {}  # hash_map that number as key and index as value
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in hash_m:
                return [hash_m[remaining], i]
            hash_m[v] = i
        return []


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_two_sum(self):
        nums = [1, 2, 2, 7, 11, 15]
        target = 9
        self.assertEqual(self.s.two_sum(nums, target), [2, 3])

    def test_two_sum_2(self):
        nums = [3, 10, 11, 2, 4, 9, 15]
        target = 6
        self.assertEqual(self.s.two_sum(nums, target), [3, 4])

    def test_two_sum_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.s.two_sum(nums, target), [0, 1])



