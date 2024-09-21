#Operadores numéricos
a = 10
b = 3
print(a > b)
print(b < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
print("suma", a + b)
print("Resta", a - b)
print("multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)

#En Python, el operador de módulo (%) se utiliza para obtener el residuo de una división entre dos números.
print("Modulo:", a % b)
#El siguiente signo es el de doble división y el resultado seria la parte entera
print("División entera:", a // b)
#queremos sumarle 2 a la variable a podrias poner a = a + 2 o mejor:
a += 2
print(a)
operacion_1 = 2 + 3 * 4
operacion_2 = 2 + (3 * 4)
print(operacion_1)
print(operacion_2)
operacion_3 = (2 + 3) * (4 ** 2) / 8 - 1
print(operacion_3)