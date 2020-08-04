import copy
import sys

from src.services.players_service import players_service


class App:
    def __init__(self, payload):
        self.payload = copy.deepcopy(payload)

    def compute_salary(self):
        if not self.payload["data"]:
            sys.exit("Data is not found")

        players = self.payload["data"]

        return players_service(players)
