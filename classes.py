import random

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Match:
    def __init__(self, days_since_game0, atp, location, tournament, series, court, surface, round, bestof, comment, winner_id, loser_id):
        self.days_since_game0 = days_since_game0
        self.atp = atp
        self.location = location
        self.tournament = tournament
        self.series = series
        self.court = court
        self.surface = surface
        self.round = round
        self.bestof = bestof
        self.comment = comment

        r = random.randint(0,1)
        if r: # If r is 1
            self.player1_id = loser_id
            self.player2_id = winner_id
        else: # If r is 0
            self.player1_id = winner_id
            self.player2_id = loser_id

        self.winner = r

class MatchPlayerStats:
    def __init__(self, match_id, player_id, rank, matchpoints, setswinrate, won):
        self.match_id = match_id
        self.player_id = player_id
        self.rank = rank
        self.matchpoints = matchpoints
        self.setswinrate = setswinrate
        self.won = won

class MatchPlayerOdds:
    def __init__(self, match_id, player_id, max, min, avg, std):
        self.match_id = match_id
        self.player_id = player_id
        self.max = max
        self.min = min
        self.avg = avg
        self.std = std
