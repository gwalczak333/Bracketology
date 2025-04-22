# Bracketology

**Bracketology** A Python library for simulating a March Madness-style NCAA tournament using teams, seeds, regions, and KenPom-style round-based win probabilities..

---

### Installation
1. Clone this repository:

```zsh
gh repo clone gwalczak333/Bracketology
```

2. Install dependencies:
```zsh
pip install -r requirements-test.txt
```
 
---

## Features

- Represent tournament Teams with seed, region, and round-specific win probabilities
- Load team data from a CSV file (optional)
- Simulate individual games using probabilistic outcomes
- Build and run an entire tournament bracket, round by round
- Display the full bracket in a readable format

---

## Structure

- `src/`
  - `bracketology_utilities.py`: Core logic (Team, Bracket, simulate_game)
- `tests/`
  - `test_simulate_game.py`: Unit tests for simulate_game()
  - `test_simulate_round.py`: Unit tests for simulate_round()
  - `test_simulate_tournament.py`: Unit tests for simulate_tournament()
  - `teams.csv`: Example team data (optional)
- `README.md`: Project overview
- `.gitignore`: Python file exclusions
- `pyproject.toml`: Project configuration and ruff setup
- `requirements-test.txt`: Requirements for testing

---

## Usage

1. Setting up data
  - Define Teams Manually

  ```python
  from bracketology_utilities import Team, Bracket, Round

  team1 = Team("Duke", "1", "East", {
      Round.SECOND_ROUND: 0.85,
      Round.SWEET_16: 0.75,
      Round.ELITE_8: 0.7,
      Round.FINAL_FOUR: 0.65,
      Round.CHAMPIONSHIP: 0.6,
  })
  team2 = Team("UNC", "8", "East", {
      Round.SECOND_ROUND: 0.45,
      Round.SWEET_16: 0.4,
      Round.ELITE_8: 0.35,
      Round.FINAL_FOUR: 0.3,
      Round.CHAMPIONSHIP: 0.25,
  })
  ```

  **OR**

  - Load Teams data from a CSV

  CSV format (example):
  ```csv
  name,seed,region,FIRST_ROUND,SECOND_ROUND,SWEET_16,ELITE_8,FINAL_FOUR,CHAMPIONSHIP
  Duke,1,East,1.0,0.85,0.75,0.7,0.65,0.6
  UNC,8,East,0.7,0.45,0.4,0.35,0.3,0.25
  ...
  ```

  ```python
  from bracketology_utilities import load_teams_from_csv

  teams = load_teams_from_csv("teams.csv")
  bracket = Bracket(teams)
  ```

2. Simulate a Game

```python
from bracketology_utilities import simulate_game

winner = simulate_game(team1, team2, Round.SECOND_ROUND)
print(f"Winner: {winner.name}")
```

3. Simulate a Full Tournament

```python
bracket = Bracket([team1, team2, team3, ..., team64])
champion = bracket.simulate_tournament()
print(f"Champion: {champion.name}")
```

---

## Development

This project uses:

- `pytest` for tests
  - Each simulation function has its own test file:
    - `test_simulate_game.py`
    - `test_simulate_round.py`
    - `test_simulate_tournament.py`
  - To run all the tests locally, use the following command:
  ```zsh
  pytest tests/
  ```
- `ruff` for code style
  - To lint: 
  ```zsh
  ruff Bracketology/
  ```


