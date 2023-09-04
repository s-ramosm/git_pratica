from calculadora import *

calculadora = Calculadora()

print ("Seleccione su operacion :  \n 1.Sumar  \n 2.Restar \n 3.Multiplicar \n" )

opt = input()

a = input("inserte el valos a: ")
b = input("inserte el valos b: ")

opt = int (opt)
a,b = int(a) , int(b)


if opt == 1:
    print(calculadora.sumar(a,b))

if opt == 2:
    print(calculadora.restar(a,b))

if opt == 3:
    print(calculadora.multiplicar(a,b))