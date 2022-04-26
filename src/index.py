from tkinter import Tk
from ui.menus import MainMenu

if __name__ == "__main__":
    window = Tk()
    window.title("Ristinolla")

    main_menu = MainMenu(window)
    main_menu.start()

    window.mainloop()
