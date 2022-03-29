"""
CS3C, Assignment #2, Timing and Big O
Gabriel Alon
Main File
"""

import time

start = time.perf_counter()

data = []
with open("latin.txt", "r") as file:
    for line in file:
        data.append(tuple(line.strip().split(",")))
    final = dict(data)


class Translator():
    def translate(latin_prompt):
        result = ""
        #    print(latin_prompt, "here is latin split")
        for i in range(len(latin_prompt)):
            try:
                outcome = final[(latin_prompt[i])].strip()  # added .strip here
                if outcome == "":
                    result += "."  # found in the dictionary without a translation
                    continue
            except Exception as e:
                result += "."  # not found in the dictionary
                continue
            if i > 0 and i < len(latin_prompt):
                result += " "
            result += (outcome)
        print(result)
        duration = time.perf_counter() - start
        print(duration)
