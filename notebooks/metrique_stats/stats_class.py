import matplotlib.pyplot as plt
from matplotlib import interactive
from math import isnan

class DegreeStat:
    def __init__(self, vertex_num, edge_num, degrees, max_degree, avg_degree,
                deg_hist=None, in_degrees=None, avg_in_degree=None, out_degrees=None,
                 avg_out_degree=None, directed=False):
        self.vertexnum = vertex_num
        self.edgenum = edge_num
        self.degrees = degrees
        self.maxdegree = max_degree
        self.avgdegree = avg_degree
        self.indegrees = in_degrees
        self.avgindegree = avg_in_degree
        self.outdegrees = out_degrees
        self.avgoutdegree = avg_out_degree
        self.deghist = deg_hist
        self.is_directed = directed


    def print(self):
        if self.is_directed:
            print("Number of vertices = ", self.vertexnum)
            print("Number of edges = ", self.edgenum)
            print("Average degree = ", self.avgdegree)
            print("Max degree = ", self.maxdegree)
            print("Average In-Degree = ", self.avgindegree)

            plt.figure(1)
            plt.hist(self.indegrees, bins=30)
            plt.title('Distribution of In-Degrees')
            plt.xlabel('In-Degree')
            plt.ylabel('Number of Nodes')
            plt.axvline(self.avgindegree, color='k', linestyle='dashed', linewidth=1)

            interactive(True)
            plt.show()

            print("Average Out-Degree = ", self.avgoutdegree)

            plt.figure(2)
            plt.hist(self.outdegrees, bins=30)
            plt.title('Distribution of Out-Degrees')
            plt.xlabel('Out-Degree')
            plt.ylabel('Number of Nodes')
            plt.axvline(self.avgoutdegree, color='k', linestyle='dashed', linewidth=1)

        else :
            print("Number of vertices = ", self.vertexnum)
            print("Number of edges = ", self.edgenum)
            print("Average degree = ", self.avgdegree)
            print("Max degree = ", self.maxdegree)

            plt.figure(1)
            plt.hist(self.degrees, bins=30)
            plt.title('Distribution of Degrees')
            plt.xlabel('Degree')
            plt.ylabel('Number of Nodes')
            plt.axvline(self.avgdegree, color='k', linestyle='dashed', linewidth=1)

        interactive(False)
        plt.show()

class PathStat:
    def __init__(self, path_length_hist, avg_path_length, shortest_paths):
        self.pathlengthhist = path_length_hist
        self.avgpathlength = avg_path_length
        self.shortestpaths = shortest_paths
        list = []
        for path in shortest_paths:
            list += path

        self.path_list = list

    def print(self):
        print("Characteristic Path Length : ", self.avgpathlength)
        plt.figure(1)
        plt.hist(self.path_list, bins=30, color='g')
        plt.title('Distribution of Shortest Path Lengths')
        plt.xlabel('Shortest Path Lengths')
        plt.ylabel('Number of Nodes')
        plt.axvline(self.avgpathlength, color='k', linestyle='dashed', linewidth=1)

        plt.show()

