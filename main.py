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
oradea.add_neighbor(sibiu)


pitesti.add_neighbor(craiova)
pitesti.add_neighbor(bucharest)
pitesti.add_neighbor(rimnicu_vilcea)

rimnicu_vilcea.add_neighbor(craiova)
rimnicu_vilcea.add_neighbor(pitesti)
rimnicu_vilcea.add_neighbor(sibiu)

sibiu.add_neighbor(arad)
sibiu.add_neighbor(fagaras)

sibiu.add_neighbor(rimnicu_vilcea)
sibiu.add_neighbor(oradea)

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
# Breadth First Search
def breadthFirstSearch(initial_node, goal_state):
    found = False
    fifo_queue.put(initial_node)
    visited_1.add(initial_node)
    parent = {}  #dict for storing the parents
    parent[initial_node] = None

    while not fifo_queue.empty():
        node = fifo_queue.get()
        visited_1.add(node)
        if node == goal_state:
            found = True
            break
        for neighbor in node.neighbors:
            if neighbor not in visited_1:
                fifo_queue.put(neighbor)
                parent[neighbor] = node #store the parent 
    
    if found:
        destination = goal_state
        path = []
        while destination is not None:
            path.append(destination)
            destination = parent[destination]

        path.reverse()
        # printing the path to our destination city
        pathString = str(path.pop(0))
        for city in path:
            pathString += " --> " + str(city)
        
        print(pathString)

    else:
        print("City not found")
    
                

# Task 5
#Depth First Search - Ashmitha Pais

def depthFirstSearch(initial_node, goal_state):
    lifo_queue = [[initial_node]]
    explored_cities = [initial_node]

    while lifo_queue:
        path = lifo_queue.pop()
 
        last_node = path[-1]

        if last_node == goal_state:
            pathString = str(path.pop(0))
            for city in path:
                pathString += " --> " + str(city)
            print(pathString)
            return
        else:
            for node in last_node.neighbors:
                if node in explored_cities:
                    continue
                if node in lifo_queue:
                    continue
                explored_cities.append(node)
                new_path = path + [node]
                lifo_queue.append(new_path)

    print(f'failure: No path found')

    
depthFirstSearch(arad, neamt)



# Task 6
# Uniform Cost Search

from Node import UniformNode

# Re-initialize the search tree with path costs
arad = UniformNode("Arad")
bucharest = UniformNode("Bucharest")
craiova = UniformNode("Craiova")
drobeta = UniformNode("Drobeta")
eforie = UniformNode("Eforie")
fagaras = UniformNode("Fagaras")
giurgiu = UniformNode("Giurgiu")
hirsova = UniformNode("Hirsova")
iasi = UniformNode("Iasi")
lugoj = UniformNode("Lugoj")
mehadia = UniformNode("Mehadia")
neamt = UniformNode("Neamt")
oradea = UniformNode("Oradea")
pitesti = UniformNode("Pitesti")
rimnicu_vilcea = UniformNode("Rimnicu Vilcea")
sibiu = UniformNode("Sibiu")
timisoara = UniformNode("Timisoara")
urziceni = UniformNode("Urziceni")
vaslui = UniformNode("Vaslui")
zerind = UniformNode("Zerind")

arad.add_neighbor(zerind, 75)
arad.add_neighbor(timisoara, 118)
arad.add_neighbor(sibiu, 140)

bucharest.add_neighbor(fagaras, 211)
bucharest.add_neighbor(giurgiu, 90)
bucharest.add_neighbor(pitesti, 101)
bucharest.add_neighbor(urziceni, 85)

craiova.add_neighbor(drobeta, 120)
craiova.add_neighbor(pitesti, 138)
craiova.add_neighbor(rimnicu_vilcea, 146)

drobeta.add_neighbor(craiova, 120)
drobeta.add_neighbor(mehadia, 75)

eforie.add_neighbor(hirsova, 86)

fagaras.add_neighbor(bucharest, 211)
fagaras.add_neighbor(sibiu, 99)

giurgiu.add_neighbor(bucharest, 90)

hirsova.add_neighbor(eforie, 86)
hirsova.add_neighbor(urziceni, 98)

iasi.add_neighbor(neamt, 87)
iasi.add_neighbor(vaslui, 92)

lugoj.add_neighbor(mehadia, 70)
lugoj.add_neighbor(timisoara, 111)

mehadia.add_neighbor(drobeta, 75)
mehadia.add_neighbor(lugoj, 70)

neamt.add_neighbor(iasi, 87)

oradea.add_neighbor(zerind, 71)
oradea.add_neighbor(sibiu, 151)

pitesti.add_neighbor(craiova, 138)
pitesti.add_neighbor(bucharest, 101)
pitesti.add_neighbor(rimnicu_vilcea, 97)

rimnicu_vilcea.add_neighbor(craiova, 146)
rimnicu_vilcea.add_neighbor(pitesti, 97)
rimnicu_vilcea.add_neighbor(sibiu, 80)

sibiu.add_neighbor(arad, 140)
sibiu.add_neighbor(fagaras, 99)
sibiu.add_neighbor(rimnicu_vilcea, 80)
sibiu.add_neighbor(oradea, 151)

timisoara.add_neighbor(arad, 118)
timisoara.add_neighbor(lugoj, 111)

urziceni.add_neighbor(bucharest, 85)
urziceni.add_neighbor(hirsova, 98)
urziceni.add_neighbor(vaslui, 142)

vaslui.add_neighbor(iasi, 92)
vaslui.add_neighbor(urziceni, 142)

zerind.add_neighbor(arad, 75)
zerind.add_neighbor(oradea, 71)

cities = [arad, bucharest, craiova, drobeta, eforie, fagaras, giurgiu, hirsova, iasi, lugoj,
          mehadia, neamt, oradea, pitesti, rimnicu_vilcea, sibiu, timisoara, urziceni, vaslui, zerind]


def uniformCostSearch(initial_node, goal_state):
    priority_queue.put((0, initial_node))  
    visited = set()
    parent = {initial_node: None}
    cost_so_far = {initial_node: 0}

    while not priority_queue.empty():
        current_cost, current_node = priority_queue.get()

        if current_node == goal_state:
           
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            total_cost = cost_so_far[goal_state]
            pathString = ' --> '.join(str(city) for city in path) + f" (Total Cost: {total_cost})"
            print(pathString)
            return

        visited.add(current_node)

        for neighbor, neighbor_cost in current_node.neighbors.items():
            new_cost = cost_so_far[current_node] + neighbor_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority_queue.put((new_cost, neighbor))
                parent[neighbor] = current_node

    print("City not found")


uniformCostSearch(arad, neamt)