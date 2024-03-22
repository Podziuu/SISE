from bfs import bfs
from astar import astar
# [13,15,7,1,8,2,4,11,10,3,12,9,14,6,5,0]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
start_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 13, 14, 15, 12]
solution = bfs(start_state, "LURD")
solution2 = astar(start_state, "hamm")
print("Rozwiązanie:", solution)
print("Rozwiązanie2:", solution2)