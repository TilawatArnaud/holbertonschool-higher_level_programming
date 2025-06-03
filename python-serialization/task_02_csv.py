#!/usr/bin/python3
"""
Module for converting CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): Path to the input CSV file

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
