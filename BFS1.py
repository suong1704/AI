from mimetypes import init
class Node:
    def __init__(sefl, name):
        sefl.name = name
        sefl.children = []
    def addChildren(self, list):
        for c in list:
            self.children.append(c)
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
    nodeA.addChildren([nodeB, nodeC])
    nodeB.addChildren([nodeD, nodeE])
    nodeC.addChildren([nodeF, nodeG])
    nodeD.addChildren([nodeH, nodeI])
    nodeE.addChildren([nodeJ, nodeK])
    nodeF.addChildren([nodeL, nodeM])
    nodeG.addChildren([nodeN, nodeO])
    result = BFS(nodeA, 'G')
    if result:
        s = 'Explored: '
        for i in result:
            s += i.name + " "
            print(s)
    else:
        print('LOI!')
# DFS