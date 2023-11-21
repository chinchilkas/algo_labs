import unittest
import src.main as main

class TestAngryCowsLocation(unittest.TestCase):


    def test_input_1(self):
        cities, gas_storages, pipelines = main.read_file("input_1.txt")
        graph = main.create_gas_pipeline_graph(cities, gas_storages, pipelines)
        result = main.bfs_unreachable_nodes(graph, gas_storages)
        expected_result = {'Г_1': set(['С', 'Б', 'Ч']), 'Г_2': set(['Б']), 'Г_3': set(['Т', 'С', 'Л', 'Ч'])}
        for key, value in expected_result.items():
            self.assertSetEqual(set(result[key]), value)

    def test_input_2(self):
        cities, gas_storages, pipelines = main.read_file("input_2.txt")
        graph = main.create_gas_pipeline_graph(cities, gas_storages, pipelines)
        result = main.bfs_unreachable_nodes(graph, gas_storages)
        expected_result = {'Г_1': set([]), 'Г_2': set(['Д', 'К', 'Т', 'Л']), 'Г_3': set(['С', 'Т', 'К', 'Л'])}
        for key, value in expected_result.items():
            self.assertSetEqual(set(result[key]), value)
