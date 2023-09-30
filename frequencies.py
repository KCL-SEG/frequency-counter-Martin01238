"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
"""test"""
def frequencies(items):
    frequencies = {}
    # Your code goes here=]
    for a in items:
        a = str(a)
        frequencies[a] = 0
    for b in items:
        b = str(b)
        frequencies[b] = frequencies[b] + 1
    return frequencies
