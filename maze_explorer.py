def dfs_can_reach(maze, start, exit_room):
    visited = []
    def dfs(room):
        visited.append(room)
        if room == exit_room:
            return True
        for next_room in maze[room]:
            if next_room not in visited:
                if dfs(next_room):
                    return True
        return False
    result = dfs(start)
    print("Visit order:", visited)
    print("Can reach", exit_room, "from", start + "?", result)
    return result
maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": []
}
dfs_can_reach(maze, "Entrance", "Exit")
