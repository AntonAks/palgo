"""
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
"""


class Solution(object):
    def merge_two_lists(self, list1: list, list2: list):
        result = []
        _min = min([len(list1), len(list2)])

        if _min == 0:
            result.extend(list1[:1])
            result.extend(list2[:1])

        for i, j in zip(list1, list2):
            result.append(i)
            result.append(j)

        result.extend(list1[3:])
        result.extend(list2[3:])


if __name__ == '__main__':
    s = Solution()

    # a = [1, 2, 4]
    # b = [1, 3, 4]
    a = [0]
    b = []

    s.merge_two_lists(a, b)
