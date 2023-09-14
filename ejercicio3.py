#Author: Jesus Ponte
#Fecha: 13/09/2023

# Sabemos que empezamos en un punto OX=0 y cualquier punto en y.
# Nuestro objetivo es llegar a un punto X del plano cartesiano
# Moviendonos en y+k, donde y es nuestra posicion inicial y k el numero de nuestro salto.
# Nos podemos mover y - 1 veces en caso de pasarnos.
# ya que siempre nos movemos de la forma en x de la forma para un paso futuro k*k+1, ejemplo: 1*2 = 3  , 2*3=6 , 3*4=12, 4*5=20
# Siempre que nos movamos a la derecha sera de la forma 1,3,6,12..... esto es una serie aritmetica de forma Sn=n(n+1)/2
# Con Sn llegamos a la suma de los pasos para sn = x
# Despejamos 2 * x ya que es nuestro paso futuro para la posicion
# como cada uno de los pasos tiene dos opciones, ir adelante o atrás,
# si k*(k + 1) = 2 * x, dimos exacto
#  si k*(k + 1) > 2 * x, tenemos que ajustar un paso atrás, si ajustamos la sucesion tenemos que, Sn = n(n+1)/2 - (n+1)
# Si el paso futuro k*(k + 1) es mayor a 2 * x,  comprobamos si el paso futuro es una posición más alta a la necesaria
# por lo que se tiene que hacer un paso de ajuste añadiendo un paso

import glob

def min_steps(x):
    k = 0

    #Loop para lograr superar la x con la suma de los pasos
    while k*(k + 1) < 2 * x:
        k += 1

    #si la posicion lograda es x+1 sabemos que debemos escoger un K que tenga direccion -1
    if k*(k + 1) / 2 == x + 1:
        k += 1
        
    return k

def unit_testing(directory, file_exp):
    files = glob.glob(path + file_exp)
    for j, file in enumerate(files):
        file_name = 'unit_test_' + str(j + 1)+ '.txt'
        print(file_name)
        with open(file_name)as f:
            tests = int(f.readline())
            for i in range(tests):
                result = min_steps(int(f.readline()))
                print(result)
                file_name_result = 'unit_test_' + str(j + 1) + '_result'
                with open(file_name_result, 'a') as f2:
                    f2.write(str(result)+'\n')
#Base directory
path = 'C:/Users/PC/PycharmProjects/gbm_ejercicio3'
#Specify the document path expression
file_exp = '/unit_test_*.txt'


unit_testing(path, file_exp)