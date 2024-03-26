from collections import deque

from node import Node
from constants import StateConstants
import time

# def dfs(start_state, order, depth):
#     max_depth = depth
#     visited = set()
#     visited_count = 1
#     processed_count = 0
#     node = Node(start_state)
    
#     def recursive_dfs(node, visited, depth):
#         nonlocal visited_count, processed_count
#         processed_count += 1
        
#         if depth > max_depth:
#             return None
        
#         if tuple(node.state) not in visited:
#             if node.state == StateConstants.GOAL_STATE.value:
#                 path = []
#                 while node.parent:
#                     path.append(node.action)
#                     node = node.parent
#                 path.reverse()
#                 return path
#             visited_count += 1
#             for direction in order:
#                 neighbors = node.get_neighbors(direction)
#                 neighbor = neighbors[0] if neighbors else None
#                 if neighbor is not None:
#                     visited.add(tuple(node.state))  
#                     result = recursive_dfs(neighbor, visited, depth + 1)
#                     if result is not None:
                        
#                         return result
            
    
#     path = recursive_dfs(node, visited, 0)
    
#     return path, visited_count, processed_count
            
        

# def dfs(start_state, order, depth):
#     max_depth = 20
#     visited = set()
#     node = Node(start_state)
#     if tuple(node.state) not in visited:
#         visited.add(tuple(node.state))
#         if node.state == StateConstants.GOAL_STATE.value:
#             path = []
#             while node.parent:
#                 path.append(node.action)
#                 node = node.parent
#             return path, len(visited), 0
#         if depth < max_depth:
#             for direction in order:
#                 neighbors = node.get_neighbors(direction)
#                 for neighbor in neighbors:
#                     if tuple(neighbor.state) not in visited:
#                         result = dfs(neighbor, order, depth + 1)
#                         if result is not None:
#                             return result
#                         # result = dfs(neighbor, order, depth += 1)
#                         # if result is not None:
#                         #     return result

# def dfs(start_state, order, max):
#     def recursive_dfs(node, visited, depth):
#         nonlocal visited_count, processed_count
        
#         visited.add(tuple(node.state))
#         processed_count += 1
#         visited_count += 1
#         node.visited = True
        
#         if depth > max:
#             return None
        
#         if node.state == StateConstants.GOAL_STATE.value:
#             path = []
#             while node.parent:
#                 path.append(node.action)
#                 node = node.parent
#             path.reverse()
#             return path
    
#         for direction in reversed(order):
#             neighbors = node.get_neighbors(direction)
#             for neighbor in neighbors:
#                 if tuple(neighbor.state) not in visited:
#                     result = recursive_dfs(neighbor, visited, depth + 1)
#                     if result is not None:
#                         return result
#         return None
        
#     start_state = Node(start_state)
#     if start_state.state == StateConstants.GOAL_STATE.value:
#         return [], 1, 0
    
#     visited = set()
#     visited_count = 1
#     processed_count = 0
    
#     path = recursive_dfs(start_state, visited, 0)
    
#     return path, visited_count, processed_count

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
