from unittest import result
from day1 import challenge1, challenge2, format_move, format_rotation


import unittest


class TestChallenge1(unittest.TestCase):

    def test_format_rotation(self):
        input_list = ['R5', 'L5']
        result_list = [format_rotation(i) for i in input_list]
        expected_list = [(1, 5), (-1, 5)]
        for r, e in zip(result_list, expected_list):
            self.assertEqual(r, e, 'incorrect rotation')
    
    def test_format_move(self):
        input_list = [(1, 5), (-1, 5)]
        result_list = [format_move(i, 0) for i in input_list]
        expected_list = [((5, 0), 1), ((-5, 0), -1)]
        for r, e in zip(result_list, expected_list):
            self.assertEqual(r, e, 'incorrect rotation')

    def test_challenge1(self):
        input = 'R5, R5, R5, R5'
        result = challenge1(input)
        self.assertEqual(result, 0, 'incorrect number of houses')

    def test_challenge2(self):
        input = 'R5, R5, R5, R5'
        result = challenge2(input)
        self.assertEqual(result, 0, 'incorrect repeated of house')


if __name__ == '__main__':
    unittest.main()
