#El primer tipo de datos compuestos que veremos será la lista

lista = ["James Jojoa", "PsicoSociedad James Jojoa", True, 1.69]
#En el mundo de la programación no contamos del 1 al 10, contamos del 0 al 9
print(lista[1])
lista[0] = "Alexander"
print(lista[0])

#La tupla es una lista que no se puede modificar
tupla = ("café", "rosquilla", "pan", True, 8.45)
print(tupla[1])
#tupla[1] = "aguapanela"
#print(tupla[1])

#Creando un conjunto set
#El conjunto no admite elementos duplicados
conjunto ={"James Jojoa", "PsicoSociedad", True, 1.66, "James Jojoa"}
print(conjunto)

#Creando un diccionario
diccionario = {
    "nombre": "James",
    "apellido": "Jojoa",
    "estatura": 1.66,
    "esta felíz": True,
    "nombre": "James",
    "edad": 33
}
print(diccionario)
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["esta felíz"])
print(diccionario["estatura"] + 0.02)
print(diccionario["edad"])