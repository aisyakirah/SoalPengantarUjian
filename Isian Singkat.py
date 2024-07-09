# Soal 1
result = "Honey" + "Boo" * 3
print(result)

# Soal 2
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'
result = capitals['Germany']
print(result)

# Soal 3
a = "23"
b = 9
print(a + b)

# Soal 4
letters = ["a", "b", "o", "c", "p"]

# a. >>>letters[1]
print("a. letters[1] =", letters[1])

# b. >>>letters[len(letters)-2]
print("b. letters[len(letters)-2] =", letters[len(letters)-2])

# c. >>>letters + ["x"]
print("c. letters + ['x'] =", letters + ["x"])

# d. >>>letters
print("d. letters =", letters)

# Soal 5
result = ' '.join('h a n d s'.split())
print(result)

# Soal 6
import json

json_string = """
[
    {"1": "one", "2": "two", "3": "three"},
    {"1": "un", "2": "deux", "3": "trois"},
    {"1": "eins", "2": "zwei", "3": "drei"}
]
"""
result = json.loads(json_string)[1]["2"]
print(result)

# Soal 7
def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1
vals = [100, 66, 55, 64, 41, 35, 18, 64]
result = pembagi_indeks1(vals, 5)
print(result)

# Soal 8
def mystery(n, m):
    p = 0
    e = 0
    while p < n:
        p = p + m
        e = e + 1
    return p
print(mystery(4, 3))