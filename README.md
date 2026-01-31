# Fraction Library

A lightweight and feature-rich Python library that provides a `Fraction` class for
performing **exact arithmetic on rational numbers** using **operator overloading** and
**method chaining**.

This library is designed to demonstrate clean object-oriented design, Python magic
methods, and mathematical correctness, making it suitable for learning, interviews,
and small-scale production use.

---

## ✨ Key Features

- Exact arithmetic with fractions (no floating-point precision loss)
- Supports addition, subtraction, multiplication, and division
- Method chaining support: `(f1 + f2) * f3 - 1`
- Automatic fraction simplification using `math.gcd()`
- Comparison operators (`==`, `<`, `<=`, `>`, `>=`)
- Supports operations with integers (`Fraction + int`, `int + Fraction`)
- Safe error handling for zero denominators and division by zero
- Conversion utilities:
  - Fraction → decimal
  - Float → Fraction
- Clean string (`__str__`) and developer (`__repr__`) representations

---

## 📦 Installation

Clone the repository and install the library in editable mode:

```bash
git clone https://github.com/USERNAME/fraction-library.git
cd fraction-library
pip install -e .
---

## 🚀 Usage Examples

### Creating Fractions
```python
from fraction import Fraction

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f1)   # 1/2
print(f2)   # 3/4

print(f1 + f2)   # 5/4
print(f1 - f2)   # -1/4
print(f1 * f2)   # 3/8
print(f1 / f2)   # 2/3


result = (Fraction(1, 2) + Fraction(2, 3)) * Fraction(3, 4) - 1
print(result)    # -1/8

f = Fraction(1, 2)

print(f + 1)     # 3/2
print(2 - f)     # 3/2
print(f * 3)     # 3/2
print(1 / f)     # 2/1

Fraction(1, 2) == Fraction(2, 4)   # True
Fraction(1, 3) < Fraction(1, 2)    # True
Fraction(3, 2) > 1                 # True


f = Fraction(2, 3)
print(f.to_decimal())              # 0.66667
print(f.to_decimal(precision=3))   # 0.667

f = Fraction.from_float(0.75)
print(f)                            # 3/4


Fraction(1, 0)     # Raises ValueError
Fraction(1, 2) / 0 # Raises ZeroDivisionError

---
