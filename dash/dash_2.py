def short(graph, src, des):
    predecessor, unseenNodes, shortestNodes, infinity, path = {}, graph, {}, 999999, []
    for node in unseenNodes:
        shortestNodes[node] = infinity
    shortestNodes[src] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortestNodes[node] < shortestNodes[minNode]:
                minNode = node
        for child, weight in graph[minNode].items():
            if weight + shortestNodes[minNode] < shortestNodes[child]:
                shortestNodes[child] = weight + shortestNodes[minNode]
                predecessor[child] = minNode
        unseenNodes.pop(minNode)

    currNode = des
    while currNode != src:
        try:
            path.insert(0, currNode)
            currNode = predecessor[currNode]
        except KeyError:
            print("invalid path")
            break

    path.insert(0, src)
    if shortestNodes[des] != infinity:
        print(shortestNodes[des])
        print(path)


graph = {"a": {"b": 2, "c": 3},
         "b": {"d": 3, "c": 5},
         "c": {"e": 6, "a": 5},
         "d": {"e": 4},
         "e": {"a": 6}}
# graph = {"a": {"b": 10, "c": 3},
#          "b": {"c": 1, "d": 2},
#          "c": {"b": 4, "d": 8, "e": 2},
#          "d": {"e": 7},
#          "e": {"d": 9}}

short(graph, "a", "e")
