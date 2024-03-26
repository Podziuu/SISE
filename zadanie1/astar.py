from queue import PriorityQueue
from node import Node
from constants import StateConstants
import time

def astar(start_state, heuristic, size):
    startTime = time.time()
    start_node = Node(start_state, size[0], size[1], heuristic)
    if start_node.state == StateConstants.get_goal_state(size[0], size[1]):
        return []
    
    visited = set()
    queue = PriorityQueue()
    queue.put(start_node)
    visited_count = 1
    processed_count = 0
    
    while not queue.empty():
        node = queue.get()
        processed_count += 1
        visited.add(tuple(node.state))
        
        if node.state == StateConstants.get_goal_state(size[0], size[1]):
            nodeDept = node.depth
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            endTime = time.time()
            return path, len(path), visited_count, processed_count, nodeDept, round((endTime - startTime) * 1000, 3)
        
        for neighbor in node.get_neighbors():
            if tuple(neighbor.state) not in visited:
                visited_count += 1
                queue.put(neighbor)
                visited.add(tuple(neighbor.state))
    
    endTime = time.time()
    return [-1, [], visited_count, processed_count, node.depth, round((endTime - startTime) * 1000, 3)]