# 1. Create and Print a Set
def create_and_print_set():
    Set = {"car", "bike", "boat", "plane", "bike"}  # Set items are unordered, unchangeable, and do not allow duplicate values.
    print("Set:", Set)
    print("Length of Set:", len(Set))  
    return Set

# 2. Demonstrate Exceptional Behavior of Sets
def exceptional_set():
    Set = {True, 22, "apple", 1}  # Set accepts all kinds of data types
    print("Set:", Set)  # Both True and 1 are considered the same value (same for False and 0). The first occurrence will be in the set.

# 3. Access Set Elements
def access_set_elements(Set):
    print("Full Set:", Set)  # {'plane', 'bike', 'boat', 'car'}
    for value in Set:
        print(value)
    print("Is boat in Set?", "boat" in Set)  # True
    print("Is train in Set?", "train" in Set)  # False

# 4. Insert and Modify Set Elements
def insert_and_modify_elements(Set):
    Set.add("bus")  # Adds a single element
    print("After add:", Set)  # {'boat', 'bus', 'car', 'plane', 'bike'}
    
    newSet = {"train", "helicopter"}
    Set.update(newSet)  # Adds elements from another set
    print("After update:", Set)  # {'plane', 'bus', 'helicopter', 'boat', 'bike', 'car', 'train'}
    
    Set.update(["bicycle", "scooty"])  # Adds elements from a list
    print("After updating list in set:", Set)  # {'bike', 'plane', 'boat', 'bicycle', 'bus', 'train', 'car', 'helicopter', 'scooty'}
    
    Tuple = ("jeep", "choper")
    Set.update(Tuple)  # Adds elements from a tuple
    print("After updating tuple in set:", Set)  # {'bike', 'plane', 'boat', 'bicycle', 'bus', 'train', 'jeep', 'choper', 'car', 'helicopter', 'scooty'}

# 5. Remove Elements from a Set
def remove_elements(Set):
    Set.remove('choper')  # Removes 'choper' from the set
    print("After removing choper element:", Set)  
    
    Set.discard('jeep')  # Removes 'jeep' from the set (no error if not found)
    print("After removing jeep element:", Set) 
    
    Set.pop()  # Removes a random element
    print("After pop:", Set)  
    
    Set.clear()  # Clears all elements from the set
    print("After clear:", Set)  # set()
    
    del Set  # Deletes the set

# 6. Join Sets
def join_sets():
    set1 = {"apple", "banana", "cucumber"}
    set2 = {1, 2, 3}
    
    # Union of sets
    unionset1 = set1.union(set2)  # Joins both sets into a new set
    unionset2 = set1 | set2  # | is also used for union
    print("Union of sets:", unionset1, unionset2)  # {1, 'cucumber', 2, 3, 'apple', 'banana'}
    
    # Union of multiple sets
    set3 = {"John", "Elena"}
    set4 = {"apple", "bananas", "cherry"}
    myset = set1.union(set2, set3, set4)  # Joins multiple sets
    print("Union of multiple sets:", myset)
    
    # Union with a list
    list1 = [33, 44, 55]
    myset = myset.union(list1)  # Joins a list to the set
    print("Union with a list:", myset)  # {1, 2, 3, 'c', 33, 'b', 'bananas', 'cherry', 44, 'John', 'apple', 55, 'Elena', 'a'}
    
    # Intersection of sets
    set1 = {"apple", "banana", "cucumber"}
    set2 = {"grape", "mango", "apple"}
    intersectionset1 = set1.intersection(set2)  # Returns common elements
    intersectionset2 = set1 & set2  # & is also used for intersection
    print("Intersection of sets:", intersectionset1, intersectionset2)  # {'apple'}
    
    # Disjoint check
    print("Are sets disjoint?", set1.isdisjoint(set2))  # Returns True if no common elements
    
    # Intersection update
    set1.intersection_update(set2)  # Updates set1 with the intersection result
    print("After intersection update:", set1)  # {'apple'}
    
    # Difference of sets
    set1 = {"apple", "banana", "cucumber"}
    set2 = {"grape", "mango", "apple"}
    differenceset1 = set1.difference(set2)  # Returns elements in set1 not in set2
    differenceset2 = set1 - set2  # - is also used for difference
    print("Difference of sets:", differenceset1, differenceset2)  # {'banana', 'cucumber'}
    
    # Difference update
    set1.difference_update(set2)  # Updates set1 with the difference result
    print("After difference update:", set1)  # {'banana', 'cucumber'}
    
    # Symmetric difference
    symmetricdifference1 = set1.symmetric_difference(set2)  # Returns elements not in both sets
    symmetricdifference2 = set1 ^ set2  # ^ is also used for symmetric difference
    print("Symmetric difference of sets:", symmetricdifference1, symmetricdifference2)  # {'banana', 'cucumber', 'grape', 'mango'}
    
    # Symmetric difference update
    set1.symmetric_difference_update(set2)  # Updates set1 with the symmetric difference result
    print("After symmetric difference update:", set1)  # {'banana', 'cucumber', 'grape', 'mango'}
    
    # Superset check
    set1 = {"grape", "mango", "apple", "banana", "cucumber"}
    set2 = {"apple", "banana", "cucumber"}
    print("Is set1 a superset of set2?", set1.issuperset(set2))  # True
    print("Is set1 a superset of set2?", set1 >= set2)  # >= is also used for superset
    
    # Subset check
    print("Is set1 a subset of set2?", set1.issubset(set2))  # False
    print("Is set1 a subset of set2?", set1 <= set2)  # <= is also used for subset

# 7. Frozen Set
def frozen_set():
    FrozenSet = frozenset((1, 2, 3))  # Returns an unchangeable frozenset object
    ListFrozenList = frozenset([1, 2, 3, 4])  # Accepts list, set, or tuple
    print("FrozenSet:", FrozenSet, "ListFrozenList:", ListFrozenList) 
    
    # Frozenset supports union, intersection, symmetric_difference, issubset, issuperset, isdisjoint
    # It does not support update-related functions because it is unchangeable

# Main Function
if __name__ == "__main__":
    Set = create_and_print_set()
    exceptional_set()
    access_set_elements(Set)
    insert_and_modify_elements(Set)
    remove_elements(Set)
    join_sets()
    frozen_set()