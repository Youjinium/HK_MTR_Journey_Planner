from queue import Queue

# Define the BFS function
def bfs(metro_graph, departure, arrival):
    
    # BFS uses FIFO queue https://www.codingem.com/what-is-a-fifo-queue/
    queue = Queue()

    # Add first station to the queue. we have a tuple of (station, path)
    queue.put((departure, [departure]))

    # Initialize a set to keep track of visited stations (Note we use set to avoid having DUPLICATES)
    visited = set()

    # Implement BFS algorithm
    # Step 1: We visit the station and pop it out of the queue and append it to the visited set
    while queue:
        # Remove first station from the queue (Get is similar to pop)
        station, path = queue.get()
        
        # If we reached our arrival station then we return this path as output
        if station == arrival:
            return path
        else:
            # Add station to the visited set
            visited.add(station)
            
            # We check the next layer of the graph (BFS) by adding all the connected stations from our current station to the queue
            for connected_station in metro_graph[station]:
                # Check if connected station hasn't already been visited (AVOID LOOPS Lines)
                if connected_station not in visited:
                    # Path represents the path from the departure station to the current station
                    queue.put((connected_station, path + [connected_station]))

    # Station not reachable
    return "Itineray NOT FOUND: " + str(arrival) + " station is not reachable from " + str(departure) + " station."







