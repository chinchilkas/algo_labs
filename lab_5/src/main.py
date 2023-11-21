from collections import deque
import re

def read_file(file_reference):
    with open(file_reference, 'r', encoding="UTF-8") as input_file:
        lines = input_file.read().splitlines()

    cities = lines[0].split(', ')
    gas_storages = lines[1].split(', ')

    pipelines = []

    line = lines[2]
    line = line[1:-1]
    matches = re.findall(r'\[.*?\]', line)

    for match in matches:
        pipelines.append(match[1:-1].split(","))

    return cities, gas_storages, pipelines

def create_gas_pipeline_graph(cities, gas_storages, pipelines):
    graph = {}

    for city in cities + gas_storages:
        graph[city] = []

    for pipeline in pipelines:
        start, end = pipeline
        graph[start].append(end)

    return graph

def bfs_unreachable_nodes(graph, gas_storages):
    unreachable_nodes = {}

    for gas_storage in gas_storages:
        start_node, other_gas_storages = gas_storage, [g for g in gas_storages if g != gas_storage]
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        unreachable_from_start = set(graph.keys()) - {start_node}

        while queue:
            current_node = queue.popleft()

            for neighbor in graph[current_node]:
                if neighbor not in visited and neighbor not in other_gas_storages:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    unreachable_from_start.discard(neighbor)

        unreachable_from_start.discard(start_node)
        unreachable_nodes[start_node] = list(unreachable_from_start - set(gas_storages))

    return unreachable_nodes


if __name__ == '__main__':
    file_cities, file_gas_storages, file_pipelines = read_file('src\input.txt')
    graph = create_gas_pipeline_graph(file_cities, file_gas_storages, file_pipelines)
    result = bfs_unreachable_nodes(graph, file_gas_storages)
    print(result)
