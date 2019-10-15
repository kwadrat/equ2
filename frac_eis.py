#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest
from fractions import Fraction


class FracEis:
    def __init__(self, four):
        """
        FracEis:
        """
        (real_num, real_den, omega_num, omega_den) = four
        self.co_real = Fraction(real_num, real_den)
        self.co_omega = Fraction(omega_num, omega_den)

    def __str__(self):
        """
        FracEis:
        """
        return "(%s, %sw)" % (self.co_real, self.co_omega)


class TestFrac(unittest.TestCase):
    def test_four_parts(self):
        """
        TestFrac:
        """
        obj = FracEis(four=(1, 2, 3, 4))
        self.assertEqual(str(obj), "(1/2, 3/4w)")
        obj = FracEis(four=(5, 6, 7, 11))
        self.assertEqual(str(obj), "(5/6, 7/11w)")
