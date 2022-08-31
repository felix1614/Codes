'''You're given a list of N words, you have to print N lines, each of them being the first vowel of the word w in alphabetical order.
If there is no vowel, you have to print NONE.
If the same letter appears in upper and lower cases, the priority goes to the lowercase aAeEiIoOuU.

Note: "y" is not considered as a vowel, the only letters which are considered as vowels are: A E I O U.
Input
Line 1 : An integer N for the number of words.
Next N lines : Each word w.
Output
N lines : First vowel of each w when its letters are taken in alphabetical order, in the lowest case it appears, NONE if there is none.
Constraints
1 ≤ N ≤ 100
Example
Input
1
AZERTY
Output
A

inout:
3
PLOP
XPLDR
LOLILOL

output:
O
NONE
I

Input:
4
Caesar
Alibi
OhohohSantA
LlLlLl

OUTPUT:
a
A
a
NONE'''


# c=[]

# tuple(map(lambda j:(print(j),c.append("")) if j in word and len(c)==0  else print("NONE") if a.index(j)==len(a)-1 and len(c)==0 else "" ,a))
a = "aAeEiIoOuU"
c=0
for i in range(int(input("Enter no: "))):
    word = input(f"Word {'' if i==0 else i+1} ")
    for j in a:
        if j in word and c==0:
            print(j)
            c+=1
        elif a.index(j)==len(a)-1 and c==0:
            print("NONE")
    c=0



