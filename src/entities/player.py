from .services.player_service import win

class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def __str__(self):
        if self.wins+self.losses+self.ties == 0:
            percentage = 0
        else:
            percentage = 100*self.wins/(self.wins+self.losses+self.ties)
        return f"Player: {self.name}\nWins: {self.wins}\nLosses: {self.losses}\nTies: {self.ties}\nPercentage: {percentage:.1f} %"

if __name__ == "__main__":
    janne = Player("Janne")
    pertti = Player("Pertti")
    print(janne)
    print(pertti)
    win(janne, 5)
    print(janne)

