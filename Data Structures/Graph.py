class Graph:
    def __init__(self) -> None:
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def getNodes(self):
        return list(self.adjacentList.keys())

    def addVertex(self, node):
        if node not in self.getNodes():
            self.adjacentList[node] = []
            self.numberOfNodes += 1
        else:
            print("Node already exists")

    def addEdge(self, node1, node2):
        # Undirected Graph
        availableNodes = self.getNodes()
        if node1 in availableNodes and node2 in availableNodes:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
        else:
            print("Either of the nodes are not available")

    def showConnections(self):
        allNodes = self.getNodes()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections += vertex + " "
            print(node + "-->" + connections)

graph = Graph()
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')

graph.addEdge('3', '1')
graph.addEdge('3', '4') 
graph.addEdge('4', '2') 
graph.addEdge('4', '5') 
graph.addEdge('1', '2') 
graph.addEdge('1', '0') 
graph.addEdge('0', '2') 
graph.addEdge('6', '5')

# Graph stucture: 
#  
# 3  ---  4  ---  5
# |       |       |
# 1  ---  2       6
#   \   /
#     0

graph.showConnections()