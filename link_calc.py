import numpy as np

def calculate_links(adj):
    """ Calculates the Link Matric acording to Eq. (10) 
    Args:
    adj: N by N adjacency matrix representing neighbourhood information

    Returns:
    link_matrix: N by N matrix where (i, j) contains the number of mutual neighbours between particles i and j
    """

    link_matrix = np.zeros(adj.shape)

    # brute force O(N^3) approach, try to optimise
    N = adj.shape[0]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                link_matrix[i][j] += (adj[i][k] * adj[k][i]) # Eq. 10

    return link_matrix

def find_best_neighbour(link_matrix):
    """ Finds the most influential neighbour for every particle
    N = Number of particles.
    Args:
    adj: N by N matrix where (i, j) contains the number of mutual neighbours between particles i and j

    Returns:
    N  by 1 vector with best neighbour for every particle.
    """
    
    best = np.zeros(link_matrix.shape[0])

    # Test if axis=0 is really required??? Remove otherwise

    for i in range(link_matrix.shape[0]):
        best_i = np.argmax(link_matrix[i], axis=0) # find the maximum along the row and return it's index
        best[i] = best_i

    return best
