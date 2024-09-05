# esports.py
# Caleb Roge
# Kody Bond

class Esports():
    
    def __init__(self, games_played, total_kills, kill_assists, total_gold, total_earnings):
        self._games_played = games_played
        self._total_kills = total_kills
        self._kill_assists = kill_assists
        self._total_gold = total_gold
        self._total_earnings = total_earnings
    
    @property
    def games_played(self):
        return self._games_played
    
    @property
    def total_kills(self):
        return self._total_kills
    
    @property
    def kill_assists(self):
        return self._kill_assists
    
    @property
    def total_gold(self):
        return self._total_gold
    
    @property
    def total_earnings(self):
        return self._total_earnings
    
    
    def __str__(self):
        """This method is automatically when an object of this class is in a print() call."""
        return (f"Esports League of Legends Player Information\n" +
                f"Games Played   : {self.games_played}\n" +
                f"Total Kills    : {self.total_kills}\n" +
                f"Kill Assists   : {self.kill_assists}\n" +
                f"Total Gold     : {self.total_gold:,}\n"  +
                f"Total Earnings : ${self.total_earnings:,}\n")
                