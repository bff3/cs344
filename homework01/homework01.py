from search import depth_first_graph_search, UndirectedGraph, RandomGraph, Problem, GraphProblem, hill_climbing, simulated_annealing, \
    exp_schedule, infinity
import random as rnd

class TSP(Problem):
    '''The problem of finding the shortest route for visiting every node in a graph'''

    def __init__(self, initial, graph):
        Problem.__init__(self, initial)
        self.graph = graph

    def actions(self, state):
        length = len(state)
        pivot = rnd.randint(0, length - 1)
        choices = [state]
        for i in range(length):
            if pivot != i:
                state_cpy = state[:]
                state_cpy[pivot], state_cpy[i] = state_cpy[i], state_cpy[pivot]
                choices.append(state_cpy)
        return choices

    def result(self, state, action):
        return action

    def value(self, state):
        distance = 0
        i = 0
        for i in range(1, len(state)):
            if self.graph.get(state[i], state[i - 1]) is not None:
                distance += self.graph.get(state[i], state[i - 1])
            else:
                distance += infinity
        return 0 - distance

def get_city_list(graphProb):
    '''get list of cities for an initial state'''
    d = graphProb.graph_dict

    city_list = []
    for city, adj_cities in d.items():
        if city not in city_list:
            city_list.append(city)
        for k in adj_cities:
            if k not in city_list:
                city_list.append(k)

    return city_list

def gen_graph(vertexstring='ABCDEFGHIJKLMNOPQRSTUVWXYZ', maxdist=10):
    graph_dict = {}
    for i in range(len(vertexstring) - 1):
        vertex_dict = {}
        for k in vertexstring[i + 1:]:
            vertex_dict[k] = rnd.randint(1, maxdist)
        graph_dict[vertexstring[i]] = vertex_dict
    return graph_dict

if __name__ == '__main__':

    # invalid_it = ['C','D','B','A']
    # valid_it = ['C','A','B','D']
    # simpleTSP = TSP(invalid_it, simple_map)
    # print(hill_climbing(simpleTSP))
    graph_dict = gen_graph(vertexstring='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(graph_dict)
    myGraph = UndirectedGraph(graph_dict)
    myTSP = TSP(get_city_list(myGraph), myGraph)
    values = []
    for _ in range(1000):
        hill_climbing_solution = hill_climbing(myTSP)
        values.append(myTSP.value(hill_climbing_solution))
        # print(hill_climbing_solution)
        # print(myTSP.value(hill_climbing_solution))
    print(max(values))

    annealing_solution = simulated_annealing(myTSP, exp_schedule(k=20, lam=0.005, limit=100000))
    print(annealing_solution)
    print(myTSP.value(annealing_solution))




