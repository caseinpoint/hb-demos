"""APIs and Requests Demo - Pretty print script

A script that takes in a path to a JSON file and pretty-prints its contents.

Usage:
    python3 prettify.py melon-info.json
"""


from sys import argv
from pprint import pprint
import json

# Read JSON string from filename given on command-line
with open(argv[1]) as f:
    json_string = f.read()

# Turn into Python dictionary
json_dict = json.loads(json_string)

# "Pretty print" it
pprint(json_dict, indent=1)
