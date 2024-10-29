from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        ss = SpreadSheet()
        ss.set("A1", "1")
        self.assertEqual(1, ss.evaluate("A1"))

    def test_evaluate_invalid_integer(self):
        ss = SpreadSheet()
        ss.set("A1", "1.5")
        self.assertEqual("#Error", ss.evaluate("A1"))

    def test_evaluate_valid_string(self):
        ss = SpreadSheet()
        ss.set("A1", "'Apple'")
        self.assertEqual("Apple", ss.evaluate("A1"))

    def test_evaluate_invalid_string(self):
        ss = SpreadSheet()
        ss.set("A1", "Apple")
        self.assertEqual("#Error", ss.evaluate("A1"))

    def test_formula_evaluate_valid_string(self):
        ss = SpreadSheet()
        ss.set("A1", "='Apple'")
        self.assertEqual("Apple", ss.evaluate("A1"))

    def test_formula_evaluate_valid_integer(self):
        ss = SpreadSheet()
        ss.set("A1", "=1")
        self.assertEqual(1, ss.evaluate("A1"))

    def test_formula_evaluate_invalid_string(self):
        ss = SpreadSheet()
        ss.set("A1", "='Apple")
        self.assertEqual("#Error", ss.evaluate("A1"))
