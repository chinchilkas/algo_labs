from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def flood_fill(matrix, coord, replacement_color):
    x, y = coord
    target_color = matrix[x][y]
    def should_add_node(coord, target_color):
        x, y = coord
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == target_color

    G = {coord: coord}

    queue = deque([start_coord])

    while queue:
        current_coord = queue.popleft()
        x, y = current_coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for neighbor in neighbors:
            if should_add_node(neighbor, target_color) and neighbor not in G.keys():
                G.update({current_coord: neighbor})
                G.update({neighbor: neighbors})
                queue.append(neighbor)

    for node in G.keys():
        x, y = node
        matrix[x][y] = replacement_color

    plt.scatter(*zip(*G.keys()), color='r', marker='o')
    plt.show()

def read_file(file_reference):
    with open(file_reference, 'r', encoding="UTF-8") as input_file:
        lines = input_file.read().splitlines()

    start_coord = tuple(map(int, lines[1].split(',')))

    replacement_color_from_file = lines[2][1]

    matrix_with_letters = []
    for line in lines[3:]:
        letters = [char for char in line if char.isalpha()]
        matrix_with_letters.append(letters)

    return matrix_with_letters, start_coord, replacement_color_from_file

def write_file(matrix_with_letters, file_reference):
    with open(file_reference, 'w', encoding="UTF-8") as output_file:
        for row in matrix_with_letters:
            output_file.write('[')
            output_file.write(', '.join(row))
            output_file.write(']' + '\n')

if __name__ == "__main__":
    matrix_from_file, start_coord, replacement_color_from_file = read_file("input.txt")
    flood_fill(matrix_from_file, start_coord, replacement_color_from_file)
    write_file(matrix_from_file, "output.txt")
