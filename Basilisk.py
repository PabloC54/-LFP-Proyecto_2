

token={
    "tk_if":"if",
    "tk_while":"while",
    "tk_switch":"switch",
    "tk_foreach":"foreach"    
}

# AFD PARA LEER JAVASCRIPT ES6

def LeerJS(script):

    estado=0

    for char in script:
        print(char)

        if estado==0:
            print(0)


        elif estado==1:
            print(1)
            

        elif estado==2:
            print(2)
            

        elif estado==3:
            print(3)
            

        elif estado==4:
            print(4)
            

        elif estado==5:
            print(5)                


# MENU PRINCIPAL

def Basilisk():

    salir=False

    while(salir==False):

        print("""
        ~~~~~~~~~~~~~~~~~
         B A S I L I S K 
        ~~~~~~~~~~~~~~~~~

        1. Ingresar un script

        2. Dibujar diagrama de bloques

        3. Dibujar diagrama de procesos

        4. Salir del programa
        """)


        opcion=input(">> ")

        if opcion=="1":
            
            directorio=input("        Ingrese el directorio del script\n")

            archivo=open(directorio)

            LeerJS(archivo.read())

        
        elif opcion=="2":
            print("op 2")
            
        elif opcion=="3":
            print("op 3")

        elif opcion=="4":
            print(""".\n..\n...""")
            salir=True    


        else:

            print("Opción no reconocida")


#~~> EJECUCIÓN <~~

Basilisk()
