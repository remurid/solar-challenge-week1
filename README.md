# solar-challenge-week1

## Overview
This project profiles, cleans, and explores solar datasets for regional comparison and ranking. It includes modular, reusable code for data profiling, cleaning, and exploratory data analysis (EDA).

## Reproducing the Environment

1. **Clone the repository:**
   ```sh
   git clone https://github.com/remurid/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Set up Python (recommended: Python 3.13):**
   Make sure you have Python 3.13 installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

> The `requirements.txt` file lists all Python dependencies needed for this project.

## Project Structure

```
solar-challenge-week1/
├── data/                # Raw and cleaned data files (not tracked by git)
├── notebooks/           # Jupyter notebooks for EDA and analysis
├── scripts/             # Utility or automation scripts
├── src/                 # Reusable Python modules (e.g., data_utils.py)
├── tests/               # Unit tests (if any)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Files/folders to exclude from git
```

## Usage
- Run EDA notebooks in the `notebooks/` directory for each country.
- Use functions in `src/data_utils.py` for summary statistics, missing value analysis, outlier detection, and cleaning.
