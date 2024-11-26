import unittest
from Solutions import Solutions

class TestMaximumMagicPathPower(unittest.TestCase):
    def setUp(self):
        self.solutions = Solutions()

    def test_no_edges(self):
        energies = [5]
        edges = []
        maxTime = 10
        self.assertEqual(self.solutions.maximumMagicPathPower(energies, edges, maxTime), 5)

    def test_single_node(self):
        energies = [10]
        edges = []
        maxTime = 0
        self.assertEqual(self.solutions.maximumMagicPathPower(energies, edges, maxTime), 10)

    def test_no_valid_paths(self):
        energies = [1, 2, 3]
        edges = [[0, 1, 5], [1, 2, 5]]
        maxTime = 3
        self.assertEqual(self.solutions.maximumMagicPathPower(energies, edges, maxTime), 1)

    def test_multiple_paths(self):
        energies = [1, 2, 3, 4]
        edges = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [0, 2, 4], [1, 3, 4]]
        maxTime = 6
        self.assertEqual(self.solutions.maximumMagicPathPower(energies, edges, maxTime), 10)

    def test_graph_with_cycles(self):
        energies = [1, 2, 3, 4]
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1]]
        maxTime = 3
        self.assertEqual(self.solutions.maximumMagicPathPower(energies, edges, maxTime), 7)

    def test_max_energy_not_longest_path(self):
        energies = [1, 2, 3, 4, 5]
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [0, 2, 2], [2, 4, 2]]
        maxTime = 4
        self.assertEqual(self.solutions.maximumMagicPathPower(energies, edges, maxTime), 12)

if __name__ == '__main__':
    unittest.main()