#Solucao de sistemas triangulares inferiores
def TriangularInferior(L,b,n):
    x = n*[0]
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += L[i][j]*x[j]
        x[i] = (b[i] - soma)/L[i][i]
    return x
n = 4
L = [[2,0,0,0],[3,5,0,0,],[1,-6,8,0],[-1,4,-3,9]]
b = [4,1,48,6]
x = TriangularInferior(L,b,n)
print(x)