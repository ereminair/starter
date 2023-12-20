import unittest
from rectangle import area , perimeter



class MyTestCase(unittest.TestCase):

    def test_normaly_rectangle_area(self):
        data = area(20 , 5)
        self.assertEqual(data , 100)

    def test_zero_rectangle_area(self):
        data = area(0 , 100)
        self.assertEqual(data , 0)

    def test_string_rectangle_area(self):
        try:
            data = area('20' , "5")
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : string")

    def test_negative_rectangle_area(self):
        try:
            data = area(25 , 5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , 125)

    def test_string_and_int_rectangle_area(self):
        try:
            data = area(20 , 5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , 100)

    def test_not_all_elem_rectangle_area(self):
        try:
            data = area(20)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : not all elements")

    def test_normaly_rectangle_perimeter(self):
        data = perimeter(20 , 5)
        self.assertEqual(data , 50)

    def test_zero_rectangle_perimeter(self):
        data = perimeter(0 , 50)
        self.assertEqual(data , 100)

    def test_string_rectangle_perimeter(self):
        try:
            data = perimeter(30, 2)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, 64)

    def test_negative_rectangle_perimeter(self):
        try:
            data = perimeter(26, 5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, 62)

    def test_string_and_int_rectangle_perimeter(self):
        try:
            data = perimeter("20" , 5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : cannot calculate string and int")

    def test_not_all_elem_rectangle_perimeter(self):
        try:
            data = perimeter(20)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : not all elements")




