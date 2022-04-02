from entities.game import TicTacToe
from services.game_service import *

if __name__ == "__main__":
    testgame = TicTacToe()
    print(testgame)
    play(testgame,1,1)
    play(testgame,0,1)
    play(testgame,0,2)
    play(testgame,1,1)
    play(testgame,0,0)
    play(testgame,2,0)
    print(testgame)
    print(check_winner(testgame))

    testgame2 = TicTacToe()
    play(testgame2,1,1)
    play(testgame2,0,0)
    play(testgame2,1,0)
    play(testgame2,0,1)
    play(testgame2,2,0)
    play(testgame2,0,2)
    print(testgame2)
    print(check_winner(testgame2))