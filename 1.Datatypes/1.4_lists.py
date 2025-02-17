# 1. Creating and Printing a List
def create_and_print_list():
    List = [1, 2, 3, 4, 5]  # List is used to store multiple values in a single variable
    print("List:", List)
    print("Length of List:", len(List))  # Prints length of list
    return List

# 2. Accessing List Elements
def access_list_elements(List):
    print("Full List:", List)  # [1, 2, 3, 4, 5]
    print("Element at index 2:", List[2])  # 3
    print("Element at index -2:", List[-2])  # 4
    print("Slicing from index 1 to 4:", List[1:4])  # [2, 3, 4]
    print("Slicing from index 2 to end:", List[2:])  # [3, 4, 5]
    print("Slicing from index -4 to -2:", List[-4:-2])  # [2, 3]
    print("Is 1 in List?", 1 in List)  # True
    print("Is 11 in List?", 11 in List)  # False

# 3. Inserting Elements into a List
def insert_elements(List):
    List.append(6)  # Inserts element at the end
    print("After append:", List)  # [1, 2, 3, 4, 5, 6]
    List.extend([7, 8, 9])  # Inserts multiple elements at the end
    print("After extend:", List)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    List.insert(0, 0)  # Inserts element at a specific index
    print("After insert:", List)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. Modifying List Elements
def modify_list():
    fruitsList = ["apple", "banana", "mango"]
    fruitsList[1] = "melon"  # Modifies element at index 1
    print("After modifying index 1:", fruitsList)  # ["apple", "melon", "mango"]
    fruitsList[1:2] = ["grapes", "orange"]  # Replaces elements from index 1 to 2
    print("After replacing slice:", fruitsList)  # ["apple", "grapes", "orange", "mango"]
    return fruitsList

# 5. Removing Elements from a List
def remove_elements(fruitsList):
    fruitsList.pop()  # Removes last element
    print("After pop:", fruitsList)  # ['apple', 'grapes', 'orange']
    fruitsList.pop(1)  # Removes element at index 1
    print("After pop at index 1:", fruitsList)  # ['apple', 'orange']
    fruitsList.remove("orange")  # Removes specific element
    print("After remove:", fruitsList)  # ['apple']
    del fruitsList[0]  # Deletes element at index 0
    print("After del:", fruitsList)  # []
    fruitsList.append("apple")
    fruitsList.clear()  # Clears all elements
    print("After clear:", fruitsList)  # []
    del fruitsList  # Deletes the list

# 6. Sorting a List
def sort_list():
    List = [1, 5, 7, 8, 4]
    List.sort()  # Sorts in ascending order
    print("Sorted List (ascending):", List)  # [1, 4, 5, 7, 8]
    List.sort(reverse=True)  # Sorts in descending order
    print("Sorted List (descending):", List)  # [8, 7, 5, 4, 1]
    print("Reversed List using slicing:", List[::-1])  # [1, 4, 5, 7, 8]
    List.sort(key=lambda x: x + 1)  # Sorts based on a custom function
    print("Sorted List with custom key:", List)  # [1, 4, 5, 7, 8]

# 7. Copying a List
def copy_list():
    List = [1, 4, 5, 7, 8]
    copyList = List.copy()  # Creates a shallow copy
    copyList.append(2)
    print("Copied List:", copyList, "Original List:", List)  # [1, 4, 5, 7, 8, 2] [1, 4, 5, 7, 8]

    copyList1 = List  # Creates a reference to the same list
    copyList1.append(2)
    print("Reference List:", copyList1, "Original List:", List)  # [1, 4, 5, 7, 8, 2] [1, 4, 5, 7, 8, 2]

    copyList2 = List[:]  # Creates a shallow copy using slicing
    copyList2.append(3)
    print("Sliced Copy:", copyList2, "Original List:", List)  # [1, 4, 5, 7, 8, 2, 3] [1, 4, 5, 7, 8, 2]

    copyList3 = list(List)  # Creates a shallow copy using the list constructor
    copyList3.append(6)
    print("List Constructor Copy:", copyList3, "Original List:", List)  # [1, 4, 5, 7, 8, 2, 6] [1, 4, 5, 7, 8, 2]

# 8. Joining Lists
def join_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 3]
    list3 = list1 + list2  # Joins two lists
    print("Joined List:", list3)  # [1, 2, 3, 4, 5, 6, 3]
    print("Count of 3 in List:", list3.count(3))  # Counts occurrences of 3

# Function Calls
if __name__ == "__main__":
    List = create_and_print_list()
    access_list_elements(List)
    insert_elements(List)
    fruitsList = modify_list()
    remove_elements(fruitsList)
    sort_list()
    copy_list()
    join_lists()