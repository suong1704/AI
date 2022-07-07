from mimetypes import init
class Node:
    def __init__(sefl, name):
        sefl.name = name
        sefl.children = []
    def addChildren(self, graph):
        for i, c in graph.items():
            if (str(i)==str(self.name)):
                for j in c:
                    print(j)
                    self.children.append(j)
def BFS(initialState, goal):
	frontier = [initialState]
	explored = []
	while frontier:
		state = frontier.pop()
		explored.append(state)
		if goal == state.name:
			return explored
		for child in state.children:
			if child not in (explored and frontier):
				frontier.append(child)
	return False
if __name__ == '__main__':
    graph ={
	'A' : ['B','C'],
	'B' : ['D','E'],
	'C' : ['F','G'],
	'D' : ['H','I'],
	'E' : ['J','K'],
	'F' : ['L','M'],
	'G' : ['N','O'],
	'H' : [],
	'I' : [],
	'J' : [],
	'K' : [],
	'L' : [],
	'M' : [],
	'N' : [],
	'O' : []
	}
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    nodeI = Node("I")
    nodeJ = Node("J")
    nodeK = Node("K")
    nodeL = Node("L")
    nodeM = Node("M")
    nodeN = Node("N")
    nodeO = Node("0")
    nodeA.addChildren(graph)
    nodeB.addChildren(graph)
    nodeC.addChildren(graph)
    nodeD.addChildren(graph)
    nodeE.addChildren(graph)
    nodeF.addChildren(graph)
    nodeG.addChildren(graph)
    result = BFS(nodeA, 'H')
    if result:
        s = 'Explored: '
        for i in result:
            s += i.name + " "
            print(s)
    else:
        print('LOI!')
   