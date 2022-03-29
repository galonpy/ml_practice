"""
CS3C, Assignment #5, LZW Compression
Gabriel Alon
Driver File
Lossless Compression, replaces multiple characters with single codes, thus increasing the compression rate.
"""
from functools import partial


class table:
    def __init__(self):
        self.table = {}
        self.initialize_table()
        self.max = 29

    def search(self, text):
        try:
            self.table[str(text)]
            return True
        except:
            return False

    def add_table(self, text):
        # assigns new code
        try:
            self.table[str(text)]
        except:
            self.table[str(text)] = (self.max + 1)
            self.max += 1

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
        self.table[' '] = 26
        self.table[','] = 27
        self.table['.'] = 28
        self.table['\n'] = 29

    #        self.table[''] = 30

    def write_output(self, text):
        file1 = open("galazw.txt", "a")
        try:
            file1.write(str(self.table[str(text.upper())]) + '\n')
        except:
            file1.write(str(self.table[str(text)]) + '\n')
        file1.close()


sub_string = ""
run_table = table()
with open("data.txt") as f:
    for char in iter(partial(f.read, 1), ''):
        try:
            sub_string += (char.upper())
        except:
            sub_string += (char)
        if run_table.search(sub_string) is True:
            continue
        else:
            run_table.write_output(sub_string[:-1])
            run_table.add_table(sub_string)
            sub_string = sub_string[-1]
print(run_table.table)

"""

my_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
           'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
           'Z': 25, ' ': 26, ',': 27, '.': 28, '\n': 29, 'TH': 30, 'HE': 31, 'E ': 32, ' T': 33, 'TI': 34, 'IM': 35,
           'ME': 36, 'E T': 37, 'TR': 38, 'RA': 39, 'AV': 40, 'VE': 41, 'EL': 42, 'LL': 43, 'LE': 44, 'ER': 45,
           'R,': 46, ', ': 47, ' F': 48, 'FO': 49, 'OR': 50, 'R ': 51, ' S': 52, 'SO': 53, 'O ': 54, ' I': 55, 'IT': 56,
           'T ': 57, ' W': 58, 'WI': 59, 'IL': 60, 'LL ': 61, ' B': 62, 'BE': 63, 'E C': 64, 'CO': 65, 'ON': 66,
           'NV': 67, 'VEN': 68, 'NI': 69, 'IE': 70, 'EN': 71, 'NT': 72, 'T T': 73, 'TO': 74, 'O S': 75, 'SP': 76,
           'PE': 77, 'EA': 78, 'AK': 79, 'K ': 80, ' O': 81, 'OF': 82, 'F ': 83, ' H': 84, 'HI': 85, 'IM,': 86,
           ', \n': 87, '\nW': 88, 'WA': 89, 'AS': 90, 'S ': 91, ' E': 92, 'EX': 93, 'XP': 94, 'PO': 95, 'OU': 96,
           'UN': 97, 'ND': 98, 'DI': 99, 'IN': 100, 'NG': 101, 'G ': 102, ' A': 103, 'A ': 104, ' R': 105, 'RE': 106,
           'EC': 107, 'CON': 108, 'NDI': 109, 'ITE': 110, 'E M': 111, 'MA': 112, 'AT': 113, 'TT': 114, 'TE': 115,
           'ER ': 116, ' TO': 117, 'O U': 118, 'US': 119, 'S.': 120, '. ': 121, ' HI': 122, 'IS': 123, 'S G': 124,
           'GR': 125, 'REY': 126, 'Y ': 127, ' EY': 128, 'YE': 129, 'ES': 130, 'S S': 131, 'SH': 132, 'HO': 133,
           'ONE': 134, 'E A': 135, 'AN': 136, 'ND ': 137, ' \n': 138, '\nT': 139, 'TW': 140, 'WIN': 141, 'NK': 142,
           'KL': 143, 'LED': 144, 'D,': 145, ', A': 146, 'AND': 147, 'D ': 148, ' HIS': 149, 'S U': 150, 'USU': 151,
           'UA': 152, 'AL': 153, 'LLY': 154, 'Y P': 155, 'PA': 156, 'ALE': 157, 'E F': 158, 'FA': 159, 'AC': 160,
           'CE': 161, 'E W': 162, 'WAS': 163, 'S F': 164, 'FL': 165, 'LU': 166, 'USH': 167, 'HED': 168, 'D A': 169,
           'AND ': 170, ' AN': 171, 'NIM': 172, 'MAT': 173, 'TED': 174, 'D.': 175, '. T': 176, 'THE': 177, 'E \n': 178,
           '\nF': 179, 'FI': 180, 'IR': 181, 'RE ': 182, ' BU': 183, 'UR': 184, 'RN': 185, 'NE': 186, 'ED': 187,
           'D B': 188, 'BR': 189, 'RI': 190, 'IG': 191, 'GH': 192, 'HT': 193, 'TL': 194, 'LY': 195, 'Y A': 196,
           'AND T': 197, 'THE ': 198, ' SO': 199, 'OFT': 200, 'T R': 201, 'RAD': 202, 'DIA': 203, 'ANC': 204,
           'CE ': 205, ' OF': 206, 'F T': 207, 'THE I': 208, 'INC': 209, 'CA': 210, 'ANDE': 211, 'ESC': 212, 'CEN': 213,
           'NT ': 214, ' \nL': 215, 'LI': 216, 'IGH': 217, 'HTS': 218, 'S I': 219, 'IN ': 220, ' TH': 221, 'HE ': 222,
           ' L': 223, 'LIL': 224, 'LIE': 225, 'ES ': 226, ' OF ': 227, ' SI': 228, 'ILV': 229, 'VER': 230, 'R C': 231,
           'CAU': 232, 'UG': 233, 'GHT': 234, 'T TH': 235, 'HE B': 236, 'BU': 237, 'UB': 238, 'BB': 239, 'BL': 240,
           'LES': 241, 'S T': 242, 'THA': 243, 'AT ': 244, ' FL': 245, 'LA': 246, 'ASH': 247, 'HED ': 248, ' AND': 249,
           'D \n': 250, '\nP': 251, 'PAS': 252, 'SS': 253, 'SE': 254, 'ED ': 255, ' IN': 256, 'N ': 257, ' OU': 258,
           'UR ': 259, ' G': 260, 'GL': 261, 'LAS': 262, 'SSE': 263, 'ES.': 264, '.\n': 265}
"""