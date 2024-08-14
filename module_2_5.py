n=int(input('Введите количество строк '))
m=int(input('Введите количество столбцов ')) 
value=int(input('Введите значение '))
def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        matrix=matrix+[]
        for j in range(m):
            matrix.append(value) 
    return matrix
 
rezult=get_matrix(n, m, value)
print(rezult)
