from itertools import product

n = ["A", "B", "C"]

result = product(n, repeat=3) # You can change the repeat more then n length

print(list(result))