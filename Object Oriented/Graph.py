class Graph:

    def __init__(self):
        self.adjList = {}
    # create a dictionary with name adjlst
    
    def __addSingleVertex(self, node):
        if node not in self.adjList.keys():
            self.adjList[node] = []
    #if node not in dictionary Create a list for node
    
    def addVertices(self, nodes):
        if type(nodes) == list:
            for node in nodes:
                self.__addSingleVertex(node)
        elif type(nodes) == str:
            self.__addSingleVertex(nodes)

    def addPath(self, node1, node2):
        if node1 in self.adjList.keys() and node2 in self.adjList.keys():
            if node1 in self.adjList[node2] or node2 in self.adjList[node1]:
                return
            else:
                self.adjList[node1].append(node2)
                self.adjList[node2].append(node1)

    def rmNode(self, node):
        if node in self.adjList.keys():
            for i in self.adjList[node]:
                self.adjList[i].remove(node)
            self.adjList.pop(node)

    def rmEdge(self, node1, node2):
        if node1 in self.adjList.keys() and node2 in self.adjList.keys():
            if node1 in self.adjList[node2] or node2 in self.adjList[node1]:
                self.adjList[node1].remove(node2)
                self.adjList[node2].remove(node1)

    def isConnected(self):
        n = 0
        for node in self.adjList.keys():
            if len(self.adjList[node]) == 0:
                return print('False')
            elif len(self.adjList[node]) == 1:
                n += 1

        if n > 2:
            return print('False')
        else:
            return print('True')

    def shortestPath(self, node1, node2):
        path = [node1]
        if node2 in self.adjList[node1]:
            path.append[node2]
        else:
            for el in self.adjList[node1]:
                if node2 in self.adjList[node2]:
                    path.extend([el, node2])


    def printGraph(self):
        print(self.adjList)

g = Graph()

g.addVertices(['a', 'b', 'c'])
g.addVertices('d')
g.addPath('a', 'b')
g.addPath('a', 'c')
g.addPath('d', 'b')

g.printGraph()

# g.rmEdge('a', 'c')
# g.printGraph()
#
# g.rmNode('a')
# g.printGraph()

g.isConnected()
