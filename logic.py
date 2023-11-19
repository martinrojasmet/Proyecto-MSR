import sys
sys.path.insert(0, 'Datos/')
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

    def run(self):
        # Inicializar el algoritmo de Dijkstra

        
        print("Hello world")
        