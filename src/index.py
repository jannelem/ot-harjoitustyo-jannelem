from ui.ui import play_game

if __name__ == "__main__":
    while True:
        print("Tervetuloa pelaamaan ristinollaa!")
        size_input = input("Anna pelilaudan koko (3...15, x lopettaa): ")
        if size_input == "x":
            print("Kiitos pelaamisesta!")
            break
        try:
            size_input = int(size_input)
            if not 3 <= size_input <= 15:
                raise ValueError
        except ValueError:
            print("Virheellinen koko!")
            continue
        play_game(size_input)
