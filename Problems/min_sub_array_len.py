from typing import List

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''


# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        result = 0
        for i, v in enumerate(nums):
            print("target >>>", i)
            for j, v2 in enumerate(nums):
                print(nums[j:j + i + 1], sum(nums[j:j + i + 1]), sum(nums[j:j + i + 1]) >= target)
                if sum(nums[j:j + i + 1]) >= target:
                    result = len(nums[j:j + i + 1])
                    return result
        return result

    def min_sub_array_len_2(self, target: int, nums: List[int]):
        length = float('inf')
        left = 0
        summ = 0

        for right in range(len(nums)):
            summ += nums[right]

            while summ >= target:
                length = min(length, right - left + 1)
                summ -= nums[left]
                left += 1

        if sum(nums) < target:
            return (0)
        elif sum(nums) == target:
            return len(nums)
        else:
            return length


if __name__ == '__main__':
    s = Solution()
    t = 213
    l = [12,28,83,4,25,26,25,2,25,25,25,12]
    print(s.min_sub_array_len_2(t, l))
    print(s.min_sub_array_len(t, l))
