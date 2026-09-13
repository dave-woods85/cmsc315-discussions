"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    if target is None: # handle null case
        return "Please insert an item to search for."
    elif not lst or lst is None: # handle empty/null list
        return "The list is empty."
    else: # perform the linear search and return the index if found, or -1 if not
        index = 0
        for item in lst:
            if item is target:
                return index
            else:
                index += 1
    return -1





def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    if not lst or lst is None: # handles an empty/null list
        return "The list is empty."
    elif target is None: # handles null case
        return "Please insert an item to look for."
    else:
        # initiate index parameters
        low = 0
        high = len(lst) -1
        while low <= high: # search until the high and low indices cross over, indicating the end of the list
            mid = (low + high) // 2 # establishing a new mid each time
            if target is lst[mid]:
                return mid # return the index of the found item
            elif target < lst[mid]:
                high = mid -1 # increment to not include the already searched mid

            else:
                low = mid + 1 # increment to not include the already searched mid
    return -1 # item not found


def print_result(result):
    """
    This is just a formatting method to cleanly separate
    search returns from either search if they are needed
    in their original formats.

    parameter 'result' is whatever the return is from the method used inside
        and is used to identify an index of a found result, not found result,
        or just the result if a string or something else is returned

    """
    if result is int:
        if result == -1:
            print("Item not found in list.")
        else:
            print(f"Item found at index: {result}")
    else:
        print(result)

def shopping_checker(lst, inv_list):
    """
    Cheks on list against an inventory and reports back the items that are not found
    :param lst: the first list to check against the inv_list
    :param inv_list: the inventory list
    :return: Either all items are in stock, or lists the items that are not
    """
    not_in_stock = [] # initialize a list for items not in stock
    if not lst or lst is None: # handle empty/null list
        return "List is empty."
    if not inv_list or inv_list is None: # handle empty/null list
        return "The store is completely out of stock for all items."
    for item in lst: # find each item that is not on the list and add it to not_in_stock
        checked_item = binary_search(inv_list, item)
        if checked_item == -1:
            not_in_stock.append(item) # add item to the not_in_stock list
    if not not_in_stock:
        return "All items in stock!" # if not_in_stock is empty then report that all items are found
    else:
        return f"These items are not in stock: {not_in_stock}" # return the list of items not found


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    small_list = [1, 2, 3, 4, 5, 6] # Small list of numbers
    print(f"This is a small list of numbers: {small_list}")

    # Linear searching
    print("Linear search for 4, which is in the list")
    print_result(linear_search(small_list, 4))
    print("Linear search for 9, which is not in the list")
    print_result(linear_search(small_list, 9))

    # Binary searching
    print("Binary search for 2, which is in the list")
    print_result(binary_search(small_list, 2))
    print("Binary search for 11, which is not in the list")
    print_result(binary_search(small_list, 11))


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Create a list of fruits from A-Z (Gemini was used for this, I'm not that knowledgeable about fruit)
    az_fruit = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Imbe", "Jackfruit",
                "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry",
                "Tangerine", "Ugli", "Voavanga", "Watermelon", "Xigua", "Yuzu", "Zwetschge"]
    # Print the entire list with nice formatting
    print("This is a list of fruits for every letter:")
    for fruit in az_fruit:
        print(f"{fruit[0]}: is {fruit}")

    # Linear searching
    print("Results for \"Watermelon\", which is in the list:")
    print_result(linear_search(az_fruit, "Watermelon"))
    print("Results for \"Blueberry\", which is not in the list:")
    print_result(linear_search(az_fruit, "Blueberry"))

    # Binary searching
    print("Results for \"Yuzu\", which is in the list:")
    print_result(binary_search(az_fruit, "Yuzu"))
    print("Results for \"Blackberry\", which is not in the list:")
    print_result(binary_search(az_fruit, "Blackberry"))

    # Binary search is much more efficient as the dataset becomes larger because it cuts the amount of items searched in
    # half every search iteration

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty_lst = [] # Empty list to test
    one_lst = ["One"] # single element list
    print("Binary Search of a single element list for something on the list, not on the list, and None:")
    print_result(binary_search(one_lst, "One"))
    print_result(binary_search(one_lst, "Two"))
    print_result(binary_search(one_lst, None))

    print("Linear and binary search an empty list:")
    print_result(linear_search(empty_lst, "Pineapple"))
    print_result(binary_search(empty_lst, "Pineapple"))

    print("Binary and linear searches for the first and last elements in the large list:")
    print_result(binary_search(az_fruit, "Apple"))
    print_result(binary_search(az_fruit, "Zwetschge"))
    print_result(linear_search(az_fruit, "Apple"))
    print_result(linear_search(az_fruit, "Zwetschge"))

    print("\n=== REAL WORLD SCENARIO ===")
    print("TODO: Demonstrate a real world scenario.")

    # Checking a shopping list against a store inventory list
    print("This will check my shopping list against the stores fruit inventory (the az_list):")
    shopping_list = ["Banana", "Strawberry", "Mango", "Yuzu", "Orange", "Blackberry", "Tomato", "Durian", "Kiwi"]
    print(f"My shopping list is: {shopping_list}")
    print_result(shopping_checker(shopping_list, az_fruit))
    print_result(shopping_checker(shopping_list, empty_lst))


if __name__ == "__main__":
    main()