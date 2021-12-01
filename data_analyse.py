import pandas as pd

df = pd.read_csv('dataset_download/country_wise_latest.csv')
df = df[['Country/Region', 'Deaths']].sort_values(by=['Deaths'], ascending=False, ignore_index=True).head(10)

print(df)
