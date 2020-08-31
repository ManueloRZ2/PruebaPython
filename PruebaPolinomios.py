import numpy as np

class polinomio():

	def __init__(self):
		self.listaCoef=[]				# inicializar los vectores para ingresar los coeficientes
		self.listaVect=np.zeros(1)		# usando listas para concatenar valores y pasarlos a vector
		self.inicializar()				# posteriormente

	def inicializar(self):
		while True:
										# Validación de la entrada propocionada por el usuario
			try:
				orden=int(input("Por favor, ingrese el orden del polinomio:"))
				if orden<0:
					print("El orden del polinomio debe ser un valor positivo. Por favor intentelo de nuevo.")
				else:
					break;

			except ValueError:
				print("Valores no válidos. Recuerde que debe ingresar un valor numérico valido.")

		self.listaCoef=[]
		for i in range(orden+1):
										# recolección de los coeficientes del polinomio en cuestión
			while True:
				try:
					coeficientes=float(input(f"Introduzca el coeficiente del término {i+1}: "))
					self.listaCoef.append(coeficientes)
					break;
				except ValueError:
					print("Coeficiente inválido. Por favor intentelo de nuevo.")
		self.listaVect=np.array(self.listaCoef)				# conversión de la lista en vector para procesos matemáticos
		print("Polinomio ingresado: ")
		mostrarPolin(self.listaVect)			

########################## FUNCIONES ################################################

def multipliEscalar(poli):

	while True:
		try:
			escalar=float(input("Ingrese el escalar por el que desea multiplicar: "))
			break;
		except ValueError:
			print("Valores no válidos. Recuerde que debe ingresar un valor numérico valido.")

	print("El resultado de la multiplicación escalar es :",poli.listaVect*escalar)  # cálculo e impresión de polinomio resultante
	mostrarPolin(poli.listaVect*escalar)
	return poli.listaVect*escalar


def sumaPolin(poli1,poli2):
	
	difOrden=(len(poli1.listaVect)-len(poli2.listaVect))   # determina el orden de los polinomios para proceder con la 
	vectCeros=np.zeros(abs(difOrden))					   # igualación de términos
		
	if len(poli1.listaVect)>len(poli2.listaVect):      	   # las siguientes condiciones permiten completar el vector más pequeño

		print("El resultado de la suma de los polinomios es :",poli1.listaVect+np.array(vectCeros.tolist()+poli2.listaCoef))
		mostrarPolin(poli1.listaVect+np.array(vectCeros.tolist()+poli2.listaCoef))
		return poli1.listaVect+np.array(vectCeros.tolist()+poli2.listaCoef)

	elif len(poli1.listaVect)<len(poli2.listaVect):

		print("El resultado de la suma de los polinomios es :",poli2.listaVect+np.array(vectCeros.tolist()+poli1.listaCoef))
		mostrarPolin(poli2.listaVect+np.array(vectCeros.tolist()+poli1.listaCoef))
		return poli2.listaVect+np.array(vectCeros.tolist()+poli1.listaCoef)
	else:

		print("El resultado de la suma de los polinomios es :")    # esta caso para cuando las longitudes de los vectores son iguales
		mostrarPolin(poli2.listaVect+poli1.listaVect)
		return poli2.listaVect+poli1.listaVect


def restaPolin(poli1,poli2):
	
	difOrden=(len(poli1.listaVect)-len(poli2.listaVect))	# determina el orden de los polinomios para proceder con la 
	vectCeros=np.zeros(abs(difOrden))						# igualación de términos
		
	if len(poli1.listaVect)>len(poli2.listaVect):			# condiciones para determinar cual vector se debe completar con ceros

		print("El resultado de la resta de los polinomios es :")
		mostrarPolin(poli1.listaVect-np.array(vectCeros.tolist()+poli2.listaCoef))
		return poli1.listaVect-np.array(vectCeros.tolist()+poli2.listaCoef)

	elif len(poli1.listaVect)<len(poli2.listaVect):

		print("El resultado de la resta de los polinomios es :")
		mostrarPolin(np.array(vectCeros.tolist()+poli1.listaCoef)-poli2.listaVect)
		return np.array(vectCeros.tolist()+poli1.listaCoef)-poli2.listaVect

	else:

		print("El resultado de la resta de los polinomios es :")  # caso para cuando sus longitudes coinciden (caso feliz)
		mostrarPolin(poli1.listaVect-poli2.listaVect)
		return poli1.listaVect-poli2.listaVect


