"""Bracketology Utilities."""


class Team:
    """Class representing a team in a tournament."""

    def __init__(self, name: str, seed: int, rating: float):
        """Initialize a Team instance."""
        self.name = name
        self.seed = seed
        self.rating = rating

    def __repr__(self) -> str:
        """String representation of the team."""
        return (
            f"Team(name='{self.name}', seed={self.seed}, rating={self.rating})"
        )

    def __eq__(self, other: object) -> bool:
        """Check equality based on name, seed, and rating."""
        return (
            isinstance(other, Team)
            and self.name == other.name
            and self.seed == other.seed
            and self.rating == other.rating
        )

    def win_probability(self, opponent: "Team") -> float:
        """Compute the probability that this team wins against another."""
        diff = self.rating - opponent.rating
        return 1 / (1 + 10 ** (-diff / 400))
