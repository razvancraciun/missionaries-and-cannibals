import random

class IDDFS_Strategy:
    def __init__(self, game, depth_step = 3):
        self.game = game
        self.visited = []
        self.parent = {}
        self.depth = {}
        self.depth_step = depth_step

    def initialize(self):
        self.game.reset()
        self.visited = []
        self.parent = {}
        self.depth = {}
        self.depth[self.game.state] = 0
        self.parent[self.game.state] = None


    def trace(self):
        trace = []
        state = self.game.state
        while self.parent[state]:
            trace.append(state)
            state = self.parent[state]
        for state in reversed(trace):
            print(state)
        print(f'Solution passes through {len(trace)} states')

    def run(self):
        self.initialize()
        shallow = [self.game.state]
        while shallow:
            shallow = self.step(shallow)
        self.game.game_over()


    def step(self, shallow):
        deep = []
        while shallow:
            self.game.state = shallow.pop()
            self.visited.append(self.game.state)
            possible_transitions = self.game.possible_transitions()
            possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
            possible_transitions = [transition for transition in possible_transitions \
                                if transition not in shallow and transition not in deep]
            for transition in possible_transitions:
                self.depth[transition] = self.depth[self.game.state] + 1
                self.parent[transition] = self.game.state
                if self.depth[transition] < self.depth_step:
                    shallow.append(transition)
                else:
                    deep.append(transition)
                if self.game.is_final_state():
                    self.trace()
                    return []
        return deep

class Backtracking_Strategy:
    def __init__(self, game):
        self.game = game
        self.visited = []
        self.parent = {}

    def run(self):
        self.initialize()
        states = [self.game.state]
        self.parent[self.game.state] = None
        while states:
            self.game.state = states.pop()
            self.visited.append(self.game.state)
            possible_transitions = self.game.possible_transitions()
            possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
            possible_transitions = [transition for transition in possible_transitions if transition not in states]
            for transition in possible_transitions:
                states.append(transition)
                self.parent[transition] = self.game.state
            if self.game.is_final_state():
                self.trace()
                self.game.game_over()
                return
        self.game.game_over()

    def trace(self):
        trace = []
        state = self.game.state
        while self.parent[state]:
            trace.append(state)
            state = self.parent[state]
        for state in reversed(trace):
            print(state)
        print(f'Solution passes through {len(trace)} states')



    def initialize(self):
        self.game.reset()
        self.visited = []
        self.parent = {}

class Random_Strategy:
    def __init__(self, game):
        self.visited = []
        self.game = game

    def run(self):
        self.initialize()
        print(f'Starting game. State: {self.game.state}')
        step = 0
        while not self.game.is_final_state() and step < 100:
            possible_transitions = self.game.possible_transitions()
            possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
            if not possible_transitions:
                self.game.game_over()
                return
            self.game.state = random.choice(possible_transitions)
            self.visited.append(self.game.state)
            print(f'Current state: {self.game.state}')
            step += 1
        self.game.game_over()

    def initialize(self):
        self.game.reset()
        self.visited = [self.game.state]
