#!/usr/bin/python3
"""Unittests for models/rectangle.py."""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestFirstRectangle(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""
    def test_create_rectangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(3, 2, 4, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 4)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 3)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_get_set(self):
        r = Rectangle(4, 2)
        self.assertEqual(r.width, 4)
        r.width = 9
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 2)
        r.height = 8
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 0)
        r.x = 8
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 0)
        r.y = 1
        self.assertEqual(r.y, 1)
        r.id = 99
        self.assertEqual(r.id, 99)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("i", 2)

        with self.assertRaises(TypeError):
            r = Rectangle([2, 4], 2)

        with self.assertRaises(TypeError):
            r = Rectangle((3, 1), 4)

        with self.assertRaises(TypeError):
            r = Rectangle({'e': 3}, 5)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 6)

        with self.assertRaises(ValueError):
            r = Rectangle(-2, 8)

        with self.assertRaises(TypeError):
            r = Rectangle(0.5, 9)

    def test_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, "i")

        with self.assertRaises(ValueError):
            r = Rectangle(5, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(8, -2)

        with self.assertRaises(TypeError):
            r = Rectangle(9, 0.5)

    def test_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, "i")

        with self.assertRaises(ValueError):
            r = Rectangle(8, 2, -2)

        with self.assertRaises(TypeError):
            r = Rectangle(9, 2, 0.5)

    def test_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 2, "i")

        with self.assertRaises(ValueError):
            r = Rectangle(8, 2, 2, -2)

        with self.assertRaises(TypeError):
            r = Rectangle(9, 2, 2, 0.5)


if __name__ == "__main__":
    unittest.main()
