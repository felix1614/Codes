from num2words import num2words
number = "11"
# a=["zero","one","two","three","four","five","six","seven","eight","nine"]
# b=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
# c=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
# for i in range(len(number)):
#     if len(number)>1 and number[len(number)-1]=="0":
#         print(f"{b[int(number[i])-2]}")
#         break
#     elif len(number)>1 and number[len(number)-1]!="0" and number[i]!="1":
#         print(f"{b[int(number[i])-2]}-{a[int(number[i+1])]}")
#         break
#     elif len(number)>1 and number[i]=="1":
#         print(f"{c[int(number[i])]}")
#         break
#     else:
#         print(f"{a[int(number[i])]}")

print(num2words(number))