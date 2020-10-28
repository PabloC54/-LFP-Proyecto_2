from io import FileIO
import traceback

archivo=""

letra=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digito=["0","1","2","3","4","5","6","7","8","9"]

tk={
    "if":"if",
    "while":"while",
    "switch":"switch",
    "foreach":"foreach",
    "case":"case",
    "dospuntos":":",
    "in":"in",
    "comilla":['"',"'"],
    "coma":",",
    "punto":".",
    "var":"var",
    "let":"let",
    "const":"const",
    "igual":"=",
    "puntocoma":";",
    "parA":"(",
    "parB":")",
    "llaveA":"{",
    "llaveB":"}",
    "asinc":"=>"
}

lista_tokens, lista_error=[], []

# AFD PARA LEER JAVASCRIPT ES6

def AFD(script):

    global tk, lista_tokens, lista_error
    lista_tokens,lista_error=[],[]

    estado, linea, columna=0, 1, 0
    lexema, token= "",""

    for char in script:
        print(char, estado)
        columna+=1

        if char=="\n": #CONTEO DE LINEAS
            linea+=1
            columna=0

        try:

            if char in letra or char in digito or char=="_":
                lexema+=char
                
            elif estado==0:                

                if char==tk["parA"]:
                    estado=2
                    token="parA"

                elif char==tk["parB"]:
                    estado=2
                    token="parB"

                elif char==tk["llaveA"]:
                    estado=2
                    token="llaveA"

                elif char==tk["llaveB"]:
                    estado=2
                    token="llaveB"

                elif char in tk["comilla"]:
                    estado=2
                    token="comilla"

                elif char==tk["igual"]:
                    estado=2
                    token="igual"

                elif char==tk["puntocoma"]:
                    estado=2
                    token="puntocoma"

                elif char==tk["dospuntos"]:
                    estado=2
                    token="dospuntos"
                
                elif lexema==tk["if"]:
                    estado=2
                    token="if"

                elif lexema==tk["while"]:
                    estado=2
                    token="while"

                elif lexema==tk["switch"]:
                    estado=2
                    token="switch"

                elif lexema==tk["case"]:
                    estado=2
                    token="case"

                elif lexema==tk["foreach"]:
                    estado=2
                    token="foreach"

                elif lexema==tk["in"]:
                    estado=2
                    token="in"

                elif lexema==tk["var"]:
                    estado=2
                    token="var"

                elif lexema==tk["let"]:
                    estado=2
                    token="let"

                elif lexema==tk["const"]:
                    estado=2
                    token="const"

                elif Variable(lexema):
                    estado=2
                    token="variable"

                elif Numero(lexema):
                    estado=2
                    token="numero"             

                else:
                    estado=-1


            if estado==2:
                print("valido elpepe","'"+token+"'","'"+lexema+"'","'"+char+"'")
                lista_tokens.append(token)
                token, lexema="", ""

                input("press enter :3")
                
                estado=0

            elif estado==-1:

                if char not in [""," ","\n"]:

                    print("error elpepe","'"+token+"'","'"+lexema+"'","'"+char+"'")
                    lista_error.append(token)
                    input("press enter :3")

                token, lexema="", ""
                
                estado=0
                

        except Exception as e:
            print("=================, fallo en "+char,estado)
            traceback.print_exc()

            input("press enter :3")


    print("se terminó en el estado "+str(estado))
    print("===================================================")   
    print(script.split("\n"))
    print(lista_tokens)        
    print(lista_error)        
            

   
def Variable(lexema):

    if lexema in [""," ","\n","true","false"] or lexema in tk.values():
        return False

    estado=0

    for char in lexema:
        
        if estado==0:

            if char =="_" or char in letra:
                estado=1
                
            else:
                estado=-1

        elif estado==1:

            if char =="_" or char in letra or char in digito:
                estado=1

            else:
                estado=-1

        if estado==-1:
            return False

    return True


def Numero(lexema):

    if lexema in [""," ","\n"]:
        return False

    estado=0

    for char in lexema:

        if estado==0:

            if char in digito:
                estado=1

            else:
                estado=-1

        elif estado==1:

            if char in digito:
                estado=1

            elif char == tk["punto"]:
                estado=2

            else:
                estado=-1

        elif estado==2:

            if char in digito:
                estado=3

            else:
                estado=-1

        elif estado==3:

            if char in digito:
                estado=3

            else:
                estado=-1

        if estado==-1:

            return False

    return True


# MENU PRINCIPAL

def Basilisk():

    global archivo

    salir=False

    while(salir==False):

        print("""
        ~~~~~~~~~~~~~~~~~
         B A S I L I S K 
        ~~~~~~~~~~~~~~~~~

        1. Cargar un script

        2. Validar con AFD

        3. Validar con AFP

        4. Dibujar diagrama de bloques de código

        5. Salir del programa
        """)


        opcion=input(">> ")

        if opcion=="1":
            
            directorio=input("        Ingrese el directorio del script\n")

            temp=open(directorio)

            if(temp):
                archivo=temp.read()

        
        elif opcion=="2":

            if archivo:
                AFD(archivo)

            else:

                print("No se ingresó el archivo xdV")
                AFD(open("test.js").read())
            

        elif opcion=="3":
            print("op 3")

        elif opcion=="4":
            print("op 4")

        elif opcion=="5":
            print(""".\n..\n...""")
            salir=True    


        else:

            print("Opción no reconocida")


#~~> EJECUCIÓN <~~

Basilisk()

# elpepe=True
# while elpepe:

#     var=input("elpepe? ")
#     print(Variable(var))

