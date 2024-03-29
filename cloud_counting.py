
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

def input_3d_matrix():
    """
    Allows the user to input a 3D matrix.
    Returns:
    list: The input 3D matrix.
    """
    layers = int(input("Enter the number of layers: "))
    rows = int(input("Enter the number of rows per layer: "))
    cols = int(input("Enter the number of columns per layer: "))

    matrix = []
    for layer in range(layers):
        print(f"Layer {layer + 1}:")
        current_layer = []
        for row in range(rows):
            current_row = list(map(int, input(f"Enter row {row + 1} with {cols} elements (0 or 1), separated by space: ").strip().split()))
            assert len(current_row) == cols, "Incorrect number of elements in the row."
            current_layer.append(current_row)
        matrix.append(current_layer)

    return matrix

# Example usage
if __name__ == "__main__":
    user_matrix = input_3d_matrix()
    print("Number of clouds:", count_clouds(user_matrix))
