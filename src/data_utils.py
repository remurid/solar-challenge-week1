"""
data_utils.py
Reusable functions for EDA: summary statistics, missing value report, outlier detection, cleaning, and imputation.
"""
import numpy as np
import pandas as pd
from scipy import stats
from IPython.display import display

def summary_and_missing(df):
    """
    Display summary statistics and missing value report for a DataFrame.
    Args:
        df (pd.DataFrame): Input DataFrame.
    Returns:
        pd.Series: Percentage of missing values per column.
    """
    print(df.describe())  # Show summary statistics
    missing_report = df.isna().sum() / len(df) * 100
    print("Columns with >5% missing values:")
    print(missing_report[missing_report > 5].sort_values(ascending=False))
    return missing_report

def detect_outliers(df, cols):
    """
    Print the number of outliers (Z-score > 3) for each specified column.
    Args:
        df (pd.DataFrame): Input DataFrame.
        cols (list): List of columns to check for outliers.
    Returns:
        np.ndarray: Boolean array indicating outlier positions.
    """
    z_scores = np.abs(stats.zscore(df[cols], nan_policy='omit'))
    outliers = (z_scores > 3)
    print("Number of outliers per column:")
    print(pd.DataFrame(outliers, columns=cols).sum())
    return outliers

def impute_median(df, cols):
    """
    Impute missing values in specified columns with the median.
    Args:
        df (pd.DataFrame): Input DataFrame.
        cols (list): List of columns to impute.
    Returns:
        pd.DataFrame: DataFrame with imputed values.
    """
    for col in cols:
        df[col] = df[col].fillna(df[col].median())
    return df

def clean_outliers(df, cols):
    """
    Replace outliers in specified columns with NaN based on Z-score > 3.
    Args:
        df (pd.DataFrame): Input DataFrame.
        cols (list): List of columns to check for outliers.
    Returns:
        pd.DataFrame: DataFrame with outliers replaced by NaN.
    """
    z_scores = np.abs(stats.zscore(df[cols], nan_policy='omit'))
    outliers = (z_scores > 3)
    df_clean = df.copy()
    for i, col in enumerate(cols):
        df_clean.loc[outliers[:, i], col] = np.nan
    return df_clean
