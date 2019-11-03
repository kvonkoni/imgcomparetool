"""manual_test.py: a manual test script for imgcompare package"""

import os, sys
import csv
import unittest

from imgcomparetool import ImageList, csv_to_tuple_list, tuple_list_to_csv

class TestImageCompareTools(unittest.TestCase):

    def test_expected_order(self):

        # Getting the absolute paths of the test images, and
        # setting the expected similarity order
        expected_order = [
            (os.path.abspath('a01.jpg'), os.path.abspath('a02.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b02.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b03.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b04.jpg')),
            (os.path.abspath('c01.jpg'), os.path.abspath('c02.jpg'))
        ]

        # Setting an initial order that is different from 
        # the expected order
        load_order = [
            (os.path.abspath('c01.jpg'), os.path.abspath('c02.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b02.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b03.jpg')),
            (os.path.abspath('b01.jpg'), os.path.abspath('b04.jpg')),
            (os.path.abspath('a01.jpg'), os.path.abspath('a02.jpg'))
        ]
    
        # Creating the test input CSV
        tuple_list_to_csv('test_image_input.csv', ['image1', 'image2'], load_order)

        # Loading and comparing images
        image_list = ImageList('test_image_input.csv')
        image_list.compare('test_image_output.csv')

        # Reading the output CSV
        result = csv_to_tuple_list('test_image_output.csv')
        sorted_result = sorted(result, key=lambda x: x[2])
        result_order = []
        for element in sorted_result:
            result_order.append((element[0], element[1]))
        
        # Assert that the resulting order matches the expected order
        self.assertEqual(expected_order, result_order)

if __name__ == '__main__':
    unittest.main()