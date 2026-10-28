import unittest

from calculator import (
    estimate_memory_gb,
    check_memory_requirements,
)


class TestMemoryCalculator(unittest.TestCase):

    def test_fp16_model_8b(self):
        self.assertAlmostEqual(
            estimate_memory_gb(8, 16), 16.0
        )

    def test_int4_model_8b(self):
        self.assertAlmostEqual(
            estimate_memory_gb(8, 4), 4.0
        )

    def test_int8_model_7b(self):
        self.assertAlmostEqual(
            estimate_memory_gb(7, 8), 7.0
        )

    def test_invalid_parameter_count(self):
        with self.assertRaises(ValueError):
            estimate_memory_gb(0, 16)

    def test_invalid_precision(self):
        with self.assertRaises(ValueError):
            estimate_memory_gb(8, 3)

    def test_sufficient_memory(self):
        result = check_memory_requirements(4, 5)
        self.assertTrue(result["feasible"])

    def test_insufficient_memory(self):
        result = check_memory_requirements(8, 6)
        self.assertFalse(result["feasible"])


if __name__ == "__main__":
    unittest.main()
