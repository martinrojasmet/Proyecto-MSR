import sys
sys.path.insert(0, 'data/')
from global_variables import graph, number_nodes, house_javier, weight1_javier, weight2_javier, weight3_javier, house_andreina, weight1_andreina, weight2_andreina, weight3_andreina, DTD, BLP, CMR, CF
import copy
from dijkstra import dijkstra

class logic:

    def __init__(self):
        self.places_to_visit = [DTD, BLP, CMR, CF]
        self.dijkstra = dijkstra()
        self.result_node = -1
        self.result_path_javier = -1
        self.result_path_andreina = -1
        self.result_time_difference = [-1, -1]

    def add_place_to_visit(self, name, carrera, calle):
        node = (abs(calle - 55)* 6) + abs(carrera - 15)
        result = {"name": name, "node": node}
        return result

    # Determinar el que tome menos tiempo y cuanto
    def get_difference_time(self, result_table_javier, result_table_andreina, destination):
        time_difference = abs(result_table_javier[destination]["cost"] - result_table_andreina[destination]["cost"])
        is_javier = False

        if result_table_javier[destination]["cost"] < result_table_andreina[destination]["cost"]:
            is_javier = True

        return (time_difference, is_javier)

    # Corregir el tiempo de Andreina o Javier si es necesario
    def fix_time_difference(self, time_difference, is_javier, result_dijkstra):
        if time_difference > 0:
            if is_javier:
                for node in result_dijkstra[0]:
                    result_dijkstra[0][node]["cost"] += time_difference
            else:
                for node in result_dijkstra[1]:
                    result_dijkstra[1][node]["cost"] += time_difference

    # Encontrar los que chocan
    def get_repeated_nodes(self, path_javier, path_andreina):
        repeated_nodes_javier = []
        repeated_nodes_andreina = []
        for node in path_javier:
            for node2 in path_andreina:
                if node[0] == node2[0]:
                    repeated_nodes_javier.append(node)
                    repeated_nodes_andreina.append(node2)

        return (repeated_nodes_javier, repeated_nodes_andreina)

    # Verificar si chocan t retornar el par de nodos que chocan
    def check_if_they_crash(self, repeated_nodes_javier, repeated_nodes_andreina):
        result = (-1, -1)
        if len(repeated_nodes_javier) > 1:
            for i in range(len(repeated_nodes_javier) - 1):
                if (repeated_nodes_javier[i+1][1] > repeated_nodes_andreina[i][1]) and (repeated_nodes_javier[i][1] < repeated_nodes_andreina[i+1][1]):
                    result = (repeated_nodes_javier[i][0], repeated_nodes_javier[i+1][0])
                    break
        return result

    def run(self):
        table_for_places_to_visit = []
        # Guardar el lugar con el menor costo posible (guardando el mayor costo y el que lo tiene) [numero de nodo, es javier, costo]
        lowest_cost_place = [-1, True, 1000]

        # Inicializar el algoritmo de Dijkstra
        result_dijkstra = (self.dijkstra.run(graph, True), self.dijkstra.run(graph, False))

        # Llenar la tabla de resultados con [numero de nodo, costo de javier, costo de andreina]
        for place in self.places_to_visit:
            table_for_places_to_visit.append([place["node"], result_dijkstra[0][place["node"]]["cost"], result_dijkstra[1][place["node"]]["cost"]])

        # Buscar el minimax del par de cada lugar
        for place in table_for_places_to_visit:
            if place[2] > place[1]:
                if place[2] < lowest_cost_place[2]:
                    lowest_cost_place = [place[0], False, place[2]]
            else:
                if place[1] < lowest_cost_place[2]:
                    lowest_cost_place = [place[0], True, place[1]]

        # Encontrar la diferencia de tiempo entre el recorrido de Javier y Andreina
        time_difference, is_javier = self.get_difference_time(result_dijkstra[0], result_dijkstra[1], lowest_cost_place[0])

        # time_difference, is_javier = self.get_difference_time(result_dijkstra[0], result_dijkstra[1], 31)
        # # RECORDAR CAMBIAR EL 31 POR EL DESTINO


        # Corregir el tiempo de Andreina o Javier si es necesario
        self.fix_time_difference(time_difference, is_javier, result_dijkstra)
        
        # Encontrar si chocan
        path_javier = self.dijkstra.get_path(result_dijkstra[0], lowest_cost_place[0])
        path_andreina = self.dijkstra.get_path(result_dijkstra[1], lowest_cost_place[0])

        # Añadir el camino de Javier y Andreina a los resultados
        self.result_path_javier = path_javier
        self.result_path_andreina = path_andreina

        # path_javier = self.dijkstra.get_path(result_dijkstra[0], 31)
        # path_andreina = self.dijkstra.get_path(result_dijkstra[1], 31) 
        # # RECORDAR CAMBIAR EL 31 POR EL DESTINO

        repeated_nodes_javier, repeated_nodes_andreina = self.get_repeated_nodes(path_javier, path_andreina)

        crash_first, crash_second = self.check_if_they_crash(repeated_nodes_javier, repeated_nodes_andreina)

        # Cambiar el recorrido del que tenga menor costo
        new_result_dijkstra = None
        if crash_first != -1:
            modified_graph = graph
            modified_graph[crash_first][crash_second] = 4
            if is_javier:
                new_result_dijkstra = self.dijkstra.run(modified_graph, True)
            else:
                new_result_dijkstra = self.dijkstra.run(modified_graph, False)

        # Arreglar los tiempos de nuevo
        if new_result_dijkstra != None:
            if is_javier:
                time_difference, is_javier = self.get_difference_time(new_result_dijkstra, result_dijkstra[1], lowest_cost_place[0])
                # # RECORDAR CAMBIAR EL 31 POR EL DESTINO
                # time_difference, is_javier = self.get_difference_time(new_result_dijkstra, result_dijkstra[1], 31)
                for node in new_result_dijkstra:
                    new_result_dijkstra[node]["cost"] += time_difference
                self.result_path_javier = self.dijkstra.get_path(new_result_dijkstra, lowest_cost_place[0])
            else:
                time_difference, is_javier = self.get_difference_time(result_dijkstra[0], new_result_dijkstra, lowest_cost_place[0])
                # # RECORDAR CAMBIAR EL 31 POR EL DESTINO
                # time_difference, is_javier = self.get_difference_time(result_dijkstra[0], new_result_dijkstra, 31)
                for node in new_result_dijkstra:
                    new_result_dijkstra[node]["cost"] += time_difference
                self.result_path_andreina = self.dijkstra.get_path(new_result_dijkstra, lowest_cost_place[0])

        # # print(self.dijkstra.get_path(new_result_dijkstra, 31))
        # # print(self.dijkstra.get_path(new_result_dijkstra, lowest_cost_place[0]))
        # print(new_result_dijkstra)

        self.result_node = lowest_cost_place[0]
        self.result_time_difference = [time_difference, is_javier]

        print(self.result_node)
        print(self.result_path_javier)
        print(self.result_path_andreina)
        print(self.result_time_difference)

    def get_shortest_path(self, node_number):
        result_dijkstra = (self.dijkstra.run(graph, True), self.dijkstra.run(graph, False))

        # Encontrar la diferencia de tiempo entre el recorrido de Javier y Andreina
        time_difference, is_javier = self.get_difference_time(result_dijkstra[0], result_dijkstra[1], node_number)

        # Corregir el tiempo de Andreina o Javier si es necesario
        self.fix_time_difference(time_difference, is_javier, result_dijkstra)
        
        # Encontrar si chocan
        path_javier = self.dijkstra.get_path(result_dijkstra[0], node_number)
        path_andreina = self.dijkstra.get_path(result_dijkstra[1], node_number)

        # Añadir el camino de Javier y Andreina a los resultados
        self.result_path_javier = path_javier
        self.result_path_andreina = path_andreina

        repeated_nodes_javier, repeated_nodes_andreina = self.get_repeated_nodes(path_javier, path_andreina)

        crash_first, crash_second = self.check_if_they_crash(repeated_nodes_javier, repeated_nodes_andreina)

        # Cambiar el recorrido del que tenga menor costo
        new_result_dijkstra = None
        if crash_first != -1:
            modified_graph = copy.deepcopy(graph)
            modified_graph[crash_first][crash_second] = 4
            if is_javier:
                new_result_dijkstra = self.dijkstra.run(modified_graph, True)
            else:
                new_result_dijkstra = self.dijkstra.run(modified_graph, False)

        # Arreglar los tiempos de nuevo
        if new_result_dijkstra != None:
            if is_javier:
                time_difference, is_javier = self.get_difference_time(new_result_dijkstra, result_dijkstra[1], node_number)
                for node in new_result_dijkstra:
                    new_result_dijkstra[node]["cost"] += time_difference
                self.result_path_javier = self.dijkstra.get_path(new_result_dijkstra, node_number)
            else:
                time_difference, is_javier = self.get_difference_time(result_dijkstra[0], new_result_dijkstra, node_number)
                for node in new_result_dijkstra:
                    new_result_dijkstra[node]["cost"] += time_difference
                self.result_path_andreina = self.dijkstra.get_path(new_result_dijkstra, node_number)

        self.result_node = node_number
        self.result_time_difference = [time_difference, is_javier]

        # print(self.result_path_javier)
        # print(self.result_path_andreina)
        # print(graph)
        # print("---------------------")
        # print(modified_graph)
        # print("=============================")

    def reset_values(self):
        self.result_node = -1
        self.result_path_javier = -1
        self.result_path_andreina = -1
        self.result_time_difference = [-1, -1]
        self.dijkstra.last_result_table = {}
