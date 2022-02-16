def Gauss(A,b,n):
    for k in range(n-1):
        #Pivoteamento
        pivo = A[k][k]
        r    = k
        for i in range(k+1,n): #Escolher  o maior elemento da coluna para pivô
            if abs(A[i][k]) > abs(pivo):
                pivo = A[i][k]
                r    = i
        if pivo == 0:
            print('Matriz Singular!')
            exit()
        if r != k: #Trocar as linhas
            for j in range(n):
                troca   = A[k][j]
                A[k][j] = A[r][j]
                A[r][j] = troca
            troca = b[k]
            b[k]  = b[r]
            b[r]  = troca
        #Eliminacao
        for i in range(k+1,n):
            m       = A[i][k]/A[k][k]
            A[i][k] = 0
            for j in range(k+1,n):
                A[i][j] -= m*A[k][j]
            b[i] -= m*b[k]
def TriangularSuperior(U,b,n):
    x      = n*[0]
    x[n-1] = b[n-1]/U[n-1][n-1]
    for i in range(n-2,-1,-1):
        soma = 0
        for j in range(i+1,n):
            soma += U[i][j]*x[j]
        x[i] = (b[i]-soma)/U[i][i]
    return x
n = 4
A = [[1,-1,2,-1],[2,-2,3,-3],[1,1,1,0],[1,-1,4,3]]
b = [-8,-20,-2,4]
Gauss(A,b,n)
print(A)
print(b)
x = TriangularSuperior(A,b,n)
for i in range(n):
    print(f'{x[i]:.4f}')