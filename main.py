# Task 1
# Node.py file has been added

# Task 2
from Node import Node

# Creating nodes for each city
arad = Node("Arad")
bucharest = Node("Bucharest")
craiova = Node("Craiova")
drobeta = Node("Drobeta")
eforie = Node("Eforie")
fagaras = Node("Fagaras")
giurgiu = Node("Giurgiu")
hirsova = Node("Hirsova")
iasi = Node("Iasi")
lugoj = Node("Lugoj")
mehadia = Node("Mehadia")
neamt = Node("Neamt")
oradea = Node("Oradea")
pitesti = Node("Pitesti")
rimnicu_vilcea = Node("Rimnicu Vilcea")
sibiu = Node("Sibiu")
timisoara = Node("Timisoara")
urziceni = Node("Urziceni")
vaslui = Node("Vaslui")
zerind = Node("Zerind")

# Adding neighbors for each city (assuming an undirected graph)

arad.add_neighbor(zerind)
arad.add_neighbor(timisoara)
arad.add_neighbor(sibiu)

bucharest.add_neighbor(fagaras)
bucharest.add_neighbor(giurgiu)
bucharest.add_neighbor(pitesti)
bucharest.add_neighbor(urziceni)

craiova.add_neighbor(drobeta)
craiova.add_neighbor(pitesti)
craiova.add_neighbor(rimnicu_vilcea)

drobeta.add_neighbor(craiova)
drobeta.add_neighbor(mehadia)

eforie.add_neighbor(hirsova)

fagaras.add_neighbor(bucharest)
fagaras.add_neighbor(sibiu)

giurgiu.add_neighbor(bucharest)

hirsova.add_neighbor(eforie)
hirsova.add_neighbor(urziceni)

iasi.add_neighbor(neamt)
iasi.add_neighbor(vaslui)

lugoj.add_neighbor(mehadia)
lugoj.add_neighbor(timisoara)

mehadia.add_neighbor(drobeta)
mehadia.add_neighbor(lugoj)

neamt.add_neighbor(iasi)

oradea.add_neighbor(zerind)

pitesti.add_neighbor(craiova)
pitesti.add_neighbor(bucharest)
pitesti.add_neighbor(rimnicu_vilcea)

rimnicu_vilcea.add_neighbor(craiova)
rimnicu_vilcea.add_neighbor(pitesti)
rimnicu_vilcea.add_neighbor(sibiu)

sibiu.add_neighbor(arad)
sibiu.add_neighbor(fagaras)

sibiu.add_neighbor(rimnicu_vilcea)

timisoara.add_neighbor(arad)
timisoara.add_neighbor(lugoj)

urziceni.add_neighbor(bucharest)
urziceni.add_neighbor(hirsova)
urziceni.add_neighbor(vaslui)

vaslui.add_neighbor(iasi)
vaslui.add_neighbor(urziceni)

zerind.add_neighbor(arad)
zerind.add_neighbor(oradea)

# Storing all the nodes in a list for easy access
cities = [arad, bucharest, craiova, drobeta, eforie, fagaras, giurgiu, hirsova, iasi, lugoj,
          mehadia, neamt, oradea, pitesti, rimnicu_vilcea, sibiu, timisoara, urziceni, vaslui, zerind]


# Task 3
import queue

fifo_queue = queue.Queue()
lifo_queue = queue.LifoQueue()
priority_queue = queue.PriorityQueue()

visited_1 = {}
visited_2 = {}
visited_3 = {}

# Task 4

# Task 5


def depthFirstSearch(initial_node, goal_state):
    lifo_queue = [[initial_node]]
    explored_cities = []
    cost = 0

    while lifo_queue:
        cost += 1
        path = lifo_queue.pop()

        last_node = path[-1]

        if last_node == goal_state:
            return path, explored_cities, cost
        else:
            for node in last_node.neighbors:
                if node in explored_cities:
                    continue
                if node in lifo_queue:
                    continue
                explored_cities.append(node)
                new_path = path + [node]
                lifo_queue.append(new_path)

    print(f'No path exists between {initial_node} and {goal_state}')
# Task 6
    
p, ec,c = depthFirstSearch(arad, bucharest)
print('-'*25)
print(p)
print('Explored Path')
print(c)
print('-'*25)
print('Explored cities', ec)
print('Cost', c)