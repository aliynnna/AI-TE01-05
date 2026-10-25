import heapq

def ucs(graph, start, goal):
    # priority queue: (cost, current_path)
    pqueue = [(0, [start])]
    visited = {}

    while pqueue:
        cost, path = heapq.heappop(pqueue)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, edge_cost in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(pqueue, (cost + edge_cost, new_path))
    return None, float('inf')

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 3)],
        'D': [('F', 6)],
        'E': [('F', 1)],
        'F': []
    }
    path, cost = ucs(graph, 'A', 'F')
    print(f"UCS Path: {' -> '.join(path)} (Total Cost: {cost})")
