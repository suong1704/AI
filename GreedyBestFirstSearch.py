import heapq
# from TreeNode import Tree

class Tree:
    def __init__(self, data, goal_cost=100000):
        self.data = data # label
        self.goal_cost = goal_cost # h(n)
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_data(self):
        return self.data
    def get_children(self):
        return self.children
    def get_parent(self):
        return self.parent
    def __lt__(self, other):
        return self.goal_cost < other.goal_cost
# def undate_frontier(frontier, new_node):
#     for i, n in enumerate(frontier):
#         if n == new_node:
#             if frontier[i].goal_cost > new_node.goal_cost:
#                 frontier[i] = new_node
def GBF_search(initial_state , goalTest):
    frontier =[]
    explored = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, initial_state)
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        if(state == goalTest):
            return explored
        for neighbor in state.get_children():
            if neighbor not in (frontier and explored):
                heapq.heappush(frontier, neighbor)
            # elif neighbor in frontier:
            #     undate_frontier(frontier, neighbor)
    return False
if __name__ == '__name__':
    A = Tree("A",6)
    B = Tree("B",3)
    C = Tree("C",4)
    D = Tree("D",5)
    E = Tree("E",3)
    F = Tree("F",1)
    G = Tree("G",6)
    H = Tree("H",2)
    I = Tree("I",5)
    J = Tree("J",4)
    K = Tree("K",2)
    L = Tree("L",0)
    M = Tree("M",4)
    N = Tree("N",0)
    O = Tree("O",4)
    A.add_child(B)
    A.add_child(C)
    A.add_child(D)
    B.add_child(E)
    B.add_child(F)
    C.add_child(G)
    C.add_child(H)
    D.add_child(I)
    D.add_child(J)
    F.add_child(K)
    F.add_child(M)
    H.add_child(N)
    H.add_child(O)
    result = GBF_search(A,L)
    if result:
        s = 'Explored: '
        for i in result:
            s += i.data + " "
            print(s)
    else:
        print('LOI!')
   
