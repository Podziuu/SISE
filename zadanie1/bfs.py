from collections import deque
from node import Node
from constants import StateConstants

def bfs(start_state, order):
    start_node = Node(start_state)
    if start_node.state == StateConstants.GOAL_STATE.value:
        return []

    visited = set()
    visited.add(tuple(start_node.state))
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        # print(node.state[:4])
        # print(node.state[4:8])
        # print(node.state[8:12])
        # print(node.state[12:16])
        # print()

        if node.state == StateConstants.GOAL_STATE.value:
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path

        for direction in order:
            neighbors = node.get_neighbors(direction)
            neighbor = neighbors[0] if neighbors else None
            if neighbor is not None:
                neighbor_state_tuple = tuple(neighbor.state)
                if neighbor_state_tuple not in visited:
                    visited.add(neighbor_state_tuple)
                    queue.append(neighbor)
