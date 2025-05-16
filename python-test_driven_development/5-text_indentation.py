#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to process

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    seps = ".?:"  # Séparateurs
    line = ""  # Stocke le texte courant
    for c in text:
        line += c  # Ajoute le caractère au texte courant
        if c in seps:  # Si c'est un séparateur
            print(line.strip())  # Imprime avec un seul saut de ligne
            print()  # Ajoute un saut de ligne
            line = ""  # Réinitialise la ligne
    if line.strip():  # Si il reste du texte à la fin
        print(line.strip(), end="")  # Imprime sans saut de ligne
