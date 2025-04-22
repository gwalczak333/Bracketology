"""Test for the load_teams_from_csv function."""

import os

from bracketology_utilities import Round, Team, load_teams_from_csv


def test_load_csv() -> None:
    """Testing the load_teams_from_csv function."""
    test_csv_path = "test_teams.csv"

    # Manually create the CSV file
    with open(test_csv_path, "w") as f:
        f.write("name,seed,region,FIRST_ROUND,SECOND_ROUND\n")
        f.write("Duke,1,East,0.9,0.75\n")
        f.write("UCLA,2,West,0.6,0.55\n")

    # Run the test
    teams = load_teams_from_csv(test_csv_path)

    expected_teams = [
        Team(
            name="Duke",
            seed="1",
            region="East",
            win_probs={
                Round.FIRST_ROUND: 0.9,
                Round.SECOND_ROUND: 0.75,
                Round.SWEET_16: 0.5,
                Round.ELITE_8: 0.5,
                Round.FINAL_FOUR: 0.5,
                Round.CHAMPIONSHIP: 0.5,
            },
        ),
        Team(
            name="UCLA",
            seed="2",
            region="West",
            win_probs={
                Round.FIRST_ROUND: 0.6,
                Round.SECOND_ROUND: 0.55,
                Round.SWEET_16: 0.5,
                Round.ELITE_8: 0.5,
                Round.FINAL_FOUR: 0.5,
                Round.CHAMPIONSHIP: 0.5,
            },
        ),
    ]

    assert teams == expected_teams

    os.remove(test_csv_path)
