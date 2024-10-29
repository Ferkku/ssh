from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        ss = SpreadSheet()
        ss.set("A1", "1")
        self.assertEqual(1, ss.evaluate("A1"))
