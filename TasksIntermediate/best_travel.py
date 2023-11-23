from unittest import TestCase
from itertools import combinations

"""
John and Mary want to travel between a few towns A, B, C ...
Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60].
John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

Example:
With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].


"""


def choose_best_sum(t, k, ls):
    itr = combinations(ls, k)
    lst = sorted([sum(i) for i in itr if sum(i) - t <= 0], reverse=True)
    if not lst:
        return None
    return lst[0]


def choose_best_sum_2(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)


class TestSolution(TestCase):

    def test_solution(self):
        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertEqual(choose_best_sum(230, 4, xs), 230)
        self.assertEqual(choose_best_sum(430, 5, xs), 430)
        self.assertEqual(choose_best_sum(430, 8, xs), None)

    def test_solution_2(self):
        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertEqual(choose_best_sum_2(230, 4, xs), 230)
        self.assertEqual(choose_best_sum_2(430, 5, xs), 430)
        self.assertEqual(choose_best_sum_2(430, 8, xs), None)
