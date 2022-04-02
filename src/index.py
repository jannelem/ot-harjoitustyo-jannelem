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