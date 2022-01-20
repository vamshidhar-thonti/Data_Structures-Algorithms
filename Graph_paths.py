# Input:
    # 4 -> n
    # 2 -> m1
    # 5 -> m2
    # 7 -> m3
    # 9 -> m4
    # 4 -> n edges
    # 2 9 -> 2 to 9
    # 7 2 -> 7 to 2
    # 7 9 -> 7 to 9
    # 9 5 -> 9 to 5
    # 7 -> start point
    # 9 -> end point

# Output:
#     1 if path between 7 and 9 exists else 0

from cmath import inf


class Path:
    # def __init__(self, members, edges):
    #     self.graph = dict()
    #     for member in members:
    #         if member not in self.graph:
    #             self.graph[member] = []
    #     for edge in edges:
    #         self.graph[edge[0]].append(edge[1])
        
    def find_path(self, graph, follower, following):
        stack = graph[follower]
        visited = dict()
        visited[follower] = True
        while len(stack) != 0:
            if following in stack:
                return 1
            deep = stack.pop()
            visited[deep] = True
            for n in graph[deep]:
                if n not in visited:
                    stack.append(n)
        return 0
    
    # TO DO
    def shortest_path(self, graph, follower, following):
        visited = set()
        s_path = []
        edge_sum = []
        def _search(graph, follower, path):
            if follower not in path:
                path.append(follower)
                for node, edge in graph[follower]:
                    _search(graph, node, path)
        _search(graph, follower, s_path)
        print(s_path)
            
        
graph1 = {
    2: [(9, 2), (5, 6)],
    5: [],
    7: [(2, 3), (9, 7)],
    9: [(5, 1)]
}

graph2 = {
    2: [9],
    5: [],
    7: [2, 9],
    9: [5]
}

graph3 = {
    1: [(5, 1), (9, 5)],
    2: [(5, 4)],
    4: [(1, 2), (8, 3)],
    5: [(7, 6)],
    7: [(9, 1)],
    8: [],
    9: [(10, 4), (2, 2), (4, 6)],
    10: [(8, 7)],
}

follower = 2
following = 8

# n_members = int(input())
# members = [int(input()) for _ in range(n_members)]

# n_edges = int(input())
# edges = [tuple(map(int, input().split(' '))) for _ in range(n_edges)]

# follower = int(input())
# following = int(input())

# print(members, edges, follower, following)

path = Path()
# print(path.find_path(graph2, follower, following))
print(path.shortest_path(graph3, follower, following))