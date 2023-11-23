import timeit
import random


def bubble_sort_1(my_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
    return my_list


def bubble_sort_2(my_list: list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


def selection_sort(my_list):
    for i in range(0, len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[i]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


def quick_sort(my_list):
    def _partition(my_list, low, high):
        # Choosing the middle element as a pivot
        # It is also possible to select the first, the last
        # Or arbitrary elements as a pivot
        pivot = my_list[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while my_list[i] < pivot:
                i += 1

            j -= 1
            while my_list[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # If the element at index i (to the left of the pivot) is greater than
            # element with index j (to the right of the pivot), swap them
            my_list[i], my_list[j] = my_list[j], my_list[i]

    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = _partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(my_list, 0, len(my_list) - 1)

    return my_list


def insertion_sort(nums):
    # We start sorting from the second element, because the first element is considered to be already sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Store a link to the index of the previous item
        j = i - 1
        # Move the elements of the sorted segment forward if they are larger than the element to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Inserting the element
        nums[j + 1] = item_to_insert


if __name__ == "__main__":

    random_list_of_nums = random.sample(range(-100, 100), 100)

    print(random_list_of_nums)
    print(f"bubble_sort 1: {min(timeit.repeat(lambda: bubble_sort_1(random_list_of_nums), number=100))}")
    print(f"bubble_sort 2: {min(timeit.repeat(lambda: bubble_sort_2(random_list_of_nums), number=100))}")
    print(f"selection_sort: {min(timeit.repeat(lambda: selection_sort(random_list_of_nums), number=100))}")
    print(f"quick_sort: {min(timeit.repeat(lambda: quick_sort(random_list_of_nums), number=100))}")
    print(f"insertion_sort: {min(timeit.repeat(lambda: insertion_sort(random_list_of_nums), number=100))}")
