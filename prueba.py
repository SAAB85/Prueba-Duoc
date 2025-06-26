entradas_viernes=(150)
entradas_sabado=(180)           #ayuda nose llamar al contador dentro de la funcion :c
entradas={}
def comprar_entradas():
    entradas_viernes=(150)
    entradas_sabado=(180)
    while True:
        nombre=input("Ingrese nombre del comprador: ")
        if nombre in entradas:
            print("Losiento el nombre que has ingresado, ya ha sido ocupado, porfavor intenta otro.")
            continue
        while True:
            try:
                fun=int(input("Eliga la funcion, funcion (1): dia viernes, funcion (2): dia sabado: "))
                if 1<=fun<=2:
                    if fun==1:
                        entradas_viernes-=1
                        entradas[nombre]=[fun]
                        print("Entrada Comprada correctamente")
                        break
                    else:
                        entradas_sabado-=1
                        entradas[nombre]=[fun]
                        print("Entrada Comprada correctamente")
                        break
                else:
                    print ("Porfavor ingresa una opcion valida (1-2)")
            except ValueError:
                print ("Porfavor Ingrese un numero")
        break


def cambio_funcion():
    nombre=input("Ingrese el nombre de la persona que desea cambiar la entrada: ")
    if nombre in entradas:
        print(f"entrada comprada para funcion n° {entradas[nombre]}")
        while True:
            try:
                fun=int(input("para que funcion desea cambiar (1-2): "))
                if 1<=fun<=2:
                    entradas[nombre][0]=fun
                    print ("Funcion cambiada correctamente")
                    break
                else:
                    print("Ingrese una opcion correcta porfavor (1-2)")
            except ValueError:
                print ("Ingrese un valor numerico correcto")
    else:
        print("El nombre que ingreso no existe, ingrese uno nombre valido")

def mostrar_stock():
    print (f"{entradas_sabado, entradas_viernes}")




while True:
    print("TOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.- Mostrar stock de funciones.")
    print("4.- Salir.")
    try:
        opcion=int(input("Ingrese una opcion: "))
        if 1<=opcion<=4:
            if opcion == 1:
                comprar_entradas()
            if opcion == 2:
                cambio_funcion()
            if opcion == 3:
                mostrar_stock()
            if opcion == 4:
                print ("Programa terminado...")
                break
        else:
            print ("Porfavor ingrese una opcion valida (1-4)")
    except ValueError:
        print ("Porfavor ingrese un valor numerico")