class EccStat:
    def __init__(self, ecc, avg_ecc, in_ecc = None, avg_in_ecc = None,
                out_ecc = None, avg_out_ecc = None, in_radius = None,
                out_radius = None, directed=False, diameter=None, radius = None):
        self.is_directed = directed
        self.ecc = ecc
        self.avgecc = avg_ecc
        self.inecc = in_ecc
        self.avginecc = avg_in_ecc
        self.outecc = out_ecc
        self.avgoutecc = avg_out_ecc
        self.radius = radius
        self.inradius = in_radius
        self.outradius = out_radius
        self.diameter = diameter

    def print(self):
        print("Average Eccentricity = ", self.avgecc)
        plt.figure(1)
        plt.hist(self.ecc, bins=30)
        plt.title('Distribution of Eccentricities')
        plt.xlabel('Eccentricity')
        plt.ylabel('Number of Nodes')
        plt.axvline(self.avgecc, color='k', linestyle='dashed', linewidth=1)

        interactive(True)
        plt.show()

        if self.is_directed:
            print("Average In-Eccentricity = ", self.avginecc)
            print("In-Radius = ", self.inradius)

            plt.figure(2)
            plt.hist(self.inecc, bins=30)
            plt.title('Distribution of In-Eccentricities')
            plt.xlabel('In-Eccentricity')
            plt.ylabel('Number of Nodes')
            plt.axvline(self.avginecc, color='k', linestyle='dashed', linewidth=1, label='Average')
            plt.show()

            print("Average Out-Eccentricity = ", self.avgoutecc)
            print("Out-Radius = ", self.outradius)

            plt.figure(3)
            plt.hist(self.outecc, bins=30)
            plt.title('Distribution of Out-Eccentricities')
            plt.xlabel('Out-Eccentricity')
            plt.ylabel('Number of Nodes')
            plt.axvline(self.avginecc, color='k', linestyle='dashed', linewidth=1, label='Average')
            interactive(False)
            plt.show()
        else :
            print("Radius = ", self.radius)
        print("Diameter = ", self.diameter)



class ConnectStat:
    def __init__(self, num_components, e_connect, v_connect, num_bi_components, directed=False):
        self.numcomponents = num_components
        self.econnect = e_connect
        self.vconnect = v_connect
        self.numbicomponents = num_bi_components
        self.is_directed = directed

    def print(self):
        if self.is_directed:
            print("Number of Strongly Connected Components = ", self.numcomponents)
        else:
            print("Number of Connected Components = ", self.numcomponents)

        print("Vertex connectivity = ", self.vconnect)
        print("Edge connectivity = ", self.econnect)
        print("Number of BiConnected Components = ", self.numbicomponents)

class ClusterStat:
    def __init__(self, num_triangles, clust_coeffs, clust_graph, directed=False):
        self.is_directed = directed
        self.numtriangles = num_triangles
        self.clustcoeffs = clust_coeffs
        self.clustgraph = clust_graph

        for i in range(len(self.clustcoeffs)):
            if isnan(self.clustcoeffs[i]):
                self.clustcoeffs[i] = -1


    def print(self):
        print("Number of triangles = ", self.numtriangles)

        plt.figure(1)
        plt.hist(self.clustcoeffs, bins=30)
        plt.title('Distribution of Vertex Cluster Coefficients')
        plt.xlabel('Cluster Coefficient')
        plt.ylabel('Number of Nodes')

        plt.show()
        print("Graph Clustering Coefficient = ", self.clustgraph)


class CentralStat:
    def __init__(self, closeness, between, directed=False, in_closeness=None, out_closeness=None):
        self.is_directed = directed
        self.closeness = closeness
        self.incloseness = in_closeness
        self.outcloseness = out_closeness
        self.between = between

    def print(self):

        plt.figure(1)
        plt.hist(self.closeness, bins=30)
        plt.title('Distribution of Vertex Closeness Centrality')
        plt.xlabel('Closeness')
        plt.ylabel('Number of Nodes')
        #plt.axvline(self.avgoutdegree, color='k', linestyle='dashed', linewidth=1)

        interactive(True)
        plt.show()
        if self.is_directed:
            plt.figure(2)
            plt.hist(self.incloseness, bins=30)
            plt.title('Distribution of Vertex In-Closeness Centrality')
            plt.xlabel('In-Closeness')
            plt.ylabel('Number of Nodes')
            plt.show()

            plt.figure(3)
            plt.hist(self.outcloseness, bins=30)
            plt.title('Distribution of Vertex Out-Closeness Centrality')
            plt.xlabel('Out-Closeness')
            plt.ylabel('Number of Nodes')
            plt.show()

        plt.figure(4)
        plt.hist(self.between, bins=30)
        plt.title('Distribution of Vertex Betweenness Centrality')
        plt.xlabel('Betweenness')
        plt.ylabel('Number of Nodes')

        interactive(False)
        plt.show()
