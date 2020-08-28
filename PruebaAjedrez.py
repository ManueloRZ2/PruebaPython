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
	posix=6			#################################							
	posiy=6
	matrix[posiy][posix] = 8											#
	for i in matrix:								#	
		contador+=1									#
													#
		for j in range(len(i)):						#
			if (contador<posiy and j==posix):		#
				matrix[contador][j] = 1				#
			
elif entrada.lower()=="torre":

	posix=6			#################################							
	posiy=4	
	matrix[posiy][posix]=8										#
	for i in matrix:								#	
		contador+=1									#
													#
		for j in range(len(i)):						#
			if ((contador<posiy or contador>posiy) and j==posix):		
				matrix[contador][j] = 1				#
			elif (contador==posiy and j!=posix):	#
			    matrix[contador][j] = 1				#
				



print("matrix:\n",matrix[0],"\n",matrix[1],"\n",matrix[2],"\n",matrix[3],"\n",matrix[4],"\n",
	  matrix[5],"\n",matrix[6],"\n",matrix[7])