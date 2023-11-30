from unittest import TestCase
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    indexes = []
    for i, v in enumerate(lst):
        if v == 0:
            indexes.append(i)
    for i, v in enumerate(indexes):
        zero = lst.pop(v - i)
        lst.append(zero)

    return lst


def move_zeros_2(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))


class TestMoveZeros(TestCase):
    def test_move_zeros(self):
        self.assertEqual(move_zeros([1, 0, 1, 2, 0, 1, 3]), [1, 1, 2, 1, 3, 0, 0])

    def test_move_zeros_2(self):
        self.assertEqual(move_zeros_2([1, 0, 1, 2, 0, 1, 3]), [1, 1, 2, 1, 3, 0, 0])
        self.assertEqual(move_zeros_2([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])