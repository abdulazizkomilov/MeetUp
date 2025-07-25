import itertools
from random import shuffle


builtins_functions = [
    "sum()",
    "min()",
    "max()",
    "sorted()",
    "zip()",
    "enumerate()",
    "map()",
    "filter()",
    "itertools.chain()",
    "all()",
    "any()",
    "reversed()",
    "len()",
    "abs()",
    "round()",
    "next()",
    "iter()",
    "slice()",
    "getattr()",
    "hasattr()",
    "isinstance()",
]


# -----------------------------------------------
# 1. sum examples
# -----------------------------------------------

def sum_slow(data):
    total = 0
    for x in data:
        total += x
    return total

def sum_fast(data):
    return sum(data)


# -----------------------------------------------
# 2. min/max examples
# -----------------------------------------------


def min_slow(data):
    m = data[0]
    for x in data[1:]:
        if x < m:
            m = x
    return m

def min_max_fast(data):
    return min(data), max(data)


# -----------------------------------------------
# 3. sort examples 
# -----------------------------------------------


def sort_slow(data):
    a = list(data)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def sort_fast(data):
    return sorted(data)


# -----------------------------------------------
# 4. combine examples
# -----------------------------------------------


def combine_slow(a, b):
    result = []
    for i in range(len(a)):
        result.append((a[i], b[i]))
    return result

def combine_fast(a, b):
    return list(zip(a, b))


# -----------------------------------------------
# 5. with_index examples 
# -----------------------------------------------


def with_index_slow(a):
    result = []
    i = 0
    for v in a:
        result.append((i, v))
        i += 1
    return result

def with_index_fast(a):
    return [(i, v) for i, v in enumerate(a)]


# -----------------------------------------------
# 6. even numbers and squares examples
# -----------------------------------------------


def evens_slow(data):
    result = []
    for x in data:
        if x % 2 == 0:
            result.append(x)
    return result

def evens_filter(data):
    return list(filter(lambda x: x % 2 == 0, data))


# -----------------------------------------------
# 7. squares examples
# -----------------------------------------------

def squares_map(data):
    return list(map(lambda x: x * x, data))


# -----------------------------------------------
# 8. flatten examples
# -----------------------------------------------


def flatten_slow(nested):
    result = []
    for sub in nested:
        for x in sub:
            result.append(x)
    return result

def flatten_fast(nested):
    return list(itertools.chain.from_iterable(nested))


# -----------------------------------------------
# Main function to demonstrate the examples
# -----------------------------------------------


def main():
    data = list(range(10))
    shuffle(data)
    nested = [[1,2], [3,4], [5]]

    # print("Data:", data)
    # print("Nested:", nested)

    # print("sum_slow:", sum_slow(data))
    # print("sum_fast:", sum_fast(data))

    # print("min_slow:", min_slow(data))
    # print("min_max_fast:", min_max_fast(data))

    # print("sort_slow:", sort_slow(data))
    # print("sort_fast:", sort_fast(data))

    # print("combine_slow:", combine_slow(data[:5], data[5:10]))
    # print("combine_fast:", combine_fast(data[:5], data[5:10]))

    # print("with_index_slow:", with_index_slow(data[:5]))
    # print("with_index_fast:", with_index_fast(data[:5]))

    # print("evens_slow:", evens_slow(data))
    # print("evens_filter:", evens_filter(data))
    # print("squares_map:", squares_map(data))

    # print("flatten_slow:", flatten_slow(nested))
    # print("flatten_fast:", flatten_fast(nested))

if __name__ == "__main__":
    main()
