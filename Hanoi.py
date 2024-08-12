from aima3.search import Problem, breadth_first_tree_search, astar_search

class Hanoi(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def actions(self, state):
        actions = []
        for i in range(3):
            for j in range(3):
                if i != j and state[i] and (not state[j] or state[i][-1] < state[j][-1]):
                    actions.append((i, j))
        return actions

    def result(self, state, action):
        state = [list(peg) for peg in state]
        disk = state[action[0]].pop()
        state[action[1]].append(disk)
        return tuple(tuple(peg) for peg in state)

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        """
        heurística baseada no peso dos discos e posição dos discos nas hastes
        """
        state = node.state
        total_cost = 0
        peg_weights = [4, 2, 0]
        for i, peg in enumerate(state):
            for disk in peg:
                total_cost += peg_weights[i] * (disk + 1)
        return total_cost

# estado inicial e objetivo
initial_state = ((2, 1, 0), (), ())
goal_state = ((), (), (2, 1, 0))

# criandoo problema
problema_hanoi = Hanoi(initial_state, goal_state)

# resolvendo c/ busca em largura (BFS)
solucao_bfs = breadth_first_tree_search(problema_hanoi)

# resolvendo c/ busca A* (heurística informada)
solucao_astar = astar_search(problema_hanoi)

# conta n° de movimentos
num_movimentos_bfs = len(solucao_bfs.path())
num_movimentos_astar = len(solucao_astar.path())

# Exibindo o número de movimentos
print("Número de movimentos com BFS:", num_movimentos_bfs)
print("Número de movimentos com A*:", num_movimentos_astar)
