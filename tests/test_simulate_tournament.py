"""Test for simulate_tournament function."""

import random

from bracketology_utilities import Bracket, Round, Team


def make_simple_team(name: str, seed: str, prob: float = 0.5) -> Team:
    """Creates simple teams in the East region to set up the test."""
    return Team(
        name,
        seed,
        "East",
        {
            Round.FIRST_ROUND: prob,
            Round.SECOND_ROUND: prob,
            Round.SWEET_16: prob,
            Round.ELITE_8: prob,
            Round.FINAL_FOUR: prob,
            Round.CHAMPIONSHIP: prob,
        },
    )


def test_simulate_tournament_single_champion() -> None:
    """Test that the simulate_tournament function returns a single champion."""
    # Create 8 teams with high win prob for early seeds
    teams = [
        make_simple_team("A", "1", 0.9),
        make_simple_team("B", "8", 0.1),
        make_simple_team("C", "2", 0.9),
        make_simple_team("D", "7", 0.1),
        make_simple_team("E", "3", 0.9),
        make_simple_team("F", "6", 0.1),
        make_simple_team("G", "4", 0.9),
        make_simple_team("H", "5", 0.1),
    ]
    random.seed(123)
    bracket = Bracket(teams)
    champion = bracket.simulate_tournament()

    assert isinstance(champion, Team)
    assert champion in teams
    assert len(bracket.rounds[-1]) == 1
    assert champion == bracket.rounds[-1][0]
