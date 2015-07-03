#!/usr/bin/env python
'''
modernize.py <olympiad dirname>

reads a dir with olympiads metadata.
It expects the dir containing a pdf folder and json file with the format that
`olympiadCsv2Json.py` returns.

Note that modernize.py is opinionated about the formating, so the pdf's
should be named as

<olympiad id><year>.pdf

where <olympiad id> should be the dir's basename, in singular form.
'''
import os.path
import json
from sys import argv

USAGE = '''Usage:
    modernize.py <olympiad dirname>

prints json with metadata to stdout.
'''

if len(argv) != 2:
    print(USAGE)
    exit(1)


assert os.path.isdir(argv[1])
targetDir = argv[1]
targetName = os.path.basename(targetDir)

if targetName.endswith('s'):
    olympiadClass = targetName[:-1]
else:
    olympiadClass = targetName

pdfUrlTemplate = 'pdf/{oClass}{year}.pdf'

with open(os.path.join(targetDir,'{name}.json'.format(name=targetName))) as f:
    olympiads = json.load(f)

for olympiad in olympiads:
    year = olympiad['year']
    pdf = pdfUrlTemplate.format(oClass=olympiadClass, year=year)
    olympiad['pdf'] = pdf

meta = {
    'oClass': olympiadClass,
    'url': 'olympiads/{target}'.format(target=targetName),
    'olympiads': olympiads}

print(json.dumps(meta))
