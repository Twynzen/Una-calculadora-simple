import numpy as np

sumar = lambda numero1, numero2 : (numero1 + numero2)

restar = lambda numero1, numero2 : numero1 - numero2

mul = lambda numero1, numero2 : numero1 * numero2

div = lambda numero1, numero2 : numero1 / numero2

print("Elija la operación que desea realizar")
print("Inserte un 1 para sumar")
print("Inserte un 2 para restar")
print("Inserte un 3 para multiplicar")
print("Inserte un 4 para dividir")

x = input("Inserte el valor: ")
valor = int(x)

num1 = input("Inserte el primer número ")
num2 = input("Inserte el segundo número ")

n1 = float(num1)
n2 = float(num2)

if valor<=0:
    print("Has digitado un número fuera del rango")
elif valor>=5:
    print("Has digitado un número fuera del rango")
elif valor==1:
    resultado=sumar(n1,n2)
    print(resultado)
elif valor==2:
    resultado=restar(n1,n2)
    print(resultado)
elif valor==3:
    resultado=mul(n1,n2)
    print(resultado)
elif valor==4:
    resultado=div(n1,n2)
    print(resultado)
