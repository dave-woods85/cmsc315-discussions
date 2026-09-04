# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

RECURSION!! Holy crap this broke my brain for a while until it finally clicked. I struggled with this for most of the
day and I can see why my software engineer friends are not fond of having to do it. but, I can also see the benefits
of using methods in that way.

2. What challenges did you encounter, and how did you overcome them?

As mentioned above, setting up the recursive methods was really difficult for me to understand at first. While I'm by
no means an expert, I think I have a much better grasp on how to set them up. I was also a bit confused as to how I 
was supposed to use the predetermined signature for the _inorder_recursive() method since it had a value argument. But,
I eventually got it. Also, it was really confusing to me how you have to call the recursive method on the main BST, and
not the individual nodes. I'm still not 100% sure how it knows to move on to the next node by calling the BST every time.

3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

BST is a really efficient way to organize values that allows for rapid searching with the fewest amount of queries. The
ordering looks random at first but, it does have sound logic once you begin to traverse the tree. The one thing I worry
about is having to rebalance a tree once values have been added, removed and moved around. Obviously the closer the BST
is to perfect, the more effectively it can be used. As far as the other data structure types, they mostly have to be
searched linearly which can become very cumbersome as the list grows very large. The fact that the binary tree (if 
it is balanced well enough) can reduce the amount of queries down to the base 2 log of the amount of items in it is
really impressive. I would relate it to the efficiency of guessing by using the 20 questions game. It's much easier
to narrow the thing they are thinking of by thinking of this or that style questions (kind of like binary).