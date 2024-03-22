from collections import deque

from node import Node
from constants import StateConstants

def dfs(start_state, order):
    maxDepth = 21
    start_node = Node(start_state)
    if start_node.state == StateConstants.GOAL_STATE.value:
        return [], 1, 0

    visited = set()
    stack = deque([start_node])
    visited_count = 1
    processed_count = 0

    while stack:
        node = stack.pop()
        processed_count += 1

        node_state_tuple = tuple(node.state)
        visited.add(node_state_tuple)

        if node.state == StateConstants.GOAL_STATE.value:
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path, visited_count, processed_count

        for direction in reversed(order):
            neighbors = node.get_neighbors(direction)
            neighbor = neighbors[0] if neighbors else None
            if neighbor is not None:
                if neighbor.depth > maxDepth:
                    continue
                neighbor_state_tuple = tuple(neighbor.state)
                if tuple(neighbor_state_tuple) not in visited:
                    visited_count += 1  
                    # visited.add(neighbor_state_tuple)
                    stack.append(neighbor)
