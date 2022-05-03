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
        return f"Pelaaja: {self.name}\nVoitot: {self.wins}\nHäviöt: {self.losses}\nTasapelit: {self.ties}\nVoitto-%: {percentage:.1f} %"
