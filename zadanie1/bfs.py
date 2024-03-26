from collections import deque
from node import Node
from constants import StateConstants
import time

def bfs(start_state, order):
    startTime = time.time()
    start_node = Node(start_state)
    if start_node.state == StateConstants.GOAL_STATE.value:
        return [], 1, 0

    visited = set()
    visited.add(tuple(start_node.state))
    queue = deque([start_node])
    visited_count = 1
    processed_count = 0
    
    while queue:
        node = queue.popleft()
        processed_count += 1

        if node.state == StateConstants.GOAL_STATE.value:
            nodeDepth = node.depth
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            endTime = time.time()
            return path, len(path), visited_count, processed_count, nodeDepth, round((endTime - startTime) * 1000, 3)

        for direction in order:
            neighbors = node.get_neighbors(direction)
            neighbor = neighbors[0] if neighbors else None
            if neighbor is not None:
                neighbor_state_tuple = tuple(neighbor.state)
                if neighbor_state_tuple not in visited:
                    visited_count += 1  
                    visited.add(neighbor_state_tuple)
                    queue.append(neighbor)
