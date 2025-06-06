"""Bracketology Utilities."""

import csv
import random
from enum import Enum


class Round(Enum):
    """Enum representing the rounds of a tournament."""

    FIRST_ROUND = "FIRST_ROUND"
    SECOND_ROUND = "SECOND_ROUND"
    SWEET_16 = "SWEET_16"
    ELITE_8 = "ELITE_8"
    FINAL_FOUR = "FINAL_FOUR"
    CHAMPIONSHIP = "CHAMPIONSHIP"


class Team:
    """Class representing a team in a tournament."""

    def __init__(
        self, name: str, seed: str, region: str, win_probs: dict[Round, float]
    ):
        """Initialize the team with its name, seed, region, and win_probs."""
        self.name = name
        self.seed = seed
        self.region = region
        self.win_probs = win_probs

    def get_win_prob(self, round_name: Round) -> float:
        """Get the win probability for a specific round."""
        return self.win_probs.get(round_name, 0.0)

    def __eq__(self, other: object) -> bool:
        """Check equality of two teams."""
        return (
            isinstance(other, Team)
            and self.name == other.name
            and self.seed == other.seed
            and self.region == other.region
            and self.win_probs == other.win_probs
        )


class Bracket:
    """Class representing a tournament bracket."""

    def __init__(self, teams: list[Team]):
        """Initialize the bracket with a list of teams."""
        self.teams = sorted(teams, key=lambda t: int(t.seed))  # Sort by seed
        self.rounds: list[list[Team]] = []

        # Round keys for matching win_probs dict keys
        self.round_keys = [
            Round.SECOND_ROUND,
            Round.SWEET_16,
            Round.ELITE_8,
            Round.FINAL_FOUR,
            Round.CHAMPIONSHIP,
        ]

    def simulate_round(
        self, remaining_teams: list[Team], round_name: Round
    ) -> list[Team]:
        """Simulate a round of the tournament with win probabilities."""
        winners = []
        for i in range(0, len(remaining_teams), 2):
            t1, t2 = remaining_teams[i], remaining_teams[i + 1]
            winner = simulate_game(t1, t2, round_name)
            winners.append(winner)
        return winners

    def simulate_tournament(self) -> Team:
        """Simulate the entire tournament and return the champion."""
        remaining_teams = self.teams
        round_idx = 0

        while len(remaining_teams) > 1 and round_idx < len(self.round_keys):
            round_name = self.round_keys[round_idx]
            self.rounds.append(remaining_teams)
            remaining_teams = self.simulate_round(remaining_teams, round_name)
            round_idx += 1

        self.rounds.append(remaining_teams)  # Final winner
        return remaining_teams[0]

    def display_bracket(self) -> None:
        """Display the tournament bracket in a readable format."""
        round_names = [
            "FIRST_ROUND",
            "SECOND_ROUND",
            "SWEET_16",
            "ELITE_8",
            "FINAL_FOUR",
            "CHAMPIONSHIP",
        ]

        for i, round_teams in enumerate(self.rounds):
            round_name = (
                round_names[i] if i < len(round_names) else f"Round {i + 1}"
            )
            print(f"\n{round_name}:")
            for team in round_teams:
                print(f"  {team.name} (Seed {team.seed})")


def load_teams_from_csv(path: str) -> list[Team]:
    """Load a list of teams from a CSV file.

    Columns: name,seed,region,FIRST_ROUND,SECOND_ROUND,SWEET_16,ELITE_8,
    FINAL_FOUR,CHAMPIONSHIP
    """
    teams = []
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"]
            seed = row["seed"]
            region = row["region"]
            win_probs = {
                Round.FIRST_ROUND: float(row.get("FIRST_ROUND", 0.5)),
                Round.SECOND_ROUND: float(row.get("SECOND_ROUND", 0.5)),
                Round.SWEET_16: float(row.get("SWEET_16", 0.5)),
                Round.ELITE_8: float(row.get("ELITE_8", 0.5)),
                Round.FINAL_FOUR: float(row.get("FINAL_FOUR", 0.5)),
                Round.CHAMPIONSHIP: float(row.get("CHAMPIONSHIP", 0.5)),
            }
            team = Team(
                name=name, seed=seed, region=region, win_probs=win_probs
            )
            teams.append(team)
    return teams


def simulate_game(team1: Team, team2: Team, round_name: Round) -> Team:
    """Simulate a game between two teams using KenPom-style win probs."""
    prob1 = team1.get_win_prob(round_name)
    prob2 = team2.get_win_prob(round_name)

    # Normalize if total > 0, else use 50/50
    total = prob1 + prob2
    p = prob1 / total if total > 0 else 0.5

    return team1 if random.random() < p else team2
