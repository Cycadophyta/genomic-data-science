def edit_distance(x, y):
    """Calculate the edit distance between two sequences using a dynamic programming approach with a matrix.
    """
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = i
    # Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            dist_hor = D[i][j-1] + 1
            dist_ver = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                dist_diag = D[i-1][j-1]
            else:
                dist_diag = D[i-1][j-1] + 1
            D[i][j] = min(dist_hor, dist_ver, dist_diag)
    # Edit distance is the value in the bottom right corner of the matrix
    return D[-1][-1]