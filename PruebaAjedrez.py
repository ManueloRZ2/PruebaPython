
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
	for i in range(6):									#
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

	
elif entrada.lower()=="caballo":
	
	posix= (random.randint(0,7))				#############				
	posiy= (random.randint(0,7))							#
	matrix[posiy][posix]=8									#
															#
	contador=posiy											#
	for i in range(2):										#
		contador-=1											#

		if (posix-1>-1 and contador>0 and i==0):
			matrix[contador-1][posix-1]=1

		if (posix-1>-1 and contador+3<8 and i==0):
			matrix[contador+3][posix-1]=1

		if (posix+1<8 and contador>0 and i==0):
			matrix[contador-1][posix+1]=1

		if (posix+1<8 and contador+3<8 and i==0):
			matrix[contador+3][posix+1]=1
##########  MOVIMIENTOS MAS INTERNOS HORIZONTALMENTE
		if (posix-2>-1 and contador>-1 and i==0):
			matrix[contador][posix-2]=1

		if (posix-2>-1 and contador+2<7 and i==0):
			matrix[contador+2][posix-2]=1

		if (posix+2<8 and contador>-1 and i==0):
			matrix[contador][posix+2]=1

		if (posix+2<8 and contador+2<8 and i==0):
			matrix[contador+2][posix+2]=1
		
elif entrada.lower()=="reina":

	posix=(random.randint(0,7))				#############				
	posiy=(random.randint(0,7))							#
	matrix[posiy][posix]=8								#
														#
	contador=posiy										#
	potencia=0											#
														#
	for i in range(6):									#
														#
			contador-=1										
			potencia+=1
			if (posix-(i+1)>-1 and contador>-1):              # unos diagonal superios izquierda
				matrix[contador][posix-(i+1)]=1

			if (posix-(i+1)>-1 and contador+(2*potencia)<8):  # unos diagonal inferior izquierda
				matrix[contador+(2*potencia)][posix-(i+1)]=1

			if (posix+(i+1)<8 and contador>-1):               # unos diagonal superior derecha
				matrix[contador][posix+(i+1)]=1

			if (posix+(i+1)<8 and contador+(2*potencia)<8):   # unos diagonal inferior inferior
				matrix[contador+(2*potencia)][posix+(i+1)]=1

	contador=-1
	for i in range(8):									
		contador+=1									
													
		for j in range(8):
			if ((contador<posiy or contador>posiy) and j==posix):		
				matrix[contador][j] = 1				
			elif (contador==posiy and j!=posix):	
			    matrix[contador][j] = 1							

elif entrada.lower()=="rey":

	posix=(random.randint(0,7))				#############				
	posiy=(random.randint(0,7))							#
	matrix[posiy][posix]=8								#
														#
	contador=posiy-1										
				
	if (posix-1>-1 and contador>-1):             	 	# unos diagonal superios izquierda
		matrix[contador][posix-1]=1

	if (posix-1>-1 and contador+2<8):  				 	# unos diagonal inferior izquierda
		matrix[contador+2][posix-1]=1

	if (posix+1<8 and contador>-1):               		# unos diagonal superior derecha
		matrix[contador][posix+1]=1

	if (posix+1<8 and contador+2<8):   					# unos diagonal inferior inferior
		matrix[contador+2][posix+1]=1

	if (posix-1>-1):
		matrix[posiy][posix-1]=1
	if (posix+1<8):
		matrix[posiy][posix+1]=1
	if (posiy-1>-1):
		matrix[posiy-1][posix]=1
	if (posiy+1<8):
		matrix[posiy+1][posix]=1


	

print("matrix:\n",matrix[0],"\n",matrix[1],"\n",matrix[2],"\n",matrix[3],"\n",matrix[4],"\n",
	  matrix[5],"\n",matrix[6],"\n",matrix[7])