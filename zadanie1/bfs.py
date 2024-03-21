from collections import deque
from node import Node

def bfs(start_state):
    start_node = Node(start_state)
    if start_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
        return []

    visited = set()
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        visited.add(tuple(node.state))
        
        for neighbor in node.get_neighbors():
            if tuple(neighbor.state) not in visited:
                if neighbor.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
                    path = []
                    while neighbor.parent:
                        path.append(neighbor.action)
                        neighbor = neighbor.parent
                    path.reverse()
                    return path
            queue.append(neighbor)
