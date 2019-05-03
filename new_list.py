L = [2, 4, 9, 16, 25]

M = [i**2 for i in L]
print(M)

for i in range(len(L)):
    L[i] = L[i] ** 2
    print(L)
