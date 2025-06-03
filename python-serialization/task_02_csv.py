#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_file_path, json_file_path):
    """
    Convert a CSV file to a JSON file.

    Args:
        csv_file_path (str): Path to the input CSV file
        json_file_path (str): Path to the output JSON file
    """
    try:
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
