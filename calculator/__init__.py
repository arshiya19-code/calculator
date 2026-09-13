Number = int | float


class Calculator:

    def __init__(self):
        self.expression = ""
        self.last_result: Number | None = None

    def _ensure_is_digit(self, value: int | str):
        if isinstance(value, str):
            value = int(value)
        if value not in range(10):
            raise ValueError("Value must a digit in [0, 9]: " + str(value))
        return value

    def _append(self, value):
        self.expression += str(value)

    def digit(self, value: int | str):
        value = self._ensure_is_digit(value)
        self._append(value)

    def plus(self):
        self._append("+")

    def minus(self):
        self._append("-")

    def multiply(self):
        self._append("*")

    def divide(self):
        self._append("/")

    def dot(self):
        self._append(".")

    def clear(self):
        self.expression = ""
        self.last_result = None

    def open_parenthesis(self):
        self._append("(")

    def close_parenthesis(self):
        self._append(")")

    def percent(self):
        self._append("/100")

    def compute_result(self) -> Number:
        try:
            import math
            result = eval(self.expression, math.__dict__)

            if not isinstance(result, (int, float)):
                raise ValueError("Result is not a number: " + str(result))

            self.last_result = result
            self.expression = str(result)
            return result

        except Exception as e:
            expression = self.expression
            self.expression = ""
            self.last_result = None
            raise ValueError("Invalid expression: " + expression) from e
