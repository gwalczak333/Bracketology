"""Test for simulate_round function."""

import random

from bracketology_utilities import Bracket, Round, Team


def test_simulate_round() -> None:
    """Give 4 teams, ensure 2 winners are returned."""
    teams = [
        Team("Duke", "1", "East", {Round.ELITE_8: 0.9}),
        Team("Auburn", "3", "South", {Round.ELITE_8: 0.1}),
        Team("Houston", "1", "Midwest", {Round.ELITE_8: 0.8}),
        Team("UCLA", "4", "West", {Round.ELITE_8: 0.2}),
    ]
    bracket = Bracket(teams)
    random.seed(0)
    winners = bracket.simulate_round(teams, Round.ELITE_8)

    # Check that 2 winners are returned
    assert len(winners) == 2

    # Check that the winners are instances of Team
    assert all(isinstance(w, Team) for w in winners)
