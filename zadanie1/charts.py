import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    return pd.read_csv('./results/Wyniki.txt', sep=' ', names=["movesInPuzzle", "puzzleID", "algorithm", "param", "moves", "visited", "processed", "depth", "time"])

def draw_chart(data, params, criteria, x_label, y_label, title, temp, log=False):
    num_params = len(params)
    bar_width = 0.5 / num_params
    for i, param in enumerate(params, 1):
        plt.bar(data[data[temp] == param]['movesInPuzzle'] + (i - 0.5 - 0.5 * num_params) * bar_width, 
                data[data[temp] == param][criteria], 
                width=bar_width, label=param, alpha=0.7)
    
    if log:
        plt.yscale('log')

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(title='Parametr')
    plt.grid(True)
    plt.show()

data = get_data()

bfsdata = data[data['algorithm'] == 'bfs']
dfsdata = data[data['algorithm'] == 'dfs']
astrdata = data[data['algorithm'] == 'astr']

bfs_grouped_data = bfsdata.groupby(['movesInPuzzle', 'param']).agg({'moves': 'mean', 'visited': 'mean', 'processed': 'mean', 'time': 'mean', 'depth': 'mean'}).reset_index()
dfs_grouped_data = dfsdata.groupby(['movesInPuzzle', 'param']).agg({'moves': 'mean', 'visited': 'mean', 'processed': 'mean', 'time': 'mean', 'depth': 'mean'}).reset_index()
astr_grouped_data = astrdata.groupby(['movesInPuzzle', 'param']).agg({'moves': 'mean', 'visited': 'mean', 'processed': 'mean', 'time': 'mean', 'depth': 'mean'}).reset_index()
all_grouped_data = data.groupby(['movesInPuzzle', 'algorithm']).agg({'moves': 'mean', 'visited': 'mean', 'processed': 'mean', 'time': 'mean', 'depth': 'mean'}).reset_index()

# Unikalne parametry
dfs_bfs_params = bfs_grouped_data['param'].unique()
astr_params = astr_grouped_data['param'].unique()
all_params = all_grouped_data['algorithm'].unique()

# Tworzenie wykresu
plt.figure(figsize=(12, 6))

# wykresy dla bfsa
# draw_chart(bfs_grouped_data, dfs_bfs_params, 'moves', "Głębokość rozwiązania", "Średnia liczba ruchów", "BFS", temp='param' )
# draw_chart(bfs_grouped_data, dfs_bfs_params, 'visited', "Głębokość rozwiązania", "Średnia liczba stanow odwiedzonych", "BFS", temp='param', log=True)
# draw_chart(bfs_grouped_data, dfs_bfs_params, 'processed', "Głębokość rozwiązania", "Średnia liczba stanow przetworzonych", "BFS", temp='param', log=True)
# draw_chart(bfs_grouped_data, dfs_bfs_params, 'depth', "Głębokość rozwiązania", "Średnia głebkość", "BFS", temp='param')
# draw_chart(bfs_grouped_data, dfs_bfs_params, 'time', "Głębokość rozwiązania", "Średni czas przetwarzania", "BFS", temp='param')
# #wykresy dla dfsa
# draw_chart(dfs_grouped_data, dfs_bfs_params, 'moves', "Głębokość rozwiązania", "Średnia liczba ruchów", "DFS", temp='param')
# draw_chart(dfs_grouped_data, dfs_bfs_params, 'visited', "Głębokość rozwiązania", "Średnia liczba stanow odwiedzonych", "DFS", temp='param', log=True)
# draw_chart(dfs_grouped_data, dfs_bfs_params, 'processed', "Głębokość rozwiązania", "Średnia liczba stanow przetworzonych", "DFS", temp='param', log=True)
# draw_chart(dfs_grouped_data, dfs_bfs_params, 'depth', "Głębokość rozwiązania", "Średnia głebkość", "DFS", temp='param')
# draw_chart(dfs_grouped_data, dfs_bfs_params, 'time', "Głębokość rozwiązania", "Średni czas przetwarzania", "DFS", temp='param')
# # wykresy dla astara
# draw_chart(astr_grouped_data, astr_params, 'moves', "Głębokość rozwiązania", "Średnia liczba ruchów", "A*", temp='param')
# draw_chart(astr_grouped_data, astr_params, 'visited', "Głębokość rozwiązania", "Średnia liczba stanow odwiedzonych", "A*", temp='param', log=True)
# draw_chart(astr_grouped_data, astr_params, 'processed', "Głębokość rozwiązania", "Średnia liczba stanow przetworzonych", "A*", temp='param', log=True)
# draw_chart(astr_grouped_data, astr_params, 'depth', "Głębokość rozwiązania", "Średnia głebkość", "A*", temp='param')
# draw_chart(astr_grouped_data, astr_params, 'time', "Głębokość rozwiązania", "Średni czas przetwarzania", "A*", temp='param')
# wykresy dla wszystkich algorytmów
draw_chart(all_grouped_data, all_params, 'moves', "Głębokość rozwiązania", "Średnia liczba ruchów", "Wszystkie algorytmy", temp='algorithm')
draw_chart(all_grouped_data, all_params, 'visited', "Głębokość rozwiązania", "Średnia liczba stanow odwiedzonych", "Wszystkie algorytmy", temp='algorithm', log=True)
draw_chart(all_grouped_data, all_params, 'processed', "Głębokość rozwiązania", "Średnia liczba stanow przetworzonych", "Wszystkie algorytmy", temp='algorithm', log=True)
draw_chart(all_grouped_data, all_params, 'depth', "Głębokość rozwiązania", "Średnia głebkość", "Wszystkie algorytmy", temp='algorithm')
draw_chart(all_grouped_data, all_params, 'time', "Głębokość rozwiązania", "Średni czas przetwarzania", "Wszystkie algorytmy", temp='algorithm')