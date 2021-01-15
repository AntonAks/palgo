def str_reverse_simple(string):
    return string[::-1]


def str_reverse_recursive(string):
    if len(string) == 2:
        return string[-1] + string[0]

    if len(string) == 1:
        return string[0]

    return string[-1] + str_reverse_recursive(string[1:len(string)-1]) + string[0]


def str_reverse(string):
    new_strings = []
    i = len(string)
    while i:
        i -= 1
        new_strings.append(string[i])
    return ''.join(new_strings)


if __name__ == '__main__':
    import timeit

    print(str_reverse_simple('abcdef'))
    print(str_reverse_recursive('abcdef'))
    print(str_reverse('abcdef'))

    string = 'qwertasdfgzxcvbpoiuylkjhgmnbvc'
    print(f"str_reverse_simple: {min(timeit.repeat(lambda: str_reverse_simple(string)))}")
    print(f"str_reverse_recursive: {min(timeit.repeat(lambda: str_reverse_recursive(string)))}")
    print(f"str_reverse: {min(timeit.repeat(lambda: str_reverse(string)))}")

