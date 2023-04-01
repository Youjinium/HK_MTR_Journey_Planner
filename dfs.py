from queue import LifoQueue

# Define the DFS function
def dfs(metro_graph, departure, arrival):
    # DFS uses LIFO queue (Stack)
    stack = LifoQueue()

    # Add first station to the stack. We have a tuple of (station, path)
    stack.put((departure, [departure]))

    # Initialize a set to keep track of visited stations (Note we use set to avoid having DUPLICATES)
    visited = set()

    # Implement DFS algorithm
    # Step 1: We visit the station and pop it out of the stack and append it to the visited set
    while stack:
        # Remove first station from the stack (Get is similar to pop)
        station, path = stack.get()

        # Uncomment to illustrate search path of algotithm
        # print(station)

        # If we reached our arrival station then we return this path as output
        if station == arrival:
  
            # Calculate the number of stations in the path
            num_stations = len(path) - 1
            return path, num_stations
        else:
            # Add station to the visited set
            visited.add(station)

            # We check the next layer of the graph (DFS) by adding all the connected stations from our current station to the stack
            for connected_station_tuple in metro_graph[station]:
                connected_station = connected_station_tuple[0]
                # Check if connected station hasn't already been visited (AVOID LOOPS Lines)
                if connected_station not in visited:
                    # Path represents the path from the departure station to the current station
                    stack.put((connected_station, path + [connected_station]))


    # Station not reachable
    return "Itinerary NOT FOUND: " + str(arrival) + " station is not reachable from " + str(departure) + " station."
