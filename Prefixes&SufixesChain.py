'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print("\t\tTEORÍA COMPUTACIONAL\n\tAlumnos:\nAcosta Flores Pablo\nSuárez Elizalde José Juan\nVera Sánchez Daniela")
c = input ("\n\nIntrudzca una cadena: ")
def ic(c): return c[::-1]
def prefijo(c):
    aux = ''
    indice = 0
    for indice in range(len(c)):
       aux += c[indice]
       print (aux)
print ("El prefijo de la cadena es ")
prefijo(c)
print ("El sufijo de la cadena es ")
prefijo(ic(c))
