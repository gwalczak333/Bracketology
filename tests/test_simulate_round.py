"""Test for simulate_round function."""

import random

from bracketology_utilities import Bracket, Round, Team


def test_simulate_round() -> None:
    """Give 4 teams, ensure 2 winners are returned."""
    teams = [
        Team("T1", "1", "A", {Round.ELITE_8: 0.9}),
        Team("T2", "2", "A", {Round.ELITE_8: 0.1}),
        Team("T3", "3", "A", {Round.ELITE_8: 0.8}),
        Team("T4", "4", "A", {Round.ELITE_8: 0.2}),
    ]
    bracket = Bracket(teams)
    random.seed(0)
    winners = bracket.simulate_round(teams, Round.ELITE_8)

    assert len(winners) == 2
    assert all(isinstance(w, Team) for w in winners)
