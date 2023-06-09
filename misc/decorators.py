from functools import cache

def my_cache(func):
    input_output_cache = {}

    def wrapper_func(arg):
        if arg in input_output_cache:
            return input_output_cache[arg]

        else:
            result = func(arg)
            input_output_cache[arg] = result
            return result

    return wrapper_func


@my_cache
def my_fibonacci(n):
    if n < 2:
        return n

    return my_fibonacci(n - 1) + my_fibonacci(n - 2)


# 1 1 2 3 5 8 ...

# @cache
# def fibonacci(n):
#     if n < 2:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)


# if __name__ == '__main__':
#     from time import time_ns
#     from random import randint
#     from pprint import pprint

#     runtimes = []
#     for _ in range(500):
#         rand_n = randint(0,500)

#         f_start = time_ns()
#         f = fibonacci(rand_n)
#         f_time = time_ns() - f_start

#         m_start = time_ns()
#         m = my_fibonacci(rand_n)
#         m_time = time_ns() - m_start

#         runtimes.append((rand_n, f_time, m_time))

#     count_mine_slower = 0
#     for r in runtimes:
#         if r[2] > r[1]:
#             count_mine_slower += 1

#     print(f'# times mine slower: {count_mine_slower}/500')
