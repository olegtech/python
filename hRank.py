









# -------------------------------------

# List Comprehension
x=1
y=1
z=2
n=3

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])


# -------------------------------------


L = []
for i in range(int(input())):
    name = input()
    score = float(input())
    L.append([name, score])

#L.sort(key = lambda x: x[1])
L2 = sorted(list(set([m for name, m in L])))[1]
L3 = [i for in range(len(L)) in L]

for i in range(len(L)):
    if L2 == (L[i][1]):
        print(sorted(L[i][0]))



print(L3)

#marksheet = []
#L2 = sorted(list(set([marks for name, marks in L])))[1]
#print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))