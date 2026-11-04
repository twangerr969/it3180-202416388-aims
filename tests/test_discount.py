import unittest

from aims.discount import calculate_discounted_total


class TestDiscount(unittest.TestCase):

    def test_calculate_discounted_total(self):
        # Giảm 20% của 100: kết quả phải là 80
        self.assertEqual(
            calculate_discounted_total(100, 20),
            80
        )

    def test_invalid_discount_percent(self):
        # Phần trăm giảm giá không được vượt quá 100
        with self.assertRaises(ValueError):
            calculate_discounted_total(100, 150)

    def test_negative_discount_percent(self):
        with self.assertRaises(ValueError):
            calculate_discounted_total(100, -10)


if __name__ == "__main__":
    unittest.main()