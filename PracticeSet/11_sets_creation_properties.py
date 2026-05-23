# ✅ 11. Sets in Python

# 🔹 What is a Set?
# A set is a collection of unordered and unique elements.
# - No duplicates allowed
# - No indexing (because unordered)
# - Mutable (we can add/remove elements)


# 🔹 Creating Sets

# 1. Using Curly Braces
s = {1, 2, 3, 4}
print(s)

# 2. Using set() Function
# Duplicates are automatically removed
s = set([1, 2, 2, 3])
print(s)   # duplicates removed


# 🔹 Properties of Sets

# ✅ 1. Unordered
# Elements do not maintain order
s = {3, 1, 2}
print(s)   # order may change


# ✅ 2. No Duplicate Elements
# Duplicate values are removed automatically
s = {1, 2, 2, 3}
print(s)   # {1, 2, 3}


# ✅ 3. Mutable
# We can add elements using add()
s = {1, 2}
s.add(3)
print(s)


# ✅ 4. No Indexing
# We cannot access elements using index
s = {1, 2, 3}
# print(s[0]) ❌ Error because sets are unordered


# ✅ 5. Set Operations
# Sets support mathematical operations like union, intersection, difference
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union → combines all elements
print(a & b)  # Intersection → common elements
print(a - b)  # Difference → elements in a but not in b


# 🧠 Exam Line:
# A set is an unordered collection of unique elements in Python.
# It does not allow duplicates, supports operations like union and intersection,
# and is mutable but does not support indexing.



# ✅ 12. Built-in String Methods

# Python provides many string methods to manipulate and analyze strings.


# 🔹 1. Case Conversion Methods
# Used to change the case of characters
s = "python"

print(s.upper())        # converts to uppercase
print(s.lower())        # converts to lowercase
print(s.capitalize())   # first letter capital
print(s.title())        # first letter of each word capital


# 🔹 2. Checking Methods
# Used to check properties of a string
s = "Python123"

print(s.isalpha())   # checks if only letters
print(s.isdigit())   # checks if only digits
print(s.isalnum())   # checks letters + numbers
print(s.islower())   # checks if lowercase


# 🔹 3. Searching Methods
# Used to find or count characters/substrings
s = "hello world"

print(s.find("world"))   # returns index of substring
print(s.count("l"))      # counts occurrences


# 🔹 4. Replace & Modify
# Used to replace characters or substrings
s = "hello"

print(s.replace("h", "H"))   # replaces h with H


# 🔹 5. Splitting and Joining
# Used to convert string to list and vice versa
s = "a,b,c"

print(s.split(","))     # splits string into list

lst = ['a', 'b', 'c']
print(",".join(lst))    # joins list into string


# 🔹 6. Strip Methods (Remove spaces)
# Used to remove extra spaces
s = "  hello  "

print(s.strip())    # removes spaces from both sides
print(s.lstrip())   # removes spaces from left
print(s.rstrip())   # removes spaces from right


# 🧠 Exam Line:
# String methods in Python are built-in functions used to manipulate and analyze strings.
# These include case conversion, checking, searching, replacing, splitting, and trimming methods.


# 🔥 Quick Summary:
# Sets:
# - Unordered, unique, no indexing
# - Mutable and supports set operations
#
# Strings:
# - Many built-in methods available
# - Used for manipulation and validation