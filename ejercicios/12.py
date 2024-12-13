lista=[4,2,6,8,3]
mayor=lista[0]
for i in lista:
    if i>mayor:
        mayor=i
print(f"El elemento mayor de la lista {lista} es: {mayor}")