# Bracketology
March Madness-inspired Python library

**Bracketology** is a Python library that simulates and analyzes single-elimination tournament brackets (e.g., NCAA March Madness). The library supports team creation, game simulation, bracket generation, and probability-based analysis.

---

## Features

- Create custom teams with stats and seeds
- Simulate tournament games based on probabilities or random draws
- Generate and resolve full tournament brackets
- Analyze win probabilities and simulate many tournaments
- Import real-world data for simulation

---

## Structure

- `src/`
  - `bracketology_utils.py`: Defines `Team` class with attributes like name, seed, and rating
  - `team.py`: Defines `Team` class with attributes like name, seed, and rating, builds and stores the tournament bracket, runs matchups and full simulations, and summarizes win rates, upset counts, etc.
- `tests/`
  - Unit tests for all core components using `pytest`
- `README.md`: Project overview
- `.gitignore`: Python file exclusions
- `pyproject.toml`: Project configuration and ruff setup

---

## Development

This project uses:

- `pytest` for tests
- `ruff` for code style
- GitHub Issues & PRs to track progress

To lint: 

```bash
ruff bracketology/
```

To run tests:

```bash
pytest tests/
```


