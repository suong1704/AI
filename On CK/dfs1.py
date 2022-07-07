from unicodedata import name


class Node:
    def __init__(sefl, name):
        sefl.name = name
        sefl.children = []
    def addChildren(self, list):
        for c in list:
            self.children.append(c)
    def addOneChildren(self, node):
        self.children.append(node)
def makeNodeTree( dinh, canh):
    node = []
    node_canh = []
    for d in dinh:
        node.append(Node(d))
    for c in canh:
        for c1 in c:
            for n in node:
                if (c1 == n.name):
                    node_canh.append(n)
    for i in range(0,len(node_canh)-1,2):
        j=i+1
        # print(i)
        for n in node:
            if (n.name == node_canh[i].name):
                n.addOneChildren(node_canh[j])
    return  node
def DFS(initialState, goal):
	frontier = [initialState]
	explored = []
	while frontier:
		state = frontier.pop(len(frontier) - 1)
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
    nodeS = Node("S")
    
    nodeS.addChildren([nodeA, nodeB, nodeC])
    nodeA.addChildren([nodeD])
    nodeB.addChildren([nodeD, nodeE, nodeG])
    nodeC.addChildren([nodeE])
    nodeD.addChildren([nodeF])
    nodeE.addChildren([nodeF, nodeH])
    nodeF.addChildren([nodeE,nodeG])
    nodeH.addChildren([nodeG])
    nodeG.addChildren([])
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
    nodeO = Node("O")
    nodeA.addChildren([nodeB, nodeC])
    nodeB.addChildren([nodeD, nodeE])
    nodeC.addChildren([nodeF, nodeG])
    nodeD.addChildren([nodeH, nodeI])
    nodeE.addChildren([nodeJ, nodeK])
    nodeF.addChildren([nodeL, nodeM])
    nodeG.addChildren([nodeN, nodeO])
    V = ["S", "A", "B", "C", "D", "E", "F", "G", "H"] 
    E = [("S", "A"), ("A","S"), ("S", "B"),("B", "S"), ("S", "C"),("C","S"), ("A", "B"), ("B", "A"),
            ("A", "D"),("D", "A"), ("B", "D"),("D", "B"), ("B", "G"),("G", "B"),
            ("B", "F"),("F", "B"),("C", "F"),("F", "C"), ("C", "B"),("B", "C"), 
            ("D", "E"), ("E", "D"),("F", "E"), ("E", "F"),("F", "H"),("H", "F"), 
            ("E", "G"),("G", "E"),("H", "G"),("G", "H")]
    list = makeNodeTree(V,E)
    for i in list[0].children:
        print(i.name)
    # print(type(list))
    result = DFS( nodeA, 'O')
    s = 'Explored: '
    if result:
        s = 'Explored: '
        for i in result:
            s += i.name + " "
        print(s)
    else:
        print('LOI!')
   