import unittest
import string_match


class TestStringMatch(unittest.TestCase):

    def setUp(self):
        self.pattern = "ABRACADABRA"
        self.pattern_begin = "HOCUS"
        self.pattern_not_found = "RABB"
        self.text = "HOCUSPOCUSABRABRACADABRA"

        print(string_match.compute_failure("abcab"))

    def test_number_search(self):
        text = "31415926535897932384626433832795028841971"
        pattern = "2384"
        self.assertEqual(16, string_match.number_search(text, pattern))

    def test_compute_failure(self):
        self.assertEqual([-1, 0, 0, 0, 1, 0, 1, 0, 1, 2, 3], string_match.compute_failure(self.pattern))

    def test_compute_opt_failure(self):
        self.assertEqual([-1, 0, 0, -1, 1, -1, 1, -1, 0, 0, -1], string_match.compute_opt_failure(self.pattern))

    def test_knuth_morris_pratt(self):
        self.assertEqual(13, string_match.knuth_morris_pratt(self.text, self.pattern))
        self.assertEqual(0, string_match.knuth_morris_pratt(self.text, self.pattern_begin))
        self.assertEqual(-1, string_match.knuth_morris_pratt(self.text, self.pattern_not_found))
