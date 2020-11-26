# Make a dictionary in Python from input values
# https://stackoverflow.com/questions/14147369/make-a-dictionary-in-python-from-input-values

n = 3
d = dict(raw_input().split() for _ in range(n))
print d

###

n = int(input("enter a n value:"))
d = {}

for i in range(n):
    keys = input() # here i have taken keys as strings
    values = int(input()) # here i have taken values as integers
    d[keys] = values
print(d)


# How can I add new keys to a dictionary?
# https://stackoverflow.com/a/1024851

d = {'key': 'value'}
print(d)
# {'key': 'value'}
d['mynewkey'] = 'mynewvalue'
print(d)
# {'key': 'value', 'mynewkey': 'mynewvalue'}

###

>>> x = {1:2}
>>> print(x)
{1: 2}

>>> d = {3:4, 5:6, 7:8}
>>> x.update(d)
>>> print(x)
{1: 2, 3: 4, 5: 6, 7: 8}
