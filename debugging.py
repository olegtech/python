
#1. Linting
#2. Use IDE
#3. Read errors
#4. pdb 
import pdb
def add(n1, n2):
    pdb.set_trace()
    return n1 + n2

add(4, '4')    