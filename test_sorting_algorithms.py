import unittest
import sorting_algorithms

class Testsorting_algorithms(unittest.TestCase):
    """docstring for TestSorting_algorithms."""


    def test_ins_sort(self):
        a = [12,3,11,14,5,7,9,4,5]
        result = sorting_algorithms.ins_sort(a)
        c_result = [3, 4, 5, 5, 7, 9, 11, 12, 14]
        self.assertEqual(result,c_result)

    def test_ins_sort2(self):
        a = [12,3,11,14,5,7,9,4,5]
        result_is2 = sorting_algorithms.ins_sort2([12,3,11,14,5,7,9,4,5])
        c_result_is2 = [3, 4, 5, 5, 7, 9, 11, 12, 14]
        self.assertEqual(result_is2,c_result_is2)

    #
    # def test_ins_sort3(self):
    #     a = [12,3,11,14,5,7,9,4,5]
    #     result = sorting_algorithms.ins_sort3(a)
    #     c_result = [3, 4, 5, 5, 7, 9, 11, 12, 14]
    #     self.assertEqual(result,c_result)

    def test_sel_sort(self):
        a = [12,3,11,14,5,7,9,4,5]
        result_ss = sorting_algorithms.sel_sort(a)
        c_result_ss = [3, 4, 5, 5, 7, 9, 11, 12, 14]
        self.assertEqual(result_ss,c_result_ss)



    def test_bub_sort(self):
        a = [12,3,11,14,5,7,9,4,5]
        result_bs = sorting_algorithms.bub_sort(a)
        c_result_bs = [3, 4, 5, 5, 7, 9, 11, 12, 14]
        self.assertEqual(result_bs,c_result_bs)




if __name__ == '__main__':
    unittest.main()
