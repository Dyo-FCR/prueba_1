#Escriba un codigo que pida un numero al uusario  y lo muestre 5 veces en pantalla

# num=input("Ingrese un numero")
# x=1
# while x <= 5 :
#     print(num)
#     x=x+1
    
    
    # Escriba un algoritmo que muestre la tabla de multiplicar del 3 del 1 al 10.
    
# x=1
# while x<=10:
#     print("3x",x,"=",(3*x))
#     x=x+1
    
# x=1
# tabla =input("ingrese el numero del cual quiere la tabla: ")
# while x<=10:
#     print(f"{tabla}x{x}={(3*x)}")
#     x+=1     
    
    
# Escriba un algoritmo que pida un número al usuario y muestre todos los números desde 1 hasta ese número.
    
# numero =int(input("ingrese el numero  "))
# x=1
# while x<= numero :
#     print(x)
#     x+=1 

# pedir un número al usuraio y generar un número aleatorio, este será el número secreto
# si  este número es igual al que digito el usuario, saldra un mensaje, Ganaste de lo contrario el mensaje sera, "Perdiste". El usuario tendra 3 intentos de adivinar el número


import random
num_sec= random.randint(1,4)
x=1

while x <=3:
    num_user=int(input("Ingrese su numero ...suerte"))
    if num_sec==num_user :
        print("ganaste")
        break
    else:
        print("Tienes",(3-x),"intentos")
        x+=1

if x==4 :
    print("Mala suerte el numero ganador era",num_sec)
                 