from random import shuffle


def sum_slow(data):
    total = 0
    for x in data:
        total += x
    return total

def sum_fast(data):
    return sum(data)


data = list(range(10))
shuffle(data)
nested = [[1,2], [3,4], [5]]

print("Data:", data)
print("Nested:", nested)

print("sum_slow:", sum_slow(data))
print("sum_fast:", sum_fast(data))
