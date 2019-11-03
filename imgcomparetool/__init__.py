#!/usr/bin/env python

"""imgcomparetool.py: a python package to measure the similarity of a list of image pairs."""

import os, sys

from PIL import Image
import csv
import time
import imagehash

class ImageList(object):

    """A list of image objects"""

    def __init__(self, input_filename):
        # Reading the image list CSV on init
        filename_pair_list = csv_to_tuple_list(input_filename)
        
        # Created Pillow image instances based on list
        image_pair_list = []
        for pair in filename_pair_list:
            file1, file2 = interpret_filepath(pair[0]), interpret_filepath(pair[1])
            image_pair_list.append((Image.open(file1), Image.open(file2)))
        
        # Setting filename list and image list attributes
        self.filename_pair_list = filename_pair_list
        self.image_pair_list = image_pair_list
    
    def compare(self, output_filename):
        result = []

        # Comparing each pair of images
        for index in range(len(self.filename_pair_list)):
            start_time = time.time()
            image1, image2 = self.image_pair_list[index][0], self.image_pair_list[index][1]
            hash1, hash2 = imagehash.average_hash(image1), imagehash.average_hash(image2)
            similarity = hash1 - hash2
            elapsed= time.time() - start_time
            result.append((self.filename_pair_list[index][0], self.filename_pair_list[index][1], similarity, elapsed))

        # Writing results to CSV
        tuple_list_to_csv(output_filename, ['image1', 'image2', 'similar', 'elapsed'], result)

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

def interpret_filepath(filepath):
    return os.path.abspath(filepath)