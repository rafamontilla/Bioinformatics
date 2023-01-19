import numpy as np

#seq1 = input("sequence 1: ")
#seq2 = input("sequence 2: ")

seq1 = "GAATTCAGTTA"
seq2 = "GGATCGA"

m1 = np.zeros((len(seq1)+1,len(seq2)+1))
m2 = np.zeros ((len(seq1), len(seq2)))

match = 5
mismatch = -3
gap = -4

for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            m2[i][j] = match
        else:
            m2[i][j] = mismatch

#print(m2)

for i in range(len(seq1)+1):
    m1[i][0] = i*gap
for j in range(len(seq2)+1):
    m1[0][j] = j*gap

for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
        m1[i][j] = max(m1[i-1][j-1] + m2[i-1][j-1], m1[i-1][j] + gap, m1[i][j-1] + gap)

print(m1)

a1 = ''
a2 = ''

ti = len(seq1)
tj = len(seq2)

while(ti>0 and tj>0):
    if(ti>0 and tj>0 and m1[ti][tj] == m1[ti-1][tj-1] + m2[ti-1][tj-1]):
        a1 = seq1[ti-1] + a1
        a2 = seq2[tj-1] + a2

        ti = ti - 1
        tj = tj - 1

    elif(ti > 0 and m1[ti][tj] == m1[ti-1][tj] + gap):
        a1 = seq1[ti-1] + a1
        a2 = '-' + a2

        ti = ti - 1

    else:
        a1 = '-' + a1
        a2 = seq2[tj-1] + a2

        tj = tj - 1

print(a1)
print(a2)
                                     
                                     
                        
        
