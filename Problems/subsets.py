from unittest import TestCase
from typing import List


"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

    def subsets_recursive(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, subset):
            result.append(subset)
            for i in range(index, len(nums)):
                backtrack(i + 1, subset + [nums[i]])
        backtrack(0, [])
        return result


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_subsets(self):
        nums = [1, 2, 3]
        self.assertEqual(self.s.subsets(nums), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    def test_subsets_recursive(self):
        nums = [1, 2, 3]
        self.assertEqual(self.s.subsets_recursive(nums), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])

