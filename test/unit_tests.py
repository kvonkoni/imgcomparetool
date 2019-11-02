"""manual_test.py: a manual test script for imgcompare package"""

import os, sys
import csv
import PIL
import unittest

# Add one folder level up to sys.path
lib_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
sys.path.append(lib_path)

from imgcomparetool import ImageList, csv_to_tuple_list, tuple_list_to_csv

class TestImageCompareTools(unittest.TestCase):

    def test_expected_order(self):

        # Getting the absolute paths of the test images
        expected_order = [
            (os.path.abspath('a01.jpg'), os.path.abspath('a02.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b02.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b03.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b04.jpg')),
            (os.path.abspath('c01.jpg'), os.path.abspath('c02.jpg'))
        ]
    
        # Creating the test input CSV
        tuple_list_to_csv('test_image_input.csv', ['image1', 'image2'], expected_order)

        # Loading and comparing images
        image_list = ImageList('test_image_input.csv')
        image_list.compare('test_image_output.csv')

        # Reading the output CSV
        result = csv_to_tuple_list('test_image_output.csv')
        sorted_result = sorted(result, key=lambda x: x[1])
        result_order = []
        for element in sorted_result:
            result_order.append((element[0], element[1]))
        
        self.assertEqual(expected_order, result_order)

if __name__ == '__main__':
    unittest.main()