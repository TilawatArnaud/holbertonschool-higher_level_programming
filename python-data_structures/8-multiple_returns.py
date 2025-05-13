#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        return (length, None)
    else:
        first = sentence[0]
        return (length, first)
