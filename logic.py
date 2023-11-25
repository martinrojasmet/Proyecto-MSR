import sys
sys.path.insert(0, 'data/')
from global_variables import graph, number_nodes, house_javier, weight1_javier, weight2_javier, weight3_javier, house_andreina, weight1_andreina, weight2_andreina, weight3_andreina, DTD, BLP, CMR, CF

from dijkstra import dijkstra

class logic:

    def __init__(self):
        self.places_to_visit = [DTD, BLP, CMR, CF]
        self.dijkstra = dijkstra()

    def add_place_to_visit(self, name, carrera, calle):
        node = (abs(calle - 55)* 6) + abs(carrera - 15)
        result = {"name": name, "node": node}

        self.places_to_visit.append(result)

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

    # Verificar si chocan
    def check_if_they_crash(self, repeated_nodes_javier, repeated_nodes_andreina):
        return 1
        # 
        # Aqui se debe verificar si chocan
        # 
                        
    def run(self):
        table_for_places_to_visit = []
        # Guardar el lugar con el menor costo (guardando el mayor costo y el que lo tiene) [numero de nodo, es javier, costo]
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

        # Corregir el tiempo de Andreina o Javier si es necesario
        self.fix_time_difference(time_difference, is_javier, result_dijkstra)
        
        # Encontrar si chocan
        path_javier = self.dijkstra.get_path(result_dijkstra[0], lowest_cost_place[0])
        path_andreina = self.dijkstra.get_path(result_dijkstra[1], lowest_cost_place[0])

        repeated_nodes_javier, repeated_nodes_andreina = self.get_repeated_nodes(path_javier, path_andreina)

             