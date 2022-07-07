import heapq

class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        # Tập số trên đỉnh
        self.goal_cost = goal_cost
        self.cost = 0
        #quãng đường đã đi từ điểm đầu đến điểm hiện tại(điểm cha) ; g(v)
        self.save_cost = 0
        self.costs = []
        self.children = []
    def addChildren(self, listnode , listcost):
        self.children = listnode
        self.costs = listcost
    def addOneChildren(self, node, cost):
        self.children.append(node)
        self.costs = cost
    def __repr__(self):
        return str(dict({
            "label": self.label,
            "save_cost" : self.save_cost,
            "goal cost": self.goal_cost
        }))
    def __eq__(self, other):
        return self.label == other.label
    def __lt__(self, other):
            return self.cost < other.cost
    def get_label(self):
        return self.label
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
        for n in node:
            if (n.name == node_canh[i].name):
                n.addOneChildren(node_canh[j])
    return  node
def A_Star( start, end):
    frontier = [start]
    heapq.heapify(frontier)
    explored = []
    while len(frontier) > 0 :
        state = heapq.heappop(frontier)
        explored.append(state)
        # print(state)
        if state == end:
            return explored
        i = 0
        for child in state.children:
            child.save_cost = state.save_cost + state.costs[i]
            child.cost = child.goal_cost + child.save_cost
            if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
                heapq.heappush(frontier, child)
            if child not in (explored and frontier):
                frontier.append(child)
            i += 1
    return False
if __name__ == "__main__":
    nodeS = Node("S", 12)
    nodeA = Node("A", 9)
    nodeB = Node("B", 8)
    nodeC = Node("C", 7)
    nodeD = Node("D", 6)
    nodeE = Node("E", 5)
    nodeF = Node("F", 4)
    nodeG = Node("G", 10)
    nodeH = Node("H", 10)
    nodeK = Node("K", 3)
    nodeM = Node("M", 9)
    nodeN = Node("N", 10)
    nodeI = Node("I", 6)
    nodeJ = Node("J", 0)
    nodeL = Node("L", 0)
    nodeZ = Node("Z", 8)

    nodeS.addChildren([nodeA, nodeB, nodeC], [5, 6, 5])
    nodeA.addChildren([nodeD, nodeE], [6, 7])
    nodeB.addChildren([nodeF, nodeG], [3 ,4])
    nodeC.addChildren([nodeH, nodeK], [6 ,4])
    nodeD.addChildren([nodeM, nodeN], [5 ,8])
    nodeE.addChildren([nodeI], [8])
    nodeF.addChildren([nodeJ, nodeL], [4, 4])
    nodeK.addChildren([nodeZ], [2])
    result = A_Star(nodeA, nodeL)

    print(nodeA.children)
    # result = A_Star(nodeA, nodeL)
    
    if result:
        s = 'explored: '
        for i in result:
            s += " " + i.label 
            # print(s);
    else:
        print('404 Not Found!')

