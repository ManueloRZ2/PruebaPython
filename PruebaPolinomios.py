import numpy as np

class polinomio():

	def __init__(self):
		self.listaCoef=[]
		self.listaVect=np.zeros(1)
		self.inicializar()

	def inicializar(self):
		while True:

			try:
				orden=int(input("Por favor, ingrese el orden del polinomio:"))
				if orden<0:
					print("El orden del polinomio debe ser un valor positivo. Por favor intentelo de nuevo.")
				else:
					break;

			except ValueError:
				print("Valores no válidos. Recuerde que debe ingresar un valor numerico valido.")

		self.listaCoef=[]
		for i in range(orden+1):
	
			while True:
				try:
					coeficientes=int(input(f"Introduzca el coeficiente del término {i+1}: "))
					self.listaCoef.append(coeficientes)
					break;
				except ValueError:
					print("Coeficiente inválido. Por favor intentelo de nuevo.")
		self.listaVect=np.array(self.listaCoef)
		print(self.listaVect)			



def multipliEscalar(poli):

	while True:
		try:
			escalar=int(input("Ingrese el escalar por el que desea multiplicar: "))
			break;
		except ValueError:
			print("Valores no válidos. Recuerde que debe ingresar un valor numerico valido.")

	print("El resultado de la multiplicación escalar es :",poli.listaVect*escalar)


def sumaPolin(poli1,poli2):
	print("El resultado de la suma de los polinomios es :",poli1.listaVect+poli2.listaVect)


################################# Main ###########################################

polinomio1=polinomio()
multipliEscalar(polinomio1)
sumaPolin(polinomio1,polinomio1)
