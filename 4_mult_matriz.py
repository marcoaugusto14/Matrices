# Escriba una función para multiplicar dos matrices.

a = [[1, 2, 3],
     [4, 5, 6]]

b = [[1, 2],
     [3, 4],
     [5, 6]]


def mult_matriz (m1, m2):
    if len(m1[0]) == len(m2):
        m3 = []
        
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1)):
                m3[i]. append(0)
        
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
                    
        return m3
    else:
        return None
    
c = mult_matriz(a,b)

if c == None:
    print("No es posible multiplicar")
else:
    for fila in c:
        print("[", end="")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")
    