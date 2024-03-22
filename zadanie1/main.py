from bfs import bfs
from dfs import dfs
from astar import astar
# [13,15,7,1,8,2,4,11,10,3,12,9,14,6,5,0]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
#[1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15]
order = "LURD"
#start_state = [1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15]
#start_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 13, 14, 15, 12]
start_state = [1, 2, 3, 0,
5, 7, 8, 4,
9, 6, 10, 12,
13, 14, 11, 15]
solution = bfs(start_state, order)
solution2 = dfs(start_state, order)
#solution3 = astar(start_state, "hamm")
print("Rozwiązanie:", solution)
print("Rozwiazanie DFS", solution2)
#print("Rozwiązanie2:", solution3)