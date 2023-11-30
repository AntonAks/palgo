# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
# Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"


def to_underscore(string: str):
    new_string = ''
    if isinstance(string, int):
        return str(string)
    for i in range(len(string)):
        if string[i].isupper():
            new_string += '_'
            new_string += string[i].lower()
        else:
            new_string += string[i].lower()
    return new_string[1:]


if __name__ == '__main__':

    to_underscore('HelloWorld')
    to_underscore(123)
