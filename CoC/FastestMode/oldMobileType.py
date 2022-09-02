"""
Back in day, people sent text messages using the number pad where each number was associated with 3-4 letters of the alphabet. You could hit the same number repeatedly to cycle through each of its letters. Or you could just press each number once and, in the end, the phone would guess what word you desired.

Today you will BE the phone and let's assume the user is using the latter method of input (1 number per letter). Given a string of numbers, output all possible letter combinations in alphabetical order.

Here are the letters associated with each number:
2 = abc
3 = def
4 = ghi
5 = jkl
6 = mno
7 = pqrs
8 = tuv
9 = wxyz
Input
Line 1: A string S of digits to map
Output
All possible described outputs for S in alphabetical order.
Constraints
2 ≤ Length of S ≤ 9
Example
Input
5
Output
j
k
l

TEST2: 23
Output:
ad
ae
af
bd
be
bf
cd
ce
cf

TEST3: 426
OUTPUT:
gam
gan
gao
gbm
gbn
gbo
gcm
gcn
gco
ham
han
hao
hbm
hbn
hbo
hcm
hcn
hco
iam
ian
iao
ibm
ibn
ibo
icm
icn
ico

TEST3:6969
OUTPUT:
mwmw
mwmx
mwmy
mwmz
mwnw
mwnx
mwny
mwnz
mwow
mwox
mwoy
mwoz
mxmw
mxmx
mxmy
mxmz
mxnw
mxnx
mxny
mxnz
mxow
mxox
mxoy
mxoz
mymw
mymx
mymy
mymz
mynw
mynx
myny
mynz
myow
myox
myoy
myoz
mzmw
mzmx
mzmy
mzmz
mznw
mznx
mzny
mznz
mzow
mzox
mzoy
mzoz
nwmw
nwmx
nwmy
nwmz
nwnw
nwnx
nwny
nwnz
nwow
nwox
nwoy
nwoz
nxmw
nxmx
nxmy
nxmz
nxnw
nxnx
nxny
nxnz
nxow
nxox
nxoy
nxoz
nymw
nymx
nymy
nymz
nynw
nynx
nyny
nynz
nyow
nyox
nyoy
nyoz
nzmw
nzmx
nzmy
nzmz
nznw
nznx
nzny
nznz
nzow
nzox
nzoy
nzoz
owmw
owmx
owmy
owmz
ownw
ownx
owny
ownz
owow
owox
owoy
owoz
oxmw
oxmx
oxmy
oxmz
oxnw
oxnx
oxny
oxnz
oxow
oxox
oxoy
oxoz
oymw
oymx
oymy
oymz
oynw
oynx
oyny
oynz
oyow
oyox
oyoy
oyoz
ozmw
ozmx
ozmy
ozmz
oznw
oznx
ozny
oznz
ozow
ozox
ozoy
ozoz

"""
keys = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
inpNumber = input("Enter keys: ")
# inpNumber = "23"
for i in range(len(inpNumber)):
    for j in keys[int(inpNumber[i])]:
        if i < len(inpNumber)-1:
            for k in keys[int(inpNumber[i+1])]:
                print(f"{j}{k}")


