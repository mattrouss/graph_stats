Clustering
==========

  A **cluster** (or cluster graph) is a graph formed from the disjoint union
  of complete graphs.

Triangle
--------

  A **triangle** is a triplet of vertices who are all neighbors to each other.
  It can also be seen as a clique of three vertices.

Clustering Coefficient
----------------------

  The **clustering coefficient** is the measure of how vertices in a graph tend
  to cluster together.

  The **global** clustering coefficient is calculated by the number of closed triplets
  of vertices (which corresponds with 3 times the number of triangles),
  over the number of all triplets.

  .. figure:: images/clust_global.svg
     :scale: 200 %
     :alt: global_clust
     :align: center

     source : Wikipedia

  The **local** clustering coefficient of a vertex in a graph quantifies
  how close its neighbors are to being a clique. 
