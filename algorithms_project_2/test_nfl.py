import pandas as pd
import graph_classes as gc  # Custom graph class

all_games = pd.read_csv("nfl_2017.csv")

full_season_graph = gc.Graph()

for index, row in all_games.iterrows():
    full_season_graph.add_edge(row['Loser'],row['Winner'])
dfs_graph = full_season_graph.dfs_and_biconnected('Philadelphia Eagles')

print("")
week_1_graph = gc.Graph()

week1 = all_games[all_games.Week.between(10, 12)]
week1.head()
for index, row in week1.iterrows():
    week_1_graph.add_edge(row['Loser'], row['Winner'])
week_1_graph_dfs = week_1_graph.dfs_and_biconnected('Minnesota Vikings')

for c_node in week_1_graph_dfs.node:
    if week_1_graph_dfs.node[c_node].articulation is True:
        print(c_node)