import random
from models.person import Person

class Player(Person):
    def __init__(self, name, team_name):
        super().__init__(name)
        self.__team_name = team_name
        self._runs    = 0
        self._wickets = 0
        self._matches = 0

    @property
    def team_name(self):
        return self.__team_name

    @property
    def runs(self):
        return self._runs

    @property
    def wickets(self):
        return self._wickets

    def update_stats(self, runs, wickets):
        self._runs    += runs
        self._wickets += wickets
        self._matches += 1

    def get_role(self):
        return "Player"

    def display_stats(self):
        print(f"  {self.name} | {self.__team_name} | R:{self._runs} W:{self._wickets}")


class Batsman(Player):
    def __init__(self, name, team_name):
        super().__init__(name, team_name)
        self.__centuries = 0

    def get_role(self):
        return "Batsman"

    def simulate_innings(self):
        runs = random.randint(15, 120)
        if runs >= 100:
            self.__centuries += 1
        return runs

    def display_stats(self):
        print(f"  {self.name} [Batsman] R:{self._runs} 100s:{self.__centuries}")


class Bowler(Player):
    def __init__(self, name, team_name):
        super().__init__(name, team_name)
        self.__five_hauls = 0

    def get_role(self):
        return "Bowler"

    def simulate_bowling(self):
        wickets = random.randint(0, 5)
        if wickets >= 5:
            self.__five_hauls += 1
        return wickets

    def display_stats(self):
        print(f"  {self.name} [Bowler] W:{self._wickets} 5w:{self.__five_hauls}")


class AllRounder(Player):
    def get_role(self):
        return "All-Rounder"

    def simulate_innings(self):
        return random.randint(20, 80)

    def simulate_bowling(self):
        return random.randint(0, 3)

    def display_stats(self):
        print(f"  {self.name} [All-Rounder] R:{self._runs} W:{self._wickets}")