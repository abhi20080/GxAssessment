import unittest

import sys

sys.path.append("../")

from main import find_closest_match


class TestPhraseSimilarity(unittest.TestCase):

    def test_find_closest_match(self):
        test_phrase = "example phrase"
        result = find_closest_match(test_phrase)
        self.assertIsNotNone(result["closest_match"])
        self.assertGreaterEqual(float(result["distance"]), 0)


# python -m unittest unit_tests/test.py