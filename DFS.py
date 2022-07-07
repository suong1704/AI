from mimetypes import init


class Node:
    def __init__(sefl, name):
        sefl.name = name
        sefl.children = []
    def addChildren(self, list):
        for c in list:
            self.children.append(c)
def DFS( initialState, goal):
    if (initialState not in explored):
        explored.append(initialState)
        if goal == initialState.name:
            return explored
        for child in initialState.children:
                DFS(child,goal)
    return False

    # frontier.append(initialState)
    # state = frontier.pop()
    # if (initialState not in explored):
    #     explored.append(state)
    #     # if goal == state.name:
    #     #     return True
    #     for child in state.children:
    #         if child == goal:
    #             explored.append(child)
    #         else:
    #             DFS(explored,frontier,child,goal)
    # return False

    # if (initialState not in explored):
    #     frontier.append(initialState)
    #     state = frontier.pop(0)
    #     explored.append(state)
    #     for child in state.children:
    #         DFS(explored,frontier,child,goal)
    # return False
if __name__ == '__main__':
    # nodeA = Node("A")
    # nodeB = Node("B")
    # nodeC = Node("C")
    # nodeD = Node("D")
    # nodeE = Node("E")
    # nodeF = Node("F")
    # nodeG = Node("G")
    # nodeH = Node("H")
    # nodeS = Node("S")
    
    # nodeS.addChildren([nodeA, nodeB, nodeC])
    # nodeA.addChildren([nodeD])
    # nodeB.addChildren([nodeD, nodeE, nodeG])
    # nodeC.addChildren([nodeE])
    # nodeD.addChildren([nodeF])
    # nodeE.addChildren([nodeF, nodeH])
    # nodeF.addChildren([nodeE,nodeG])
    # nodeH.addChildren([nodeG])
    # nodeG.addChildren([])
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
    explored = []
    frontier = []
    result = DFS( nodeA, 'H')
    s = 'Explored: '
    for i in explored:
        s += i.name + " "
        print(s)
    # if result:
    #     s = 'Explored: '
    #     for i in explored:
    #         s += i.name + " "
    #         print(s)
    # else:
    #     print('LOI!')
   