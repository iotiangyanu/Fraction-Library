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
