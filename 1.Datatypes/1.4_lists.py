List = [1,2,3,4,5] # List is used to multiple values in single variable

print(len(List)) # Prints length of list 5

#Accessing List

print(List)  # [1,2,3,4,5]
print(List[2]) # 3
print(List[-2]) # 4
print(List[1:4]) # [2,3,4]
print(List[2:]) #[3,4,5]
print(List[-4:-2]) #[2,3]
print(1 in List) # True
print(11 in List) # False

# Inserting Elements

List.append(6) # Inserts Elements at last 
print(List) # [1,2,3,4,5,6]
List.extend([7,8,9]) # Inserts List of Elements at last  it also accepts tuple
print(List) # [1,2,3,4,5,6,7,8,9]
List.insert(0,1) # Inserts element at Particular index
print(List) # [0,1,2,3,4,5,6,7,8,9]

fruitsList = ["apple", "banana", "mango"]
fruitsList[1]="melon"
print(fruitsList) # ["apple", "melon", "mango"]
fruitsList[1:2]=["grapes","orange"]
print(fruitsList) # ["apple", "grapes","orange", "mango"]

# Removing Elements

fruitsList.pop()  # Remove last element
print(fruitsList) # ['apple', 'grapes', 'orange']
fruitsList.pop(1)  # Removes element at 1st index
print(fruitsList) # ['apple', 'orange']
fruitsList.remove("orange") # Removes the element that present in list
print(fruitsList) # ['apple']
del fruitsList[0] # Removes 0th Element
fruitsList.append("apple")
fruitsList.clear() # clears all the elements in the list
print(fruitsList) 
del fruitsList # Delete the list


# Sort list

List  = [1,5,7,8,4]
List.sort()
print(List) # [1,4,5,7,8]
List.sort(reverse=True)
print(List) # [8,7,5,4,1]
print(List[::-1]) # [1,4,5,7,8] also used to reverse
List.sort(key=lambda x: x + 1) # sorts with order with given function
print(List)


# Copy

copyList = List.copy()
copyList.append(2)
print(copyList, List) # [1, 4, 5, 7, 8, 2] [1, 4, 5, 7, 8]

copyList1 = List
copyList1.append(2)
print(copyList1,List) # [1, 4, 5, 7, 8, 2] [1, 4, 5, 7, 8, 2]

copyList2 = List[:]
copyList2.append(3)
print(copyList2,List) # [1, 4, 5, 7, 8, 2, 3] [1, 4, 5, 7, 8, 2]

copyList2 = list(List)
copyList2.append(6)
print(copyList2,List) # [1, 4, 5, 7, 8, 2, 3, 6] [1, 4, 5, 7, 8, 2]

# Join 2 lists

list1 = [1,2,3]
list2 = [4,5,6,3]
list3 = list1+ list2 
print(list3) # [1, 2, 3, 4, 5, 6, 3]

print(list3.count(3)) # counts no of elements 2