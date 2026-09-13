# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

I already knew how to perform a linear search, but of course that was not the complex part of this project. The binary
search was much more interesting because I had to handle the changing of the search indices  while keeping in mind that
either the high or low needed to update so the middle search index wasn't reused. The lesson material was helpful
for this as they have a Java example that I was able to get a hint from.

2. What challenges did you encounter, and how did you overcome them?

The challenges revolved around handle the null or empty list cases, or rather remembering to handle them. The other
challenge was the proper updating of the search indices for the binary search as mentioned above. The last part was
having some kind of decent formatting for the results of the searches, which I made a separate method to handle. For
instance, I didn't want to just print out -1 if an item was not found but still wanted that to be the return from 
the search method. The print_results() method simply translated a -1 to a readable statement.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

Linear search is good for short lists or for things that just happen to be at the front of the list, but its the most
adept for searching unsorted lists when compared to binary searching. Binary searching finds its strength with large
sorted datasets, as it can drastically reduce the amount of items searched. For the shopping list, when searching for
the last item in the list or an item not on the list, the linear search would have to search every item, but the binary 
search would only have to search a fraction of them.