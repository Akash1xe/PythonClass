print("Tuple Exercise 1: Maximum and Minimum")
T = (10, 5, 20, 3)
print("Maximum:", max(T))
print("Minimum:", min(T))

print("\nTuple Exercise 2: Count Occurrences")
T = (1, 2, 3, 2, 4, 2)
print("Count of 2:", T.count(2))

print("\nTuple Exercise 3: Convert List to Tuple")
L = [10, 20, 30]
T = tuple(L)
print(T)

print("\nTuple Exercise 4: Check Element Existence")
T = (10, 20, 30)
if 20 in T:
    print("Element exists")
else:
    print("Element does not exist")

print("\nTuple Exercise 5: Unpack Tuple")
T = (10, 20, 30)
a, b, c = T
print(a, b, c)