"""
    Unit test cases for irish lottery draw script.
"""

__author__ = 'me@kartheek.net (Karnati Kartheek)'

import unittest
from datetime import datetime, timedelta
from scripts import irish_lottery_draw

class NextDrawTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_draw_date_for_current_date(self):
        self.assertNotEqual(irish_lottery_draw.next_draw_date(), None)

    def test_draw_date_for_monday(self):
        monday = datetime(2017, 4, 3, 12, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(monday),
            datetime(2017, 4, 5, 20, 0))

    def test_draw_date_for_tuesday(self):
        tuesday = datetime(2017, 4, 4, 12, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(tuesday),
            datetime(2017, 4, 5, 20, 0))

    def test_draw_date_for_wednesday(self):
        wednesday = datetime(2017, 4, 5, 12, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(wednesday),
            datetime(2017, 4, 5, 20, 0))

        # Checking at 8 PM(ie 20 in 24hr clock).
        day = datetime(2017, 4, 5, 20, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(day),
            datetime(2017, 4, 8, 20, 0))

        # Checking at 10 PM(ie 22 in 24hr clock).
        day = datetime(2017, 4, 5, 22, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(day),
            datetime(2017, 4, 8, 20, 0))

    def test_draw_date_for_thursday(self):
        day = datetime(2017, 4, 6, 12, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(day),
            datetime(2017, 4, 8, 20, 0))

    def test_draw_date_for_friday(self):
        friday = datetime(2017, 4, 7, 12, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(friday),
            datetime(2017, 4, 8, 20, 0))

    def test_draw_date_for_saturday(self):
        day = datetime(2017, 4, 8, 12, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(day),
            datetime(2017, 4, 8, 20, 0))

        # Checking at 8 PM(ie 20 in 24hr clock).
        day = datetime(2017, 4, 8, 20, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(day),
            datetime(2017, 4, 12, 20, 0))

        # Checking at 10 PM(ie 22 in 24hr clock).
        day = datetime(2017, 4, 8, 22, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(day),
            datetime(2017, 4, 12, 20, 0))

    def test_draw_date_for_sunday(self):
        day = datetime(2017, 4, 9, 13, 0)
        self.assertEqual(
            irish_lottery_draw.next_draw_date(day),
            datetime(2017, 4, 12, 20, 0))



if __name__ == '__main__':
    unittest.main()
