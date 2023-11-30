import random
import timeit

random_list_of_nums = random.sample(range(-100000, 100000), 100000)


def _range_test(int_list):
    for i in range(len(int_list)):
        int_list[i] = int_list[i] + 1


def _enumerate_test(int_list):
    for i, v in enumerate(int_list):
        int_list[i] = int_list[i] + 1
        # int_list[i] = v + 1


if __name__ == '__main__':

    # dis.dis(_range_test)
    print(f"_range_test: {min(timeit.repeat(lambda: _range_test(random_list_of_nums), number=100))}")
    print("-"*100)
    # dis.dis(_enumerate_test)
    print(f"_enumerate_test: {min(timeit.repeat(lambda: _enumerate_test(random_list_of_nums), number=100))}")
