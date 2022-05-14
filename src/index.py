from entities.game import TicTacToe
from entities.player import Player
from services.game_service import GameService
from services.player_service import PlayerService
from ui.ui import UI

from tkinter import Tk

window = Tk()
window.title("Ristinolla")
ui = UI(window)
ui.start()

window.mainloop()