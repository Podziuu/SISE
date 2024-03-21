from collections import deque
from node import Node

def bfs(start_state, order):
    start_node = Node(start_state)
    if start_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
        return []

    visited = set()
    visited.add(tuple(start_node.state))
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        for direction in order:
            for neighbor in node.get_neighbors(direction):
                neighbor_state_tuple = tuple(neighbor.state)
                if neighbor_state_tuple not in visited:
                    visited.add(neighbor_state_tuple)
                    if neighbor.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
                        path = []
                        while neighbor.parent:
                            path.append(neighbor.action)
                            neighbor = neighbor.parent
                        path.reverse()
                        return path
                    queue.append(neighbor)
