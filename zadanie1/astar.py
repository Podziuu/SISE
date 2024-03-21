from queue import PriorityQueue
from node import Node

def astar(start_state, heuristic):
    start_node = Node(start_state)
    if start_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
        return []
    
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_node))
    
    while queue:
        node = queue.get()
        if heuristic == "hamm":
            distance = node[1].hamming_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        elif heuristic == "manh":
            distance = node[1].manhattan_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        visited.add(tuple(node[1].state))
        
        if node[1].state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
            path = []
            while node[1].parent:
                path.append(node[1].action)
                node[1] = node[1].parent
            path.reverse()
            return path
        
        for neighbor in node[1].get_neighbors():
            if tuple(neighbor.state) not in visited:
                queue.put((distance, neighbor))
                print(distance)
                visited.add(tuple(neighbor.state))
    
    return None