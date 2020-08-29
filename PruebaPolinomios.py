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
					coeficientes=float(input(f"Introduzca el coeficiente del término {i+1}: "))
					self.listaCoef.append(coeficientes)
					break;
				except ValueError:
					print("Coeficiente inválido. Por favor intentelo de nuevo.")
		self.listaVect=np.array(self.listaCoef)
		print(self.listaVect)			

########################## FUNCIONES ################################################

def multipliEscalar(poli):

	while True:
		try:
			escalar=float(input("Ingrese el escalar por el que desea multiplicar: "))
			break;
		except ValueError:
			print("Valores no válidos. Recuerde que debe ingresar un valor numerico valido.")

	print("El resultado de la multiplicación escalar es :",poli.listaVect*escalar)


def sumaPolin(poli1,poli2):
	
	difOrden=(len(poli1.listaVect)-len(poli2.listaVect))
	vectCeros=np.zeros(abs(difOrden))
		
	if len(poli1.listaVect)>len(poli2.listaVect):

		print("El resultado de la suma de los polinomios es :",poli1.listaVect+np.array(vectCeros.tolist()+poli2.listaCoef))

	elif len(poli1.listaVect)<len(poli2.listaVect):

		print("El resultado de la suma de los polinomios es :",poli2.listaVect+np.array(vectCeros.tolist()+poli1.listaCoef))

	else:

		print("El resultado de la suma de los polinomios es :",poli2.listaVect+poli1.listaVect)


def restaPolin(poli1,poli2):
	
	difOrden=(len(poli1.listaVect)-len(poli2.listaVect))
	vectCeros=np.zeros(abs(difOrden))
		
	if len(poli1.listaVect)>len(poli2.listaVect):

		print("El resultado de la resta de los polinomios es :",poli1.listaVect-np.array(vectCeros.tolist()+poli2.listaCoef))

	elif len(poli1.listaVect)<len(poli2.listaVect):

		print("El resultado de la resta de los polinomios es :",np.array(vectCeros.tolist()+poli1.listaCoef)-poli2.listaVect)

	else:

		print("El resultado de la resta de los polinomios es :",poli1.listaVect-poli2.listaVect)


def multipliPolin(poli1,poli2):

	vectResult=np.zeros((len(poli1.listaVect)+len(poli2.listaVect))-1)

	for i in range (len(poli1.listaVect)):

		for j in range(len(poli2.listaVect)):
				vectResult[i+j]=vectResult[i+j]+(poli1.listaVect[i]*poli2.listaVect[j])


	print("El producto de polinomios es: ", vectResult)





################################# Main ###########################################



polinomio1=polinomio()
polinomio2=polinomio()

#multipliEscalar(polinomio1)
#sumaPolin(polinomio1,polinomio2)
#restaPolin(polinomio1,polinomio2)
multipliPolin(polinomio1,polinomio2)
