import csv
import itertools
# https://data.gov.hk/en-data/dataset/mtr-data-routes-fares-barrier-free-facilities

def create_metro_system(metro_system, station):
    if station not in metro_system:
        metro_system[station] = []

def add_next_station(metro_system, prev_row, row, next_row):
    if prev_row is not None:
        station = prev_row['English Name']
        create_metro_system(metro_system, station)

        # Add the adjacent stations to the current station
        if row is not None:
            if prev_row['Line Code'] == row['Line Code']:
                next_station = row['English Name']
                if next_station not in metro_system[station]:
                    # (Station name, cost)
                    cost = int(row['Sequence']) - int(prev_row['Sequence'])
                    station_tuple = (next_station, cost)
                    metro_system[station].append(station_tuple)

    if row is not None:
        station = row['English Name']
        create_metro_system(metro_system, station)

        # Add previous station to the current station
        if prev_row is not None:
            if prev_row['Line Code'] == row['Line Code']:
                prev_station = prev_row['English Name']
                if prev_station not in metro_system[station]:
                    # (Station name, cost)
                    cost = int(row['Sequence']) - int(prev_row['Sequence'])
                    station_tuple = (prev_station, cost)
                    metro_system[station].append(station_tuple)
        
        # Add next station to the current station
        if next_row is not None:
            if row['Line Code'] == next_row['Line Code']:
                next_station = next_row['English Name']
                if next_station not in metro_system[station]:
                    # (Station name, cost)
                    cost = int(next_row['Sequence']) - int(row['Sequence'])
                    station_tuple = (next_station, cost)
                    metro_system[station].append(station_tuple)

    if next_row is not None:
        station = next_row['English Name']
        create_metro_system(metro_system, station)

        #Add previous station to the current station
        if row is not None:
            if row['Line Code'] == next_row['Line Code']:
                prev_station = row['English Name']
                if prev_station not in metro_system[station]:
                    # (Station name, cost)
                    cost = int(next_row['Sequence']) - int(row['Sequence'])
                    station_tuple = (prev_station, cost)
                    metro_system[station].append(station_tuple)
            

def generate_hk_metro_system():
    metro_system = {}
    # Read the CSV file and create a dictionary with station sequences
    with open('mtr_lines_and_stations.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]

        # Create a sliding window of three rows
        row_window = itertools.islice(itertools.zip_longest(rows, rows[1:], rows[2:]), len(rows))

        for prev_row, row, next_row in row_window:

            add_next_station(metro_system, prev_row, row, next_row)

    return metro_system

print(generate_hk_metro_system())
