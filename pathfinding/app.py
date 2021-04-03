from Graph.Graph import Graph
from Graph.Node import Node
from utils.dijkstra import dijkstra

if __name__ == "__main__":    

    node_1 = Node('a')
    node_2 = Node('b')
    node_3 = Node('c')
    node_4 = Node('d')
    node_5 = Node('e')
    node_6 = Node('f')
    node_7 = Node('g')
    node_8 = Node('h')
    node_9 = Node('i')
    node_10 = Node('j')
    node_11 = Node('k')
    node_12 = Node('l')
    node_13 = Node('s')

    graph = Graph()

    graph.add_node(node_1)
    graph.add_node(node_2)
    graph.add_node(node_3)
    graph.add_node(node_4)
    graph.add_node(node_5)
    graph.add_node(node_6)
    graph.add_node(node_7)
    graph.add_node(node_8)
    graph.add_node(node_9)
    graph.add_node(node_10)
    graph.add_node(node_11)
    graph.add_node(node_12)
    graph.add_node(node_13)

    graph.add_edge('a', 'b', 3)
    graph.add_edge('a', 'd', 4)
    graph.add_edge('a', 's', 7)
    
    graph.add_edge('b', 's', 2)
    graph.add_edge('b', 'd', 4)
    graph.add_edge('b', 'h', 1)
    
    graph.add_edge('c', 's', 3)
    graph.add_edge('c', 'l', 2)
    
    graph.add_edge('d', 'f', 5)
    
    graph.add_edge('e', 'g', 2)
    graph.add_edge('e', 'k', 5)
    
    graph.add_edge('f', 'h', 3)
    
    graph.add_edge('g', 'h', 2)
    
    graph.add_edge('i', 'k', 4)
    graph.add_edge('i', 'j', 6)
    graph.add_edge('i', 'l', 4)
    
    graph.add_edge('j', 'k', 4)
    graph.add_edge('j', 'l', 4)
    
    graph.add_edge('k', 'e', 5)
    
    dijkstra_path = dijkstra(graph.adj_list, 's', 'e')
    print(dijkstra_path)
    