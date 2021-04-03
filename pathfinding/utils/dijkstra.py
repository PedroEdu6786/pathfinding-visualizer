import math

from Graph.Graph import Graph
from Graph.Node import Node

#Constants
DISTANCE = 0
PREV_VERTEX = 1

VERTEX_ID = 'vertex_id'
EDGES = 'edges'
COST = 'COST'

#initializes dijkstra costs and previous vertex of each node
def init_path_costs(src, unvisited_vertices):
    INITIAL_COST = 0
    PREV_VERTEX = None
    costs = {src: [INITIAL_COST, PREV_VERTEX]}
    
    #Assigns minimum cost to all vertices
    for key in unvisited_vertices:
        if key != src:
            costs[key] = [math.inf, PREV_VERTEX]
            
    return costs

#calculates next vertex to visit according to priority_queue
def next_vertex(priority_queue):
    #Sorts priority queue to order weights for next path
    priority_queue = sorted(priority_queue, key = lambda val: val[COST])        
    
    #Reverse the queue to pop out smallest weight instead of pulling
    priority_queue.reverse()
    
    #returns dictionary of format: { VERTEX_ID: vertex_id, COST: vertex_distance }
    return priority_queue.pop()

def dijkstra(graph, src, goal):
    
    #List of vertices yet to visit and its costs
    unvisited_vertices = [*graph]
    costs = init_path_costs(src, unvisited_vertices)
    
    #Current visited vertex
    curr_vertex = src
    priority_queue = [] #Queue with priority vertices of smaller costs
    
    #if curr_vertex is none, then there's no path between src and goal
    #if curr_vertex != goal, then src has reached the goal
    #if unvisited_vertices is empty then it has checked all vertices
    while unvisited_vertices and curr_vertex != None and curr_vertex != goal:    
        
        #Visits all vertices near the current vertex
        for vertex in graph[curr_vertex][EDGES]:
            
            #vertex id and weight/distance of next vertice in the list
            vertex_id = vertex.node_id
            vertex_distance = vertex.weight + costs[curr_vertex][DISTANCE]
            
            #Checks if the vertice is not already visited and if its a shorter path
            if vertex_distance < costs[vertex_id][DISTANCE] and vertex_id in unvisited_vertices:
                #Updates shortest distance to a vertex
                costs[vertex_id][DISTANCE] = vertex_distance #distance
                costs[vertex_id][PREV_VERTEX] = curr_vertex #previous vertex
                
                priority_queue.append({ VERTEX_ID: vertex_id, COST: vertex_distance })
                    
        #Remove current vertex from unvisited list and added to visited list
        unvisited_vertices.remove(curr_vertex)
        
        #Update current vertex for next path
        curr_vertex = next_vertex(priority_queue)[VERTEX_ID]
        
        #Remove repeated vertex equal to current vertex from priority_queue
        priority_queue = [vertex for vertex in priority_queue if not vertex[VERTEX_ID] == curr_vertex]
        
    return costs