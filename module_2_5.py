n=3  # количество строк
m=4  # количество столбцов
value=10  # значение
def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        matrix=matrix+[]
        for j in range(m):
            matrix.append(value) 
    return matrix
 
rezult=get_matrix(n, m, value)
print(rezult)
