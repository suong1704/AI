def dfs_limit(g, start, goal, limit=-1):
    '''
    Perform depth first search of graph g.
    if limit >= 0, that is the maximum depth of the search.
    '''
    SENTINEL = object()
    visitedStack = [start]
    path = []

    while visitedStack:
        currentVertex = visitedStack.pop()

        if currentVertex == goal: 
            path.append(currentVertex)
            return ' -> '.join(path)

        elif currentVertex == SENTINEL:
            #finished this level; go back up one level
            limit += 1
            path.pop()

        elif limit != 0:
            # go one level deeper, push sentinel
            limit -= 1
            path.append(currentVertex)
            visitedStack.append(SENTINEL)
            visitedStack.extend(g.getVertex(currentVertex).getConnections())