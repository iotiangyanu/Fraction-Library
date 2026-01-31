from math import gcd


class Fraction:
    """
    A class to represent a mathematical fraction and support
    arithmetic operations, comparisons, and method chaining.
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Initialize a Fraction object.

        :param numerator: Integer numerator
        :param denominator: Integer denominator (cannot be zero)
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.num = numerator
        self.den = denominator
        self._simplify()

    def _simplify(self):
        """
        Simplifies the fraction using GCD and ensures
        the denominator is always positive.
        """
        g = gcd(self.num, self.den)
        self.num //= g
        self.den //= g

        # Keep denominator positive
        if self.den < 0:
            self.num *= -1
            self.den *= -1

    # -------------------- STRING REPRESENTATION --------------------

    def __str__(self):
        """
        User-friendly string representation.
        """
        return f"{self.num}/{self.den}"

    def __repr__(self):
        """
        Developer-friendly representation.
        """
        return f"Fraction({self.num}, {self.den})"

    # -------------------- ARITHMETIC OPERATIONS --------------------

    def __add__(self, other):
        """
        Add two fractions.
        Supports Fraction + Fraction and Fraction + int.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)

        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __radd__(self, other):
        """
        Support int + Fraction.
        """
        return self + other

    def __sub__(self, other):
        """
        Subtract two fractions.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)

        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __rsub__(self, other):
        """
        Support int - Fraction.
        """
        return Fraction(other, 1) - self

    def __mul__(self, other):
        """
        Multiply two fractions.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)

        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __rmul__(self, other):
        """
        Support int * Fraction.
        """
        return self * other

    def __truediv__(self, other):
        """
        Divide two fractions.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)

        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")

        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    # -------------------- COMPARISON OPERATORS --------------------

    def __eq__(self, other):
        """
        Check equality of two fractions.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)

        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        """
        Check if one fraction is less than another.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)

        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        """
        Check if one fraction is less than or equal to another.
        """
        return self < other or self == other

    # -------------------- UTILITY METHODS --------------------

    def to_decimal(self, precision: int = 5):
        """
        Convert fraction to decimal with given precision.

        :param precision: Number of decimal places
        """
        return round(self.num / self.den, precision)

    @staticmethod
    def from_float(value: float, tolerance: float = 1e-10):
        """
        Convert a float to a Fraction using approximation.

        :param value: Floating-point number
        :param tolerance: Precision tolerance
        """
        den = 1
        while abs(value * den - round(value * den)) > tolerance:
            den *= 10

        num = round(value * den)
        return Fraction(num, den)
