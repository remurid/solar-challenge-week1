# solar-challenge-week1

## Overview
This project profiles, cleans, and explores solar datasets for regional comparison and ranking. It includes modular, reusable code for data profiling, cleaning, and exploratory data analysis (EDA), as well as an interactive dashboard for visual insights.

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
├── app/                 # Streamlit dashboard application
│   ├── main.py          # Main Streamlit app script
│   └── ...
├── data/                # Raw and cleaned data files (not tracked by git)
├── notebooks/           # Jupyter notebooks for EDA and cross-country analysis
├── scripts/             # Utility or automation scripts
├── src/                 # Reusable Python modules (e.g., data_utils.py, country_comparator.py)
├── tests/               # Unit tests (if any)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Files/folders to exclude from git
```

## Usage
- Run EDA notebooks in the `notebooks/` directory for each country (e.g., `benin_eda.ipynb`).
- Use functions in `src/data_utils.py` for summary statistics, missing value analysis, outlier detection, and cleaning.
- Use `src/country_comparator.py` for cross-country comparison and statistical analysis (see `compare_countries.ipynb`).
- Launch the interactive dashboard:
  ```sh
  streamlit run app/main.py
  ```
  Use the sidebar to select countries and metrics for comparison. The dashboard provides boxplots and a ranking table for solar potential.

## Cross-Country Comparison
- See `notebooks/compare_countries.ipynb` for a full analysis comparing Benin, Sierra Leone, and Togo.
- Includes boxplots, summary tables, statistical tests, and key insights for solar potential.



