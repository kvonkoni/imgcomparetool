"""manual_test.py: a manual test script for imgcompare package"""

import os, sys
import csv
import unittest

# Add one folder level up to sys.path
lib_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
sys.path.append(lib_path)
import core

def csv_to_tuple_list(input_filename, header=True):
    with open(input_filename) as input_csv:
            csv_reader = csv.reader(input_csv, delimiter=',')
            tuple_list = []
            line_count = 0
            for row in csv_reader:
                if line_count == 0 and header:
                    line_count += 1
                else:
                    tuple_list.append(tuple(row))
                    line_count += 1
    return tuple_list

def tuple_list_to_csv(output_filename, header, tuple_list):
    with open(output_filename, 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(header)
            for element in tuple_list:
                csv_writer.writerow(element)


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
        core.stream('test_image_input.csv', 'test_image_output.csv')

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