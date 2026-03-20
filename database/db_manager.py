import sqlite3

class DatabaseManager:
    def __init__(self, db_name="cricket_tournament.db"):
        self.__conn   = sqlite3.connect(db_name)
        self.__cursor = self.__conn.cursor()
        self.__create_tables()

    def __create_tables(self):
        self.__cursor.executescript("""
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS players (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                name      TEXT NOT NULL,
                role      TEXT NOT NULL,
                team_name TEXT NOT NULL,
                runs      INTEGER DEFAULT 0,
                wickets   INTEGER DEFAULT 0,
                matches   INTEGER DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS matches (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                team1       TEXT NOT NULL,
                team2       TEXT NOT NULL,
                winner      TEXT,
                motm        TEXT,
                team1_score INTEGER DEFAULT 0,
                team2_score INTEGER DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS points_table (
                team_name TEXT PRIMARY KEY,
                played  INTEGER DEFAULT 0,
                won     INTEGER DEFAULT 0,
                lost    INTEGER DEFAULT 0,
                points  INTEGER DEFAULT 0
            );
        """)
        self.__conn.commit()

    def save_team(self, name):
        try:
            self.__cursor.execute("INSERT INTO teams (name) VALUES (?)", (name,))
            self.__cursor.execute("INSERT OR IGNORE INTO points_table (team_name) VALUES (?)", (name,))
            self.__conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_all_teams(self):
        self.__cursor.execute("SELECT name FROM teams")
        return [r[0] for r in self.__cursor.fetchall()]

    def save_player(self, player):
        self.__cursor.execute(
            "INSERT INTO players (name, role, team_name) VALUES (?,?,?)",
            (player.name, player.get_role(), player.team_name))
        self.__conn.commit()

    def get_players_by_team(self, team_name):
        self.__cursor.execute(
            "SELECT name, role, runs, wickets, matches FROM players WHERE team_name=?",
            (team_name,))
        return self.__cursor.fetchall()

    def update_player_stats(self, name, runs, wickets):
        self.__cursor.execute(
            "UPDATE players SET runs=runs+?, wickets=wickets+?, matches=matches+1 WHERE name=?",
            (runs, wickets, name))
        self.__conn.commit()

    def get_top_batsmen(self, limit=5):
        self.__cursor.execute(
            "SELECT name, team_name, runs, matches FROM players ORDER BY runs DESC LIMIT ?", (limit,))
        return self.__cursor.fetchall()

    def get_top_bowlers(self, limit=5):
        self.__cursor.execute(
            "SELECT name, team_name, wickets, matches FROM players ORDER BY wickets DESC LIMIT ?", (limit,))
        return self.__cursor.fetchall()

    def save_match(self, team1, team2, winner, motm, score1, score2):
        self.__cursor.execute(
            "INSERT INTO matches (team1,team2,winner,motm,team1_score,team2_score) VALUES (?,?,?,?,?,?)",
            (team1, team2, winner, motm, score1, score2))
        self.__conn.commit()

    def get_all_matches(self):
        self.__cursor.execute("SELECT team1,team2,winner,motm,team1_score,team2_score FROM matches")
        return self.__cursor.fetchall()

    def update_points(self, winner, loser):
        self.__cursor.execute(
            "UPDATE points_table SET played=played+1, won=won+1, points=points+2 WHERE team_name=?", (winner,))
        self.__cursor.execute(
            "UPDATE points_table SET played=played+1, lost=lost+1 WHERE team_name=?", (loser,))
        self.__conn.commit()

    def get_points_table(self):
        self.__cursor.execute(
            "SELECT team_name, played, won, lost, points FROM points_table ORDER BY points DESC")
        return self.__cursor.fetchall()

    def close(self):
        self.__conn.close()