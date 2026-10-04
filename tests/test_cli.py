import io
import unittest

from calculator.ui.cli import CalculatorCLI


class TestCalculatorCli(unittest.TestCase):
    def setUp(self):
        self.output = io.StringIO()

    def test_cli_with_sliced_expression(self):
        CalculatorCLI(["1", "+", "2"], channel=self.output).run()
        self.assertEqual("3\n", self.output.getvalue())

    def test_cli_with_invalid_expression(self):
        CalculatorCLI(["1", "+"], channel=self.output).run()
        self.assertEqual("Invalid expression: 1 +\n", self.output.getvalue())

    def test_cli_with_single_expression(self):
        CalculatorCLI(["3-2"], channel=self.output).run()
        self.assertEqual("1\n", self.output.getvalue())
