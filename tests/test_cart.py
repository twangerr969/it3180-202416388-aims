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


if __name__ == "__main__":
    unittest.main()