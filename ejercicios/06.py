n=int(input("Ingresa un numero"))
primo=True
for i in range(2,n):
    if n%i==0:
        primo = False
if primo == False:
    print(f"El numero {n} no es primo")
else:
    print(f"El numero {n} es primo")


    
