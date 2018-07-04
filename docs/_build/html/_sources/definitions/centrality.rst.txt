Centrality
==========

  Measures of **centrality** identify the most *important* vertices in the graph,
  according to certain factors.

Betweenness Centrality
----------------------

  **Betweenness** centrality is a measure of centrality based on shortest paths.
  For a vertex in the graph, it represents the number of shortest paths that
  pass through the vertex.

  .. figure:: images/betweennessCentrality.png
     :scale: 100 %
     :alt: between
     :align: center

     Graph betweenness : higher - red, lower - green

     source : GraphStream



Closeness Centrality
--------------------

  **Closeness** centrality is also a measure of centrality based on shortest paths.
  For a given vertex in a graph, it is the calculated sum of the shortest paths
  between the vertex and all the other vertices of the graph. The more central
  a vertex is, the closer it is to all the others.