def multipliPolin(poli1,poli2):

	vectResult=np.zeros((len(poli1.listaVect)+len(poli2.listaVect))-1)  # tamaño del vector resultante según el tamaño de 
																		# los vectores de los polinomios asociados a la operación
	for i in range (len(poli1.listaVect)):								
																		# se recorren los vectores asemejandose a una distributiva
		for j in range(len(poli2.listaVect)):							
				vectResult[i+j]=vectResult[i+j]+(poli1.listaVect[i]*poli2.listaVect[j])  # vector con las multiplicaciones y sumas resultantes

	print("El polinomio resultante luego de multiplicarlos es: ", "\n")
	mostrarPolin(vectResult)			
	return vectResult			
	


def evaluarPolin(poliResult):

	potencia=len(poliResult)
	resultado=0
	while True:				# toma el valor para evaluar en el polinomio que se ingrese en la función
	    try:
	    	x=float(input("Por favor ingrese el valor para evaluar en X: "))		# validación de datos ingresados
	    	break;
	    except ValueError:
	    	print ("Valor inválido. Por favor inténtelo de nuevo.")

	for i in range(len(poliResult)):
		resultado=resultado+(poliResult[i]*(x**(len(poliResult)-1-i)))	 # acumulador para resultado de evaluación y suma de términos

	  
	print("Al evaluar el polinomio resulta:",resultado)
	

def mostrarPolin(poli):
	
	print(f" ({poli[0]})X^{len(poli)-1}", end="")		        # impresión del primer término
	for i in range(len(poli)):
		if i!=(len(poli)-1) and i!=0:
			print(f" + ({poli[i]})X^{len(poli)-1-i}", end="")	# impresión de tértminos en medio	
	print(f" + ({poli[i]})X^{len(poli)-1-i}","\n") 		        # impresión el último termino

def validacion(vector):
	while True:
			try:
				opcion=int(input("¿Desea evaluar el polinomio previo? 1.SI  2.NO (ingrese el valor numérico asociado a la opción): "))
				if opcion==1:
					evaluarPolin(vector)
					break;
				elif opcion==2:
					break;
				else:
					print("Opción inexistente. Por favor ingresa un valor asociado en el menú.")
			except ValueError:
				print("Valor de opción incorrecto. Por favor, inténtalo de nuevo.")


################################# Main ###########################################

# Menú para selección de parte del usuario
while True:
	while True:

		try:
			print("#################################","\n",
			"# 1.sumar polinomios              #","\n",
			"# 2.restar polinomios             #","\n",
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
		validacion(vector)		
	elif opcion==2:
		print("IMPORTANTE: ingrese primero el polinomio 'minuendo', posteriormente ingrese el polinomio 'sustraendo'", "\n")
		polinomio1=polinomio()
		polinomio2=polinomio()
		vector=restaPolin(polinomio1,polinomio2)
		validacion(vector)
	elif opcion==3:
		polinomio1=polinomio()
		vector=multipliEscalar(polinomio1)
		validacion(vector)
	elif opcion==4:
		polinomio1=polinomio()
		polinomio2=polinomio()	
		vector=multipliPolin(polinomio1,polinomio2)
		validacion(vector)
	elif opcion==5:
		polinomio1=polinomio()
		evaluarPolin(polinomio1.listaVect)
	elif opcion==6:
		print("Hasta pronto. Programa finalizado")
		break;
	else:
		print("Opción inexistente. Por favor ingresa un valor asociado en el menú.")
