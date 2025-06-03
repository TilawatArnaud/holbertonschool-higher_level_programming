#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
and then saves them to a file as a JSON representation.
"""

import sys
import json
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        items = []
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
