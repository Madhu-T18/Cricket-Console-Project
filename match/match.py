import random
from models.team import Team
from models.player import Batsman, Bowler, AllRounder
from database.db_manager import DatabaseManager

class Match:
    def __init__(self, team1: Team, team2: Team):
        self.__team1  = team1
        self.__team2  = team2
        self.__score1 = 0
        self.__score2 = 0

    def __simulate_innings(self, team: Team):
        total = 0
        for p in team.players:
            if isinstance(p, Batsman):
                runs = p.simulate_innings()
                p.update_stats(runs, 0)
                total += runs
            elif isinstance(p, Bowler):
                wkts = p.simulate_bowling()
                p.update_stats(0, wkts)
            elif isinstance(p, AllRounder):
                runs = p.simulate_innings()
                wkts = p.simulate_bowling()
                p.update_stats(runs, wkts)
                total += runs
        return total + random.randint(20, 50)

    def play(self, db: DatabaseManager):
        print(f"\n  {'═'*50}")
        print(f"  🏏  {self.__team1.name}  vs  {self.__team2.name}")
        print(f"  {'═'*50}")

        self.__score1 = self.__simulate_innings(self.__team1)
        self.__score2 = self.__simulate_innings(self.__team2)

        print(f"  {self.__team1.name} ➜ {self.__score1} runs")
        print(f"  {self.__team2.name} ➜ {self.__score2} runs")

        if self.__score1 > self.__score2:
            winner, loser = self.__team1.name, self.__team2.name
        elif self.__score2 > self.__score1:
            winner, loser = self.__team2.name, self.__team1.name
        else:
            winner = loser = "Draw"

        all_players = self.__team1.players + self.__team2.players
        batters = [p for p in all_players if isinstance(p, (Batsman, AllRounder))]
        motm = max(batters, key=lambda p: p.runs).name if batters else "N/A"

        print(f"\n  Winner : {winner}")
        print(f"  MOTM   : {motm}")
        print(f"  {'═'*50}")

        db.save_match(self.__team1.name, self.__team2.name, winner, motm, self.__score1, self.__score2)
        if winner != "Draw":
            db.update_points(winner, loser)
        for p in all_players:
            db.update_player_stats(p.name, p.runs, p.wickets)