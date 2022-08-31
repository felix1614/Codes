a = "ramesh"
(print("True") if "".join(sorted(a.lower())) == a.lower() else print(("".join(sorted(a.lower())))[1]))
# if "".join(sorted(a.lower()))==a.lower():
#     print("True")
# else:
#     print(("".join(sorted(a.lower())))[1])
