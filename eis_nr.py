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

class TestNumber(unittest.TestCase):
    def test_create_number(self):
        '''
        TestNumber:
        '''
        obj = EisNumber()
        self.assertEqual(obj.part_real, 0)
        self.assertEqual(obj.part_omega, 0)

    def test_set_parts(self):
        '''
        TestNumber:
        '''
        obj = EisNumber(1, 2)
        self.assertEqual(obj.part_real, 1)
        self.assertEqual(obj.part_omega, 2)

    def test_add_numbers(self):
        '''
        TestNumber:
        '''
        obj_a = EisNumber(10, 20)
        obj_b = EisNumber(3, 4)
        obj_c = obj_a + obj_b
        self.assertEqual(obj_c.part_real, 13)
        self.assertEqual(obj_c.part_omega, 24)
