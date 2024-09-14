a = 5
b = 8
c = a + b
print(c)
nombre = "James"
nombre = "Alexander"
#Podemos concluir que las variables son modificables
print(nombre)

numero = 10 #primero ejecuta esta linea de código y verás que se imprime el 10
#numero =10+1 #luego ejecuto esta linea de código y verás que se imprime el 11
numero += 5 #de esta forma le sumamos 5 a la variable número
numero -= 5 #de esta manera le restamos 5 a la variable número
print(numero)

nombre = "James Alexander Jojoa"
bienvenida = "Hola " + nombre + " feliz noche"
print(bienvenida)

bienvenida = f"Hola  {nombre}  feliz noche"
print(bienvenida)
#del bienvenida #borramos la variable, es decir, que ya no esta declarada
#print(bienvenida)

nombre = True
bienvenida = f"Hola {nombre} feliz noche"
print("ola" in bienvenida)

print("Betty" not in bienvenida)
print("Hola" not in bienvenida)

nombreCompletoDeTuProfe = "Jheyson Galvis" #CamelCase sirve pare definir variables
nombre_completo_de_tu_profe = "Jheyson Galvis" #Snake Case este es el recomendado en Python segun la documentación