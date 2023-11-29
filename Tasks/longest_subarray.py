from unittest import TestCase


# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].


class Solution(object):
    def longest_subarray(self, nums: list) -> int:
        _str = [len(j) for j in ''.join([str(i) for i in nums]).split('0')]
        if len(_str) == 1:
            return sum(nums) - 1
        _sum = 0
        for i in range(len(_str) - 1):
            if _sum < _str[i] + _str[i + 1]:
                _sum = _str[i] + _str[i + 1]
        return _sum

    def longest_subarray_2(self, nums):

        left = maxt = 0

        count = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                count -= 1
            while count < 0:
                if nums[left] == 0:
                    count += 1
                left += 1

            maxt = max(maxt, right - left)

        return maxt


class TestSolution(TestCase):

    def test_solution_1(self):
        s = Solution()
        self.assertEqual(s.longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)
        self.assertEqual(s.longest_subarray([0, 1, 1, 1, 0, 1, 1, 1, 1]), 7)
        self.assertEqual(s.longest_subarray([1, 1, 1, 1, 1, 1, 1, 1, 1]), 8)

    def test_solution_2(self):
        s = Solution()
        self.assertEqual(s.longest_subarray_2([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)
        self.assertEqual(s.longest_subarray_2([0, 1, 1, 1, 0, 1, 1, 1, 1]), 7)
        self.assertEqual(s.longest_subarray_2([1, 1, 1, 1, 1, 1, 1, 1, 1]), 8)
