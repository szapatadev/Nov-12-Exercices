dias = [
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
]
n = int(input("Ingrese un numero del 1 al 7, correspondiente al dia de la semana: "))

if n > 0 and n < 8:
    print(f"El dia de la semana correspondiente al numero es: {dias[n-1]}")
else:
    print("El numero no esta entre 1 y 7")