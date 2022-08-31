import numpy

word = "ShAzam"
# d=[]
# for i in word:
#     if i in d:
#         print('true')
#         break
#     else:
#         d+=i,
#
# if len(d)==len(word):
#     print('false')

# for a, b in zip(word, word[1:]):
#     if a == b: print("true"); quit()
# print("false")


# num = "153"
# c = tuple(map(lambda i: int(i)**len(num), num))
# print('true') if str(sum(c)) == num else print('false')


# d = list(map(lambda x: int(input()), range(int(input("enter qty: ")))))
# c = list(map(lambda i: str(d[i]), d))
# print(" ".join(c))
# h = 10
# w = 2
# x, y = 10, 0
# d=[]
# for i in range(h):
#     d += [i for i in input()],
#
# print(len(d))
# if len(d)<h:
#     print(d[y][x])
# else:
#     print('Invalid coordinate')
# x=19019012
# y=12345678
# c=input()
# print(int(sum(list(map(lambda x: ord(x),c)))/len(c)))


memory = {}


def memoize_factorial(f):
    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(5))
# print(facto(5))  # directly coming from saved memory





