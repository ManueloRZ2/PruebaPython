import numpy as np
import random

class Ficha():

	def __init__(self):

		self.posix=(random.randint(0,7))
		self.posiy=(random.randint(0,7))
		self.matrix=[[0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0]]
		self.GenerarTablero()

	def GenerarTablero(self):
		self.matrix[self.posiy][self.posix]=8

##################################		
class FichaPeon(Ficha):
	
	def __init__(self):
		super().__init__()
		self.Movimientos()
	
	def Movimientos(self):
		contador=-1
		for i in self.matrix:									
			contador+=1									
													
			for j in range(len(i)):						
				if (contador<self.posiy and j==self.posix):		
					self.matrix[contador][j] = 1

		print("matrix:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7])			


###################################
class FichaTorre(Ficha):
	
	def __init__(self):
		super().__init__()
		self.Movimientos()

	def Movimientos(self):
		contador=-1
		for i in range(8):									
			contador+=1									
													
			for j in range(8):
				if ((contador<self.posiy or contador>self.posiy) and j==self.posix):		
					self.matrix[contador][j] = 1				
				elif (contador==self.posiy and j!=self.posix):	
				    self.matrix[contador][j] = 1

		print("matrix:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7])	

###################################
class FichaAlfil(Ficha):
	contador=0										
	potencia=0


	def Movimientos(self):
		self.contador=self.posiy

		for i in range(6):									
															
			self.contador-=1										
			self.potencia+=1
			if (self.posix-(i+1)>-1 and self.contador>-1):              # unos diagonal superior izquierda
				self.matrix[self.contador][self.posix-(i+1)]=1

			if (self.posix-(i+1)>-1 and self.contador+(2*self.potencia)<8):  # unos diagonal inferior izquierda
				self.matrix[self.contador+(2*self.potencia)][self.posix-(i+1)]=1

			if (self.posix+(i+1)<8 and self.contador>-1):               # unos diagonal superior derecha
				self.matrix[self.contador][self.posix+(i+1)]=1

			if (self.posix+(i+1)<8 and self.contador+(2*self.potencia)<8):   # unos diagonal inferior inferior
				self.matrix[self.contador+(2*self.potencia)][self.posix+(i+1)]=1

		print("matrix:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7])	
		
#####################################
class FichaCaballo(Ficha):

	def Movimientos(self):
		contador=(self.posiy)											
		for i in range(2):										
			contador-=1											

			if (self.posix-1>-1 and contador>0 and i==0):
				self.matrix[contador-1][self.posix-1]=1

			if (self.posix-1>-1 and contador+3<8 and i==0):
				self.matrix[contador+3][self.posix-1]=1

			if (self.posix+1<8 and contador>0 and i==0):
				self.matrix[contador-1][self.posix+1]=1

			if (self.posix+1<8 and contador+3<8 and i==0):
				self.matrix[contador+3][self.posix+1]=1

	##########  MOVIMIENTOS MAS INTERNOS HORIZONTALMENTE #########

			if (self.posix-2>-1 and contador>-1 and i==0):
				self.matrix[contador][self.posix-2]=1

			if (self.posix-2>-1 and contador+2<7 and i==0):
				self.matrix[contador+2][self.posix-2]=1

			if (self.posix+2<8 and contador>-1 and i==0):
				self.matrix[contador][self.posix+2]=1

			if (self.posix+2<8 and contador+2<8 and i==0):
				self.matrix[contador+2][self.posix+2]=1

		print("matrix:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7])

######################################
class FichaReina(Ficha):

	def Movimientos(self):
		contador=self.posiy
								
		potencia=0											
														
		for i in range(6):									
															
			contador-=1										
			potencia+=1
			if (self.posix-(i+1)>-1 and contador>-1):              # unos diagonal superios izquierda
				self.matrix[contador][self.posix-(i+1)]=1

			if (self.posix-(i+1)>-1 and contador+(2*potencia)<8):  # unos diagonal inferior izquierda
				self.matrix[contador+(2*potencia)][self.posix-(i+1)]=1

			if (self.posix+(i+1)<8 and contador>-1):               # unos diagonal superior derecha
				self.matrix[contador][self.posix+(i+1)]=1

			if (self.posix+(i+1)<8 and contador+(2*potencia)<8):   # unos diagonal inferior inferior
				self.matrix[contador+(2*potencia)][self.posix+(i+1)]=1

		contador=-1
		for i in range(8):									
			contador+=1									
														
			for j in range(8):
				if ((contador<self.posiy or contador>self.posiy) and j==self.posix):		
					self.matrix[contador][j] = 1				
				elif (contador==self.posiy and j!=self.posix):	
				    self.matrix[contador][j] = 1	

		print("matrix:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7])		    

class FichaRey(Ficha):

	def Movimientos(self):
		contador=self.posiy-1										
				
		if (self.posix-1>-1 and contador>-1):             	 	# unos diagonal superios izquierda
			self.matrix[contador][self.posix-1]=1

		if (self.posix-1>-1 and contador+2<8):  				 	# unos diagonal inferior izquierda
			self.matrix[contador+2][self.posix-1]=1

		if (self.posix+1<8 and contador>-1):               		# unos diagonal superior derecha
			self.matrix[contador][self.posix+1]=1

		if (self.posix+1<8 and contador+2<8):   					# unos diagonal inferior inferior
			self.matrix[contador+2][self.posix+1]=1

		if (self.posix-1>-1):
			self.matrix[self.posiy][self.posix-1]=1
		if (self.posix+1<8):
			self.matrix[self.posiy][self.posix+1]=1
		if (self.posiy-1>-1):
			self.matrix[self.posiy-1][self.posix]=1
		if (self.posiy+1<8):
			self.matrix[self.posiy+1][self.posix]=1

		print("matrix:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7])

while True:
	
	while True:

		try:
			fichaSeleccion=input("Ingrese la ficha de la cual desea ver movimientos (peon, torre, alfil, caballo, reina, rey). Para finalizar el programa, ingerese: salir :")
			break;
		except ValueError:
			print("La ficha ingresada no existe, por favor intentelo de nuevo.")

	if fichaSeleccion.lower()=="peon":
		miPeon=FichaPeon()
		
	elif fichaSeleccion.lower()=="torre":
		miTorre=FichaTorre()
		
	elif fichaSeleccion.lower()=="alfil":
		miAlfil=FichaAlfil()
		miAlfil.Movimientos()

	elif fichaSeleccion.lower()=="caballo":
		miCaballo=FichaCaballo()
		miCaballo.Movimientos()

	elif fichaSeleccion.lower()=="reina":
		miReina=FichaReina()
		miReina.Movimientos()

	elif fichaSeleccion.lower()=="rey":
		miRey=FichaRey()
		miRey.Movimientos()

	elif fichaSeleccion.lower()=="salir":
		print("Hasta pronto.")
		break;

	else:
		print("La opción no existe. Por favor, inténtelo de nuevo.")


'''
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