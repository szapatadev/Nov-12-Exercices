palabra = input("Por favor ingresa una palabra de la cual quieras saber cuantas a tiene: ")
conteo = palabra.count('a') + palabra.count('A')
print(f"La palabra {palabra} tiene {conteo} a")