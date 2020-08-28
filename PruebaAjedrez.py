
import numpy as np
import random

matrix= [[0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0]]


print("matrix:\n",matrix[0],"\n",matrix[1],"\n",matrix[2],"\n",matrix[3],"\n",matrix[4],"\n",
	  matrix[5],"\n",matrix[6],"\n",matrix[7])

entrada=input("ingresar ficha:")
contador=-1

if entrada.lower()=="peon":
	posix=(random.randint(0,7))			#############							
	posiy=(random.randint(0,7))						#
	matrix[posiy][posix] = 8						#
	for i in matrix:								#	
		contador+=1									#
													#
		for j in range(len(i)):						#
			if (contador<posiy and j==posix):		#
				matrix[contador][j] = 1				#
			
elif entrada.lower()=="torre":

	posix=(random.randint(0,7))			#############						
	posiy=(random.randint(0,7))						#
	matrix[posiy][posix]=8							#
	
	for i in range(8):								#	
		contador+=1									#
													#
		for j in range(8):
			if ((contador<posiy or contador>posiy) and j==posix):		
				matrix[contador][j] = 1				#
			elif (contador==posiy and j!=posix):	#
			    matrix[contador][j] = 1				#

elif entrada.lower()=="alfil":

	posix=(random.randint(0,7))				#############				
	posiy=(random.randint(0,7))							#
	matrix[posiy][posix]=8								#
														#
	contador=posiy										#
	potencia=0											#
	for i in range(8):									#
														#
		contador-=1										#
		potencia+=1
		if (posix-(i+1)>-1 and contador>-1):              # unos diagonal superios izquierda
			matrix[contador][posix-(i+1)]=1

		if (posix-(i+1)>-1 and contador+(2*potencia)<8):  # unos diagonal inferior izquierda
			matrix[contador+(2*potencia)][posix-(i+1)]=1

		if (posix+(i+1)<8 and contador>-1):               # unos diagonal superior derecha
			matrix[contador][posix+(i+1)]=1

		if (posix+(i+1)<8 and contador+(2*potencia)<8):   # unos diagonal inferior inferior
			matrix[contador+(2*potencia)][posix+(i+1)]=1

	
'''
def saltoCaballo(hor, ver):

    if hor<1 or hor>8 or ver<1 or ver>8:

        return []

    return sorted([[hor+i, ver+j] for i in [-2, 2, 1, -1] for j in [-1, 1, 2, -2] if abs(i)!=abs(j) and hor+i>0 and hor+i<9 and ver+j>0 and ver+j<9])
    '''

print("matrix:\n",matrix[0],"\n",matrix[1],"\n",matrix[2],"\n",matrix[3],"\n",matrix[4],"\n",
	  matrix[5],"\n",matrix[6],"\n",matrix[7])