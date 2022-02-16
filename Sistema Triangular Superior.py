#Solucao de sistemas triangular superior
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
U = [[5,-2,6,1],[0,3,7,-4],[0,0,4,5],[0,0,0,2]]
b = [1,-2,28,8]
x = TriangularSuperior(U,b,n)
print(x)