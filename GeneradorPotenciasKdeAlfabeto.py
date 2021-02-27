'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from itertools import product
print("POTENCIA K DE UN ALFABETO\n\tIntegrantes:\nAcosta Flores Pablo\nSuárez Elizaldo José Juan\nVera Sánchez Daniela\n")
c = input("Introduzca un alfabeto **SIN ESPACIOS NI COMAS: ")
k = int(input("Introduzca la potencia k del alfabeto: "))
j = 0
pot = product(c, repeat = k)
print ("\nLa potencia k de su alfabeto es:\n")
for j in list(pot):
    print (j)
