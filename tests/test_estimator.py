import unittest
from src.estimator import avaliar_viabilidade


class TestEstimator(unittest.TestCase):
    def test_pesos_excedem_ram(self):
        self.assertIn("OOM", avaliar_viabilidade(16, 8))

    def test_pesos_cabem(self):
        self.assertIn("cabem", avaliar_viabilidade(4, 8))
