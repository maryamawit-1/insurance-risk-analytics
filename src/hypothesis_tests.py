from scipy.stats import ttest_ind, chi2_contingency
from statsmodels.stats.weightstats import ztest
import pandas as pd


def run_ttest(group_a, group_b):
    stat, p = ttest_ind(group_a, group_b, nan_policy="omit")
    return stat, p


def run_ztest(group_a, group_b):
    stat, p = ztest(group_a, group_b)
    return stat, p


def run_chi_square(table):
    stat, p, dof, expected = chi2_contingency(table)
    return stat, p


def decision(p):
    return "Reject H₀" if p < 0.05 else "Fail to Reject H₀"