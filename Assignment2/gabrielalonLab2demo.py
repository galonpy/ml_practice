"""
CS3C, Assignment #2, Timing and Big O
Gabriel Alon
Driver File

This program is O(n) because it only goes one "for" loop deep at a time

vergo veritas
5.4334288420000005

Vernandense vero
9.374895018

verto
12.348262866

verus
15.423113696

utpote
seeing
195.969061507

Vernandense
45.804393108999996

"""

from Assignment2.gabrielalonLab2 import *

if __name__ == '__main__':
    run_status = None

    while run_status != "satisfied":
        latin_prompt = input("Enter a latin phrase: ").split(" ")
        Translator.translate(latin_prompt)
        continue

"""
Enter a latin phrase: vergo veritas
bend truth
3.541504274
Enter a latin phrase: Vernandense vero
. in
6.629300124
Enter a latin phrase: verto
flee
11.010701474000001
Enter a latin phrase: verus
true
13.898346335000001
Enter a latin phrase: utpote
seeing
16.690813276
Enter a latin phrase: Vernandense
.
19.12736161
"""
