#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest

class EisNumber:
    def __init__(self, given_real=None, given_omega=None):
        '''
        EisNumber:
        '''
        if given_real is None:
            given_real = 0
        self.part_real = given_real
        if given_omega is None:
            given_omega = 0
        self.part_omega = given_omega

    def __add__(self, other):
        '''
        EisNumber:
        '''
        tmp_real = self.part_real + other.part_real
        tmp_omega = self.part_omega + other.part_omega
        return EisNumber(tmp_real, tmp_omega)

    def __sub__(self, other):
        '''
        EisNumber:
        '''
        tmp_real = self.part_real - other.part_real
        tmp_omega = self.part_omega - other.part_omega
        return EisNumber(tmp_real, tmp_omega)

    def __mul__(self, other):
        '''
        EisNumber:
        '''
        a = self.part_real
        b = self.part_omega
        c = other.part_real
        d = other.part_omega
        tmp_real = a * c - b * d
        tmp_omega = b * c + a * d - b * d
        return EisNumber(tmp_real, tmp_omega)

    def __eq__(self, other):
        '''
        EisNumber:
        '''
        return (
            self.part_real == other.part_real and
            self.part_omega == other.part_omega
            )

    def __repr__(self):
        '''
        EisNumber:
        '''
        return (
            'EisNumber(%d, %d)' % (self.part_real, self.part_omega)
            )

    def mouse(self):
        '''
        EisNumber:
        '''
        a = self.part_real
        b = self.part_omega
        if 1:
            ##############################################################################
            value = a * a - a * b + b * b
            ##############################################################################
        else:
            ##############################################################################
            if b:
                value = b ** 2
            else:
                value = a ** 2
            ##############################################################################
        return value


class TestNumber(unittest.TestCase):
    def test_create_number(self):
        '''
        TestNumber:
        '''
        obj = EisNumber()
        self.assertEqual(obj, EisNumber(0, 0))

    def test_set_parts(self):
        '''
        TestNumber:
        '''
        obj = EisNumber(1, 2)
        self.assertEqual(obj, EisNumber(1, 2))

    def test_add_numbers(self):
        '''
        TestNumber:
        '''
        obj_a = EisNumber(10, 20)
        obj_b = EisNumber(3, 4)
        obj_c = obj_a + obj_b
        self.assertEqual(obj_c, EisNumber(13, 24))

    def test_substract_numbers(self):
        '''
        TestNumber:
        '''
        obj_a = EisNumber(10, 20)
        obj_b = EisNumber(3, 4)
        obj_c = obj_a - obj_b
        self.assertEqual(obj_c, EisNumber(7, 16))

    def test_multiply_by_zero(self):
        '''
        TestNumber:
        '''
        obj_a = EisNumber(1, 2)
        obj_b = EisNumber()
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(0, 0))

    def test_multiply_by_three(self):
        '''
        TestNumber:
        '''
        obj_a = EisNumber(2, 3)
        obj_b = EisNumber(5)
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(10, 15))

    def test_multiply_by_omega(self):
        '''
        TestNumber:
        '''
        obj_a = EisNumber(1, 0)
        obj_b = EisNumber(0, 1)
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(0, 1))

    def test_omega_by_omega(self):
        '''
        TestNumber:
        '''
        obj_a = EisNumber(0, 1)
        obj_b = EisNumber(0, 1)
        obj_c = obj_a * obj_b
        self.assertEqual(obj_c, EisNumber(-1, -1))

    def test_real_only(self):
        '''
        TestNumber:
        '''
        obj = EisNumber(2, 0)
        self.assertEqual(obj.mouse(), 4)
        obj_b = EisNumber(3, 0)
        self.assertEqual(obj_b.mouse(), 9)
        obj_c = EisNumber(0, 5)
        self.assertEqual(obj_c.mouse(), 25)
        obj_d = EisNumber(0, 7)
        self.assertEqual(obj_d.mouse(), 49)
        obj_e = EisNumber(2, 3)
        self.assertEqual(obj_e.mouse(), 7)
