from heapq import *
from heuristics import create_heuristic_table

#define Greedy function

def greedy_search(metro_graph, departure, arrival):
    heap = [] # Initialize an empty minheap to store stations to be expanded
    visited = set() # Initialize a set to keep track of visited stations
    heuristic_table = create_heuristic_table(arrival) # Create a heuristic table using the arrival as a reference
    heappush(heap, (heuristic_table.get(departure), [departure])) # Add the departure to the heap with its heuristic value as priority

    while len(heap) > 0:
        path = heappop(heap)[1] # path of the station with the lowest heuristic value
        current = path[-1] # last of the path is the current station
        if current == arrival: # arrival found
            return path, len(path)-1
        if current not in visited:
            visited.add(current) # if current not vidsited yet, marked as visited
        for adjacent, _ in metro_graph.get(current):
            if adjacent not in visited: # For each adjacent station not visited yet, add it to the heap with its heuristic and update path
                heappush(heap, (heuristic_table.get(adjacent), path+[adjacent]))
    return "Itineray NOT FOUND: " + str(departure) + " station is not reachable from " + str(arrival) + " station." # arrival not found
