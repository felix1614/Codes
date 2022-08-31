'''Given a random string of characters compare the first and last letter and either:

Swap their positions if either one is a vowel and the other a consonant.
Change their casing if they are both vowels or consonants.

Proceed to do the same with the second letter and the second to last and so on.

Consider Vowels: "a", "e", "i", "o", "u" and their uppercase versions.
Input
The string: input which needs to be converted.
Output
A string with the correct conversion.
Constraints
input is at least 2 characters long

input has even amount of letters

input doesn't contain numbers

input doesn't contain spaces
Example
Input
LAMERINOCE             ECONOMUNDO       GAVIOTAS        economundo      terMAL      monotacorama
Output
ECONIREMAL             ecNUMONOdo       gaviotas        ECnumonoDO      TERmal      amarocatonom'''

# inp=list(map(str,"LAMERINOCE"))
# inp_1=inp[::-1]
# fin=inp
# # print(inp)
# # print(inp_1)
# for i in range(len(inp)):
#     if inp[i].lower() in "aeiou" or inp_1[i].lower() in "aeiou":
#         fin[i]=inp_1[i]
#     elif inp[i]
#
# print("".join(fin))
w=list("economundo")
p = 0
q = len(w) - 1

while p < q:
    a = w[p].lower() in 'aeiou'
    b = w[q].lower() in 'aeiou'
    if a == b:
        if w[p].islower():
            w[p] = w[p].upper()
        else:
            w[p] = w[p].lower()

        if w[q].islower():
            w[q] = w[q].upper()
        else:
            w[q] = w[q].lower()
    else:
        w[p], w[q] = w[q], w[p]

    p += 1
    q -= 1

print("".join(w))
