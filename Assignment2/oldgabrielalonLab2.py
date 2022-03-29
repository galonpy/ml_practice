import time
start = time.perf_counter()

data = []
with open("latin.txt", "r") as file:
    for line in file:
        data.append(tuple(line.split(", ")))
    final = dict((key, value[:-1]) for key, value in data)

type_x = None

while type_x != "satisfied":
        latin_prompt = input("Enter a latin phrase: ").split(" ")
        result = ""
      #  print(latin_prompt, "here is latin split")
        for i in range(len(latin_prompt)):
            try:
                outcome = final[(latin_prompt[i])]
            except Exception as e:
                result += "."
                continue
            if i>0 and i<len(latin_prompt):
                result += " "
            result += (outcome)
        print(result)
        duration = time.perf_counter() - start
        print(duration)



