#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest
from fractions import Fraction


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


class TestFrac(unittest.TestCase):
    def test_four_parts(self):
        """
        TestFrac:
        """
        obj = FracEis(four=(1, 2, 3, 4))
        self.assertEqual(str(obj), "(1/2, 3/4w)")
        obj = FracEis(four=(5, 6, 7, 11))
        self.assertEqual(str(obj), "(5/6, 7/11w)")

    def test_two_parts(self):
        """
        TestFrac:
        """
        a = Fraction(12, 13)
        b = Fraction(17, 19)
        c = FracEis(two=(a, b))
        self.assertEqual(str(c), "(12/13, 17/19w)")

    def test_add_values(self):
        """
        TestFrac:
        """
        a = FracEis(four=(1, 2, 3, 4))
        b = FracEis(four=(1, 3, 3, 4))
        c = a + b
        self.assertEqual(str(c), "(5/6, 3/2w)")

    def test_substract_values(self):
        """
        TestFrac:
        """
        a = FracEis(four=(1, 2, 3, 4))
        b = FracEis(four=(1, 3, 3, 4))
        c = a - b
        self.assertEqual(str(c), "(1/6, 0w)")

    def test_multiply_values(self):
        """
        TestFrac:
        """
        a = FracEis(four=(1, 2, 3, 5))
        b = FracEis(four=(7, 11, 13, 17))
        c = a * b
        self.assertEqual(str(c), "(-263/1870, 571/1870w)")

    def test_no_arguments(self):
        """
        TestFrac:
        """
        self.assertRaises(RuntimeError, FracEis)
