# Summary Toolkit

A modular project summary generator. Produces a structured summary
report from project source files.

## Setup

```bash
make setup
```

Installs dependencies, runs self-checks, and generates a sample
summary report in `build/summary.txt`.

## Files

- `scripts/report.py` — CLI report generator
- `data/stats.json` — project statistics
- `tests/` — self-check suite
- `requirements.txt` — external packages
