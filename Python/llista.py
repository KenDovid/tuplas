numeros = [1, 10, 15, 20, 30, 40, 50, 7, 20]

def saludar (nombre):
    print ("hola python saluda", nombre)

saludar("David") 

def num (numeros):
    print (numeros)

num(numeros)

diccionario=[
    {"nombre": "David", "edad": 20,"ciudad": 'Funza'},
    {"nombre": "Pepe", "edad": 18,"ciudad": 'Madrid'},
    {"nombre": "Pablo", "edad": 25,"ciudad": 'Mosquera' },
    {"nombre": "Martin", "edad": 14,"ciudad": 'Bogotá'},
    {"nombre": "Santiago", "edad": 22,"ciudad": 'Faca' },
    {"nombre": "Alejandro", "edad": 11,"ciudad": 'Bojacá'}]

for i in range(0, 6):
    val = diccionario[i]["nombre"] 
    print (val)


nombre = (input("Ingrese su nombre: "))
edad = (input("Ingrese su edad: "))

archivo = open("Dic.txt", "a")
archivo.write(nombre + ", " + str(edad) + "\n")
archivo.close()