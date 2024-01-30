import unittest
from triangle import classify_triangle


class TestTriangleClassification(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a triangle")

    def test_large_numbers(self):
        self.assertEqual(classify_triangle(300, 400, 500), "Scalene and Right")

    def test_one_side_zero(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Not a triangle")

    def test_negative_side_length(self):
        self.assertEqual(classify_triangle(-2, 3, 4), "Not a triangle")


if __name__ == '__main__':
    unittest.main()
