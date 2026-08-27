"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""
from readline import insert_text


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.

    A: Existing elements are moved to the right from the point of insertion.

    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.

    A: Since the insertion causes all the elements to the right to shift, the more
      elements that are to the right, the more operations need to be performed to
      move them.

    """
    if index <= len(lst):
        lst.insert(index, value) # inserts the value at the specified index
    else:
        lst.insert(len(lst), value) # inserts the value at the end if the index is outside the list
        print(f"The value {value} was placed at the end of the list in index: {len(lst)-1} instead of index: {index}")



def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.

    A: Specifying an index that is out of range will cause an error unless it is handled.

    """
    if index < len(lst): # check for index that is in range
        print(f"Deleted {lst[index]} from index: {index}.")
        return lst.pop(index)
    else:
        print(f"The specified index: {index} is out range for the list. Please use range 0 - {len(lst) -1}")
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.

    A: It is a linear search because it will find the first matching value and stop there. It scans sequentially because
    that is how the items are stored in memory in this type of list, so it's faster to do it that way.

    """
    if value in lst:
        index = lst.index(value)
        print(f"The value: {value} was found at index: {index}.")
        return index
    else:
        print(f"The value: {value} was not found in this list.")
        return -1



def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    # Requirements:
    # 1. Create a list containing several values.
    my_list = [22, 13, 44, 100, 9, 1, 21, 41, 176, 38]
    # 2. Display the original list.
    print("Starting List: ")
    print(my_list)
    # 3. Test insertion at:
    #    - the beginning
    print("Insert at the beginning: ")
    insert_at(my_list, 0, 8)
    print(my_list)
    #    - the middle
    print("Insert in the middle: ")
    insert_at(my_list, int(len(my_list)/2), 7)
    print(my_list)
    #    - the end
    print("Insert at the end: ")
    insert_at(my_list, len(my_list), 6)
    print(my_list)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    print("Deleting from the beginning")
    delete_at(my_list, 0)
    print(my_list)
    #    - the middle
    print("Deleting from the middle")
    delete_at(my_list, int(len(my_list)/2))
    print(my_list)
    #    - the end
    print("Deleting from the end")
    delete_at(my_list, len(my_list)-1)
    print(my_list)



    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    # Requirements:
    # 1. Search for a value that exists.
    print(f"Search a value that exists in: {my_list}")
    search_value(my_list,38)
    # 2. Search for a value that does not exist.
    print(f"Search a value that does not exist in: {my_list}")
    search_value(my_list, 1000)




    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    # inserting a value well outside the length of the list
    print("Inserting a value well outside the list length: ")
    insert_at(my_list, 100, 9999)
    print(my_list)
    # deleting a value outside the length of the list
    print("Deleting a value well outside the list length: ")
    delete_at(my_list, 19)
    print(my_list)

    # ===============================
    # Real World Scenario
    # ===============================
    # Creating a grocery list with items to add to, remove from, and check for items on.

    # Creating a grocery list with a few items
    groceries = ["Brisket", "Milk", "Sesame Oil", "Honey", "Gochujang"]
    print(f"Shopping List: {groceries}")

    # Adding groceries into the list next to a like item
    print("Adding brisket to my list: ")
    insert_at(groceries, search_value(groceries,"Brisket") +1, "Pork Belly")
    print(f"Shopping List: {groceries}")
    # Deleting an item I don't need

    print("Deleting milk from my list")
    delete_at(groceries, search_value(groceries, "Milk"))
    print(f"Shopping List: {groceries}")

    # Checking for an item
    print("Making sure gochujang is on my list")
    search_value(groceries, "Gochujang")

if __name__ == "__main__":
    main()