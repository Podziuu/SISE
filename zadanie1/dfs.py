from collections import deque

from node import Node
from constants import StateConstants
import time

def dfs(start_state, order, size):
    startTime = time.time()
    maxDepth = 20
    start_node = Node(start_state, size[0], size[1])
    if start_node.state == StateConstants.get_goal_state(size[0], size[1]):
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

        if node.state == StateConstants.get_goal_state(size[0], size[1]):
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
    
    endTime = time.time()
    return [-1, [], visited_count, processed_count, node.depth, round((endTime - startTime) * 1000, 3)]
