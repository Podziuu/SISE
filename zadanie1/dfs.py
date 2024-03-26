from collections import deque

from node import Node
from constants import StateConstants
import time

def dfs(start_state, order, max):
    startTime = time.time()
    maxDepth = max
    start_node = Node(start_state)
    if start_node.state == StateConstants.GOAL_STATE.value:
        return [], 1, 0

    visited = set()
    stack = deque([start_node])
    visited_count = 0
    processed_count = 0

    while stack:
        node = stack.pop()
        processed_count += 1
        node.visited = True

        visited.add(tuple(node.state) + tuple([node.depth]))

        if node.state == StateConstants.GOAL_STATE.value:
            nodeDepth = node.depth
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            endTime = time.time()
            return path, len(path), visited_count, processed_count, nodeDepth, round((endTime - startTime) * 1000, 3)
       
        for direction in reversed(order):
            neighbors = node.get_neighbors(direction)
            neighbor = neighbors[0] if neighbors else None
            if neighbor is not None:
                if neighbor.depth > maxDepth:
                    continue
                if tuple(neighbor.state) + tuple([neighbor.depth]) not in visited:
                    visited_count += 1 
                    stack.append(neighbor)
