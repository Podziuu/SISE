from queue import PriorityQueue
from node import Node

def astar(start_state, heuristic):
    start_node = Node(start_state, heuristic)
    if start_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
        return []
    
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_node))
    
    while not queue.empty():
        node = queue.get()[1]
        if heuristic == "hamm":
            distance = node.hamming_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        elif heuristic == "manh":
            distance = node.manhattan_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        visited.add(tuple(node.state))
        
        if node.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path
        
        for neighbor in node.get_neighbors():
            if tuple(neighbor.state) not in visited:
                queue.put((distance, neighbor))
                visited.add(tuple(neighbor.state))
    
    return None