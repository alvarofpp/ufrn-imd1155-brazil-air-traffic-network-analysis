import os.path
import pandas as pd
import networkx as nx
from tqdm import tqdm

years = [2019, 2020, 2021]

# Read dataframe
df = pd.read_csv('https://github.com/alvarofpp/dataset-flights-brazil/raw/main/data/anac.zip')
df_airports = pd.read_csv('https://github.com/alvarofpp/dataset-flights-brazil/raw/main/data/airports.csv')

for year in tqdm(years):
    filename = 'data/air_traffic_{}.graphml'.format(year)
    if os.path.exists(filename):
        continue

    df_filtered = df[df['year'] == year]
    airports_codes = pd.concat(
        [df_filtered['origin_airport_abbreviation'], df_filtered['destination_airport_abbreviation']],
        axis=0
    ).dropna().unique()
    df_filtered_airports = df_airports[df_airports['code'].isin(airports_codes)]

    # Create graph
    G = nx.Graph()

    # Add nodes
    for index, row in df_filtered_airports.iterrows():
        G.add_node(row['code'],
                   name=row['name'],
                   country=row['country'],
                   latitude=float(row['lat_geo_point']),
                   longitude=float(row['lon_geo_point']),
                   )

    # Add edges
    df_edges = df_filtered[[
        'origin_airport_abbreviation',
        'destination_airport_abbreviation',
    ]].dropna()
    df_edges = df_edges.groupby(df_edges.columns.tolist(), as_index=False).size()
    for index, row in df_edges.iterrows():
        if row['origin_airport_abbreviation'] == row['destination_airport_abbreviation']:
            continue
        G.add_edge(row['origin_airport_abbreviation'], row['destination_airport_abbreviation'],
                   flight_count=row['size'])

    # Export to graphml
    nx.write_graphml(G, filename)
