randomLetter = [*input("Enter words")]
Words = list(map(str, input("Enter words with  separated by ,: ").split(",")))
for word in Words:
    c = ""
    for j in word:
        if j in randomLetter:
            c += j
    if sorted(c) == sorted(word):
        print(f"word found: {word}")
    else:
        print(f"word not found: {word}")


# for word in Words:
#     # print(word.split())
#     if [*word] in randomLetter:
#     # if sorted(c) == sorted(word):
#         print(f"word found: {word}")
#     else:
#         print(f"word not found: {word}")
#
#
#
#
