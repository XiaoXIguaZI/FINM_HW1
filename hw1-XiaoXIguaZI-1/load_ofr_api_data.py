"""
Pull from the short-term funding API
Info here:
https://www.financialresearch.gov/short-term-funding-monitor/api/
"""
import pandas as pd
import numpy as np

##########################################################
## Template

series_descriptions = {
    'REPO-TRI_AR_OO-P': 'Tri-Party Average Rate: Overnight/Open (Preliminary)',
    'REPO-TRI_TV_OO-P': 'Tri-Party Transaction Volume: Overnight/Open (Preliminary)',
    'REPO-TRI_TV_TOT-P': 'Tri-Party Transaction Volume: Total (Preliminary)',
    'REPO-DVP_AR_OO-P': 'DVP Service Average Rate: Overnight/Open (Preliminary)',
    'REPO-DVP_TV_OO-P': 'DVP Service Transaction Volume: Overnight/Open (Preliminary)',
    'REPO-DVP_TV_TOT-P': 'DVP Service Transaction Volume: Total (Preliminary)', 
    'REPO-DVP_OV_TOT-P': 'DVP Service Outstanding Volume: Total (Preliminary)',
    'REPO-GCF_AR_OO-P': 'GCF Repo Service Average Rate: Overnight/Open (Preliminary)',
    'REPO-GCF_TV_OO-P': 'GCF Repo Service Transaction Volume: Overnight/Open (Preliminary)',
    'REPO-GCF_TV_TOT-P': 'GCF Repo Service Transaction Volume: Total (Preliminary)',
    'FNYR-BGCR-A': 'Broad General Collateral Rate',
    'FNYR-TGCR-A': 'Tri-Party General Collateral Rate',
}

def pull_variable_from_ofr_api(mnemonic=None):
    """
    An example:
    https://data.financialresearch.gov/v1/series/timeseries?mnemonic=REPO-TRI_AR_TOT-F
    """
    url = f'https://data.financialresearch.gov/v1/series/timeseries?mnemonic={mnemonic}'
    df = pd.read_json(url)
    df.columns = ["Date",mnemonic]
    df.set_index("Date", inplace=True)
    df.index = pd.to_datetime(df.index)
    return df

def pull_repo_data(start_date, end_date, series_list=list(series_descriptions.keys())):
    dfs = []

    for mnemonic in series_descriptions.keys():
        df_single = pull_variable_from_ofr_api(mnemonic)
        dfs.append(df_single)
    
    df = pd.concat(dfs, axis=1)
    df = df.loc[start_date:end_date]

    return df

start_date = '2014-08-22'
end_date = '2024-01-03'
print(pull_repo_data(start_date, end_date, series_descriptions))