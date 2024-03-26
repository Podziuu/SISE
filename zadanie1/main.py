from bfs import bfs
from dfs import dfs
from astar import astar
# [13,15,7,1,8,2,4,11,10,3,12,9,14,6,5,0]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
# [1, 2, 3, 4, 5, 6, 11, 7, 9, 10, 0, 8, 13, 14, 15, 12]
start_state = [1, 2, 3, 4, 5, 6, 11, 7, 9, 10, 0, 8, 13, 14, 15, 12]
solution = bfs(start_state, "LURD")
solution2 = astar(start_state, "hamm")
# solution3 = dfs(start_state, "LURD", 0)
print("Rozwiązanie BFS:", solution)
print("Rozwiązanie A*:", solution2)

for i in range(24):
    solution3 = dfs(start_state, "LURD", i)
    print("Rozwiazanie DFS dla glebi ", i, solution3)