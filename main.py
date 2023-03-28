import mtr
import bfs

def main():
    # Generate the HK Metro System
    metro_system = mtr.generate_hk_metro_system()

    # Define the start and end station
    depature = 'Hong Kong'
    arrival = 'Central'

    # Find the shortest path using BFS
    shortest_path = bfs.bfs(metro_system, depature, arrival)

    # Print the shortest path
    print(f"The shortest path from {depature} to {arrival} is {shortest_path}")

if __name__ == "__main__":
    main()