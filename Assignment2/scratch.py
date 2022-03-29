import time
start = time.perf_counter()

data = []
with open("latin.txt", "r") as file:
    for line in file:
        data.append(tuple(line.strip().split(","))) #allows gap so that that outlier is defined
 #   print(data[0]) #('abbas', 'father\n') vs. ('abbas', 'father') after.strip
 #   print(type(data[0]))
   # final = dict((key, value) for key, value in data)
#    final = dict((key, value) for key, value in data)
    final = dict(data)
#print(final.keys())
#print(final.values())
#print(final['abbas'])

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
"""
Enter a latin phrase: ergo
therefore
3.669232134
Enter a latin phrase: propter
because of
4.662843841
Enter a latin phrase: hoc
this
5.945124100999999
Enter a latin phrase: ergo propter hoc
therefore because of this
8.557869663
"""