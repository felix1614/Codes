# c = 4
# a = 0
# for i in range(int(input())):
#     row = input()
#     a += sum(list(map(lambda a: int(a) if a!='1' else 0,row.split())))    #except 1 everything appends
# print(a)
# b = sum([sum(list(map(lambda a: int(a) if a != '1' else 0, input(f"row {i}: ").split()))) for i in range(1, int(input("num of rows: "))+ 1)])

print(sum([sum(list(map(lambda a: int(a) if a != '1' else 0, input(f"row {i}: ").split())))
           for i in range(1, int(input("num of rows: ")) + 1)]))
# print(b)
# A MATRIX WHICH SUMS ALL NUMBERS EXCEPT 1 SUM OF ALL
