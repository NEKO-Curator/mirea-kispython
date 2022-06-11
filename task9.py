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

    def crack(self):
        return self.update({
            State.A: [State.B, 0],
            State.D: [State.A, 4],
            State.F: [State.A, 7],
            State.C: [State.D, 2],
        })

    def tag(self):
        return self.update({
            State.B: [State.C, 1],
            State.G: [State.A, 8],
            State.D: [State.E, 3],
            State.E: [State.F, 5],
            State.F: [State.G, 6],
        })

    def trim(self):
        return self.update({
            State.G: [State.C, 9],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        print("update ->")
        print(self.state)
        print(signal)
        return signal


def main():
    return StateMachine()

if __name__ == '__main__':
    o = main()
    print(o.crack())
    o.tag()
