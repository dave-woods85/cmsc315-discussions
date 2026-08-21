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
        self.stack = [] # new empty stack
        self._firstIndex = 0 # index of the last item placed onto the stack (the top)

    def push(self, value):
        # TODO (Student): Add value to the stack.
        self.stack.append(value) # places the value on the "top" of the stack
        self._firstIndex = self.stack[len(self.stack) -1] #update the index for the top of the stack
        # Add a short comment explaining why this operation supports LIFO behavior.
        # placing the item at the top of the stack will ensure that it will be the first item to be removed by popping


    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        if len(self.stack) == 0:
            print("Nothing in stack")
        else:
            popped_item = self.stack[self._firstIndex]
            del[self._firstIndex]
            return popped_item
        # Improve or explain empty-stack handling.
        # Empty stack is handled by notifying the user that the stack is empty

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        return self.stack[self._firstIndex]
        # Add a comment explaining what peek does.
        # Peek returns the top value in the stack without altering the stack

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0 # Returns true if the stack is empty or false if it contains any items


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        pass

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        pass


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
my_stack = Stack()
my_stack.push(4)
my_stack.push(90)
my_stack.push(55)
print(my_stack)
my_stack.pop()
my_stack.push(10)
print(my_stack)
print("      test popping from an empty stack,")
empty_stack = Stack()
my_stack.pop()
print("      test peeking at an empty stack,")
my_stack.peek()
print("      and verify a single-item stack becomes empty after removal.")
empty_stack.push(1)
print(empty_stack)
empty_stack.pop()
print(empty_stack)

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
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

if __name__ == "__main__":
    main()

