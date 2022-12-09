# 400 invalid syntax  -> bad request
# 401 unauthorized
# 403 forbidden
# 404 not found
# 500 internal server error
# 501 invalid response
# 502 bad gateway
# import heapq
# from collections import defaultdict
#
#
# def shortes(graph, src, des):
#     h = []
#     heapq.heappush(h, (0, src))
#     # path = []
#     while len(h) != 0:
#         currcost, currvtx = heapq.heappop(h)
#         # path += currvtx,
#         if currvtx == des:
#             print(f"path {src} to {des} with cost {currcost}")
#             print(path)
#             break
#         for neigh, neighcost in graph[currvtx]:
#             heapq.heappush(h, (currcost + neighcost, neigh))
#
#
# graph = defaultdict(list)
# # v, e = map(int, input().split())
# e = int(input("Enter no of path:"))  # length of the dict
# for i in range(e):
#     mainNode, key, weight = input("Enter src node, neighbour node and weight: ").split()
#     graph[mainNode].append((key, int(weight)))
# src, dec = input("Enter SCR and DES: ").split()
# shortes(graph, src, dec)
# import heapq
# from collections import defaultdict
#
#
# def short(graph, src, des):
#     heap = []
#     heapq.heappush(heap, (0, src))
#     while len(heap) != 0:
#         currWeight, currNode = heapq.heappop(heap)
#         if currNode == des:
#             print(f"shortest path between {src} - {des} is {currWeight}")
#             break
#
#         for nighbour, neighbourWeigh in graph[currNode]:
#             heapq.heappush(heap, (currWeight+neighbourWeigh, nighbour))
#
#
# graph = defaultdict(list)
# length = int(input())
# for i in range(length):
#     node, neighbour, weight = input().split()
#     graph[node] += (neighbour, int(weight)),
#
# src, des = input().split()
# short(graph, src, des)
#


"""
7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 3
E D 4
A D
"""


def short(graph, start, goal):
    shortestDist = {}
    predessor = {}
    unseenNodes = graph
    infinity = 999999
    path = []
    for nodes in unseenNodes:
        shortestDist[nodes] = infinity
    shortestDist[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortestDist[node] < shortestDist[minNode]:
                minNode = node
        for child, weight in graph[minNode].items():
            if weight + shortestDist[minNode] < shortestDist[child]:
                shortestDist[child] = weight + shortestDist[minNode]
                predessor[child] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predessor[currentNode]

        except KeyError:
            print("path unreachable")
            break

    path.insert(0, start)
    if shortestDist[goal] != infinity:
        print(f"weight: {str(shortestDist[goal])}")
        print(f"path: {'->'.join(path)}")


graph = {"a": {"b": 10, "c": 3},
         "b": {"c": 1, "d": 2},
         "c": {"b": 4, "d": 8, "e": 2},
         "d": {"e": 7},
         "e": {"d": 9}}

short(graph, "b", "d")