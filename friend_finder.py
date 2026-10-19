def bfs_shortest_path(graph, start, goal):
    queue = [[start]]
    visited = [start]
    while queue:
        path = queue.pop(0)
        person = path[-1]
        if person == goal:
            return path
        for friend in graph[person]:
            if friend not in visited:
                visited.append(friend)
                queue.append(path + [friend])
    return None
network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira", "Ahmed"],
    "Omar": ["Sara"],
    "Hira": ["Zara"],
    "Ahmed": ["Zara"]
}
result = bfs_shortest_path(network, "Ali", "Hira")
if result:
    print("Shortest chain from Ali to Hira:", result)
    print("Number of introductions needed:", len(result) - 1)
else:
    print("No connection found between Ali and Hira.")
