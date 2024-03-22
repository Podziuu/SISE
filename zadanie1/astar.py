from queue import PriorityQueue
from node import Node
from constants import StateConstants

def astar(start_state, heuristic):
    start_node = Node(start_state, heuristic)
    if start_node.state == StateConstants.GOAL_STATE.value:
        return []
    
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_node))
    visited_count = 1
    processed_count = 0
    
    while not queue.empty():
        node = queue.get()[1]
        processed_count += 1
        visited.add(tuple(node.state))
        
        if node.state == StateConstants.GOAL_STATE.value:
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path, visited_count, processed_count
        
        for neighbor in node.get_neighbors():
            if tuple(neighbor.state) not in visited:
                if heuristic == "hamm":
                    distance = neighbor.hamming_distance(StateConstants.GOAL_STATE.value)
                elif heuristic == "manh":
                    distance = neighbor.manhattan_distance(StateConstants.GOAL_STATE.value)
                visited_count += 1
                queue.put((distance + neighbor.depth, neighbor))
                visited.add(tuple(neighbor.state))
    
    return None