# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

This assignment was relatively easy since we didn't have to create any functions. I basically learned how to use Python's
built-in dictionary functionality, which is useful!

2. What challenges did you encounter, and how did you overcome them?

No real challenges here other than looking up what functions/methods were available for Python's dictionary and then
making sure to the get syntax right. I tried to challenge myself with the real-world scenario by using a for loop to
update the dictionary values for a master inventory based on the days transactions.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

Has tables behave like the Python dictionary where a key-value pair can be inserted. It appears, just based off my
limited testing that Python's dictionary uses a linear method for insertion as adding to the dictionary simply appends
to the end. Collisions happen when two items attempt to occupy the same bucket. Has tables can deal with this in a few
different ways to include:
- chaining: adding multiple items to a bucket
- open addressing: various probing methods to search for empty buckets