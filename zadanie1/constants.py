from enum import Enum

class StateConstants(Enum):
    def get_goal_state(rows, cols):
        return [i + 1 if i < rows * cols - 1 else 0 for i in range(rows * cols)]