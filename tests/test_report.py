import json, os

def test_stats_exists():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "stats.json")
    assert os.path.exists(path)

def test_stats_valid():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "stats.json")
    with open(path) as fh:
        d = json.load(fh)
    assert "language" in d
