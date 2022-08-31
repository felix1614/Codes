"""
In Australian schools there is a kid's crypto-language (similar to 'pig latin') in which words have the substring 'alib'
 inserted before the first vowel to make understanding the sentence hard for non-speakers of the language.

A simple example ('alib' is inserted before the first vowel of each word):
Hello world → Halibello waliborld

Words starting with vowels have the 'alib' preceding the word, correct the capitalisation if the word is capitalised
(e.g. I → Alibi):
Am I an ugly painter? → Alibam Alibi aliban alibugly palibainter?

Vowels are 'Aa Ee Ii Oo Uu' (not 'Yy'). Leave all punctuation in place. No underscores or digits used in tests.
Input
1 Line : Text to translate (i.e. a sentence/paragraph).
Output
1 Line : The text encrypted into the Alibi language.
Constraints
Input text is always a single line, less than 70 words, and less than 500 characters.
No underscores or digits used in tests.
No words with internal capitalisation e.g. 'CodinGame' used in tests.
Example
Input
Simple test case
Output
Salibimple talibest calibase
"""

sentence = "Simple test case"
da = sentence
c = []
for i in da.split(" "):
    for j in i:
        if j in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            c += f"{i[:i.index(j)]}alib{i[i.index(j):]}",
            break
print(" ".join(c))
