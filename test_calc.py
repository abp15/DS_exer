import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,15)
        self.assertEqual(result, 25)
        self.assertEqual(calc.add(-1,-1), -2)
        self.assertEqual(calc.add(-1,1), 0)

    def test_subtract(self):
        result = calc.subtract(10,15)
        self.assertEqual(result, -5)
        self.assertEqual(calc.subtract(-1,-1), 0)
        self.assertEqual(calc.subtract(-1,1), -2)

    def test_multiply(self):
        result = calc.multiply(10,15)
        self.assertEqual(result, 150)
        self.assertEqual(calc.multiply(-1,-1), 1)
        self.assertEqual(calc.multiply(-1,1), -1)

    def test_divide(self):
        result = calc.divide(10,5)
        self.assertEqual(result, 2)
        self.assertEqual(calc.divide(-1,-1), 1)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(5,2), 2.5)
        #with self.assert(ValueError):
        #calc.divide(10,0)

if __name__ == '__main__':
    unittest.main()
