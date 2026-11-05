import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

        self.dvd1 = DigitalVideoDisc(
            "The Lion King", category="Animation"
        )
        self.dvd2 = DigitalVideoDisc(
            "Star Wars", category="Science Fiction"
        )
        self.dvd3 = DigitalVideoDisc(
            "Aladdin", category="Animation"
        )

        self.cart.items = [self.dvd1, self.dvd2, self.dvd3]

    def test_search_by_category(self):
        result = search_by_category(self.cart, "Animation")

        self.assertEqual(result, [self.dvd1, self.dvd3])

    def test_search_by_category_case_insensitive(self):
        result = search_by_category(self.cart, "animation")

        self.assertEqual(result, [self.dvd1, self.dvd3])

    def test_search_by_category_not_found(self):
        result = search_by_category(self.cart, "Horror")

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()