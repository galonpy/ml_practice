"""
CS3C, Assignment #6, HTML Trees
Gabriel Alon
Main File
Feeds in an HTML file, creates a Python list
for every ordered or unordered list in the HTML document
"""

from ListCollector import *

html_file = ""

with open("lists.html") as f:
    for line in f:
        html_file += line.strip()

parser = ListCollector()
parser.feed(html_file)
print(parser.getLists())

"""
[['An item', 'Another', 'And another one'], ['Item one', 'Item two', 'Item three', 'Item four', 'End of input.']]
"""
