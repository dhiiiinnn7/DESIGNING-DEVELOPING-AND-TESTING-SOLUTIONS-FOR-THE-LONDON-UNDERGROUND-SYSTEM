import pandas as pd  # IMPORTING PANDAS TO IMPORT THE EXCEL SPREADSHEET INTO PYTHON
import sys  # TO GIVE NODES INFINITY VALUE
import time  # Time Complexity
import matplotlib.pyplot  # FOR HISTOGRAM PURPOSES
from datetime import datetime, timedelta  # IMPORTING THIS MODULE FOR TASK 3 PURPOSES
from colorama import Fore  # IMPORTING THIS MODULE FOR TASK 3 PURPOSES


# --------------------------------------------------------------------

# TASK 2 (CLOSING STATIONS)
closed_station = '' or 'N/A'  # CHOOSE STATION TO CLOSE

# --------------------------------------------------------------------

# TASK 3 (FEATURE 1 OF 2/ CLOSING TRAIN LINES)
closed_train_line = '' or 'N/A'  # CHOOSE TRAIN LINE TO CLOSE

# --------------------------------------------------------------------
data = pd.read_excel(r"C:\Users\dhini\PycharmProjects\COMP 1828 - ALGORITHM LONDON TUBE\London Underground Data.xlsx")
d = data.to_dict(orient='index')
data.plot.hist(y="Minutes")
matplotlib.pyplot.show()

# STORE THE DATA IN THIS FUNCTION
def initial_graph():
    # IMPORTING THE DATA EXCEL SHEET INTO PYTHON
    data = pd.read_excel(r"C:\Users\dhini\PycharmProjects\COMP 1828 - ALGORITHM LONDON TUBE\London Underground Data.xlsx")
    d = data.to_dict(orient='index')
    # READING THE EXCEL SHEET AND SAVING IT IN A DICTIONARY
    graph = {}

    # ITERATING OVER ALL OF THE EXCEL SHEET DATA TO PREPARE
    # THE DATA FOR USE IN THE DIJKSTRA METHOD BY FORMATTING IT IN A GRAPH DICTIONARY

    for i in d.values():

        # CHECKS IF THE STATION 1 IS SIMILAR TO THE PICKED CLOSED STATION
        if i['Station_1'] == closed_station:
            continue
        # IF IT IS THEN POP THE STATION OUT OF THE DATA SHEET (GRAPH)

        # CHECKS IF THE TRAIN LINE USED IS SIMILAR TO THE PICKED CLOSED TRAIN LINE (TASK 3)
        if i['Tubeline'] == closed_train_line:
            continue
        # IF IT IS THEN IGNORE THE TRAIN LINE AND CHOOSE ANOTHER ALTERNATIVE
        # LOOKING INTO THE GRAPH IF STATION 1 IS IN IT
        if not graph.get(i['Station_1']):
            graph[i['Station_1']] = {}

        # LOOKING INTO THE GRAPH IF STATION 2 IS IN IT
        if not graph.get(i['Station_2']):
            graph[i['Station_2']] = {}

        # FORMAT - FOR THE CODE TO FOLLOW
        graph[i['Station_1']][i['Station_2']] = i['Minutes']
        graph[i['Station_2']][i['Station_1']] = i['Minutes']
        # DID THE SAME CODE FOR BOTH OF THE STATIONS SO THE TRAIN COULD ALSO GO BACK

    return graph


# FUNCTION FOR DIJKSTRA
def dijkstra(graph, starting_point, destination):
    dt = datetime.now()

    if starting_point == closed_station:
        print('Path not reachable') and graph.pop(closed_station)  # LETS USER KNOW PATH IS NOT REACHABLE
        return dijkstra(initial_graph(), input('Type starting point: '), input('Type destination: '))
    elif destination == closed_station:
        print('Path not reachable') and graph.pop(closed_station)
        return dijkstra(initial_graph(), input('Type starting point: '), input('Type destination: '))
    else:
        shortest_path = {}  # CREATES A DICTIONARY AND STORES THE SHORTEST NODES TO THE STARTING POINT
        adj_node = {}
        max_value = sys.maxsize  # SETTING THE MAX VALUE AS INFINITY
        queue = []
        unvisited_nodes = graph  # WE WILL MARK ALL THE STATIONS AS UNVISITED
        for node in unvisited_nodes:
            shortest_path[node] = max_value  # SETTING THE NODES AS INFINITY
            shortest_path[node] = float("inf")  # PICKS THE STATION WITH THE SHORTEST TIME BETWEEN NODES
            adj_node[node] = None
            queue.append(node)  # NODE GETS ADDED INTO THE QUEUE

        shortest_path[starting_point] = 0  # SETS THE STARTING POINT TO 0

        while queue:
            # FIND MINIMUM DISTANCE WHICH WAS NOT MARKED AS CURRENT
            key_min = queue[0]
            min_val = shortest_path[key_min]
            for n in range(1, len(queue)):
                if shortest_path[queue[n]] < min_val:
                    key_min = queue[n]
                    min_val = shortest_path[key_min]
            current_node = key_min
            queue.remove(current_node)

            for i in graph[current_node]:
                alternate = graph[current_node][i] + shortest_path[current_node]
                if shortest_path[i] > alternate:
                    shortest_path[i] = alternate
                    adj_node[i] = current_node

        # THE OUTPUT IN THE TERMINAL
        print('\nThis journey is estimated to take ' + str(shortest_path[destination]) + ' minutes.')
        print("The path is: " + destination, end=' <- ')
        # STORES THE MINUTES TAKEN AND ADDS IT TO THE CURRENT TIME FOR EXPECTED TIME TO GET THERE
        td = timedelta(minutes=shortest_path[destination])

        while True:
            destination = adj_node[destination]
            if destination is None:
                print("")
                break
            print(destination, end=' <- ')

        # TASK 3 (FEATURE 2 OF 2 / PRINTING EXPECTED TIME)
        my_date = dt + td
        print("\nThe time you will get there by is: " + Fore.MAGENTA + str(my_date))

        start_time = time.time()  # Time Complexity
        print("The program took " + str(time.time() - start_time) + " seconds.")

        # REQUEST TO RESET THE PROGRAM
        while True:

            while True:
                answer = str(input(Fore.RESET + '\nDo you want to make another search? (Yes/No): '))
                if answer in ('Yes', 'No'):
                    break
                print("invalid input.")
            if answer == 'Yes':
                # IF ANSWER IS YES RUN THE FUNCTION AGAIN
                return dijkstra(initial_graph(), input('Type starting point: '), input('Type destination: '))
            else:
                # FOR ANY OTHER ANSWER PRINT WHAT IS BELOW
                print("Thanks for using the journey planner.")
                break


# STATUS OF THE STATIONS AND TRAIN LINES (TASK 3)
print('The closed station is ' + str(closed_station)
      + ' / The closed train line is ' + str(closed_train_line))

# USE OF THE FUNCTIONS
dijkstra(initial_graph(), input('Type starting point: '), input('Type destination: '))

