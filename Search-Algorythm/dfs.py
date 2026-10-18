def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    path = dfs(graph, 'A', 'F')
    print("DFS Path:", " -> ".join(path) if path else "Not found")