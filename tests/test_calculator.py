import unittest
from src.calculator import calcular_memoria_gb


class TestCalculator(unittest.TestCase):
    def test_fp16_8b(self):
        self.assertAlmostEqual(calcular_memoria_gb(8, "FP16"), 14.901161, places=4)

    def test_int4_8b(self):
        self.assertAlmostEqual(calcular_memoria_gb(8, "INT4"), 3.725290, places=4)

    def test_precisao_invalida(self):
        with self.assertRaises(ValueError):
            calcular_memoria_gb(8, "FP32")
