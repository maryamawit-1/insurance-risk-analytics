# Insurance Risk Analytics

## Objective
Perform exploratory data analysis on insurance claim data to identify risk patterns and profitability insights.

## Project Structure
- notebooks/ → analysis notebooks
- src/ → reusable python modules
- tests/ → unit tests
- reports/ → findings

## Task 1
Git setup, CI/CD, and Exploratory Data Analysis.

## Data Version Control (Task 2)

### Reproduce data pipeline

1. Clone repository

```bash
git clone https://github.com/maryamawit-1/insurance-risk-analytics
cd insurance-risk-analytics
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Pull tracked data

```bash
dvc pull
```

4. Run conversion

```bash
python src/data/convert_data.py
```

5. Run cleaning

```bash
python src/data/clean_data.py
```