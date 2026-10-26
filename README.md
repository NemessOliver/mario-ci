# Mario CI

The CS50 "Mario" pyramid in Python, with pytest tests and a GitHub Actions workflow that runs the tests on every push.

```
Height: 4
   #
  ##
 ###
####
```

## Files

| File | What it does |
|---|---|
| `mario.py` | asks for a height (1–8) and prints the pyramid |
| `test_mario.py` | 7 pytest tests (normal heights, right alignment, height 0, bad input) |
| `.github/workflows/ci.yml` | the CI workflow: on every push GitHub installs Python 3.12 + pytest and runs the tests |

## Run it yourself (VS Code terminal)

```
python3 mario.py
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
python -m pytest -q
```

## CI

Every push starts the **Mario CI** workflow (tab *Actions* on GitHub).
Green check = all tests passed, red cross = a test failed.
