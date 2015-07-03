#!/usr/bin/env python
'''
olympiadCsv2Json.py: Converts a csv with metadata to json and
prints to stdout.

@author: ixxra (garciamx@gmail.com)

see olympiads folder to see the csv files the program is supposed to read.
Basically, they are a table with

year, city and country

if this is an international competition, or

year, city and state

if this is a national olympiad.

This is a utility tool, as json ought to be the new format, given that it
plays well with templating engines, as mustache.
'''
import csv
import json
from sys import argv

USAGE = '''Usage:
    olympiadCsv2Json.py <input csv>

Converts a csv with olympiad metadata to json and prints to stdout.
'''

if len(argv) != 2:
    print (USAGE)
    exit(1)

with open(argv[1]) as f:
    reader = csv.reader(f)
    lines = [l for l in reader]

header = lines[0]
olympiads = []

for olympiad in lines[1:]:
    olympiads.append(dict(zip(header, olympiad)))

print(json.dumps(olympiads))
