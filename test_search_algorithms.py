import unittest
import search_algorithms



class Testsearch_algorithms(unittest.TestCase):




    def test_linear_search(self):
        target = 12
        data = [5,6,7,8,9,10,11,12,17,21,25,27,35,37,42,45,50]
        result = search_algorithms.linear_search(data, target)
        self.assertEqual(result, (7,True))

    def test_binary_search_iter(self):
        target = 50
        data = [5,6,7,8,9,10,11,12,17,21,25,27,35,37,42,45,50]
        result = search_algorithms.binary_search_iter(data, target)
        self.assertEqual(result, True)

    def test_binary_search_recur(self):
        target = 300
        data = [5,6,7,8,9,10,11,12,17,21,25,27,35,37,42,45,50]
        result = search_algorithms.binary_search_recur(data, target, 0, len(data)-1)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
