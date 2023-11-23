import random


random_list_of_nums = random.sample(range(0, 1000), 100)


def binary_search(value, list_of_values):

    list_of_values.sort()

    low = 0
    mid = len(list_of_values) // 2
    high = len(list_of_values) - 1

    while list_of_values[mid] != value and low <= high:
        if value > list_of_values[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("No value")
    else:
        print("ID =", mid)


if __name__ == '__main__':



    binary_search(14, random_list_of_nums)