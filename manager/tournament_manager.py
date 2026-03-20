from database.db_manager import DatabaseManager
from models.team import Team
from models.player import Batsman, Bowler, AllRounder, Player
from match.match import Match
from exceptions.errors import TeamNotFoundError, NotEnoughPlayersError, TournamentError

class TournamentManager:
    ROLE_MAP = {"1": Batsman, "2": Bowler, "3": AllRounder}

    def __init__(self):
        self.__db    = DatabaseManager()
        self.__teams = {}

    def __team(self, name):
        if name not in self.__teams:
            raise TeamNotFoundError(name)
        return self.__teams[name]

    def restore_session(self):
        for tname in self.__db.get_all_teams():
            team = Team(tname)
            for name, role, runs, wickets, _ in self.__db.get_players_by_team(tname):
                Cls = {"Batsman": Batsman, "Bowler": Bowler, "All-Rounder": AllRounder}.get(role, Player)
                p   = Cls(name, tname)
                p.update_stats(runs, wickets)
                team.add_player(p, silent=True)
            self.__teams[tname] = team

    def add_team(self):
        name = input("  Team name: ").strip().title()
        if self.__db.save_team(name):
            self.__teams[name] = Team(name)
            print(f"  ✔  '{name}' added!")
        else:
            print(f"  ✘  '{name}' already exists.")

    def add_player(self):
        teams = self.__db.get_all_teams()
        if not teams:
            print("  ✘  Add a team first."); return
        print("  Teams:", ", ".join(teams))
        tname = input("  Team name: ").strip().title()
        try:
            team = self.__team(tname)
        except TeamNotFoundError as e:
            print(f"  ✘  {e}"); return
        pname = input("  Player name: ").strip().title()
        print("  1.Batsman  2.Bowler  3.All-Rounder")
        Cls = self.ROLE_MAP.get(input("  Role: ").strip())
        if not Cls:
            print("  ✘  Invalid."); return
        player = Cls(pname, tname)
        team.add_player(player)
        self.__db.save_player(player)

    def play_match(self):
        teams = self.__db.get_all_teams()
        if len(teams) < 2:
            print("  ✘  Need at least 2 teams."); return
        print("  Teams:", ", ".join(teams))
        t1 = input("  Team 1: ").strip().title()
        t2 = input("  Team 2: ").strip().title()
        try:
            team1 = self.__team(t1)
            team2 = self.__team(t2)
            if team1.count() < 2: raise NotEnoughPlayersError(team1.name, team1.count())
            if team2.count() < 2: raise NotEnoughPlayersError(team2.name, team2.count())
        except TournamentError as e:
            print(f"  ✘  {e}"); return
        Match(team1, team2).play(self.__db)

    def view_points_table(self):
        rows = self.__db.get_points_table()
        if not rows: print("  No matches yet."); return
        print(f"\n  {'Team':<22} P   W   L  Pts")
        print("  " + "─"*38)
        for i, (t, p, w, l, pts) in enumerate(rows, 1):
            print(f"  {i}. {t:<20} {p}   {w}   {l}   {pts}")

    def view_player_stats(self):
        print("\n  Top Batsmen:")
        for name, team, runs, m in self.__db.get_top_batsmen():
            print(f"    {name:<22} {team:<18} R:{runs} M:{m}")
        print("\n  Top Bowlers:")
        for name, team, wkts, m in self.__db.get_top_bowlers():
            print(f"    {name:<22} {team:<18} W:{wkts} M:{m}")

    def view_match_results(self):
        for i, (t1, t2, w, motm, s1, s2) in enumerate(self.__db.get_all_matches(), 1):
            print(f"\n  Match {i}: {t1} {s1} vs {t2} {s2} | Winner:{w} MOTM:{motm}")

    def view_squads(self):
        for tname in self.__db.get_all_teams():
            print(f"\n  {tname}")
            for name, role, r, wk, m in self.__db.get_players_by_team(tname):
                print(f"    {name:<22} {role:<14} R:{r} W:{wk} M:{m}")

    def close(self):
        self.__db.close()