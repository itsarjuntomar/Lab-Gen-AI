# Week 5 – Token Economics

A small Python budget planner that estimates token consumption, hosted API cost, RPM/TPM capacity, and daily/monthly budget status before building an LLM feature.

## Files

- `budget.py` – reads planning assumptions, calculates usage/cost, applies a safety margin, and prints a go/no-go report.
- `test_budget.py` – tests cost and capacity calculations.
- `.env.example` – sample assumptions; copy it to `.env` and edit values.
- `requirements.txt` – Python dependency.
- `.gitignore` – excludes local secrets and generated files.

## Setup

Activate your existing lab virtual environment and install:

```powershell
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` in this folder. The sample prices and limits are illustrative; replace them with the current price and quota for your exact model, account, and tier.

## Run

```powershell
python budget.py
```

## Run tests

```powershell
python -m unittest test_budget.py
```

## Formulas

- Input tokens/day = requests/day × average input tokens/request
- Output tokens/day = requests/day × average output tokens/request
- Daily cost = (input tokens/day × input price + output tokens/day × output price) ÷ 1,000,000
- Monthly cost = daily cost × 30
- Peak RPM and total TPM are multiplied by the safety-margin factor.

The planner checks RPM, TPM, daily budget, and monthly budget separately. Its result is a planning estimate, not a billing guarantee. Provider quota definitions and retry billing can differ.
