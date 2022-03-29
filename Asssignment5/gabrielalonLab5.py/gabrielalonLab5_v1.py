"""
CS3C, Assignment #5, LZW Compression
Gabriel Alon
Driver File
"""
from functools import partial

with open("data.txt") as f:
    for char in iter(partial(f.read, 1), ''):
        print(char)
#When encoding, the characters are examined one at a time
# and appended to an input string, and searched for in the table.
class table:
    def __init__(self, input_text):
        self.table = {}
        self.initialize_table()
        print(self.table, "table here")
        self.text = input_text

    def search_table(self,text):
        text in self.table
    def add_table(self,text):
        #assigns new code
        pass

    def initialize_table(self):
        self.table['A'] = 0
        self.table['B'] = 1
        self.table['C'] = 2
        self.table['D'] = 3
        self.table['E'] = 4
        self.table['F'] = 5
        self.table['G'] = 6
        self.table['H'] = 7
        self.table['I'] = 8
        self.table['J'] = 9
        self.table['K'] = 10
        self.table['L'] = 11
        self.table['M'] = 12
        self.table['N'] = 13
        self.table['O'] = 14
        self.table['P'] = 15
        self.table['Q'] = 16
        self.table['R'] = 17
        self.table['S'] = 18
        self.table['T'] = 19
        self.table['U'] = 20
        self.table['V'] = 21
        self.table['W'] = 22
        self.table['X'] = 23
        self.table['Y'] = 24
        self.table['Z'] = 25
        self.table[''] = 26
        self.table[','] = 27
        self.table['.'] = 28

    def write_output(self):
        file1 = open("galazw.txt", "a")
        file1.write(str1)
        file1.close()

data = []
with open("data.txt", "r") as file:
    for line in file:
        data.append(tuple(line.strip().split(",")))
print(data)
search_table = table(data)

try:
    search_table.search_table is True
    search_table.append_next_in_text()
#If the string is found in the table, then the next
# character is read and appended to the string and it is looked up again
except:
    # the code for the last string that was found is written to the output,
    # the new string that was encountered in the string but not found in the table
    # is added to the tables, and the process continues
    sub_string = text[:-1]
    search_table.add_table(sub_string)
    search_table.next_in_next()

"""
sub_string = ""
for i in source:
    i = read_one_more_from_source
    sub_string.append(i)
    if table.search(sub_string) is True:
        continue
    else:
        table.write_output(sub_string[-1])
        table.add_table(sub_string)
        sub_string = substring[-1]
"""

