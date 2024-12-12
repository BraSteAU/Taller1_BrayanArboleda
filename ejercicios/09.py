num1=int(input("Ingrese el numero 1 "))
num2=int(input("Ingrese el numero 2 "))
a=num1
b=num2
temp=0
while num2!=0:
    temp=num2
    num2=num1%num2
    num1=temp
print(f"El MCD de {a} y {b} es: {num1}")
    
