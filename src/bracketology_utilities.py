"""Bracketology Utilities."""

import random
from enum import Enum


class Round(Enum):
    """Enum representing the rounds of a tournament."""

    FIRST_ROUND = "First Round"
    SECOND_ROUND = "Second Round"
    SWEET_16 = "Sweet 16"
    ELITE_8 = "Elite 8"
    FINAL_FOUR = "Final Four"
    CHAMPIONSHIP = "Championship"


class Team:
    """Class representing a team in a tournament."""

    def __init__(
        self, name: str, seed: str, region: str, win_probs: dict[Round, float]
    ):
        """Initialize the team with its name, seed, region, and win_probs."""
        self.name = name
        self.seed = seed
        self.region = region
        self.win_probs = (
            win_probs  # {"Rd2": 99.5, "Swt16": 84.6, ..., "Champ": 22.9}
        )

    def get_win_prob(self, round_name: Round) -> float:
        """Get the win probability for a specific round."""
        return self.win_probs.get(round_name, 0.0)

    def __repr__(self) -> str:
        """Return a string representation of the team."""
        return f"{self.seed} {self.name}"

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
        current_round = self.teams
        round_idx = 0

        while len(current_round) > 1 and round_idx < len(self.round_keys):
            round_name = self.round_keys[round_idx]
            self.rounds.append(current_round)
            current_round = self.simulate_round(current_round, round_name)
            round_idx += 1

        self.rounds.append(current_round)  # Final winner
        return current_round[0]

    def display_bracket(self) -> None:
        """Display the tournament bracket in a readable format."""
        round_names = [
            "First Round",
            "Second Round",
            "Sweet 16",
            "Elite 8",
            "Final Four",
            "Championship",
        ]

        for i, round_teams in enumerate(self.rounds):
            round_name = (
                round_names[i] if i < len(round_names) else f"Round {i + 1}"
            )
            print(f"\n{round_name}:")
            for team in round_teams:
                print(f"  {team.name} (Seed {team.seed})")


def simulate_game(team1: Team, team2: Team, round_name: Round) -> Team:
    """Simulate a game between two teams using KenPom-style win probs."""
    prob1 = team1.get_win_prob(round_name)
    prob2 = team2.get_win_prob(round_name)

    # Normalize if total > 0, else use 50/50
    total = prob1 + prob2
    p = prob1 / total if total > 0 else 0.5

    return team1 if random.random() < p else team2


if __name__ == "__main__":
    team1 = Team(
        "Duke",
        "1",
        "East",
        {
            Round.FIRST_ROUND: 98.7,
            Round.SECOND_ROUND: 88.2,
            Round.SWEET_16: 72.5,
            Round.ELITE_8: 54.1,
            Round.FINAL_FOUR: 38.6,
            Round.CHAMPIONSHIP: 21.0,
        },
    )
    team2 = Team(
        "UNC",
        "2",
        "East",
        {
            Round.FIRST_ROUND: 95.4,
            Round.SECOND_ROUND: 70.1,
            Round.SWEET_16: 60.2,
            Round.ELITE_8: 33.9,
            Round.FINAL_FOUR: 22.5,
            Round.CHAMPIONSHIP: 10.2,
        },
    )

    bracket = Bracket([team1, team2])  # For simplicity, just 2 teams here
    champ = bracket.simulate_tournament()
    bracket.display_bracket()
    print(f"\nChampion: {champ}")
