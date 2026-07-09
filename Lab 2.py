from collections import deque

# Social Network Graph
graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
}


# -------------------- BFS --------------------
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    print("\n===== BFS Traversal =====")

    while queue:
        current = queue.popleft()

        print("\nCurrent Node :", current)
        print("Queue        :", list(queue))
        print("Visited      :", list(visited))

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Find path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nShortest Path (BFS):")
    print(" -> ".join(path))


# -------------------- DFS --------------------
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    print("\n===== DFS Traversal =====")

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)

            print("\nCurrent Node :", current)
            print("Stack        :", stack)
            print("Visited      :", list(visited))

            if current == goal:
                break

            # Push neighbors in reverse alphabetical order
            for neighbor in sorted(graph[current], reverse=True):
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = current
                    stack.append(neighbor)

    # Find path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nPath Found (DFS):")
    print(" -> ".join(path))


# -------------------- Main Program --------------------
source = "Alice"
goal = "Bob"

bfs(graph, source, goal)
dfs(graph, source, goal)