#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from frac_eis import FracEis

verbose_tests = 0


class EisNumber(FracEis):
    def __init__(self, given_real=None, given_omega=None):
        """
        EisNumber:
        """
        if given_real is None:
            given_real = 0
        if given_omega is None:
            given_omega = 0
        super(EisNumber, self).__init__(four=(given_real, 1, given_omega, 1))


class TestNumber(unittest.TestCase):
    def test_create_number(self):
        """
        TestNumber:
        """
        obj = EisNumber()
        self.assertEqual(obj, EisNumber(0, 0))

    def test_set_parts(self):
        """
        TestNumber:
        """
        obj = EisNumber(1, 2)
        self.assertEqual(obj, EisNumber(1, 2))

    def test_add_numbers(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(10, 20)
        obj_b = EisNumber(3, 4)
        obj_c = obj_a + obj_b
        self.assertEqual(obj_c, EisNumber(13, 24))

    def test_substract_numbers(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(10, 20)
        obj_b = EisNumber(3, 4)
        obj_c = obj_a - obj_b
        self.assertEqual(obj_c, EisNumber(7, 16))

    def test_multiply_by_zero(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(1, 2)
        obj_b = EisNumber()
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(0, 0))

    def test_multiply_by_three(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(2, 3)
        obj_b = EisNumber(5)
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(10, 15))

    def test_multiply_by_omega(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(1, 0)
        obj_b = EisNumber(0, 1)
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(0, 1))

    def test_omega_by_omega(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(0, 1)
        obj_b = EisNumber(0, 1)
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(-1, -1))

    def test_real_only(self):
        """
        TestNumber:
        """
        obj = EisNumber(2, 0)
        self.assertEqual(obj.norm(), 4)
        obj_b = EisNumber(3, 0)
        self.assertEqual(obj_b.norm(), 9)
        obj_c = EisNumber(0, 5)
        self.assertEqual(obj_c.norm(), 25)
        obj_d = EisNumber(0, 7)
        self.assertEqual(obj_d.norm(), 49)
        obj_e = EisNumber(2, 3)
        self.assertEqual(obj_e.norm(), 7)

    def test_div_mod(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(2, 3)
        obj_b = EisNumber(1, 0)
        obj_c = obj_a / obj_b
        self.assertEqual(obj_c, EisNumber(2, 3))

    def test_rest_from_div_mod(self):
        """
        TestNumber:
        """
        a = EisNumber(4, 1)
        b = EisNumber(3, 1)
        d = a * b
        e = d / a
        self.assertEqual(e, EisNumber(3, 1))

    def test_conj(self):
        """
        TestNumber:
        """
        obj_a = EisNumber(2, 0)
        self.assertEqual(obj_a.conjugate(), EisNumber(2, 0))
        obj_b = EisNumber(0, 1)
        self.assertEqual(obj_b.conjugate(), EisNumber(-1, -1))
        obj_c = EisNumber(0, -1)
        self.assertEqual(obj_c.conjugate(), EisNumber(1, 1))
        obj_d = EisNumber(0, -2)
        self.assertEqual(obj_d.conjugate(), EisNumber(2, 2))
        obj_e = EisNumber(0, -3)
        self.assertEqual(obj_e.conjugate(), EisNumber(3, 3))
        obj_f = EisNumber(0, 2)
        self.assertEqual(obj_f.conjugate(), EisNumber(-2, -2))
        obj_f = EisNumber(2, 2)
        self.assertEqual(obj_f.conjugate(), EisNumber(0, -2))
