import unittest

from te5t9527.graphviz import generate_graph


class TestGraphviz(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_graph(self):
        generate_graph()
