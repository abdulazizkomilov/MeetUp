# def slow_function():
#     total = 0
#     for i in range(10**8):
#         total += i
#     return total

# def main():
#     slow_function()

# if __name__ == "__main__":
#     main()


# cProfile
# python3 -m cProfile profiling.py

# -------------------------------------


# @profile
# def slow():
#     total = 0
#     for i in range(10**6):
#         total += i
#     return total

# slow()


# kernprof
# kernprof -l -v profiling.py


# -------------------------------------


# def slow_function():
#     total = 0
#     for i in range(10**8):
#         total += i
#     return total

# def main():
#     slow_function()

# if __name__ == "__main__":
#     main()


# snakeviz
# python3 -m cProfile -o profiling.prof profiling.py
# snakeviz profiling.prof


# -------------------------------------


# from memory_profiler import profile

# @profile
# def my_func():
#     a = [i for i in range(100_000)]
#     b = [i*2 for i in a]
#     return b

# my_func()


# memory_profiler
# python3 -m memory_profiler profiling.py
