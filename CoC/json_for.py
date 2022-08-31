import json

e = dict()
for j in [input(f"Enter text_{i+1}: ") for i in range(int(input("Enter qty: ")))]:
    if len(e) > 0 and j.split(" ")[0] in e.keys():
        e[j.split(" ")[0]].extend(filter(lambda a: j.index(a) != 0, j.split(" ")))
    else:
        e[j.split(" ")[0]] = list(filter(lambda a: j.index(a) != 0, j.split(" ")))
# print(f'''{str(e).replace("'",'"')}''')
print(json.dumps(e))
# print()
# print(d)
# print(f'''{str(e.get("cat")).replace("'",'"')}''')

# cat reh veh deh
# rat meh geh teh
# rat hej keh leh

