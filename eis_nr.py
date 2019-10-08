#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest

class EisNumber:
    def __init__(self, given_omega=None, given_real=None):
        '''
        EisNumber:
        '''
        if given_omega is None:
            given_omega = 0
        self.part_omega = given_omega
        if given_real is None:
            given_real = 0
        self.part_real = given_real

class TestNumber(unittest.TestCase):
    def test_create_number(self):
        '''
        TestNumber:
        '''
        obj = EisNumber()
        self.assertEqual(obj.part_omega, 0)
        self.assertEqual(obj.part_real, 0)

    def test_set_parts(self):
        '''
        TestNumber:
        '''
        obj = EisNumber(1, 2)
        self.assertEqual(obj.part_omega, 1)
        self.assertEqual(obj.part_real, 2)
