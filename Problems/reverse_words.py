from unittest import TestCase


# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence: str):
    lst = sentence.split()
    for i in range(len(lst)):
        if len(lst[i]) >= 5:
            lst[i] = lst[i][::-1]
    return ' '.join(lst)


def spin_words_2(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


class TestSpin(TestCase):

    def test_spin_function(self):
        self.assertEqual(spin_words("This is another test"), "This is rehtona test")
        self.assertEqual(spin_words("This is a test"), "This is a test")

    def test_spin_function2(self):
        self.assertEqual(spin_words_2("This is another test"), "This is rehtona test")
        self.assertEqual(spin_words_2("This is a test"), "This is a test")

