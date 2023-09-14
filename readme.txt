Autor: Jesus Ponte
Fecha: 12/09/2023

El problema está dividido en dos funciones:
1)unit_testing, la cual recibe por parametros un string del directorio donde se encuentran las pruebas unitarias,
y el formato del nombre de las pruebas unitarias que siguen el siguiente ejemplo: 'unit_test_1.txt'.
Esta función se encarga de leer cada una de las pruebas unitarias.

2)min_steps(x), recibe por parametro un int que representa el punto en el plano a donde queremos llegar.

Sabemos que empezamos en un punto OX=0 y cualquier punto en y.
Nuestro objetivo es llegar a un punto X del plano cartesiano
Moviendonos en y+k, donde y es nuestra posicion inicial y k el numero de nuestro salto.
Nos podemos mover y - 1 veces en caso de pasarnos.
ya que siempre nos movemos de la forma en x de la forma para un paso futuro k*k+1, ejemplo: 1*2 = 3  , 2*3=6 , 3*4=12, 4*5=
Siempre que nos movamos a la derecha sera de la forma 1,3,6,12..... esto es una serie aritmetica de forma Sn=n(n+1)/2
Con Sn llegamos a la suma de los pasos para sn = x
Despejamos 2 * x ya que es nuestro paso futuro para la posicion
como cada uno de los pasos tiene dos opciones, ir adelante o atrás,
si k*(k + 1) = 2 * x, dimos exacto
si k*(k + 1) > 2 * x, tenemos que ajustar un paso atrás, si ajustamos la sucesion tenemos que, Sn = n(n+1)/2 - (n+1)
Si el paso futuro k*(k + 1) es mayor a 2 * x,  comprobamos si el paso futuro es una posición más alta a la necesaria
por lo que se tiene que hacer un paso de ajuste añadiendo un paso

Nota: Se puede agregar una apertura de los documentos 'unit_test_*_result.txt' para hacer una limpieza de las respuestas.
Para no sobreescribir los documentos se pueden eliminar para que se generen al momento de correr el programa.