F = []

for n in range(0,56):

    if n == 0 or n == 1:

        F.insert(n,n)

    elif n == 2:

        F.insert(n,(n-1))

    elif n >= 3:

        F.insert(n,int(F[n-1]+F[n-2]))

        if int(F[n-1]+F[n-2]) == int(55):

            break

print(F)