#!/usr/bin/env python

"""manual_test.py: a manual test script for imgcompare package"""

import os, sys
import csv

# Add one folder level up to sys.path
lib_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
sys.path.append(lib_path)

from imgcomparetool import ImageList, tuple_list_to_csv

def main():

    # Getting the absolute paths of the test images
    file_pair_list = [
        (os.path.abspath('a01.jpg'), os.path.abspath('a02.jpg')),
        (os.path.abspath('b01.jpg'), os.path.abspath('b02.jpg')),
        (os.path.abspath('b01.jpg'), os.path.abspath('b03.jpg')),
        (os.path.abspath('b01.jpg'), os.path.abspath('b04.jpg')),
        (os.path.abspath('c01.jpg'), os.path.abspath('c02.jpg'))
    ]
    
    # Creating the test input CSV
    tuple_list_to_csv('test_image_input.csv', ['image1', 'image2'], file_pair_list)
    
    # Loading and comparing images
    image_list = ImageList('test_image_input.csv')
    image_list.compare('test_image_output.csv')

if __name__ == '__main__':
    main()