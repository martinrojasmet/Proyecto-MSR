import sys
sys.path.insert(0, 'data/')
from global_variables import number_nodes, house_javier, house_andreina, weight1_javier, weight2_javier, weight3_javier, weight1_andreina, weight2_andreina, weight3_andreina, weight4

class dijkstra():

    def __init__(self):
        self.last_result_table = {}
        
    # Llenar la tabla de resultados con valores iniciales
    def fill_result_table(self, result_table, source):
        for node_number in range(0, number_nodes):
            result_table[node_number] = {"cost": 1000, "before": ""}
        result_table[source]["cost"] = 0

    # Convertir el peso de la arista al valor numerico real
    def convert_weight(self, weight, is_javier):
        result = -1000
        if is_javier:
            weight1 = weight1_javier
            weight2 = weight2_javier
            weight3 = weight3_javier
        else:
            weight1 = weight1_andreina
            weight2 = weight2_andreina
            weight3 = weight3_andreina

        if weight == 1:
            result = weight1
        elif weight == 2:
            result = weight2
        elif weight == 3:
            result = weight3
        else:
            result = weight4
        return result

    # Imprimir la tabla de resultados
    def print_last_result_table(self):
        for node in self.last_result_table:
            print(node, self.last_result_table[node])

    # Obtener el camino de un nodo a otro
    def get_path(self, result_table, destination):
        path = []
        path.append((destination, result_table[destination]["cost"]))
        destination = result_table[destination]["before"]
        while destination != "":
            path.append((destination, result_table[destination]["cost"]))
            destination = result_table[destination]["before"]
        return path[::-1]
        
    # Ejecutar el algoritmo de Dijkstra
    def run(self, graph, is_javier):
        result_table = {}
        visited_nodes = []
        if is_javier:
            source = house_javier
        else:
            source = house_andreina

        min_cost_neighbor = [-1, 1001]

        # Llenar la tabla de resultados
        self.fill_result_table(result_table, source)

        # Inicializar el nodo temporal
        temp_node = source
        
        while not len(visited_nodes) == number_nodes: 
        # Primer paso: agregar si es mas corto el camino de los vecinos
            for neighbor in graph[temp_node]:
                if neighbor not in visited_nodes:
                    new_cost = result_table[temp_node]["cost"] + self.convert_weight(graph[temp_node][neighbor], is_javier)
                    old_cost = result_table[neighbor]["cost"]

                    if new_cost < old_cost:
                        result_table[neighbor]["cost"] = new_cost
                        result_table[neighbor]["before"] = temp_node

        # Segundo paso: buscar el nodo vecino de menor costo
            for node in result_table:
                if node not in visited_nodes and node != temp_node:
                    if result_table[node]["cost"] < min_cost_neighbor[1]:
                        min_cost_neighbor[0] = node
                        min_cost_neighbor[1] = result_table[node]["cost"]

        # Tercer paso: actualizar el nodo temporal y agregar el anterior a la lista de visitados
            visited_nodes.append(temp_node)
            temp_node = min_cost_neighbor[0]
            min_cost_neighbor = [-1, 1001]
        
        self.last_result_table = result_table
        return result_table