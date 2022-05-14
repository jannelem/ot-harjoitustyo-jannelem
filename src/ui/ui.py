from tkinter import OptionMenu, Tk, ttk, IntVar, StringVar
from services.player_service import PlayerService
from services.game_service import GameService
from entities.player import Player
from entities.game import TicTacToe


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        
    def start(self):
        self._show_main_menu()
    
    def _handle_start_game(self, board_size, player_x, player_o):
        if board_size != 0:
            new_game = TicTacToe(board_size, player_x, player_o)
            self._show_game_view(new_game)
    
    def _handle_return_to_main_menu(self):
        pass
        

    def _show_main_menu(self):
        self._current_view = MainMenu(self._root, self._handle_start_game)
        self._current_view.pack()
    
    def _show_game_view(self, game):
        self._hide_current_view()
        self._current_view = GameView(self._root, game, self._handle_return_to_main_menu)
        self._current_view.pack()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None



        

class MainMenu:
    def __init__(self, root, handle_start_game):
        self._root = root
        self._handle_start_game = handle_start_game
        self._frame = None

        self.player_service = PlayerService()
        self.players = {}
        self.players["Vieras"] = Player("Vieras")
        self.players["Risti"] = Player("Risti")
        self.players["Nolla"] = Player("Nolla")
        self.players["Kolmas pelaaja"] = Player("Kolmas pelaaja")

        self._initialize()



    def pack(self):
        self._frame.pack()
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Päävalikko")

        player_x_label = ttk.Label(master=self._frame, text="Pelaaja X")
        player_x_variable = StringVar()
        player_x_variable.set("Vieras")
        player_x_dropdown = ttk.OptionMenu(self._frame, player_x_variable, *self.players.keys())
        
        player_o_label = ttk.Label(master=self._frame, text="Pelaaja O")
        player_o_variable = StringVar()
        player_o_variable.set("Vieras")
        player_o_dropdown = ttk.OptionMenu(self._frame, StringVar(), *self.players.keys())
        board_size_label = ttk.Label(master=self._frame, text="Ruudukon koko")

        board_size_variable = IntVar()
        board_size_dropdown = OptionMenu(self._frame, board_size_variable, *list(range(3,16)))
        
        play_button = ttk.Button(master=self._frame, text="Aloita peli", command=lambda: self._handle_start_game(board_size_variable.get(),self.players[player_x_variable.get()],self.players[player_o_variable.get()]))
        
        playerstats_button = ttk.Button(master=self._frame, text="Pelaajatilastot")
        hiscore_button = ttk.Button(master=self._frame, text="Parhaat pelaajat")

        label.grid(row=0, column=0, columnspan=3)

        player_x_label.grid(row=1, column=0)
        player_x_dropdown.grid(row=1, column=1)
        player_o_label.grid(row=2, column=0)
        player_o_dropdown.grid(row=2, column=1)
        board_size_label.grid(row=3, column=0)
        board_size_dropdown.grid(row=3, column=1)
        play_button.grid(row=1, column=2, rowspan=3)

        playerstats_button.grid(row=4, column=0, columnspan=3)
        hiscore_button.grid(row=5, column=0, columnspan=3)

class GameView:
    def __init__(self, root, game, handle_return_to_main_menu):
        self._root = root
        self._game = game
        self._handle_return_to_main_menu = handle_return_to_main_menu
        self._frame = None
        self._game_service = GameService(PlayerService())

        self._initialize()

    def pack(self):
        self._frame.pack()
    
    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)

        if self._game.turn == 1:
            status_text = "Vuorossa: X (" + self._game.player_x.name + ")"
        elif self._game.turn == -1:
            status_text = "Vuorossa: O (" + self._game.player_y.name + ")"
        
        status_label = ttk.Label(master=self._frame, text=status_text)
        status_label.grid(row=0, column=0)

        board_buttons=[]
        for _ in range(self._game.board_size):
            button_row=[]
            for __ in range(self._game.board_size):
                button_text=""
                if self._game.board[_][__].value == 1:
                    button_text="X"
                elif self._game.board[_][__].value == -1:
                    button_text="O"
                row=_
                column=__
                button_row.append(ttk.Button(master=self._frame,text=button_text,command=lambda: print("nappi",row,column)))
            board_buttons.append(button_row)
        for _ in range(len(board_buttons)):
            for __ in range(len(board_buttons)):
                board_buttons[_][__].grid(row=_+1, column=__)
        
                                

    
    def destroy(self):
        self._frame.destroy()       


    
