# Bracketology
March Madness-inspired Python library

**Bracketology** is a Python library that simulates and analyzes single-elimination tournament brackets (e.g., NCAA March Madness). The library supports team creation, game simulation, bracket generation, and probability-based analysis.

---

## Features

- Create custom teams with stats and seeds
- Simulate tournament games based on probabilities or random draws
- Generate and resolve full tournament brackets
- Analyze win probabilities and simulate many tournaments

---

## Structure

- `src/`
  - `bracketology_utilities.py`: Defines `Team` class with attributes like name, seed, and rating, as well as Bracket class, which simulates rounds and the tournament. 
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
ruff Bracketology/
```

To run tests:

```bash
pytest tests/
```


