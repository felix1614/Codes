def shortest_path(graph, start, goal):
    import queue
    dist = {node: float('inf') if node != start else 0 for node in graph}
    predecessor = {node: None for node in graph}
    q = queue.PriorityQueue()
    q.put((0, start))
    path = []

    while not q.empty():
        cur_dist, cur_node = q.get()
        if cur_node == goal:
            break
        for child, weight in graph[cur_node].items():
            if dist[cur_node] + weight < dist[child]:
                dist[child] = dist[cur_node] + weight
                predecessor[child] = cur_node
                q.put((dist[child], child))

    if dist[goal] != float('inf'):
        current = goal
        while current != start:
            if current not in predecessor:
                print("Path not found")
                return
            path.append(current)
            current = predecessor[current]
        path.append(start)
        print(f"Shortest Path: {' -> '.join(path[::-1])}")
        print(f"Weight: {dist[goal]}")
    else:
        print("Path not found")


graph_ = {"a": {"b": 10, "c": 3},
          "b": {"c": 1, "d": 2},
          "c": {"b": 4, "d": 8, "e": 2},
          "d": {"e": 7},
          "e": {"d": 7}}

shortest_path(graph_, "a", "d")
