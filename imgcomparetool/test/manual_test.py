#!/usr/bin/env python

"""manual_test.py: a manual test script for imgcompare package"""

import os, sys
import csv

# Add one folder level up to sys.path
lib_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
sys.path.append(lib_path)
import core

def main():
    
    # Loading and comparing images
    core.stream('test_image_input.csv', 'test_image_output.csv')

if __name__ == '__main__':
    main()