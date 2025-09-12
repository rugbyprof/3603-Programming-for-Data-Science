with open("students.csv") as file:
    lines = file.read().split("\n")
del lines[0]
newDict = {"first": [], "last": [], "math": [], "science": []}
for line in lines:

    first, last, math, science = line.split(",")
    print(f"{first} {last} {math} {science}")
    newDict["first"].append(first)
    newDict["last"].append(last)
    newDict["math"].append(int(math))
    newDict["science"].append(int(science))

print(newDict)
import json

with open("students.json", "w") as file:
    json.dump(newDict, file)
