"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""
from random import random
import time

def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    temp_list = lst.copy() # create new list
    for s in range(len(temp_list) -1): # iterate through list
        for r in range(len(temp_list) - 1 - s): # iterate through adjacent
            if temp_list[r] > temp_list[r + 1]: # check and swap
                temp_item = temp_list[r]
                temp_list[r] = temp_list[r + 1]
                temp_list[r + 1] = temp_item

    return temp_list




def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # establish indices
    start_index = 0
    end_index = len(lst) - 1
    if len(lst) == 1: # return the list if it is only one element
        return lst
    mid_index = (start_index + end_index) // 2 # find middle
    left = lst[0: mid_index + 1] # create a left list
    right = lst[mid_index + 1: end_index + 1] # create a right list
    # recursively break the list down and create a left and right list
    left_sort = merge_sort(left)
    right_sort = merge_sort(right)

    return merge(left_sort, right_sort) # merge the left and right back together, sorting each time




def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    merged = [] # empty list to append to
    # create indices
    left_pos = 0
    right_pos = 0

    while left_pos < len(left) and right_pos < len(right): # check to see if both sides have items
        if left[left_pos] < right[right_pos]: # append the left if it is a smaller value and increment the index
            merged.append(left[left_pos])
            left_pos += 1
        else:
            merged.append(right[right_pos]) # otherwise append the right and increment the index
            right_pos += 1
    for i in range(len(left) - left_pos): # append any remaining items from the left
        merged.append(left[left_pos])
        left_pos += 1
    for i in range(len(right) - right_pos): # append any remaining items from the right
        merged.append(right[right_pos])
        right_pos += 1
    return merged # return the assembled list



def print_wrap(lst, size):
    """
    Prints out a list at a designated wrap size (number of items per line)
    """
    remains = lst.copy() # Copy the passed list
    while len(remains) >= size: # Check for entire printable line
        print(remains[0 : size])
        del remains[0 : size] # remove the printed line from the list
    if remains:
        print(remains) # print the rest of the list under the wrap size if not None



def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    random_list = []
    for i in range(100): # create a randomly generated list of 100 items from 0-99
        random_list.append(int(random() * 100))
    print("Random Unsorted List:")
    print_wrap(random_list, 20) # print out the list 20 items per line
    start_time = int(time.time() * 1000)
    print("Bubble Sorted List:")
    print_wrap(bubble_sort(random_list), 20) # print the sorted list 20 items per line
    print("Time elapsed: ", (time.time() * 1000) - start_time, "ms") # show the time it took
    start_time = int(time.time() * 1000)
    print_wrap(merge_sort(random_list), 20) # print the sorted list 20 items per line
    print("Time elapsed: ", (time.time() * 1000) - start_time, "ms") # show how long it took




    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    print("2nd Dataset will be the real-world scenario.")
    print("Alphabetizing a list of 100 applicant names!")
    # AI was used to generate this list... I don't think I could come up with 100 names haha
    names = [
        "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William", "Sophia",
        "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alexander", "Harper",
        "Mason", "Camila", "Michael", "Gianna", "Ethan", "Abigail", "Daniel", "Luna", "Jacob", "Ella",
        "Logan", "Elizabeth", "Jackson", "Sofia", "Levi", "Avery", "Sebastian", "Scarlett", "Mateo", "Eleanor",
        "Jack", "Madison", "Owen", "Layla", "Theodore", "Penelope", "Aiden", "Aria", "Samuel", "Chloe",
        "Joseph", "Grace", "John", "Ellie", "David", "Nora", "Wyatt", "Hazel", "Matthew", "Zoey",
        "Luke", "Riley", "Asher", "Janis", "Carter", "Aurora", "Julian", "Lily", "Grayson", "Nova",
        "Leo", "Hannah", "Jayden", "Emilia", "Gabriel", "Zoe", "Isaac", "Stella", "Lincoln", "Elena",
        "Anthony", "Paisley", "Hudson", "Audrey", "Dylan", "Maya", "Christopher", "Elizabeth", "Joshua", "Naomi",
        "Andrew", "Bella", "Lincoln", "Natalie", "Jonathan", "Charlotte", "Caleb", "Alice", "Ryan", "Eva"
    ]
    # print the unsorted names list
    print("Unsorted Names List:")
    print_wrap(names, 10)

    # print the Bubble Sorted list
    print("Bubble Sorted Names List:")
    start_time = int(time.time() * 1000)
    print_wrap(bubble_sort(names), 10)
    print("Time elapsed: ", (time.time() * 1000) - start_time, "ms") # show how long it took

    # print the Merge Sorted list
    print("Merge Sorted Names List:")
    start_time = int(time.time() * 1000)
    print_wrap(merge_sort(names), 10)
    print("Time elapsed: ", (time.time() * 1000) - start_time, "ms") # show how long it took


# ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")




if __name__ == "__main__":
    main()