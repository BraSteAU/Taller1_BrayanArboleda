numero=int(input("Ingrese numero para calcular factorial"))
factorial=1
for i in range(1,numero):
    factorial+=factorial*i
print(f"El factorial de {numero} es: {factorial} ")