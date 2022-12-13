
numero_decimal = int(input("ingrese un número entero "))
print("{numero_decimal}")
numero_decimal = 29 # este es el número que queremos convertir a binario
modulos = [] # la lista para guardar los módulos

while numero_decimal != 0: # mientras el número de entrada sea diferente de cero
    # paso 1: dividimos entre 2
    modulo = numero_decimal % 2
    cociente = numero_decimal // 2
    modulos.append(modulo) # guardamos el módulo calculado
    numero_decimal = cociente # el cociente pasa a ser el número de entrada

print(modulos)
     
numero_binario = '1010110'

posicion = len(numero_binario) - 1 #posición del primer dígito por la izquierda

for digito_string in numero_binario:
	digito = int(digito_string)
	print(f'Dígito: {digito}, posición: {posicion}')
	posicion -= 1 # restamos 1 a la posición
     
