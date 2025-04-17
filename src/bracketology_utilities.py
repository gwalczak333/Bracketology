"""Bracketology Utilities."""

import random


class Team:
    """Class representing a team in a tournament."""

    def __init__(
        self, name: str, seed: int, adj_o: float, adj_d: float, adj_t: float
    ):
        self.name = name
        self.seed = seed
        self.adj_o = adj_o
        self.adj_d = adj_d
        self.adj_t = adj_t

    @property
    def adj_em(self) -> float:
        """Adjusted Efficiency Margin (AdjEM) = AdjO - AdjD."""
        return self.adj_o - self.adj_d  # Adjusted Efficiency Margin

    def __repr__(self) -> str:
        """String representation of the Team object."""
        return f"Team('{self.name}', seed={self.seed}, AdjO={self.adj_o}, AdjD={self.adj_d})"

    def __eq__(self, other: object) -> bool:
        """Check equality of two Team objects."""
        return (
            isinstance(other, Team)
            and self.name == other.name
            and self.seed == other.seed
            and self.adj_o == other.adj_o
            and self.adj_d == other.adj_d
        )

    def expected_score(self, opponent: "Team") -> float:
        """Compute expected margin of victory using KenPom-style ratings."""
        off_vs_def = self.adj_o - opponent.adj_d
        def_vs_off = opponent.adj_o - self.adj_d
        return (off_vs_def - def_vs_off) / 2  # Average margin

    def win_probability(self, opponent: "Team") -> float:
        """Compute win probability using expected margin and logistic regression.

        KenPom-style: p = 1 / (1 + 10^(-margin/10))
        """
        margin = self.expected_score(opponent)
        return 1 / (1 + 10 ** (-margin / 10))


class Bracket:
    """Class representing a tournament bracket."""

    def __init__(self, teams: list[Team]):
        """Initialize the Bracket with a list of teams."""
        self.teams = sorted(teams, key=lambda t: t.seed)
        self.rounds: list[list[Team]] = []

    def simulate_round(self, teams: list[Team]) -> list[Team]:
        """Simulate a round of the tournament."""
        winners = []
        for i in range(0, len(teams), 2):
            t1, t2 = teams[i], teams[i + 1]
            winner = simulate_game(t1, t2)
            winners.append(winner)
        return winners

    def simulate_tournament(self) -> Team:
        """Simulate the entire tournament and return the champion."""
        current_round = self.teams
        while len(current_round) > 1:
            self.rounds.append(current_round)
            current_round = self.simulate_round(current_round)
        self.rounds.append(current_round)  # Final winner
        return current_round[0]  # Champion

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


def simulate_teams(num_teams: int = 64) -> list[Team]:
    """Simulate a list of teams with random attributes."""
    teams = []
    for i in range(num_teams):
        name = f"Team {i + 1}"
        seed = (i % 16) + 1
        adj_o = round(random.uniform(105, 120), 2)
        adj_d = round(random.uniform(90, 105), 2)
        adj_t = round(random.uniform(65, 72), 2)
        team = Team(
            name=name, seed=seed, adj_o=adj_o, adj_d=adj_d, adj_t=adj_t
        )
        teams.append(team)
    return teams


def simulate_game(team1: Team, team2: Team) -> Team:
    """Simulate a game between two teams using win probabilities."""
    prob = team1.win_probability(team2)
    return team1 if random.random() < prob else team2


if __name__ == "__main__":
    teams = simulate_teams()
    bracket = Bracket(teams)
    champion = bracket.simulate_tournament()
    (print(f"Champion: {champion.name}, Seed: {champion.seed}"),)
    bracket.display_bracket()
