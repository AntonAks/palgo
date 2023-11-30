def numbers_in_str(string) -> tuple[list, int]:
    numbers = []
    last_was_int = False
    for char in string:
        if char.isdigit() and not last_was_int:
            numbers.append(int(char))
            last_was_int = True
        elif char.isdigit() and last_was_int:
            _temp = str(numbers.pop()) + char
            numbers.append(int(_temp))
        else:
            last_was_int = False
    return numbers, sum(numbers)



if __name__ == '__main__':
    s = 'kjn3kj57kjn6nl101l2knl3kn5ll6lkmn323l,m2lk4j;23shfqrxlo1okdf45'
    print(numbers_in_str(s))
