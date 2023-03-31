import mtr
import bfs
import greedy
def main():
    # Generate the HK Metro System
    metro_system = mtr.generate_hk_metro_system()

    # Define the start and end station
    depature = 'Airport'
    arrival = 'Ocean Park'

    # Find the shortest path using BFS
    shortest_path, num_stations = bfs.bfs(metro_system, depature, arrival)
    # Find the shortest path using GREEDY
    Gshortest_path, Gnum_stations = greedy.greedy_search(metro_system, depature, arrival)

    # Print the shortest path
    print(f"BFS: The shortest path from {depature} to {arrival} is {shortest_path}. Number of stations: {num_stations}")
    print(f"GREEDY: The shortest path from {depature} to {arrival} is {Gshortest_path}. Number of stations: {Gnum_stations}")
if __name__ == "__main__":
    main()