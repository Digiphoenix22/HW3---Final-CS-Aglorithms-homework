
def dfs(matrix, x, y, z, visited):
    """
    Depth-First Search (DFS) to explore connected '1's in the 3D matrix.
    Args:
    matrix (list): 3D matrix representing the clouds and sky.
    x, y, z (int): Current coordinates in the matrix.
    visited (set): Set to keep track of visited coordinates.
    """
    if (x < 0 or x >= len(matrix) or
        y < 0 or y >= len(matrix[0]) or
        z < 0 or z >= len(matrix[0][0]) or
        (x, y, z) in visited or
        matrix[x][y][z] == 0):
        return
    
    # Mark current cell as visited
    visited.add((x, y, z))

    # Explore neighbors (horizontally, vertically, and across layers)
    dfs(matrix, x + 1, y, z, visited)
    dfs(matrix, x - 1, y, z, visited)
    dfs(matrix, x, y + 1, z, visited)
    dfs(matrix, x, y - 1, z, visited)
    dfs(matrix, x, y, z + 1, visited)
    dfs(matrix, x, y, z - 1, visited)


def count_clouds(matrix):
    """
    Count the number of clouds in a 3D matrix.
    Args:
    matrix (list): 3D matrix representing the clouds and sky.
    Returns:
    int: Total number of clouds.
    """
    if not matrix or not matrix[0]:
        return 0

    visited = set()
    cloud_count = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for z in range(len(matrix[0][0])):
                if matrix[x][y][z] == 1 and (x, y, z) not in visited:
                    dfs(matrix, x, y, z, visited)
                    cloud_count += 1

    return cloud_count

# Example usage
if __name__ == "__main__":
    # Example matrices
    example_1 = [[[1, 1, 0], [0, 1, 0], [1, 0, 0]],
                 [[1, 1, 0], [0, 1, 0], [1, 0, 0]]]

    example_2 = [[[1, 0, 0], [0, 1, 0], [1, 0, 0]],
                 [[1, 0, 0], [0, 1, 0], [1, 0, 0]]]

    example_3 = [[[1, 0, 0], [0, 1, 0], [1, 0, 0]],
                 [[1, 0, 0], [0, 0, 0], [1, 0, 0]]]

    # Test the function
    print("Example 1 - Number of clouds:", count_clouds(example_1))
    print("Example 2 - Number of clouds:", count_clouds(example_2))
    print("Example 3 - Number of clouds:", count_clouds(example_3))
