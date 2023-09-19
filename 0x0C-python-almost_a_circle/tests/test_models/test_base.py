#!/usr/bin/python3
"""Unittests for models/rectangle.py."""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testbaseclass(unittest.TestCase):
    def testcreateclass(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def testprivate(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects


if __name__ == '__main__':
    unittest.main()
