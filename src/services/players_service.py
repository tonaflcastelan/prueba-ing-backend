from src.constants.constants import LEVELS
from src.helpers.operations import get_average, get_percent


def players_service(players) -> dict:
    """
    Compute goals by player and team and return full salary
    """
    teams = group_by_team(players)
    total_goals = team_goals(players)
    for player in players:
        minimum_goals = LEVELS[player["nivel"]]
        goals = teams[player["equipo"]]["goals"]
        total_goals = teams[player["equipo"]]["team_goals"]
        player_goal = get_percent(player["goles"], minimum_goals)
        team_goal = get_percent(goals, total_goals)
        average = get_average(player_goal, team_goal)
        salary = get_salary_player(player, average)
        player["sueldo_completo"] = salary
    return players


def group_by_team(players):
    """
    Get goals grouped by team
    """
    teams = {}
    for player in players:
        team = player["equipo"]
        team_goals = LEVELS[player["nivel"]]
        player["team_goals"] = team_goals
        if team in teams:
            teams[team]["goals"] += player["goles"]
            teams[team]["team_goals"] += player["team_goals"]
        else:
            teams[team] = {"goals": player["goles"], "team_goals": player["team_goals"]}
    return teams


def get_salary_player(player, average) -> float:
    """
    Get full salary per player
    """
    bono = (average * player["bono"]) / 100
    return bono + player["sueldo"]


def team_goals(players) -> dict:
    """
    Get total goals by team 
    """
    goals = 0
    team_goals = 0
    for player in players:
        team_goals += LEVELS[player["nivel"]]
        goals += player["goles"]
    return team_goals, goals
