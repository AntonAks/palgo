import pytest


class Solution(object):
    def length_of_last_word(self, s) -> int:
        result = s.split()
        return len(result[len(result) - 1])


@pytest.fixture
def solution():
    s = Solution()
    return s


@pytest.fixture
def word():
    return "Hello Beautiful World!"


@pytest.fixture
def word2():
    return "Test Driven Development"


def test_function_call(solution, word):
    solution.length_of_last_word(word)


def test_instance(solution, word):
    assert isinstance(solution.length_of_last_word(word), int)


def test_length_of_last_word(solution, word):
    assert solution.length_of_last_word(word) == 6


def test_length_of_last_word2(solution, word2):
    assert solution.length_of_last_word(word2) == 11







