#Adivina el número
import random

print("Bienvenido al juego de adivina un número")
print("Adivian un número del 1 al 100")

numero_secreto = random.randint(1,100)

adivinado = False

while not adivinado:
    numero_usuario = int(input("Ingresa un número: "))

    if(numero_usuario == numero_secreto):
          print ("Felicidades has acertado")
          adivinado = True
    elif numero_usuario < numero_secreto:    
        print("El número secreto es mas alto")  
    else:
        print("El Numero es mas bajo")
