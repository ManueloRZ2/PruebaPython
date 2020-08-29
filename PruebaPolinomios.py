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
		print("Polinomio ingresado: ")
		mostrarPolin(self.listaVect)			

########################## FUNCIONES ################################################

def multipliEscalar(poli):

	while True:
		try:
			escalar=float(input("Ingrese el escalar por el que desea multiplicar: "))
			break;
		except ValueError:
			print("Valores no válidos. Recuerde que debe ingresar un valor numerico valido.")

	print("El resultado de la multiplicación escalar es :",poli.listaVect*escalar)
	mostrarPolin(poli.listaVect*escalar)
	return poli.listaVect*escalar


def sumaPolin(poli1,poli2):
	
	difOrden=(len(poli1.listaVect)-len(poli2.listaVect))
	vectCeros=np.zeros(abs(difOrden))
		
	if len(poli1.listaVect)>len(poli2.listaVect):

		print("El resultado de la suma de los polinomios es :",poli1.listaVect+np.array(vectCeros.tolist()+poli2.listaCoef))
		mostrarPolin(poli1.listaVect+np.array(vectCeros.tolist()+poli2.listaCoef))
		return poli1.listaVect+np.array(vectCeros.tolist()+poli2.listaCoef)

	elif len(poli1.listaVect)<len(poli2.listaVect):

		print("El resultado de la suma de los polinomios es :",poli2.listaVect+np.array(vectCeros.tolist()+poli1.listaCoef))
		mostrarPolin(poli2.listaVect+np.array(vectCeros.tolist()+poli1.listaCoef))
		return poli2.listaVect+np.array(vectCeros.tolist()+poli1.listaCoef)
	else:

		print("El resultado de la suma de los polinomios es :")
		mostrarPolin(poli2.listaVect+poli1.listaVect)
		return poli2.listaVect+poli1.listaVect


def restaPolin(poli1,poli2):
	
	difOrden=(len(poli1.listaVect)-len(poli2.listaVect))
	vectCeros=np.zeros(abs(difOrden))
		
	if len(poli1.listaVect)>len(poli2.listaVect):

		print("El resultado de la resta de los polinomios es :")
		mostrarPolin(poli1.listaVect-np.array(vectCeros.tolist()+poli2.listaCoef))
		return poli1.listaVect-np.array(vectCeros.tolist()+poli2.listaCoef)

	elif len(poli1.listaVect)<len(poli2.listaVect):

		print("El resultado de la resta de los polinomios es :")
		mostrarPolin(np.array(vectCeros.tolist()+poli1.listaCoef)-poli2.listaVect)
		return np.array(vectCeros.tolist()+poli1.listaCoef)-poli2.listaVect

	else:

		print("El resultado de la resta de los polinomios es :")
		mostrarPolin(poli1.listaVect-poli2.listaVect)
		return poli1.listaVect-poli2.listaVect


def multipliPolin(poli1,poli2):

	vectResult=np.zeros((len(poli1.listaVect)+len(poli2.listaVect))-1)

	for i in range (len(poli1.listaVect)):

		for j in range(len(poli2.listaVect)):
				vectResult[i+j]=vectResult[i+j]+(poli1.listaVect[i]*poli2.listaVect[j])

	print("El polinomio resultante luego de multiplicarlos es: ", "\n")
	mostrarPolin(vectResult)			
	return vectResult			
	


def evaluarPolin(poliResult):

	potencia=len(poliResult)
	resultado=0
	while True:
	    try:
	    	x=float(input("Por favor ingrese el valor para reemplazar en X: "))	
	    	break;
	    except ValueError:
	    	print ("Valor inválido. Por favor inténtelo de nuevo.")

	for i in range(len(poliResult)):
		resultado=resultado+(poliResult[i]*(x**(len(poliResult)-1-i)))

	  
	print("Al evaluar el polinomio resulta:",resultado)
	

def mostrarPolin(poli):
	
	print(f" ({poli[0]})X^{len(poli)-1}", end="")
	for i in range(len(poli)):
		if i!=(len(poli)-1) and i!=0:
			print(f" + ({poli[i]})X^{len(poli)-1-i}", end="")
	print(f" + ({poli[i]})X^{len(poli)-1-i}","\n") 

	


################################# Main ###########################################

while True:
	while True:

		try:
			print("#################################","\n",
			"# 1.sumar                         #","\n",
			"# 2.restar                        #","\n",
			"# 3.multiplicar por escalar       #","\n",
			"# 4.multiplicación de polinomios  #","\n",
			"# 5.evaluar polinomio             #","\n",
			"# 6.salir                         #","\n",
			"#################################","\n",)
			opcion=int(input("Este programa se encarga de realizar operaciones con polinomios, a continuación ingrese una opción del menú: "))
			break;
		except ValueError:
			print("Valor inválido. Por inténtalo de nuevo.")

	if opcion==1:
		polinomio1=polinomio()
		polinomio2=polinomio()
		vector=sumaPolin(polinomio1,polinomio2)
		evaluarPolin(vector)
	elif opcion==2:
		polinomio1=polinomio()
		polinomio2=polinomio()
		vector=restaPolin(polinomio1,polinomio2)
		evaluarPolin(vector)
	elif opcion==3:
		polinomio1=polinomio()
		vector=multipliEscalar(polinomio1)
		evaluarPolin(vector)
	elif opcion==4:
		polinomio1=polinomio()
		polinomio2=polinomio()	
		vector=multipliPolin(polinomio1,polinomio2)
		evaluarPolin(vector)
	elif opcion==5:
		polinomio1=polinomio()
		evaluarPolin(polinomio1.listaVect)
	elif opcion==6:
		break;
	else:
		print("Opción inexistente. Por favor ingresa un valor asociado en el menú.")
