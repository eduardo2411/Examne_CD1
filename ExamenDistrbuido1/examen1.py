import os
from gt import greent
from cb import callb

def menu():
    os.system('clear')# solo funciona con
    print("Bienvenido Selecciones una opcion: \n")
    print("\t1- Green Thread ")
    print("\t2- Callback ")

    print("\t9- Salir ")

while True:
    #mostrar el menu
    menu()

    #solicitamos una opcion al usuario
    opcionMenu= raw_input("Insertar un numero >> ")

    if opcionMenu == "1":
        os.system('clear')
        greent()

        a=raw_input("\n Quieres regresar al menu principal y=si?: ")
        if a=="y":
            menu()
        else :
            pass

    elif opcionMenu == "2":
        os.system('clear')
        print("")
        callb()

        a=raw_input("\n Quieres regresar al menu principal y=si?: ")
        if a=="y":
            menu()
        else :
            pass
    elif opcionMenu == "9":
        break
    else:
        print("")
        raw_input("no has seleccionado una opcion valida  \npulsa la tecla enter para continuar")
