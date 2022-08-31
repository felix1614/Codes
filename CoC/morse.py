print(int("".join(["0" if i == "-----" else str(i.count(".")) if i[0].startswith(".") else str((i.count("-")) + 5) if i[
    0].startswith("-") else "" for i in input("Enter: ").split(" ")])))
# print("".join(["" if i==0 else str(i) for i in d]))
# print(int("".join(d)))
