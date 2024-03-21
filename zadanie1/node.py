class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state # stan węzła
        self.parent = parent # rodzic węzła
        self.action = action # ruch, którym rodzic przeszedł do tego węzła
        
    def get_neighbors(self):
        neighbors = []
        empty = self.state.index(0)
        if empty % 4 != 0: # ruch w lewo
            new_state = self.state[:]
            new_state[empty], new_state[empty - 1] = new_state[empty - 1], new_state[empty]
            neighbors.append(Node(new_state, self, "L"))
        if empty % 4 != 3: # ruch w prawo
            new_state = self.state[:]
            new_state[empty], new_state[empty + 1] = new_state[empty + 1], new_state[empty]
            neighbors.append(Node(new_state, self, "R"))
        if empty > 3: # ruch w góre
            new_state = self.state[:]
            new_state[empty], new_state[empty - 4] = new_state[empty - 4], new_state[empty]
            neighbors.append(Node(new_state, self, "U"))
        if empty < 12: # ruch w dół
            new_state = self.state[:]
            new_state[empty], new_state[empty + 4] = new_state[empty + 4], new_state[empty]
            neighbors.append(Node(new_state, self, "D"))