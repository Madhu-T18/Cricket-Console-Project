from models.player import Player

class Team:
    def __init__(self, name):
        self.__name    = name
        self.__players = []

    @property
    def name(self):
        return self.__name

    @property
    def players(self):
        return list(self.__players)

    def add_player(self, player: Player, silent=False):
        self.__players.append(player)
        if not silent:
            print(f"  ✔  {player.name} ({player.get_role()}) → {self.__name}")

    def count(self):
        return len(self.__players)