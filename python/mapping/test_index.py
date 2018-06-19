import unittest
from index import color_mark

class TestColorMark(unittest.TestCase):
    def test_color(self):
        self.assertEqual(color_mark(9), ("green", "check"))
        self.assertEqual(color_mark(7), ("orange", "cloud"))
        self.assertEqual(color_mark(4), ("red", "info-sign"))

    def test_error(self):
        self.assertRaises(ValueError, color_mark, -2)

if __name__ == '__main__':
    unittest.main()
