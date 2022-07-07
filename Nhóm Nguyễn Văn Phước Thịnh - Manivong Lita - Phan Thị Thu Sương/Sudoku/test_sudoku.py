import time
import functools

from sudoku import *

def test_2x2 ():
    game = readGame("""
        3 4 _ _
        _ 2 _ _
        _ _ 4 _
        _ _ 2 1
    """)      
    assert game == [
        [ 3,    4,  "_", "_"],
        ["_",   2,  "_", "_"],
        ["_",  "_",  4,  "_"],
        ["_", "_",   2,   1],
    ]      
    solvedGame = solveGame(game)
    assert checkSolved(solvedGame)
    print("solvedGame")
    printGame(solvedGame)

    # badGame = readGame("""
    #     1 1 1 _
    #     2 2 _ 2
    #     3 _ 3 3
    #     _ 4 4 4
    # """)      
    # try: solveGame(badGame)      
    # except ValueError: pass      
    # else: assert False      

def test_3x3_and_4x4 ():
    gameTexts = [
        # Easy:
        # """
        #     5 3 _   _ 7 _   _ _ _
        #     6 _ _   1 9 5   _ _ _
        #     _ 9 8   _ _ _   _ 6 _

        #     8 _ _   _ 6 _   _ _ 3
        #     4 _ _   8 _ 3   _ _ 1
        #     7 _ _   _ 2 _   _ _ 6

        #     _ 6 _   _ _ _   2 8 _
        #     _ _ _   4 1 9   _ _ 5
        #     _ _ _   _ 8 _   _ 7 9
        # """,

        # # Hard:
        # """
        #     _ 1 3   _ _ _   _ 5 _
        #     _ _ 5   _ _ 8   _ 4 3
        #     _ 6 _   _ _ _   _ _ 7

        #     _ _ _   4 _ _   _ _ _
        #     _ _ 1   _ _ 2   _ _ _
        #     _ _ _   _ _ 5   _ 6 8

        #     _ 5 4   2 _ _   _ _ 9
        #     2 _ _   3 _ _   _ 8 _
        #     _ _ 7   5 _ 1   _ _ _
        # """,

        # # Hard:
        # """
        #     9 _ _   _ _ 7   1 2 _
        #     6 _ 7   9 _ _   _ _ _
        #     2 _ _   _ _ _   _ 8 _

        #     _ _ _   3 _ _   _ _ _
        #     _ _ 8   _ _ _   _ 4 3
        #     _ _ _   _ _ 5   9 _ _

        #     _ 4 _   1 _ _   _ _ _
        #     _ _ _   _ _ _   6 5 _
        #     _ 3 5   _ _ 8   _ _ _
        # """,

        # # Hard:
        # """
        #     _ _ 7   8 _ _   _ _ _ 
        #     _ _ 3   7 4 _   _ _ 6
        #     2 8 _   _ 5 _   4 _ _

        #     1 9 _   _ _ _   _ _ _
        #     7 _ _   4 8 9   _ _ 1
        #     _ _ _   _ _ _   _ 4 3

        #     _ _ 9   _ 3 _   _ 6 2
        #     8 _ _   _ 6 5   3 _ _
        #     _ _ _   _ _ 4   1 _ _
        # """,

        # # Hard:
        # """
        #     _ _ _   _ _ _   _ _ 2 
        #     _ 2 3   _ _ _   _ _ 1 
        #     _ _ _   _ 6 8   _ _ _ 

        #     _ 9 4   5 _ _   _ _ 3 
        #     _ 7 _   _ 1 _   _ 5 _ 
        #     _ _ _   _ _ _   _ 8 _ 

        #     _ 5 _   7 4 _   _ _ _ 
        #     6 _ _   _ _ _   7 2 _ 
        #     _ _ 9   _ _ _   _ 1 _ 

        # Hard:
        # """
        #     _ _ _   _ _ _   3 _ _ 
        #     _ _ 1   _ _ 9   _ 8 _ 
        #     2 _ _   _ 3 _   _ _ 7 

        #     6 _ _   _ 2 _   1 _ _ 
        #     _ _ _   5 _ 3   _ _ _ 
        #     _ 8 _   _ _ _   _ _ 9 

        #     7 _ _   4 6 _   _ _ 3 
        #     _ 2 _   _ _ _   _ _ _ 
        #     _ _ 9   _ 7 _   _ 5 _ 
        # """,
        """
            _ _ _   2 6 _   7 _ 1 
            6 8 _   _ 7 _   _ 9 _ 
            1 9 _   _ _ 4   5 _ _ 

            8 2 _   1 _ _   _ 4 _ 
            _ _ 4   6 _ 2   9 _ _ 
            _ 5 _   _ _ 3   _ 2 8 

            _ _ 9   3 _ _   _ 7 4 
            _ 4 _   _ 5 _   _ 3 6 
            7 _ 3   _ 1 8   _ _ _ 
        """,

       
    ]
    for gameText in  gameTexts[0:]:
        print("---------------------------------------------------------")      
        game = readGame(gameText)      
        printGame(game)      
        solvedGame = solveGame(game, verbose=True, search="bfs")      
        assert checkSolved(solvedGame)      
        printGame(solvedGame)      
        print("---------------------------------------------------------")      

def timer (fn):
    @functools.wraps(fn)
    def wrapper (*a, **ka):
        t0 = time.time()      
        result = fn(*a, **ka)      
        tDiff = time.time() - t0      
        print(f"Time taken by {fn.__name__}(.): {tDiff}")      
        return result      
    return wrapper      


if __name__ == "__main__":
    solveGame = timer(solveGame)      
    test_3x3_and_4x4()      