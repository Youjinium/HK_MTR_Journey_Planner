import csv
import bfs
import mtr

def create_heuristic_table(arrival_station):

    #Initialize heuristic table
    heuristic_table = {}

    # Generate the HK Metro System
    metro_system = mtr.generate_hk_metro_system()

    with open('mtr_lines_and_stations.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        for row in reader:
            station = row['English Name']
            heuristic_table[station] = bfs.bfs(metro_system, station, arrival_station)[1]

    return heuristic_table

def store_heuristic_table_as_csv(arrival_station, heuristic_table):
    with open(str(arrival_station) + '_heuristic_table.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Station', 'Distance'])
        for station, distance in heuristic_table.items():
            writer.writerow([station, distance])


# Create heuristic table and store as csv 
def main(arrival_station):
    heuristic_table = create_heuristic_table(arrival_station)
    store_heuristic_table_as_csv(arrival_station, heuristic_table)
