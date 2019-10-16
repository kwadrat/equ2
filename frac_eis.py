#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest
from fractions import Fraction

verbose_tests = 0


class FracEis:
    def __init__(self, four=None, two=None):
        """
        FracEis:
        """
        if four is not None:
            (real_num, real_den, omega_num, omega_den) = four
            self.co_real = Fraction(real_num, real_den)
            self.co_omega = Fraction(omega_num, omega_den)
        elif two is not None:
            (co_real, co_omega) = two
            self.co_real = co_real
            self.co_omega = co_omega
        else:
            raise RuntimeError(
                "Specify two or four parameters to define Eisenstein fraction"
            )

    def __str__(self):
        """
        FracEis:
        """
        return "FracEis(four=(%d, %d, %d, %d))" % (
            self.co_real.numerator,
            self.co_real.denominator,
            self.co_omega.numerator,
            self.co_omega.denominator,
        )

    def math_view(self):
        """
        FracEis:
        """
        return "(%s, %sw)" % (self.co_real, self.co_omega)

    def __add__(self, other):
        """
        FracEis:
        """
        new_real = self.co_real + other.co_real
        new_omega = self.co_omega + other.co_omega
        return FracEis(two=(new_real, new_omega))

    def __sub__(self, other):
        """
        FracEis:
        """
        new_real = self.co_real - other.co_real
        new_omega = self.co_omega - other.co_omega
        return FracEis(two=(new_real, new_omega))

    def __mul__(self, other):
        """
        FracEis:
        """
        a = self.co_real
        b = self.co_omega
        c = other.co_real
        d = other.co_omega
        tmp_real = a * c - b * d
        tmp_omega = b * c + a * d - b * d
        return FracEis(two=(tmp_real, tmp_omega))

    def norm(self):
        """
        FracEis:
        """
        a = self.co_real
        b = self.co_omega
        value = a * a - a * b + b * b
        return value

    def __eq__(self, other):
        """
        FracEis:
        """
        return self.co_real == other.co_real and self.co_omega == other.co_omega

    def div_mod(self, other):
        """
        FracEis:
        """
        a = self.co_real
        b = self.co_omega
        c = other.co_real
        d = other.co_omega
        bottom = other.norm()
        e = a * c + b * d - a * d
        f = b * c - a * d
        if verbose_tests:
            print()
            tmp_format = "bottom"; print("Eval: %s %s" % (tmp_format, eval(tmp_format)))
            tmp_format = "e"; print("Eval: %s %s" % (tmp_format, eval(tmp_format)))
            tmp_format = "f"; print("Eval: %s %s" % (tmp_format, eval(tmp_format)))
        g, h = divmod(e, bottom)
        i, j = divmod(f, bottom)
        result = (FracEis(two=(g, i)), FracEis(two=(h, j)))
        return result

    def __repr__(self):
        """
        FracEis:
        """
        return str(self)


class TestFrac(unittest.TestCase):
    def test_four_parts(self):
        """
        TestFrac:
        """
        obj = FracEis(four=(1, 2, 3, 4))
        self.assertEqual(str(obj), "FracEis(four=(1, 2, 3, 4))")
        obj = FracEis(four=(5, 6, 7, 11))
        self.assertEqual(str(obj), "FracEis(four=(5, 6, 7, 11))")

    def test_two_parts(self):
        """
        TestFrac:
        """
        a = Fraction(12, 13)
        b = Fraction(-17, 19)
        c = FracEis(two=(a, b))
        self.assertEqual(str(c), "FracEis(four=(12, 13, -17, 19))")

    def test_add_values(self):
        """
        TestFrac:
        """
        a = FracEis(four=(1, 2, 3, 4))
        b = FracEis(four=(1, 3, 3, 4))
        c = a + b
        self.assertEqual(str(c), "FracEis(four=(5, 6, 3, 2))")

    def test_substract_values(self):
        """
        TestFrac:
        """
        a = FracEis(four=(1, 2, 3, 4))
        b = FracEis(four=(1, 3, 3, 4))
        c = a - b
        self.assertEqual(str(c), "FracEis(four=(1, 6, 0, 1))")

    def test_multiply_values(self):
        """
        TestFrac:
        """
        a = FracEis(four=(1, 2, 3, 5))
        b = FracEis(four=(7, 11, 13, 17))
        c = a * b
        self.assertEqual(c.math_view(), "(-263/1870, 571/1870w)")
        self.assertEqual(str(c), "FracEis(four=(-263, 1870, 571, 1870))")
        self.assertEqual(repr(c), "FracEis(four=(-263, 1870, 571, 1870))")

    def test_no_arguments(self):
        """
        TestFrac:
        """
        self.assertRaises(RuntimeError, FracEis)

    def test_norm(self):
        """
        TestFrac:
        """
        obj_a = FracEis(four=(1, 1, 1, 1))
        self.assertEqual(obj_a.norm(), 1)
        obj_a = FracEis(four=(1, 1, 1, 2))
        self.assertEqual(obj_a.norm(), Fraction(3, 4))

    def test_compare_values(self):
        """
        TestFrac:
        """
        obj_a = FracEis(four=(2, 4, 2, 3))
        obj_b = FracEis(four=(1, 2, 6, 9))
        self.assertEqual(obj_a == obj_b, True)

    def test_div_mod(self):
        """
        TestFrac:
        """
        obj_a = FracEis(four=(2, 1, 3, 1))
        obj_b = FracEis(four=(1, 1, 0, 1))
        obj_c, obj_d = obj_a.div_mod(obj_b)
        self.assertEqual(obj_c, FracEis(four=(2, 1, 3, 1)))
        self.assertEqual(obj_d, FracEis(four=(0, 1, 0, 1)))
