import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import load_merged_repo_data

series_descriptions = load_merged_repo_data.series_descriptions
start_date = "2014-08-22"
end_date = "2024-01-03"
df = load_merged_repo_data.load_all(start_date=start_date, end_date=end_date)


###

start_date = '2014-08-01'
end_date = '2019-09-01'
sliced_df = df.loc[start_date:end_date]

i_replicated_figure_1, ax = plt.subplots()
ax.fill_between(sliced_df.index, sliced_df['DFEDTARU']/3.6, color='gray', alpha=0.3, label='Federal funds target window')
ax.plot(sliced_df.index, sliced_df['REPO-TRI_AR_OO-P']/3.6, color='darkblue', label='Tri-party repo average rate')
ax.plot(sliced_df.index, sliced_df['EFFR']/3.6, color='lightblue', label='Effective federal funds rate')

target_date = pd.to_datetime('2019-09-17')
target_rate = 1.0
ax.scatter(target_date, target_rate, color='red', label='Sept.17, 2019: 3.06%')

ax.set_ylabel('Spread over Federal Funds Target')
ax.set_title('Figure 1: Repo Rate Spikes, August 2014–September 2019')

ax.legend()
ax.set_xticks(pd.date_range(start='2014-08-01', end='2019-09-01', freq='MS'))
ax.set_yticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.xticks(rotation=45)

plt.show()


###


mask = df['REPO-TRI_AR_OO-P'] > df['DFEDTARU']
spike_dates = df.index[mask]
    
print(spike_dates)