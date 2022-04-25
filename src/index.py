from ui.game import play_game
from ui.menus import MainMenu
from tkinter import Tk

if __name__ == "__main__":
    window = Tk()
    window.title("Ristinolla")

    main_menu = MainMenu(window)
    main_menu.start()

    window.mainloop()
    