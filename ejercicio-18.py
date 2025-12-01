palabra = input("Pon una palabra: ")
palabraInvertida = palabra[::-1]
if palabra == palabraInvertida:
 print(f"La palabra que ingresaste es un palindromo")
else:
 print("La palabra que ingresaste no es un palindromo")