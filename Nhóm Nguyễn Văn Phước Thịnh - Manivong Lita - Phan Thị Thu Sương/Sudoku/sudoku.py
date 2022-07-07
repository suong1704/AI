

import math        
from collections import defaultdict        
import itertools        
import functools        
import copy        

@functools.lru_cache()
def intSqrt (n):
    "Computes integer square-root of perfect squares."
    rootN = int(math.sqrt(n))
    if rootN ** 2 != n:
        raise ValueError(f"Expected a perfect square, not: {n}")
    return rootN

def readGame (s):
    "Reads a string-represented game as a list of rows."
    rows = []
    for line in s.splitlines():
        if line.strip():
            rows.append([])
            for word in line.split():
                if word.isdigit():
                    rows[-1].append(int(word))
                elif word == "_" * len(word):
                    rows[-1].append("_")
                else:
                    raise ValueError(f"Unexpected word: {word}")
    n = len(rows)
    rootN = intSqrt(n)        
    assert rootN ** 2 == n        
    for i in range(n):
        if len(rows[i]) != n:
            raise ValueError("Game-grid isn't a perfect square.")        
    return rows        

def printGame (game):
    "Pretty-prints `game`."        
    n = len(game)        
    rootN = intSqrt(n)        
    maxDigits = len(str(n))            # 16 -> len('16') -> 2
    output = ""        
    leftPad = lambda s: s if len(s) == maxDigits else leftPad(" " + s)        
    for (i, row) in enumerate(game):
        if i % rootN == 0:
            output += "\n"        
        for (j, cell) in enumerate(row):
            if j % rootN == 0:
                output += " " * 2        
            output += leftPad(str(cell)) + " "        
        output += "\n"        
    print(output)        

def getRow (i, game):
    "Returns the i^th row in `game`."        
    return game[i]        

def getCol (j, game):
    "Returns the j^th column in `game`."        
    return list(map(lambda row: row[j], game))        

def getBoxStartPos (i, j, rootN):
    "Returns starting position of box containing (i, j)."        
    iBox = math.floor(i / rootN) * rootN        
    jBox = math.floor(j / rootN) * rootN        
    return (iBox, jBox)

def getFlatBox (i, j, game):
    "Returns inner-box w.r.t (i, j), as a _flat_ list."        
    rootN = intSqrt(len(game))        
    iBox, jBox = getBoxStartPos(i, j, rootN)        
    flatBox = []        
    for ii in range(iBox, iBox + rootN):
        for jj in range (jBox, jBox + rootN):
            flatBox.append(game[ii][jj])        
    return flatBox        

def collectPossibleTrioLists (game):
    "Collects possibly deducible trios, (i, j, x), in `game`."        
    n, rootN = len(game), intSqrt(len(game))        
    isFilled = True                        # Initial assumption
    cellwise = defaultdict(list)        
    rowwise = defaultdict(list)        
    colwise = defaultdict(list)        
    boxwise = defaultdict(list)        
    #
    @functools.lru_cache()
    def getRowSet (i): return set(getRow(i, game))        
    #
    @functools.lru_cache()
    def getColSet (j): return set(getCol(j, game))        
    #
    @functools.lru_cache()
    def getBoxSet (iBox, jBox):
        return set(getFlatBox(iBox, jBox, game))        
    #
    iBox, jBox = (0, 0)        
    for i in range(n):
        if i % rootN == 0:
            iBox = i        
        for j in range(n):
            if j % rootN == 0:
                jBox = j         
            if game[i][j] == "_":
                isFilled = False        
                rowSet = getRowSet(i)        
                colSet = getColSet(j)        
                boxSet = getBoxSet(iBox, jBox)        
                for x in range(1, n+1):
                    if x not in (rowSet | colSet | boxSet):
                        trio = (i, j, x)        
                        cellwise[(i, j)].append(trio)        
                        rowwise[(i, x)].append(trio)        
                        colwise[(j, x)].append(trio)        
                        boxwise[((iBox, jBox), x)].append(trio)        
    possibleTrioLists = itertools.chain(
        cellwise.values(), rowwise.values(),
        colwise.values(), boxwise.values(),
    )        
    return (possibleTrioLists, isFilled)        

def deduce (game):
    "Tries to logically fill game using the rules of Sudoku."        
    putCount = 0
    minTrioList = None
    (iterTrioLists, isFilled) = collectPossibleTrioLists(game)
    for trioList in iterTrioLists:
        if len(trioList) == 1:
            (i, j, x) = trioList[0]
            if game[i][j] == "_":
                game[i][j] = x
                putCount += 1
        elif len(trioList) == 0:
            pass
        elif (not minTrioList) or len(trioList) < len(minTrioList):
            minTrioList = trioList
    # Finally ...
    if putCount:
        return deduce(game)        
    # otherwise ...
    # printGame(game)        
    return (isFilled, minTrioList)        

def solveGame (inputGame, verbose=False, search=""):
   
    solutionList = [inputGame]       
    maxSolListLen = 1
    while solutionList:
        game = solutionList.pop(0 if search == "" else -1)
        (isFilled, minTrioList) = deduce(game)
    return game

def checkSolved (game):
    n = len(game)        
    rootN = intSqrt(n)        
    fullSet = set(range(1, n+1))        
    for k in range(0, n):
        rowAndColOk = (
            set(getRow(k, game)) == fullSet and
            set(getCol(k, game)) == fullSet #and
        )        
        if not rowAndColOk:
            return False        
    for i in range(0, n, rootN):
        for j in range(0, n, rootN):
            if set(getFlatBox(i, j, game)) != fullSet:
                return False        
    return True        