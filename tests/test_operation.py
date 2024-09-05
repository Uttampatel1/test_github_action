from src.math_operations import add, subtract, multiply, divide
import unittest

class TestMyFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-4, 5), -20)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertRaises(ValueError, divide, 10, 0)

if __name__ == "__main__":
    unittest.main()
