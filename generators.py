# A generator is a function that returns an object (iterator) 
# which we can iterate over (one value at a time).
# https://www.programiz.com/python-programming/generator

# Generators - iterable

def generatorf(n):
  for i in range(n):
    yield i

g = generatorf(1)
next(g)
next(g)
print(next(g))

for _ in generatorf(10):
  print(_)

# -------------------------------------

# Generators Performance

from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5


long_time()
long_time2()

# -------------------------------------

def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break


class MyGen:
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(1,100)
for i in gen:
    print(i)


# -------------------------------------

# Exercise_ Fibonacci Numbers    

# Here is an example generator which calculates fibonacci numbers:
# generator version
def fib(number):
    a =  0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(100):
    print(x)



def fib2(number):
    a =  0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(100))
