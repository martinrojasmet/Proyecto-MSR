import sys
sys.path.insert(0, 'data/')
from global_variables import graph, number_nodes

from testing import modified_graph

from dijkstra import dijkstra

from logic import logic

def main():
    
    dijkstral = dijkstra()
    # dijkstral.run(graph, True)
    # print(dijkstral.run(graph, True))
    # print("")
    # print(dijkstral.run(modified_graph, False))

    log = logic()
    log.run()

    # print(dijkstral.get_path(dijkstral.run(modified_graph, False), 31))
    # dijkstral.get_path(dijkstral.run(modified_graph, False), 31)
    # dijkstral.print_last_result_table()
    
main()