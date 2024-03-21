class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state # stan węzła
        self.parent = parent # rodzic węzła
        self.action = action # ruch, którym rodzic przeszedł do tego węzła
        self.depth = 0 if parent is None else parent.depth + 1 # głębokość węzła
        
    def get_neighbors(self, direction="LURD"):
        neighbors = []
        empty = self.state.index(0)
        if empty % 4 != 0 and direction == "L": # ruch w lewo
            new_state = self.state[:]
            new_state[empty], new_state[empty - 1] = new_state[empty - 1], new_state[empty]
            neighbors.append(Node(new_state, self, "L"))
        if empty % 4 != 3 and direction == "R": # ruch w prawo
            new_state = self.state[:]
            new_state[empty], new_state[empty + 1] = new_state[empty + 1], new_state[empty]
            neighbors.append(Node(new_state, self, "R"))
        if empty > 3 and direction == "U": # ruch w góre
            new_state = self.state[:]
            new_state[empty], new_state[empty - 4] = new_state[empty - 4], new_state[empty]
            neighbors.append(Node(new_state, self, "U"))
        if empty < 12 and direction == "D": # ruch w dół
            new_state = self.state[:]
            new_state[empty], new_state[empty + 4] = new_state[empty + 4], new_state[empty]
            neighbors.append(Node(new_state, self, "D"))
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
        return (self.depth + self.manhattan_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) < (other.depth + other.manhattan_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])))