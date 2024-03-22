from bfs import bfs
from dfs import dfs
from astar import astar
# [13,15,7,1,8,2,4,11,10,3,12,9,14,6,5,0]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
start_state = [1, 2, 3, 4,
5, 6, 7, 8,
13, 9, 15, 11,
0, 10, 14, 12]
solution = bfs(start_state, "LURD")
solution2 = dfs(start_state, "LURD")
#solution3 = astar(start_state, "hamm")
print("Rozwiązanie:", solution)
print("Rozwiazanie DFS", solution2)
#print("Rozwiązanie2:", solution3)