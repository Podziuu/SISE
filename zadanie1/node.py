from constants import StateConstants

class Node:
    def __init__(self, state, rows, cols, metric=None, parent=None, action="ROOT"):
        self.state = state # stan węzła
        self.parent = parent # rodzic węzła
        self.action = action # ruch, którym rodzic przeszedł do tego węzła
        self.depth = 0 if parent is None else parent.depth + 1 # głębokość węzła
        self.metric = metric if parent is None else parent.metric # metryka
        self.visited = False # czy węzeł był odwiedzony
        self.rows = rows
        self.cols = cols
        
    def get_neighbors(self, direction=None):
        neighbors = []
        empty = self.state.index(0)
        if empty % self.cols != 0 and self.action != "R" and direction in ["L", None]: # ruch w lewo
            new_state = self.state[:]
            new_state[empty], new_state[empty - 1] = new_state[empty - 1], new_state[empty]
            neighbors.append(Node(new_state, self.rows, self.cols, self.metric, self, "L"))
        if empty % self.cols != (self.cols - 1) and self.action != "L" and direction in ["R", None]: # ruch w prawo
            new_state = self.state[:]
            new_state[empty], new_state[empty + 1] = new_state[empty + 1], new_state[empty]
            neighbors.append(Node(new_state, self.rows, self.cols, self.metric, self, "R"))
        if empty >= self.cols and self.action != "D"and direction in ["U", None]: # ruch w góre
            new_state = self.state[:]
            new_state[empty], new_state[empty - 4] = new_state[empty - 4], new_state[empty]
            neighbors.append(Node(new_state, self.rows, self.cols, self.metric, self, "U"))
        if empty < (self.rows - 1) * self.cols and self.action != "U" and direction in ["D", None]: # ruch w dół
            new_state = self.state[:]
            new_state[empty], new_state[empty + 4] = new_state[empty + 4], new_state[empty]
            neighbors.append(Node(new_state, self.rows, self.cols, self.metric, self, "D"))
        return neighbors
    
    
    def hamming_distance(self, goal_state):
        return sum(s != g and s!= 0 for s, g in zip(self.state, goal_state))
    
    def manhattan_distance(self, goal_state):
        distance = 0
        size = len(self.state)
        for i in range(size):
            if self.state[i] != 0:
                goal_index = goal_state.index(self.state[i])
                current_row, current_col = i // self.cols, i % self.cols
                goal_row, goal_col = goal_index // self.cols, goal_index % self.cols
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance
    
    def __lt__(self, other):
        if self.metric == "hamm":
            return self.depth + self.hamming_distance(StateConstants.get_goal_state(self.rows, self.cols)) < (other.depth + other.hamming_distance(StateConstants.get_goal_state(other.rows, other.cols)))
        elif self.metric == "manh":
            return (self.depth + self.manhattan_distance(StateConstants.get_goal_state(self.rows, self.cols)) < (other.depth + other.manhattan_distance(StateConstants.get_goal_state(other.rows, other.cols))))