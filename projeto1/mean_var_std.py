import numpy as np


def calculate(list):

    #caso nao tenha 9 numeros não rodara o codigo
    if len(list) != 9:
        print('ValuErro: Deve conter nove numeros')
    else:

        #fazendo uma array
        array = np.array(list)
        matrix = np.reshape(array, (3,3))

        #calculando os valores dentro da matrix
        mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), matrix.mean().item()]
        var = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), matrix.var().item()]
        std = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), matrix.std().item()]
        max = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), matrix.max().item()]
        min = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), matrix.min().item()]   
        
        #printa os resultados 
        calculations = {
            'mean': mean,
            'variance': var,
            'standard deviation': std,
            'max': max,
            'min': min
        }
        print(calculations)


calculate([0,1,2,3,4,5,6,7,8])
    