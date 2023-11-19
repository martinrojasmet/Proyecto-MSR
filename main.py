import sys
sys.path.insert(0, 'data/')
from global_variables import graph, number_nodes

from dijkstra import dijkstra

def main():
    
    dijkstral = dijkstra()
    dijkstral.run(35, graph, True)
    print(dijkstral.run(35, graph, True))
    # dijkstral.print_last_result_table()
    
main()