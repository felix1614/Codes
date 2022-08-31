"""
A simple text encryption/decryption algorithm where every character is shifted with another one, the solution is to find the seed factor
Input
Line 1 : Encrypted Text
Line 2 : Decrypted Text
Output
Replacement factor
Constraints
Example
Input
abc
fgh
Output
5

a
b       1

This is a simple phrase
eyz?1z?1r1?z~?}v1?y?r?v         17


A day that is void of your voice is to mean an incomplete one. For with your voice comes the soul melting laughter which is all I need to have a great and happy day. I hope mine makes you feel the same way.
C"fc{"vjcv"ku"xqkf"qh"{qwt"xqkeg"ku"vq"ogcp"cp"kpeqorngvg"qpg0"Hqt"ykvj"{qwt"xqkeg"eqogu"vjg"uqwn"ognvkpi"ncwijvgt"yjkej"ku"cnn"K"pggf"vq"jcxg"c"itgcv"cpf"jcrr{"fc{0"K"jqrg"okpg"ocmgu"{qw"hggn"vjg"ucog"yc{0

2
"""
a = "abc"
print(a[::-1])
