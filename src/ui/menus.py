from tkinter import Tk, ttk
from ui.game import play_game


class MainMenu():
    def __init__(self, root):
        self._root = root
        self._entry = None

    def start(self):
        label = ttk.Label(
            master=self._root, text="Tervetuloa Ristinollaan! Monenko ruudun ruudukko? (3-15)")
        self._entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Pelaa!",
                            command=self._handle_button_click)
        label.pack()
        self._entry.pack()
        button.pack()

    def _handle_button_click(self):
        entry_value = self._entry.get()
        try:
            entry_value = int(entry_value)
            if entry_value < 3 or entry_value > 15:
                raise ValueError
            play_game(entry_value)
        except ValueError:
            pass
