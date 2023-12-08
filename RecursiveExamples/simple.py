
def list_sum(lst):
    if not lst:
        return 0
    else:
        a = lst[0]
        b = list_sum(lst[1:])
        r = a + b
        return r



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
