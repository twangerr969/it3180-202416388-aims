import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm 20 DVD đầu tiên: tất cả phải thành công
        for i in range(20):
            dvd = DigitalVideoDisc(title=f"DVD {i + 1}")
            self.assertTrue(cart.add_dvd(dvd))

        self.assertEqual(len(cart.items), 20)

        # DVD thứ 21 phải bị từ chối
        dvd_21 = DigitalVideoDisc(title="DVD 21")
        self.assertFalse(cart.add_dvd(dvd_21))

        self.assertEqual(len(cart.items), 20)

    def test_sort_by_title(self):
        cart = Cart()

        dvd1 = DigitalVideoDisc("Star Wars", cost=24.95)
        dvd2 = DigitalVideoDisc("Aladdin", cost=18.99)
        dvd3 = DigitalVideoDisc("The Lion King", cost=19.95)

        cart.items = [dvd1, dvd2, dvd3]

        cart.sort_by_title()

        expected = ["Aladdin", "Star Wars", "The Lion King"]
        actual = [dvd.title for dvd in cart.items]

        self.assertEqual(actual, expected)

    def test_sort_by_cost(self):
        cart = Cart()

        dvd1 = DigitalVideoDisc("Star Wars", cost=24.95)
        dvd2 = DigitalVideoDisc("Aladdin", cost=18.99)
        dvd3 = DigitalVideoDisc("The Lion King", cost=19.95)

        cart.items = [dvd1, dvd2, dvd3]

        cart.sort_by_cost()

        expected = [18.99, 19.95, 24.95]
        actual = [dvd.cost for dvd in cart.items]

        self.assertEqual(actual, expected)

    def test_sort_empty_cart(self):
        cart = Cart()

        cart.sort_by_title()
        self.assertEqual(cart.items, [])

        cart.sort_by_cost()
        self.assertEqual(cart.items, [])

    def test_sort_single_dvd(self):
        cart = Cart()

        dvd = DigitalVideoDisc("Aladdin", cost=18.99)
        cart.items = [dvd]

        cart.sort_by_title()
        self.assertEqual(cart.items, [dvd])

        cart.sort_by_cost()
        self.assertEqual(cart.items, [dvd])


if __name__ == "__main__":
    unittest.main()
