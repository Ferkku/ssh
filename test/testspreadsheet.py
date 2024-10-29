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

    def test_formula_evaluate_valid_with_reference(self):
        ss = SpreadSheet()
        ss.set("A1", "=B1")
        ss.set("B1", "42")
        self.assertEqual(42, ss.evaluate("A1"))

    def test_formula_evaluate_invalid_with_reference(self):
        ss = SpreadSheet()
        ss.set("A1", "=B1")
        ss.set("B1", "42.5")
        self.assertEqual("#Error", ss.evaluate("A1"))

    def test_formula_evaluate_circular_reference(self):
        ss = SpreadSheet()
        ss.set("A1", "=B1")
        ss.set("B1", "=A1")
        self.assertEqual("#Circular", ss.evaluate("A1"))

    def test_formula_evaluate_valid_arithmetic(self):
        ss = SpreadSheet()
        ss.set("A1", "=1+3")
        self.assertEqual(4, ss.evaluate("A1"))

    def test_formula_evaluate_invalid_arithmetic(self):
        ss = SpreadSheet()
        ss.set("A1", "=1+3.5")
        self.assertEqual("#Error", ss.evaluate("A1"))

    def test_formula_evaluate_division_by_zero(self):
        ss = SpreadSheet()
        ss.set("A1", "=1/0")
        self.assertEqual("#Error", ss.evaluate("A1"))