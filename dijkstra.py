class dijkstra():

    def __init__(self, destination, graph, number_nodes, is_javier):
        self.destination = destination
        self.graph = graph
        self.result_table = {}
        self.visited_nodes = []
        self.number_nodes = number_nodes
        if is_javier:
            self.source = 7
            self.weight1 = 5
            self.weight2 = 7
            self.weight3 = 10
        else:
            self.source = 20
            self.weight1 = 7
            self.weight2 = 9
            self.weight3 = 12
        
    # Llenar la tabla de resultados con valores iniciales
    def fill_result_table(self):
        for node_number in range(0, self.number_nodes):
            self.result_table[node_number] = {"cost": 1000, "before": ""}
        self.result_table[self.source]["cost"] = 0

    # Convertir el peso de la arista al valor numerico real
    def convert_weight(self, weight):
        result = -1000
        if weight == 1:
            result = self.weight1
        elif weight == 2:
            result = self.weight2
        elif weight == 3:
            result = self.weight3
        return result

    def run(self):
        min_cost_neighbor = [-1, 1001]

        # Llenar la tabla de resultados
        self.fill_result_table()

        # Inicializar el nodo temporal
        temp_node = self.source
        
        while not len(self.visited_nodes) == self.number_nodes: 
            # Primer paso: agregar si es mas corto el camino de los vecinos
            for neighbor in self.graph[temp_node]:
                if neighbor not in self.visited_nodes:
                    new_cost = self.result_table[temp_node]["cost"] + self.convert_weight(self.graph[temp_node][neighbor])
                    old_cost = self.result_table[neighbor]["cost"]

                    if new_cost < old_cost:
                        self.result_table[neighbor]["cost"] = new_cost
                        self.result_table[neighbor]["before"] = temp_node

            # Segundo paso: buscar el nodo vecino de menor costo
            for node in self.result_table:
                if node not in self.visited_nodes and node != temp_node:
                    if self.result_table[node]["cost"] < min_cost_neighbor[1]:
                        min_cost_neighbor[0] = node
                        min_cost_neighbor[1] = self.result_table[node]["cost"]

            # Tercer paso: actualizar el nodo temporal y agregar el anterior a la lista de visitados
            self.visited_nodes.append(temp_node)
            temp_node = min_cost_neighbor[0]
            min_cost_neighbor = [-1, 1001]
        
        # Imprimir la tabla de resultados
        for node in self.result_table:
            print(node, self.result_table[node])
