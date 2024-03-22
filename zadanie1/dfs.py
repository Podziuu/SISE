from collections import deque

from node import Node
from constants import StateConstants

def dfs(start_state, order, depth):
    max_depth = depth
    visited = set()
    visited_count = 1
    processed_count = 0
    node = Node(start_state)
    
    def recursive_dfs(node, visited, depth):
        nonlocal visited_count, processed_count
        processed_count += 1
        
        if depth > max_depth:
            return None
        
        if tuple(node.state) not in visited:
            if node.state == StateConstants.GOAL_STATE.value:
                path = []
                while node.parent:
                    path.append(node.action)
                    node = node.parent
                path.reverse()
                return path
            visited_count += 1
            for direction in order:
                neighbors = node.get_neighbors(direction)
                neighbor = neighbors[0] if neighbors else None
                if neighbor is not None:
                    result = recursive_dfs(neighbor, visited, depth + 1)
                    if result is not None:
                        visited.add(tuple(node.state))  
                        return result
            
    
    path = recursive_dfs(node, visited, 0)
    
    return path, visited_count, processed_count
            
        

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

# def dfs(start_state, order, max):
#     maxDepth = max
#     start_node = Node(start_state)
#     if start_node.state == StateConstants.GOAL_STATE.value:
#         return [], 1, 0

#     visited = set()
#     stack = deque([start_node])
#     visited_count = 1
#     processed_count = 0

#     while stack:
#         node = stack.pop()
#         # print(node.depth)
#         processed_count += 1
#         node.visited = True

#         # if node.depth > maxDepth:
#         #     continue

#         if node.state == StateConstants.GOAL_STATE.value:
#             path = []
#             while node.parent:
#                 path.append(node.action)
#                 node = node.parent
#             path.reverse()
#             return path, len(visited), processed_count
        
#         node_state_tuple = tuple(node.state)
        
#         # print(node.all_neighbors_visited())
#         # if node.all_neighbors_visited(maxDepth):
#         #     print("witam")
#         #     visited.add(node_state_tuple)
            
#         for direction in reversed(order):
#             neighbors = node.get_neighbors(direction)
#             neighbor = neighbors[0] if neighbors else None
#             if neighbor is not None:
#                 if neighbor.depth > maxDepth:
#                     neighbor.visited = True
#                     continue
#                 neighbor_state_tuple = tuple(neighbor.state)
#                 if tuple(neighbor_state_tuple) not in visited:
#                     visited_count += 1 
#                     stack.append(neighbor)
