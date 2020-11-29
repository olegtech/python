









# -------------------------------------

# List Comprehension
x=1
y=1
z=2
n=3

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])


# -------------------------------------

L,L4 = [], []
for i in range(int(input())):
    name = input()
    score = float(input())
    L.append([name, score])

L2 = sorted(list(set([m for name, m in L])))[1]

for i in range(len(L)):
    if L2 == (L[i][1]):
        L4.append(L[i][0])

L4.sort()

for i in L4:
    print(i)

# comments  
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


# -------------------------------------


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores


    query_name = input()
    print( format( (sum(student_marks[query_name]) / 3 ), ".2f" ) )


# -------------------------------------

