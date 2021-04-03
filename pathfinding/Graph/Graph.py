from .Edge import Edge
class Graph:
    def __init__(self):
        self.adj_list = {}
        
    #params
    #node (Node): node to add to graph 
    def add_node(self, node):
        self.adj_list[node.id] = {
            'node': node,
            'edges': []
        }
    
    #params
    #node1_id (string): id of first vertex
    #node2_id (string): id of second vertex
    #weight (int): distance between vertices
    
    #des
    #add a weighted edge between 2 vertex
    #add: exception when edge already exists
    def add_edge(self, node1_id, node2_id, weight = 1):
        
        new_edge = Edge(node2_id, weight)
        self.adj_list[node1_id]['edges'].append(new_edge)
        
        new_edge = Edge(node1_id, weight)
        self.adj_list[node2_id]['edges'].append(new_edge)