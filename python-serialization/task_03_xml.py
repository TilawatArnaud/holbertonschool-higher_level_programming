#!/usr/bin/python3
"""
Module for serializing and deserializing Python dictionaries to/from XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the file to save the XML to
    """
    try:
        root = ET.Element('data')

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        ET.indent(tree, '    ')
        tree.write(filename, encoding='utf-8', xml_declaration=True)

    except Exception as e:
        print(f"Error during XML serialization: {e}")
        raise


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from

    Returns:
        dict: The deserialized dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        raise
    except FileNotFoundError:
        print(f"File not found: {filename}")
        raise
    except Exception as e:
        print(f"Error during XML deserialization: {e}")
        raise
