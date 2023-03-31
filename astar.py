from heapq import *
from heuristics import create_heuristic_table

#define A* function

def astar_search(metro_graph, departure, arrival):
    heap = [] # Initialize an empty minheap to store stations to be expanded
    visited = set() # Initialize a set to keep track of visited stations
    heuristic_table = create_heuristic_table(arrival) # Create a heuristic table using the arrival as a reference
    heappush(heap, (heuristic_table.get(departure), 0, [departure])) # Add the departure to the heap with its heuristic value and its path cost, the priority is their sum

    while len(heap) > 0:
        station_node = heappop(heap) # station with the lowest total cost
        path_cost = station_node[1] # path cost of the station
        path = station_node[2] # path of the station with the lowest heuristic value
        current = path[-1] # last of the path is the current station
        if current == arrival: # arrival found
            return path, len(path)-1
        if current not in visited:
            visited.add(current) # if current not visited yet, marked as visited
        for adjacent, cost in metro_graph.get(current):
            if adjacent not in visited: # For each adjacent station not visited yet, add it to the heap with its total cost and path cost and update path
                heappush(heap, (path_cost + cost + heuristic_table.get(adjacent), path_cost + cost, path+[adjacent]))
    return "Itineray NOT FOUND: " + str(departure) + " station is not reachable from " + str(arrival) + " station." # arrival not found
