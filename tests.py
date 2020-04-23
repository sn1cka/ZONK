from unittest import TestCase

from ZONK.zonk_scores_calculator import ScoresCalculator


class ZonkTest(TestCase):
    def setUp(self):
        self.zonk_scores_test_data = [
            [[1, 1, 1, 1, 1, 1], 4000],
            [[6, 6, 6, 6, 6, 6], 2400],
            [[1, 1, 2, 2, 3, 3], 750],
            [[1, 2, 3, 4, 5, 6], 1500],
            [[1, 2, 4, 5, 4, 3], 150],
            [[2, 6, 6, 2, 4, 3], 0],
            [[6, 5, 4, 3, 2, 1], 1500],
            [[2, 3, 3, 2, 4, 3], 300],
            [[2, 4, 4, 2, 4, 3], 400],
            [[5, 6, 5, 5, 4, 3], 500],
            [[6, 6, 6, 5, 1, 3], 750],
            [[3, 3, 3, 2, 4, 3], 600],
            [[5, 5, 5, 5, 5, 1], 1600],
            [[1, 1, 1, 1, 5, 3], 2050],
            [[1, 1, 2, 2, 3, 3], 750],
            [[1, 1, 5, 2, 4, 3], 250],
            [[6, 6, 6, 6, 5, 3], 1250],
            [[5, 5, 5, 5, 1, 3], 1100],
            [[3, 3, 4, 2, 4, 6], 0],
            [[2, 2, 1, 2, 1, 1], 1200],
            [[2, 2, 1], 100]
        ]


    def test_zonk_scores_test_data(self):
        score_calculator = ScoresCalculator()
        for combination, expected_result in self.zonk_scores_test_data:
            actual_result = score_calculator.calculate_points(combination)
            message = "\n %d-й тест в функции get_range_list провален \n ожидалось %d \n получено %s" % (
                self.zonk_scores_test_data.index([combination, expected_result]), expected_result,
                actual_result)
            self.assertEqual(actual_result, expected_result, message)
