from src.helpers.operations import get_average, get_percent


def test_averege():
    avg = get_average(2, 3)
    assert avg == 2.5


def test_percent():
    percent = get_percent(66, 6)
    assert percent == 1100
