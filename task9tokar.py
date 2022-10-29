from enum import Enum
from turtle import update


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7


class StateMachine:
    state = State.A

    def scale(self):
        return self.update({
            State.B: [State.C, 1],
            State.C: [State.A, 4],
            State.D: [State.E, 5],
            State.E: [State.F, 7],
        })

    def swap(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.F, 2],
            State.C: [State.D, 3],
            State.E: [State.E, 8],
            State.D: [State.G, 6],
            State.F: [State.G, 9],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        print("update ->")
        print(self.state)
        print(signal)
        return signal


def main():
    return StateMachine()

