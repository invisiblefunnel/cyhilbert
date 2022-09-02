import random
import unittest

import cyhilbert

# Assume the hilbertcurve package is correct
from hilbertcurve.hilbertcurve import HilbertCurve


class TestHilbert(unittest.TestCase):
    def test_hilbert(self):
        hc = HilbertCurve(cyhilbert.BITS_PER_DIM, cyhilbert.DIMS)

        for _ in range(100_000):
            x = random.randint(0, cyhilbert.MAX)
            y = random.randint(0, cyhilbert.MAX)
            expected = hc.distance_from_point((x, y))
            actual = cyhilbert.hilbert(x, y)
            self.assertEqual(expected, actual)

    def test_hilbert_min_max(self):
        min_max = (0, cyhilbert.MAX)
        hc = HilbertCurve(cyhilbert.BITS_PER_DIM, cyhilbert.DIMS)

        for x in min_max:
            for y in min_max:
                actual = cyhilbert.hilbert(x, y)
                expected = hc.distance_from_point((x, y))
                self.assertEqual(expected, actual)

    def test_hilbert_bad_input(self):
        bad_inputs = (-1, cyhilbert.MAX + 1)

        for x in bad_inputs:
            y = random.randint(0, cyhilbert.MAX)
            with self.assertRaises(AssertionError):
                cyhilbert.hilbert(x, y)

        for y in bad_inputs:
            x = random.randint(0, cyhilbert.MAX)
            with self.assertRaises(AssertionError):
                cyhilbert.hilbert(x, y)
