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



