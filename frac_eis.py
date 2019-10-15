#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest


class FracEis:
    def __init__(self, four):
        """
        FracEis:
        """
        (self.real_num, self.real_den, self.omega_num, self.omega_den) = four

    def __str__(self):
        """
        FracEis:
        """
        return "(%(real_num)d/%(real_den)d, %(omega_num)d/%(omega_den)dw)" % dict(
            real_num=self.real_num,
            real_den=self.real_den,
            omega_num=self.omega_num,
            omega_den=self.omega_den,
        )


class TestFrac(unittest.TestCase):
    def test_four_parts(self):
        """
        TestFrac:
        """
        obj = FracEis(four=(1, 2, 3, 4))
        self.assertEqual(str(obj), "(1/2, 3/4w)")
        obj = FracEis(four=(5, 6, 7, 11))
        self.assertEqual(str(obj), "(5/6, 7/11w)")
