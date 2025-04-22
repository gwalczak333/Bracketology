"""Test for simulate_game function."""

from bracketology_utilities import Round, Team, simulate_game


def test_simulate_game() -> None:
    """Test the simulate_game function."""
    # Create three teams with win probabilities
    team1 = Team(
        name="Duke",
        seed="1",
        region="East",
        win_probs={
            Round.SECOND_ROUND: 0.8,
            Round.SWEET_16: 0.7,
            Round.ELITE_8: 0.6,
            Round.FINAL_FOUR: 0.5,
            Round.CHAMPIONSHIP: 0.4,
        },
    )
    team2 = Team(
        name="UCLA",
        seed="2",
        region="West",
        win_probs={
            Round.SECOND_ROUND: 0.2,
            Round.SWEET_16: 0.3,
            Round.ELITE_8: 0.4,
            Round.FINAL_FOUR: 0.5,
            Round.CHAMPIONSHIP: 0.6,
        },
    )
    team3 = Team(
        name="Auburn",
        seed="1",
        region="South",
        win_probs={
            Round.SECOND_ROUND: 0.5,
            Round.SWEET_16: 0.4,
            Round.ELITE_8: 0.3,
            Round.FINAL_FOUR: 0.0,
            Round.CHAMPIONSHIP: 0.0,
        },
    )

    # Simulate a game between the two teams
    winner1 = simulate_game(team1, team2, Round.SECOND_ROUND)

    winner2 = simulate_game(team1, team3, Round.FINAL_FOUR)

    # Check that the winner is one of the teams
    assert winner1 in [team1, team2]

    # Check that the winner is the expected team with the higher win prob
    # Since Auburn has a 0% chance of winning in the FINAL_FOUR, team1 should
    # win
    assert winner2 == team1
