n1 = int(input("ingresa un numero "))
n2 = int(input("ingresa otro numero "))

if n1 > n2:
    print(f"El primer numero es mayor: {n1}")
elif n2 > n1:
    print(f"El segundo numero es mayor: {n2}")
else:
    print(f"Los dos numeros son el mismo")