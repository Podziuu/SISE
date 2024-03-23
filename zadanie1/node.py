from constants import StateConstants

class Node:
    def __init__(self, state, metric=None, parent=None, action="ROOT"):
        self.state = state # stan węzła
        self.parent = parent # rodzic węzła
        self.action = action # ruch, którym rodzic przeszedł do tego węzła
        self.depth = 0 if parent is None else parent.depth + 1 # głębokość węzła
        self.metric = metric if parent is None else parent.metric # metryka
        self.visited = False # czy węzeł był odwiedzony
        
    def get_neighbors(self, direction=None):
        neighbors = []
        empty = self.state.index(0)
        if empty % 4 != 0 and self.action != "R" and direction in ["L", None]: # ruch w lewo
            new_state = self.state[:]
            new_state[empty], new_state[empty - 1] = new_state[empty - 1], new_state[empty]
            neighbors.append(Node(new_state, None, self, "L"))
        if empty % 4 != 3 and self.action != "L" and direction in ["R", None]: # ruch w prawo
            new_state = self.state[:]
            new_state[empty], new_state[empty + 1] = new_state[empty + 1], new_state[empty]
            neighbors.append(Node(new_state, None, self, "R"))
        if empty > 3  and self.action != "D"and direction in ["U", None]: # ruch w góre
            new_state = self.state[:]
            new_state[empty], new_state[empty - 4] = new_state[empty - 4], new_state[empty]
            neighbors.append(Node(new_state, None, self, "U"))
        if empty < 12 and self.action != "U" and direction in ["D", None]: # ruch w dół
            new_state = self.state[:]
            new_state[empty], new_state[empty + 4] = new_state[empty + 4], new_state[empty]
            neighbors.append(Node(new_state, None, self, "D"))
        return neighbors
    
    
    def hamming_distance(self, goal_state):
        return sum(s != g and s!= 0 for s, g in zip(self.state, goal_state))
    
    def manhattan_distance(self, goal_state):
        distance = 0
        size = len(self.state)
        for i in range(size):
            if self.state[i] != 0:
                goal_index = goal_state.index(self.state[i])
                distance += abs(i % 4 - goal_index % 4) + abs(i // 4 - goal_index // 4)
        return distance
    
    def __lt__(self, other):
        if self.metric == "hamm":
            return self.depth + self.hamming_distance(StateConstants.GOAL_STATE.value) < (other.depth + other.hamming_distance(StateConstants.GOAL_STATE.value))
        elif self.metric == "manh":
            return (self.depth + self.manhattan_distance(StateConstants.GOAL_STATE.value) < (other.depth + other.manhattan_distance(StateConstants.GOAL_STATE.value)))