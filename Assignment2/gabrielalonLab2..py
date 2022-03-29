"""
CS3C, Assignment #1, Movie Objects and Classes
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

type_x = None

while type_x != "satisfied":
        latin_prompt = input("Enter a latin phrase: ").split(" ")
        result = ""
    #    print(latin_prompt, "here is latin split")
        for i in range(len(latin_prompt)):
            try:
                outcome = final[(latin_prompt[i])].strip() #added .strip here
                if outcome == "":
                    result += "."
                    continue
            except Exception as e:
                result += "."
                continue
            if i>0 and i<len(latin_prompt):
                result += " "
            result += (outcome)
        print(result)
        duration = time.perf_counter() - start
        print(duration)
