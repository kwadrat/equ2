#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest

class EisNumber:
    def __init__(self):
        '''
        EisNumber:
        '''
        self.part_omega = 0
        self.part_real = 0

class TestNumber(unittest.TestCase):
    def test_create_number(self):
        """
        TestNumber:
        """
        obj = EisNumber()
        self.assertEqual(obj.part_omega, 0)
        self.assertEqual(obj.part_real, 0)
