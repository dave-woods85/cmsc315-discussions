"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack = [] # new empty stack (list)


    def push(self, value):
        # TODO (Student): Add value to the stack.
        try:
            if int(value): # check for proper integer input
                self.stack.append(value) # places the value on the "top" of the stack (which is the end of the list)
        except ValueError:
            print("Please enter an integer")
        # Add a short comment explaining why this operation supports LIFO behavior.
        # placing the item at the top of the stack will ensure that it will be the first item to be removed by popping


    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        if self.is_empty():
            return print("Nothing in stack to pop")
        else:
            popped_item = self.stack[-1]
            del(self.stack[-1])
            return popped_item
        # Improve or explain empty-stack handling.
        # Empty stack is handled by notifying the user that the stack is empty

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        if self.is_empty():
            return print("Nothing in stack to peek at")
        else:
            return self.stack[-1]
        # Add a comment explaining what peek does.
        # Peek returns the top value in the stack without altering the stack

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0 # Returns true if the stack is empty or false if it contains any items



class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        self.queue = [] # Empty list to start with
        # Hint: collections.deque is useful for efficient queue operations.


    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        try:
            if int(value): # check for proper integer input
                self.queue.append(value) # Adds value to the end of the list
        except ValueError:
            print("Please enter an integer")
        # Add a short comment explaining why this operation supports FIFO behavior.
        # this still adds to the end of the list, the difference will be in where we draw the items from


    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        if self.is_empty():
            return print("Nothing in queue to dequeue")
        else:
            dequeued_item = self.queue[0]
            del(self.queue[0]) # remove the item that has been dequeued (which also shifts the rest of the items)
            return dequeued_item
        # Explain or improve empty-queue handling.
        # the if statement checks for an empty list and informs the user


    def front(self):
        # TODO (Student): Return the front value without removing it.
        if self.is_empty():
            return print("This queue is empty")
        else:
            return self.queue[0]
        # Add a comment explaining what front returns.
        # front returns the item at the front of the queue (index 0)

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0 # Returns true if the stack is empty or false if it contains any items



def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
my_stack = Stack() # new stack creation
my_stack.push(4) # adding 4 items to the stack
my_stack.push(90)
my_stack.push(55)
my_stack.push(900)
print(my_stack.stack) # printing the new stack with the 4 items
my_stack.pop() # removing the item last added
my_stack.push(10) # adding another item to the stack
print(my_stack.stack) # proof of LIFO behavior (expected: 4 90 55 10)
print("      test for non integer input,")
my_stack.push('test') # this should inform the user of an improper input
print("      test popping from an empty stack,")
empty_stack = Stack()
empty_stack.pop() # this should inform the user why nothing can be popped
print("      test peeking at an empty stack,")
empty_stack.peek() # this should inform the user that the stack is empty
print("      and verify a single-item stack becomes empty after removal.")
empty_stack.push(1)
print(empty_stack.stack) # showing the addition of a single item
empty_stack.pop()
print(empty_stack.stack) # showing the removal of the single item

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
my_queue = Queue() # new queue creation
my_queue.enqueue(4) # adding 4 items to the queue
my_queue.enqueue(10)
my_queue.enqueue(55)
my_queue.enqueue(123)
print(my_queue.queue) # printing the queue with the 4 items
my_queue.dequeue()
my_queue.enqueue(99)
print(my_queue.queue) # showing FIFO behavior (expected: 10, 55, 123, 99)
print("      testing for non integer input")
my_queue.enqueue("test")
print("      test dequeueing from an empty queue,")
empty_queue = Queue() # create an empty queue
empty_queue.dequeue() # this should inform the user that the queue is empty
print("      test viewing the front of an empty queue,")
empty_queue.front() # this should inform the user that the queue is empty
print("      and verify a single-item queue becomes empty after removal.")
empty_queue.enqueue(1) # adding a single item to the empty queue
print(empty_queue.queue) # showing the item added
empty_queue.dequeue() # removing the single item
print(empty_queue.queue) # proving the item has been removed

if __name__ == "__main__":
    main()

