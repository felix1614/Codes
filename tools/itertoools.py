# import itertools as iter
a=[1,2,3,4,5,6,7,8,9,10]
# b=['a','b','c','d']

# print("zip",list(zip(a,b)))
# print("zip_long",list(iter.zip_longest(a,b)))
def gen(i):
    # for i in a:
    yield i*i

b=[gen(i).__next__() for i in range(1,10+1)]
# b=[next(gen(i)) for i in range(1,10+1)]
print(b)

# for i in gen(a):
#     print(i)
# import cProfile
# cProfile.run('sum(i*2 for i in range(1000000))')