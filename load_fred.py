import pandas_datareader.data as web
import pandas as pd
import numpy as np

import os
from pathlib import Path
##########################################################
## Template
series_descriptions = {
    'DPCREDIT': 'Discount Window Primary Credit Rate',
    'EFFR': 'Effective Federal Funds Rate', 
    'IORB': 'Interest on Reserve Balances',
    'IOER': 'Interest on Excess Reserves',
    'OBFR':  'Overnight Bank Funding Rate',
    'SOFR': 'SOFR',
    'IORR': 'Interest on Required Reserves',
    'DFEDTARU': 'Federal Funds Target Range - Upper Limit',
    'DFEDTARL': 'Federal Funds Target Range - Lower Limit',
    'WALCL': 'Federal Reserve Total Assets',
    'TOTRESNS': 'Reserves of Depository Institutions: Total',
    'TREAST': 'Treasuries Held by Federal Reserve',
    'CURRCIR': 'Currency in Circulation',
    'GFDEBTN': 'Federal Debt: Total Public Debt',
    'WTREGEN': 'Treasury General Account',
    'RRPONTSYAWARD': 'Fed ON/RRP Award Rate',
    'RRPONTSYD': 'Treasuries Fed Sold In Temp Open Mark',
    'RPONTSYD': 'Treasuries Fed Purchased In Temp Open Mark',
    'Gen_IORB': 'Interest on Reserves',

}

forward_fill = [
    "OBFR",
    "DPCREDIT",
    "TREAST",
    "TOTRESNS",
    "WTREGEN",
    "WALCL",
    "CURRCIR",
    "RRPONTSYAWARD",
]

fill_zeros = ["RRPONTSYD", "RPONTSYD"]


def pull_fred_repo_data(start_date, end_date, series_list=list(series_descriptions.keys())):
    """
    Lookup series code, e.g., like this:
    https://fred.stlouisfed.org/series/RPONTSYD
    """
    df = web.DataReader(list(series_descriptions.keys()), 'fred', start_date, end_date)
    df["Gen_IORB"] = df['IORB'].fillna(df['IOER'])
    df[forward_fill] = df[forward_fill].fillna(method='ffill')
    df[fill_zeros] = df[fill_zeros].fillna(0)

    return df

result = pull_fred_repo_data('2012-01-01', '2024-01-03', series_descriptions)
print(result)

# , ffill=True