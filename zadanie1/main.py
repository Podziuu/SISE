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

dimensions, start_state = FileManager.getPuzzle(input_filename)

if(strategy == "bfs"):
    solution = bfs(start_state, additional_parameter, dimensions)
elif(strategy == "dfs"):
    solution = dfs(start_state, additional_parameter, dimensions)
elif(strategy == "astr"):
    solution = astar(start_state, additional_parameter, dimensions)
    
FileManager.writeToFile(solution, output_filename, "sol")
FileManager.writeToFile(solution, additional_output_filename, "stats")