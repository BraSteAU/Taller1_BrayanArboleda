cadena=input("Ingresa una cadena ")
contador=0
for letra in cadena:
    if letra in "aeiou":
        contador+=1
print(f"La palabra {cadena} contiene {contador} vocales")