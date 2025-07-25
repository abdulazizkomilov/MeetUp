import time
from collections import defaultdict, deque, Counter, namedtuple
from dataclasses import dataclass


# -----------------------------------------------
# 1. List vs Set — Searching for an element
# -----------------------------------------------


"""
List: Searching 1,000,000 elements using list

Time Complexity: O(n)
"""

nums_list = list(range(1_000_000))
start = time.time()
print("List: ", 999_999 in nums_list)
list_search_time = time.time() - start
print("List Search Time:", list_search_time)


"""
Set: Searching 1,000,000 elements using set

Time Complexity: O(1)
"""

nums_set = set(nums_list)
start = time.time()
print("Set: ", 999_999 in nums_set)
set_search_time = time.time() - start
print("Set Search Time:", set_search_time)


# -----------------------------------------------
# 1.1 List vs Set — Performance Comparison
# -----------------------------------------------


if set_search_time > 0:
    speedup = list_search_time / set_search_time
    print(f"Set is approximately {speedup:.2f} times faster than list.")
else:
    print("Set search time too fast to compare reliably.")


# -----------------------------------------------
# 2. defaultdict — Word frequency counter
# -----------------------------------------------


"""
Using defaultdict to count word frequency in a string

Time Complexity: O(n)
"""

text = "apple banana apple orange banana apple"
words = text.split()

counter = defaultdict(int)
for word in words:
    counter[word] += 1

print("\ndefaultdict count:", dict(counter))


# -----------------------------------------------
# 3. deque — Efficient Queue Operations
# -----------------------------------------------


"""
Using deque for fast queue operations

Time Complexity: O(1) for popleft()
"""

q = deque([1, 2, 3, 4, 5])
q.popleft()
print("\ndeque after popleft:", q)


# -----------------------------------------------
# 4. Counter — Most common elements
# -----------------------------------------------


"""
Using Counter to find the most common element

Time Complexity: O(n)
"""

nums = [4, 1, 2, 2, 3, 4, 4, 1, 2]
most_common = Counter(nums).most_common(1)
print("\nMost common:", most_common)


# -----------------------------------------------
# 5. namedtuple — Readable structured data
# -----------------------------------------------


"""
Using namedtuple for clean, readable data structures

Time Complexity: O(1) for access
"""

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print("\nNamedTuple Point:", p)
print("\nNamedTuple Point:", p.x, p.y)


# -----------------------------------------------
# 6. dataclass — Cleaner classes with less boilerplate
# -----------------------------------------------


"""
Using dataclass for simplified class definitions

Time Complexity: O(1) for access
"""

@dataclass
class Product:
    name: str
    price: float

item = Product(name="Keyboard", price=49.99)
print("\nDataclass Product:", item.name, item.price)
