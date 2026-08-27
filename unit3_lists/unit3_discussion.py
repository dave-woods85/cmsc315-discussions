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
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    if index <= len(lst):
        lst.insert(index, value) # inserts the value at the specified index
    else:
        lst.insert(len(lst), value) # inserts the value at the end if the index is outside the list
        print(f"The value {value} was placed at the end of the list in index {len(lst)-1} instead of at {index}")



def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if index < len(lst): # check for index that is in range
        print(f"Deleted {lst[index]} from index: {index}.")
        lst.pop(index)
    else:
        print(f"The specified index: {index} is out range for the list. Please use range 0 - {len(lst) -1}")


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    pass


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    my_list = [22, 13, 44, 100, 9]
    # 2. Display the original list.
    print(my_list)
    # 3. Test insertion at:
    #    - the beginning
    insert_at(my_list, 0, 8)
    #    - the middle
    insert_at(my_list, 3, 7)
    #    - the end
    insert_at(my_list, len(my_list), 6)

    # 4. Display the list after each insertion.
    print(my_list)
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    delete_at(my_list, 0)
    print(my_list)
    #    - the middle
    delete_at(my_list, 3)
    print(my_list)
    #    - the end
    delete_at(my_list, len(my_list))
    print(my_list)
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.


    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

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
    delete_at(my_list, 19)
    print(my_list)



if __name__ == "__main__":
    main()