def ucs_cheapest_route(graph, start, goal):
    queue = [(0, [start])]
    visited = []
    explored = []
    while queue:
        queue.sort()
        cost, path = queue.pop(0)
        city = path[-1]
        if city in visited:
            continue
        visited.append(city)
        explored.append(path)
        print("Exploring route:", path, "Cost:", cost)
        if city == goal:
            print("Cheapest route:", path)
            print("Total ticket cost:", cost)
            print("Total routes explored:", len(explored))
            return path, cost
        for next_city, price in graph[city]:
            if next_city not in visited:
                new_path = path + [next_city]
                new_cost = cost + price
                queue.append((new_cost, new_path))
    print("No route found")
    return None, 0
flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": []
}
ucs_cheapest_route(flights, "Islamabad", "Quetta")
