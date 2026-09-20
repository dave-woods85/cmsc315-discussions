"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.



    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # new empty dictionary
    hash_table =  {}
    # Adding 5 students with student ID keys
    hash_table.update({1 : "Aaron", 2 : "Blake", 3 : "Christopher", 4 : "David", 5 : "Eric"})

    # Similarly to a hash table, a dictionary stores key-value pairs in "buckets".
    # It also has the ability to update values for an existing key.

    print(hash_table)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")
    print("Student Roster:")
    for s in hash_table: # retrieve each individual student from the table
        print(f"ID: {s} Name: " + hash_table.get(s))

    # The lookup uses the provided key and searches the entire table for that key. If it exists the associated value
    # is returned.

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    # Printing the current dictionary
    print("Current Roster:")
    for s in hash_table: # retrieve each individual student from the table
        print(f"ID: {s} Name: " + hash_table.get(s))
    # Updating 2 entries
    hash_table.update({1 : "Alex", 3 : "Charles"})
    # Printing the updated dictionary
    print("Updated Roster:")
    for s in hash_table: # retrieve each individual student from the table
        print(f"ID: {s} Name: " + hash_table.get(s))

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    # Printing the current dictionary
    print("Current Roster:")
    for s in hash_table: # retrieve each individual student from the table
        print(f"ID: {s} Name: " + hash_table.get(s))
    # Removing 2 Students
    del hash_table[1]
    del hash_table[3]
    # printing updated dictionary
    print("Updated Roster:")
    for s in hash_table: # retrieve each individual student from the table
        print(f"ID: {s} Name: " + hash_table.get(s))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Look up missing key
    print(f"Student ID 6: ",  hash_table.get(6))
    # Delete a missing key using pop instead of del for safety
    missing_student = hash_table.pop("Frank", None)
    print("Missing Student: ", missing_student)
    # Updating a missing key essentially adds it to the dictionary
    hash_table.update({6 : "Frank"})
    print("Updated missing key: " + hash_table.get(6))
    # Using an empty dictionary returns, wait for it... an empty dictionary
    empty_dictionary = {}
    print(empty_dictionary)

    print("\n=== REAL WORLD SCENARIO ===")
    # Updating the inventory for a used video game store
    game_inventory = {} # initial inventory is empty
    print("Purchased initial stock from a game collector.")
    # purchasing some initial stock of old games
    day1_bought = {"Rayman" : 3, "Sonic & Knuckles" : 1, "Chrono Trigger" : 4, "Lion King" : 2,
                         "Final Fantasy VI" : 1, "Paper Mario" : 3}
    # update the master inventory with day 1 transactions
    game_inventory.update(day1_bought)
    # print out day 1 transactions
    print("Day 1\nWe bought:")
    for g in game_inventory:
        print(game_inventory.get(g), "copies of", g)
    # print out day 2 transactions
    print("Day2\nWe bought:")
    day2_bought = {"Acro the Acrobat" : 2, "Oddworld: Abe's Odyssey" : 3}
    for g in day2_bought:
        print(day2_bought.get(g), "copies of", g)
        game_inventory.update({g : day2_bought.get(g)}) # update the master inventory

    day2_sold = {"Rayman" : 1, "Paper Mario" : 2}
    print("We sold:")
    for g in day2_sold:
        print(day2_sold.get(g), "copies of", g)
        game_inventory.update({g : game_inventory.get(g) - day2_sold.get(g)}) # update the master inventory quantity

    # print the master inventory after transactions
    print("Current Stock:")
    for g in game_inventory:
        print(game_inventory.get(g), "copies of", g)





if __name__ == "__main__":
    main()