import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, kruskal

class CountryComparator:
    """
    Class for cross-country solar data comparison and statistical analysis.
    """
    def __init__(self, benin_path, sierraleone_path, togo_path):
        """
        Load cleaned datasets and combine them for analysis.
        """
        self.df_benin = pd.read_csv(benin_path, parse_dates=['Timestamp'])
        self.df_sierraleone = pd.read_csv(sierraleone_path, parse_dates=['Timestamp'])
        self.df_togo = pd.read_csv(togo_path, parse_dates=['Timestamp'])
        self.df_benin['Country'] = 'Benin'
        self.df_sierraleone['Country'] = 'Sierra Leone'
        self.df_togo['Country'] = 'Togo'
        self.df_all = pd.concat([self.df_benin, self.df_sierraleone, self.df_togo], ignore_index=True)

    def plot_boxplots(self, metrics=['GHI', 'DNI', 'DHI']):
        """
        Plot boxplots for each metric by country.
        """
        for metric in metrics:
            plt.figure(figsize=(8, 5))
            sns.boxplot(x='Country', y=metric, data=self.df_all, palette='Set2')
            plt.title(f'{metric} Distribution by Country')
            plt.ylabel(metric)
            plt.xlabel('Country')
            plt.show()

    def summary_table(self):
        """
        Return a summary table (mean, median, std) for GHI, DNI, DHI by country.
        """
        summary = self.df_all.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std'])
        return summary

    def statistical_tests(self):
        """
        Run one-way ANOVA and Kruskal–Wallis tests for GHI across countries.
        Returns a dict with p-values.
        """
        ghi_benin = self.df_benin['GHI'].dropna()
        ghi_sierraleone = self.df_sierraleone['GHI'].dropna()
        ghi_togo = self.df_togo['GHI'].dropna()
        anova_stat, anova_p = f_oneway(ghi_benin, ghi_sierraleone, ghi_togo)
        kruskal_stat, kruskal_p = kruskal(ghi_benin, ghi_sierraleone, ghi_togo)
        return {'anova_p': anova_p, 'kruskal_p': kruskal_p}

    def plot_avg_ghi_bar(self):
        """
        Plot a bar chart ranking countries by average GHI.
        """
        avg_ghi = self.df_all.groupby('Country')['GHI'].mean().sort_values(ascending=False)
        plt.figure(figsize=(6, 4))
        sns.barplot(x=avg_ghi.index, y=avg_ghi.values, palette='viridis')
        plt.title('Average GHI by Country')
        plt.ylabel('Average GHI')
        plt.xlabel('Country')
        plt.show()
