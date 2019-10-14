import unittest
from more_fun_with_collections.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_A_switch_average(self):
        grade = "A"
        score = 100
        result = 1001
        self.assertEqual(result, switch_average(grade), score)

    def test_B_switch_average(self):
        grade1 = "B"
        score1 = 90
        result1 = 90
        self.assertEqual(result1, switch_average(grade1), score1)


if __name__ == '__main__':
    unittest.main()
