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


if __name__ == "__main__":
    teams = simulate_teams()
    for t in teams[:5]:  # Print the first 5 teams
        print(t)
