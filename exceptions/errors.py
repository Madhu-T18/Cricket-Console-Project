class TournamentError(Exception):
    pass

class TeamNotFoundError(TournamentError):
    def __init__(self, name):
        super().__init__(f"Team '{name}' not found.")

class NotEnoughPlayersError(TournamentError):
    def __init__(self, team, count):
        super().__init__(f"'{team}' has only {count} player(s). Need at least 2.")