i = 0
n = 1
suma = 0
nPalabra = ""

while nPalabra != "fin":
    nPalabra = input("Ingresa un numeros para hacer un promedio, preciona 'fin' para el resultado: ")
    if nPalabra != "fin":
     n = int(nPalabra)
     suma += n
     i += 1
else:
    print(f"El promedio de todos los valores es {suma / i}")