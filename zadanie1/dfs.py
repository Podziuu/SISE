from collections import deque

from node import Node

def dfs(start_state, order):
    maxDepth = 8
    start_node = Node(start_state)
    if start_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
        return []

    visited = set()
    stack = deque([start_node])

    while stack:
        node = stack.pop()

        if node.depth > maxDepth:
            continue

        # print(node.state[:4])
        # print(node.state[4:8])
        # print(node.state[8:12])
        # print(node.state[12:16])
        # print()

        if node.state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path

        for direction in reversed(order):
            neighbor = node.get_neighbors(direction)
            if neighbor is not None:
                neighbor_state_tuple = tuple(neighbor.state)
                if tuple(neighbor_state_tuple) not in visited:
                    visited.add(neighbor_state_tuple)
                    stack.append((neighbor))
