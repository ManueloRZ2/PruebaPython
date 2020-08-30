import numpy as np
import random

class Ficha():

	def __init__(self):                         # constructor generador del tablero y las posiciones aleatorias de la ficha

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
		super().__init__()				# llamado del constructor padre
		self.Movimientos()				# uso de la funcón para determinar movimientos
	
	def Movimientos(self):
		contador=-1						# el contador hace referencia a la fila que se está recorriendo
		for i in self.matrix:									
			contador+=1									
													                                                 
			for j in range(len(i)):												# posicionamientos posibles del peón
				if self.posiy == 6:					
					if (contador<self.posiy and j==self.posix and 0<self.posiy-contador<3):		# en caso de encontrarse en la posición de inicio del juego
						self.matrix[contador][j] = 1
				else:
					if (contador<self.posiy and j==self.posix and 0<self.posiy-contador<2):		# en cualquier casilla distinta a las de inicio
						self.matrix[contador][j] = 1

		print("Tablero para Peón:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7], "\n")			


###################################
class FichaTorre(Ficha):
	
	def __init__(self):
		super().__init__()				# llamado del constructor padre
		self.Movimientos()				# uso de la funcón para determinar movimientos

	def Movimientos(self):
		contador=-1						# el contador hace referencia a la fila que se está recorriendo
		for i in range(8):									
			contador+=1									
													
			for j in range(8):
				if ((contador<self.posiy or contador>self.posiy) and j==self.posix):	# posiciona unos cuando la fila y la columna coinciden	
					self.matrix[contador][j] = 1				
				elif (contador==self.posiy and j!=self.posix):	
				    self.matrix[contador][j] = 1

		print("Tablero para Torre:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7], "\n")	

###################################
class FichaAlfil(Ficha):
	
	def __init__(self):
		super().__init__()				# llamado del constructor padre
		self.Movimientos()				# uso de la funcón para determinar movimientos

	def Movimientos(self):
		contador=0						# el contador hace referencia a la fila que se está recorriendo					
		potencia=0						# para éste caso se recorren las filas desde la posición de
		contador=self.posiy  			# la ficha hacia arriba, evitando recorrer toda la matríz

		for i in range(6):									
															
			contador-=1										
			potencia+=1								# condiciones de posicionamiento de los unos, evitando desbordar el tablero
			if (self.posix-(i+1)>-1 and contador>-1):              		# unos diagonal superior izquierda
				self.matrix[contador][self.posix-(i+1)]=1

			if (self.posix-(i+1)>-1 and contador+(2*potencia)<8):  		# unos diagonal inferior izquierda
				self.matrix[contador+(2*potencia)][self.posix-(i+1)]=1

			if (self.posix+(i+1)<8 and contador>-1):               		# unos diagonal superior derecha
				self.matrix[contador][self.posix+(i+1)]=1

			if (self.posix+(i+1)<8 and contador+(2*potencia)<8):   		# unos diagonal inferior inferior
				self.matrix[contador+(2*potencia)][self.posix+(i+1)]=1

		print("Tablero para Alfil:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7], "\n")	
		
#####################################
class FichaCaballo(Ficha):

	def __init__(self):
		super().__init__()				# llamado del constructor padre
		self.Movimientos()				# uso de la funcón para determinar movimientos

	def Movimientos(self):
		contador=(self.posiy)			# el contador hace referencia a la fila que se está recorriendo								
		for i in range(2):										
			contador-=1											

			if (self.posix-1>-1 and contador>0 and i==0):		# posicionamientos de cuatro unos referenciados entre sí
				self.matrix[contador-1][self.posix-1]=1			# junto con la validación de desborde de tablero

			if (self.posix-1>-1 and contador+3<8 and i==0):
				self.matrix[contador+3][self.posix-1]=1

			if (self.posix+1<8 and contador>0 and i==0):
				self.matrix[contador-1][self.posix+1]=1

			if (self.posix+1<8 and contador+3<8 and i==0):
				self.matrix[contador+3][self.posix+1]=1

	##########  MOVIMIENTOS MAS INTERNOS HORIZONTALMENTE #########

			if (self.posix-2>-1 and contador>-1 and i==0):		# posicionamientos del resto de unos referenciados entre sí
				self.matrix[contador][self.posix-2]=1			# junto con la validación de desborde de tablero

			if (self.posix-2>-1 and contador+2<7 and i==0):
				self.matrix[contador+2][self.posix-2]=1

			if (self.posix+2<8 and contador>-1 and i==0):
				self.matrix[contador][self.posix+2]=1

			if (self.posix+2<8 and contador+2<8 and i==0):
				self.matrix[contador+2][self.posix+2]=1

		print("Tablero para Caballo:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7], "\n")

######################################
class FichaReina(Ficha):

	def __init__(self):
		super().__init__()				# llamado del constructor padre
		self.Movimientos()				# uso de la funcón para determinar movimientos

	def Movimientos(self):
		contador=self.posiy  			# el contador hace referencia a la fila que se está recorriendo	
								
		potencia=0											
														
		for i in range(6):									
															# movimientos similares del alfil
			contador-=1										
			potencia+=1
			if (self.posix-(i+1)>-1 and contador>-1):             		 # unos diagonal superior izquierda
				self.matrix[contador][self.posix-(i+1)]=1

			if (self.posix-(i+1)>-1 and contador+(2*potencia)<8):  		 # unos diagonal inferior izquierda
				self.matrix[contador+(2*potencia)][self.posix-(i+1)]=1

			if (self.posix+(i+1)<8 and contador>-1):               		 # unos diagonal superior derecha
				self.matrix[contador][self.posix+(i+1)]=1

			if (self.posix+(i+1)<8 and contador+(2*potencia)<8):  		 # unos diagonal inferior inferior
				self.matrix[contador+(2*potencia)][self.posix+(i+1)]=1

		contador=-1
		for i in range(8):									# movimientos similares de la torre
			contador+=1									
														
			for j in range(8):							
				if ((contador<self.posiy or contador>self.posiy) and j==self.posix):		
					self.matrix[contador][j] = 1				
				elif (contador==self.posiy and j!=self.posix):	
				    self.matrix[contador][j] = 1	

		print("Tablero para Reina:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7],"\n")		    

class FichaRey(Ficha):

	def __init__(self):
		super().__init__()					# llamado del constructor padre
		self.Movimientos()					# uso de la funcón para determinar movimientos

	def Movimientos(self):
		contador=self.posiy-1						# el contador hace referencia a la fila que se está recorriendo					
				
		if (self.posix-1>-1 and contador>-1):             	 		# unos diagonal superior izquierda
			self.matrix[contador][self.posix-1]=1

		if (self.posix-1>-1 and contador+2<8):  				 	# unos diagonal inferior izquierda
			self.matrix[contador+2][self.posix-1]=1

		if (self.posix+1<8 and contador>-1):               			# unos diagonal superior derecha
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

		print("Tablero para Rey:\n",self.matrix[0],"\n",self.matrix[1],"\n",self.matrix[2],"\n",self.matrix[3],"\n",self.matrix[4],"\n",
	  	self.matrix[5],"\n",self.matrix[6],"\n",self.matrix[7], "\n")



print("El siguiente programa se encarga de mostrar las posiciones de posibles movimientos de las fichas de ajedrez. Las fichas marcan su posición de forma aleatoria con un 8, los movimientos posibles se determinan por 1 y las posiciones inválidas con 0.","\n")
while True:
	
	while True:

		try:
			fichaSeleccion=input("Para continuar por favor ingrese la ficha de la cual desea ver movimientos (peon, torre, alfil, caballo, reina, rey). Para finalizar el programa, ingerese 'salir' :")
			break;
		except ValueError:
			print("La ficha ingresada no existe, por favor intentelo de nuevo.")

	if fichaSeleccion.lower()=="peon":
		miPeon=FichaPeon()
		
	elif fichaSeleccion.lower()=="torre":
		miTorre=FichaTorre()
		
	elif fichaSeleccion.lower()=="alfil":
		miAlfil=FichaAlfil()
		

	elif fichaSeleccion.lower()=="caballo":
		miCaballo=FichaCaballo()
		

	elif fichaSeleccion.lower()=="reina":
		miReina=FichaReina()
		

	elif fichaSeleccion.lower()=="rey":
		miRey=FichaRey()
		

	elif fichaSeleccion.lower()=="salir":
		print("Hasta pronto.")
		break;

	else:
		print("La opción no existe. Por favor, inténtelo de nuevo.")


