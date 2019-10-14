import unittest
from more_fun_with_collections.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_A_switch_average(self):
        grade = "A"
        score = 100
        result = 100
        self.assertEqual(result, switch_average(grade), score)

    def test_B_switch_average(self):
        grade1 = "B"
        score1 = 90
        result1 = 90
        self.assertEqual(result1, switch_average(grade1), score1)

    def test_C_switch_average(self):
        grade2 = "C"
        score2 = 80
        result2 = 80
        self.assertEqual(result2, switch_average(grade2), score2)
    def test_D_switch_average(self):
        grade3 = "D"
        score3 = 60
        result3 = 60
        self.assertEqual(result3, switch_average(grade3), score3)



if __name__ == '__main__':
    unittest.main()
