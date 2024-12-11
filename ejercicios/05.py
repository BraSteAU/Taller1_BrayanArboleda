numero = int(input("Ingresa un numero para mostrar su tabla de multiplicar"))
r=0
for i in range(1,11):
    r=i*numero
    print(f"{i} * {numero} = {r}")