#!/usr/bin/env python

"""core.py: a python package to measure the similarity of a list of image pairs."""

import os, sys

from PIL import Image
import codecs
import csv
import time
import imagehash
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def stream(input_file, output_file):
    '''Streaming input CSV, calling comparison function, streaming output CSV'''
    encoding = "utf-8"

    # Using codec to stream both input and output CSVs line-by-line
    with codecs.open(input_file, "r", encoding) as in_stream, codecs.open(output_file, "w", encoding) as out_stream:
        reader = csv.reader(in_stream)
        writer = csv.writer(out_stream)

        # Reading input header and witing output header
        headers = next(reader)
        writer.writerow((headers[0], headers[1], "similar", "elapsed"))
        
        # Reading input and writing output line0by-line
        for in_row in reader:
            file1, file2 = in_row
            similarity, elapsed = compare(file1, file2)
            out_row = (file1, file2, similarity, elapsed)
            writer.writerow(out_row)

def compare(file1, file2):
    
    '''Comparing a pair of image files'''
    
    start_time = time.time()

    # Reading images one-at-a-time, calculating hash, cleaning up
    with Image.open(file1) as image:
        hash1 = imagehash.average_hash(image)
    with Image.open(file2) as image:
        hash2 = imagehash.average_hash(image)
    
    # Using hashes to calculate similarity
    similarity = hash1 - hash2
    
    elapsed= time.time() - start_time

    return (similarity, elapsed)