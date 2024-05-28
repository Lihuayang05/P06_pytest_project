import pytest
from calculator.calculator import Calculator

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero error")
        return a / b

class TestCalculator:
    def test_add(self):
        # Arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # Act
        result = cal.add(a, b)

        # Assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # Arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # Act
        result = cal.subtract(a, b)

        # Assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # Arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # Act
        result = cal.multiply(a, b)

        # Assert
        expected = 5332114  # Corrected expected value
        assert result == expected

    def test_divide(self):
        # Arrange
        a = 4321
        b = 0  # Dividing by zero
        cal = Calculator()

        # Act & Assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)



