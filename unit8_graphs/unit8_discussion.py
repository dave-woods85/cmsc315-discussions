"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque, defaultdict


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # create an empty queue for the vertices
    frontier_queue = deque([start])
    # create a list of visited nodes
    visited_nodes = []
    if graph == [] or start == "" or start is None:
        return "List empty or no starting node"
    # while there are items in the queue, continue traversing
    while frontier_queue:
        current_node = frontier_queue.popleft() # grab the next item in the queue
        if current_node not in visited_nodes:
            visited_nodes.append(current_node) # add this node to visited list
        for e in graph[current_node]: # traverse all adjacent
            if e not in visited_nodes:
                frontier_queue.append(e) # add new nodes to queue
    return visited_nodes


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # draw the graph out by connected edges
    my_graph_edges = [("A", "B"), ("A", "C"), ("A", "D"),
                ("B", "D"), ("B" , "E"), ("C", "F"), ("D", "F")]

    # create a dictionary to hold vertices and their adjacent nodes
    my_graph = defaultdict(list)

    # for each vertex, add their adjacent nodes to their dict
    # slot in both directions since this is not a digraph
    for x, y in my_graph_edges:
        my_graph[x].append(y)
        my_graph[y].append(x)

    # neatly print out each vertex and its adjacent nodes
    for vertex, adjacent in my_graph.items():
        print(f"Vertex {vertex} is adjacent to {adjacent}.")



    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")
    print("Traversal from start node C:")
    print(bfs(my_graph, "C"))
    # Because BFS uses a queue, the first adjacent nodes encountered will be
    # the next set of nodes visited, which by nature is the next closest node

    # add an additional node connected to D
    my_graph["D"].append("G")
    my_graph["G"].append("D")
    print("Traversal from start node C after adding a new node:")
    print(bfs(my_graph, "C"))


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    # Traversal from a different starting node (the last node)
    print("Traversal from start node G:")
    print(bfs(my_graph, "G"))

    # Empty graph and node test
    print("Testing empty graph and node:")
    my_empty_graph = []
    print(bfs(my_empty_graph, ""))



if __name__ == "__main__":
    main()