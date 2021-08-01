import pandas as pd

url = 'https://github.com/alvarofpp/dataset-flights-brazil/raw/main/data/anac.zip'
years = [2019, 2020, 2021]

# Read dataframe
df = pd.read_csv(url)

# Save filtered dataframe
df[df['year'].isin(years)].to_csv('data/airports.csv', index=False, encoding='utf-8')
