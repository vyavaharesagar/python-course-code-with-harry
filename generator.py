"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration
"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# for i in g:
#     print(i)

h = "harry"
# string is an iterable
# for c in h:
    # print(c)
# h = 45687687 #it will give the error "int object is not iterable"

print(iter(h)) #return an iterator object
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())