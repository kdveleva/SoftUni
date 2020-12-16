from project.player.player import Player


class PlayerRepository:
    count: int  # the count of players
    players: list  # collection of players

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        try:
            player = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {player.username} already exists!")
        except IndexError:
            self.players.append(player)
            self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!") # could a space be an empty string
        else:
            player_to_remove = self.find(player)
            self.players.remove(player_to_remove)
            self.count -= 1

    def find(self, username: str):
        try:
            player_to_return = [x for x in self.players if x.username == username][0]
            return player_to_return
        except IndexError:
            return "Player not found"
