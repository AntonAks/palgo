# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
# that checks whether the two arrays have the "same" elements, with the same multiplicities
# (the multiplicity of a member is the number of times it appears).
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# Examples
# Valid arrays
a = [-121, -144, 19, -161, 19, -144, 19, -11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    array1 = [abs(i) for i in array1]
    array2 = [abs(i) for i in array2]
    array1.sort()
    array2.sort()
    for i in range(len(array1)):
        if array1[i]**2 != array2[i]:
            return False
    return True


def comp2(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except Exception:
        return False


if __name__ == '__main__':
    print(comp(a, b))
