from src.services.players_service import (
    get_salary_player,
    group_by_team,
    players_service,
    team_goals,
)

players = [
    {
        "nombre": "Juan Perez",
        "nivel": "C",
        "goles": 10,
        "sueldo": 50000,
        "bono": 25000,
        "sueldo_completo": None,
        "equipo": "rojo",
    },
    {
        "nombre": "EL Cuauh",
        "nivel": "Cuauh",
        "goles": 30,
        "sueldo": 100000,
        "bono": 30000,
        "sueldo_completo": None,
        "equipo": "azul",
    },
    {
        "nombre": "Cosme Fulanito",
        "nivel": "A",
        "goles": 7,
        "sueldo": 20000,
        "bono": 10000,
        "sueldo_completo": None,
        "equipo": "azul",
    },
    {
        "nombre": "El Rulo",
        "nivel": "B",
        "goles": 9,
        "sueldo": 30000,
        "bono": 15000,
        "sueldo_completo": None,
        "equipo": "rojo",
    },
]


def test_team_goals():
    goals = team_goals(players)
    assert goals[0] == 80
    assert goals[1] == 56


def test_salary_player():
    player = {
        "nombre": "EL Cuauh",
        "nivel": "Cuauh",
        "goles": 30,
        "sueldo": 100000,
        "bono": 30000,
        "sueldo_completo": None,
        "equipo": "azul",
    }
    salary = get_salary_player(player, 95)
    assert salary == 128500


def test_group_team():
    teams = group_by_team(players)
    assert type(teams) is dict
    assert teams["rojo"]["team_goals"] == 25
    assert teams["azul"]["team_goals"] == 55


def test_players_service():
    service = players_service(players)
    assert type(service) is list
    assert service is not None
