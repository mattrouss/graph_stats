from py2neo import Graph, Node, authenticate, Relationship
from igraph import Graph as IGraph, mean

import metrique_stats.stats_class

import pandas as pd


def init_neo_graph():
    """

    Returns the Neo4j graph of the default database

    """
    #authenticate("http://simulab.li.kernix.net:7475", "dbse", "pass4dbse")
    #graph = PGraph("http://simulab.li.kernix.net:7475")
    #authenticate("http://neo:7474", "neo4j", "password")
    graph = Graph("http://neo4j:password@neo:7474")

    return graph


def neo_to_igraph(query, graph, directed=False):

    """

    Returns an igraph graph converted from a neo4j subgraph obtained by query.

    """

    data = graph.cypher.execute(query)
    ig = IGraph.TupleList(data, directed)

    return ig


# Degree statistics of iGraph

def degree_stats(graph):
    """
    Gathers graph statistics relative to its degree and returns a DegreeStat object.

    Args:
        graph - an igraph Graph.

    Returns:
        degreestats - a DegreeStat object.

    """

    #Basic operations
    vertex_num = graph.vcount()
    edge_num = graph.ecount()

    #Degrees
    if graph.is_directed() :
        degrees = graph.degree()
        max_degree = graph.maxdegree()
        avg_degree = mean(degrees)
        in_degrees = graph.indegree()
        avg_in_degree = mean(in_degrees)
        out_degrees = graph.outdegree()
        avg_out_degree = mean(out_degrees)

        degreestats = stats_class.DegreeStat(vertex_num=vertex_num, edge_num=edge_num,
                    degrees=degrees, max_degree=max_degree, avg_degree=avg_degree,
                    in_degrees=in_degrees, avg_in_degree=avg_in_degree,
                    out_degrees=out_degrees,avg_out_degree=avg_out_degree,directed=graph.is_directed())
    else:
        degrees = graph.degree()
        max_degree = graph.maxdegree()
        avg_degree = mean(degrees)
        hist = graph.degree_distribution()

        degreestats = stats_class.DegreeStat(vertex_num=vertex_num, edge_num=edge_num,
                    degrees=degrees, max_degree=max_degree, avg_degree=avg_degree,
                     deg_hist=hist,directed=graph.is_directed())

    return degreestats


# Path statistics of graph

def path_stats(graph):
    """
    Gathers graph statistics relative to paths and returns a PathStat object.

    Args:
        graph - an igraph Graph.

    Returns:
        pathstats - a PathStat object.

    """
    Directed = graph.is_directed()
    #Path length
    path_length_hist = graph.path_length_hist(directed=Directed)
    avg_path_length = graph.average_path_length(directed=Directed)

    # Shortest paths
    shortest_paths = graph.shortest_paths()

    pathstats = stats_class.PathStat(path_length_hist, avg_path_length, shortest_paths)
    return pathstats

# Eccentricity statistics of graph

def ecc_stats(graph):
    """
    Gathers graph statistics relative to eccentricity and returns an EccStat object.

    Args:
        graph - an igraph Graph.

    Returns:
        eccstats - a EccStat object.

    """

    ecc = graph.eccentricity()
    avg_ecc = mean(ecc)

    if graph.is_directed():
        in_ecc = graph.eccentricity(mode='IN')
        avg_in_ecc = mean(in_ecc)
        out_ecc = graph.eccentricity(mode='OUT')
        avg_out_ecc = mean(out_ecc)

        in_radius = graph.radius('IN')
        out_radius = graph.radius(mode='OUT')

        diameter = graph.diameter(directed=True)

        eccstats = stats_class.EccStat(ecc, avg_ecc, in_ecc, avg_in_ecc, out_ecc, avg_out_ecc, in_radius, out_radius,graph.is_directed(), diameter )


    else:
        radius = graph.radius()
        diameter = graph.diameter(directed=False)

        eccstats = stats_class.EccStat(ecc, avg_ecc, directed=graph.is_directed(), diameter=diameter, radius=radius )

    return eccstats

# Connectivity statistics of graph

def connect_stats(graph):
    """
    Gathers graph statistics relative to connectivity and returns a ConnectStat object.

    Args:
        graph - an igraph Graph.

    Returns:
        connectstats - a ConnectStat object.

    """
    #Simple connectivity
    if graph.is_directed():
        num_components = len(graph.components(mode='STRONG'))

    else:
        num_components = len(graph.components(mode='WEAK'))

    e_connect = graph.edge_connectivity()
    v_connect = graph.vertex_connectivity(checks=True)

    #Biconnectivity
    num_bi_components = len(graph.biconnected_components())

    connectstats = stats_class.ConnectStat(num_components, e_connect, v_connect, num_bi_components, graph.is_directed())
    return connectstats


# Cluster statistics of the graph

def cluster_stats(graph):
    """
    Gathers graph statistics relative to clusters and returns a ClusterStat object.

    Args:
        graph - an igraph Graph.

    Returns:
        clusterstats - a ClusterStat object.

    """
    num_triangles = len(graph.cliques(min=3, max=3))

    if graph.is_directed():
        num_clusters = len(graph.clusters(mode='STRONG'))
    else :
        num_clusters = len(graph.clusters(mode='WEAK'))

    #Clustering Coefficient : probability that 2 neighbors of a vertex are connected.

    clust_coeffs = graph.transitivity_local_undirected()
    clust_graph = graph.transitivity_undirected()

    clusterstats = stats_class.ClusterStat( num_triangles, num_clusters, clust_coeffs, clust_graph, directed=graph.is_directed())
    return clusterstats

# Centrality statistics of graph

def central_stats(graph):
    """
    Gathers graph statistics relative to centrality and returns a CentralStat object.

    Args:
        graph - an igraph Graph.

    Returns:
        centralstats - a CentralStat object.

    """
    Directed = graph.is_directed()
    # Betweenness centrality

    between = graph.betweenness(directed=Directed)

    # Closeness centrality
    closeness = graph.closeness()
    if Directed:

        in_closeness = graph.closeness(mode='IN')
        out_closeness =  graph.closeness(mode='OUT')
        centralstats = stats_class.CentralStat(closeness=closeness,between=between, directed=Directed, in_closeness=in_closeness, out_closeness=out_closeness)
    else:
        centralstats = stats_class.CentralStat(closeness, between, Directed)

    return centralstats
