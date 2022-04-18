
from ast import comprehension
from asyncio import events


# list comprehension

# standard way
ls = []

for i in range(100):
    if i%3==0:
        ls.append(i)

# print(ls)

# using list comprehension
# ls = [x for x in range(100) if x%3==0]

# print(ls)

#dictionary comprehension

# dict1 = {i:f"item {i}" for i in range(5) }

# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)

# set comprehension

# dresses = {dress for dress in ["dress1","dress2","dress2","dress3","dress1"]}
# print(type(dresses))


# generator comprehensions

events = (i for i in range(100) if  i%2==0)
print(type(events))