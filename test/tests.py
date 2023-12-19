import os
import unittest
import filecmp
import src.main as main

matrix_from_file, start_coord, replacement_color_from_file = main.read_file("lab_4/src/input.txt")
main.flood_fill(matrix_from_file, start_coord, replacement_color_from_file)
main.write_file(matrix_from_file, "output_example.txt")

class TestAngryCowsLocation(unittest.TestCase):
    def compare_files(self, file1, file2):
        return filecmp.cmp(file1, file2)

    def get_project_root(self):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def test_files_are_different(self):
        project_root = self.get_project_root()
        file1_path = os.path.join(project_root, 'src', 'input.txt')
        file3_path = os.path.join(project_root, 'test', 'output_example.txt')

        self.assertFalse(self.compare_files(file1_path, file3_path))
