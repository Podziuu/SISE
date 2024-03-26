from bfs import bfs
from dfs import dfs
from astar import astar
import sys
from fileManager import FileManager

strategy = sys.argv[1]
additional_parameter = sys.argv[2]
input_filename = sys.argv[3]
output_filename = sys.argv[4]
additional_output_filename = sys.argv[5]
start_state = [1, 2, 3, 4, 5, 6, 11, 7, 9, 10, 0, 8, 13, 14, 15, 12]

if(strategy == "bfs"):
    solution = bfs(start_state, additional_parameter, [4, 4])
elif(strategy == "dfs"):
    solution = dfs(start_state, additional_parameter, [4, 4])
elif(strategy == "astr"):
    solution = astar(start_state, additional_parameter, [4,4])
    
FileManager.writeToFile(solution, output_filename, "sol")
FileManager.writeToFile(solution, additional_output_filename, "stats")