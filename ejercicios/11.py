numero=str(int(input("Ingresa un numero")))
nuevo=""
for i in numero:
    nuevo=i+nuevo
print(f"Numero incial {numero}")
print(f"Numero invertido {nuevo}")