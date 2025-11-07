# Program to create and display a set

# Creating a set
my_set = {10, 20, 30, 40, 50}

# Displaying the set
print("The created set is:", my_set)


# Program to create a set with different data types

my_set = {10, "Python", 3.14, True}
print("Set with different data types:", my_set)



# Program to add a single element to a set

my_set = {1, 2, 3}
my_set.add(4)
print("Set after adding an element:", my_set)



# Program to add multiple elements to a set

my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print("Set after adding multiple elements:", my_set)



# Program to remove an element using remove()

my_set = {10, 20, 30, 40}
my_set.remove(30)
print("Set after removing element 30:", my_set)



# Program to remove an element using discard()

my_set = {10, 20, 30, 40}
my_set.discard(50)
print("Set after using discard():", my_set)



# Program to clear all elements from a set

my_set = {1, 2, 3, 4}
my_set.clear()
print("Set after clearing:", my_set)



# Program to check if an element exists in a set

my_set = {10, 20, 30, 40}
if 20 in my_set:
    print("20 exists in the set")
else:
    print("20 does not exist in the set")



# Program to find the length of a set

my_set = {1, 2, 3, 4, 5}
print("Length of the set:", len(my_set))



# Program to iterate through a set and print its elements

my_set = {"apple", "banana", "cherry"}
print("Elements in the set:")
for item in my_set:
    print(item)



# Program to find the union of two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print("Union of sets:", union_set)



# Program to find the intersection of two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)



# Program to find the difference of two sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

difference_set = set1.difference(set2)
print("Difference of set1 - set2:", difference_set)



# Program to find the symmetric difference of two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

sym_diff = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", sym_diff)



# Program to check if a set is a subset of another set

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print("Is set1 a subset of set2?", set1.issubset(set2))



# Program to check if a set is a superset of another set

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}

print("Is set1 a superset of set2?", set1.issuperset(set2))



# Program to check if two sets are disjoint

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))



# Program to remove all elements of one set from another set

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}

set1.difference_update(set2)
print("Set after removing all elements of set2:", set1)



# Program to create the power set of a given set

import itertools

my_set = {1, 2, 3}
power_set = []

for i in range(len(my_set) + 1):
    power_set.extend(itertools.combinations(my_set, i))

print("Power set of", my_set, "is:", power_set)



# Program to find the Cartesian product of two sets

set1 = {1, 2}
set2 = {'a', 'b'}

cartesian_product = {(x, y) for x in set1 for y in set2}
print("Cartesian Product:", cartesian_product)



# Program to count distinct elements from a list using a set

my_list = [1, 2, 2, 3, 4, 4, 5]
distinct_count = len(set(my_list))
print("Number of distinct elements:", distinct_count)



# Program to find duplicate elements in a list using a set

my_list = [1, 2, 3, 2, 4, 3, 5]
seen = set()
duplicates = {x for x in my_list if x in seen or seen.add(x)}
print("Duplicate elements:", duplicates)



# Program to remove duplicates from a list using a set

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)



# Program to convert a string into a set of characters

text = "python"
char_set = set(text)
print("Set of characters:", char_set)



# Program to find common letters in two strings using sets

str1 = "hello"
str2 = "world"

common_letters = set(str1) & set(str2)
print("Common letters:", common_letters)



# Program to find unique words in a sentence using a set

sentence = "Python is easy and Python is powerful"
unique_words = set(sentence.split())
print("Unique words:", unique_words)



# Program to check if two strings are anagrams using sets

str1 = "listen"
str2 = "silent"

if set(str1) == set(str2):
    print("Strings are anagrams (using sets)")
else:
    print("Strings are not anagrams")



# Program to create a frozen set and demonstrate its properties

fset = frozenset([1, 2, 3, 4])
print("Frozen set:", fset)

# fset.add(5)  # ❌ This will cause an error because frozen sets are immutable
print("Frozen set is immutable and cannot be changed.")



# Program to find maximum and minimum values in a set

my_set = {5, 10, 15, 20, 25}
print("Maximum value:", max(my_set))
print("Minimum value:", min(my_set))



# Program to perform all basic set operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference:", A ^ B)
