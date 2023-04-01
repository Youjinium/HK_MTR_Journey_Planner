import mtr
import bfs
import greedy
import astar
import dfs

def main():
    # Generate the HK Metro System
    metro_system = mtr.generate_hk_metro_system()

    # Define the start and end station
    depature = 'Airport'
    arrival = 'Hong Kong'

    # Find the shortest path using BFS
    Bshortest_path, Bnum_stations = bfs.bfs(metro_system, depature, arrival)

    # Find the shortest path using DFS
    Dshortest_path, Dnum_stations = dfs.dfs(metro_system, depature, arrival)

    # Find the shortest path using GREEDY
    Gshortest_path, Gnum_stations = greedy.greedy_search(metro_system, depature, arrival)

    # Find the shortest path using A*
    Ashortest_path, Anum_stations = astar.astar_search(metro_system, depature, arrival)

    # Print the shortest path
    print(f"BFS: The shortest path from {depature} to {arrival} is {Bshortest_path}. Number of stations: {Bnum_stations} \n")
    print(f"DFS: The shortest path from {depature} to {arrival} is {Dshortest_path}. Number of stations: {Dnum_stations} \n")
    print(f"GREEDY: The shortest path from {depature} to {arrival} is {Gshortest_path}. Number of stations: {Gnum_stations} \n")
    print(f"A*: The shortest path from {depature} to {arrival} is {Ashortest_path}. Number of stations: {Anum_stations} \n")
  

if __name__ == "__main__":
    main()