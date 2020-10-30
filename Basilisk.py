import traceback

archivo=""

letra=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

digito=["0","1","2","3","4","5","6","7","8","9"]


tk={ "if":"if",
    "while":"while",
    "switch":"switch",
    "foreach":"foreach",
    "case":"case",
    "in":"in",
    "dospuntos":":",
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

terminales=tk.keys()

no_terminales=["S","ASIGNACION","SENTENCIA_IF","SENTENCIA_WHILE","SENTENCIA_FOREACH","SENTENCIA_SWITCH","DECLARAR_FUNCION","LLAMAR_FUNCION","TIPO_VARIABLE","VALOR","SENTENCIA_CASE","SENTENCIA_DEFAULT","BREAK","PARAMETRO"]

lista_tokens, lista_error=[], []


# AFD PARA ANÁLISIS LÉXICO
def AFD(script):

    global tk, lista_tokens, lista_error
    lista_tokens,lista_error=[],[]

    estado, linea, columna=0, 1, 0
    lexema, token, char_sig= "","",""

    i=0;
    for char in script:

        i+=1
        

        try:
            char_sig=script[i]
        except:
            char_sig="#"

        print(char, estado)
        columna+=1

        if char=="\n": #CONTEO DE LINEAS
            linea+=1
            columna=0

        try:

            if char_sig in letra or char in digito or char=="_":
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
                
                lista_tokens.append(token)
                token, lexema="", ""
                
                estado=0

            elif estado==-1:

                if char not in [""," ","\n"]:
                    lista_error.append(token)

                token, lexema="", ""
                
                estado=0
                

        except Exception as e:
            print("=================, fallo en "+char,estado)
            traceback.print_exc()


    print(lista_tokens)        
    print(lista_error)        


# AP PARA ANÁLISIS SINTÁCTICO
def AP():

    estado, i="q0", 0

    pila=[]

    lista_tokens.append("#")

    while i<len(lista_tokens-1):

        token, token_sig, cabeza_pila=lista_tokens[i], lista_tokens[i+1], pila[len(pila)-1]
        
        if estado=="q0":

            pila.append("#")
            estado="q1"

        elif estado=="q1":

            pila.append("S")
            estado="q2"

        elif estado=="q2":#CONSIDERAR USAR ELIF EN CABEZA_PILA

            if cabeza_pila=="S":

                if token in ["var","let","const"]:

                    pila.append("ASIGNACION")
                    #FIX THIS, TAMBIEN DECLARAR_FUNCION INICIA CON tipo de variable

                elif token=="if":

                    pila.append("SENTENCIA_IF")
                    print("iffff")

                elif token=="while":

                    pila.append("SENTENCIA_WHILE")

                elif token=="foreach":

                    pila.append("SENTENCIA_FOREACH")

                elif token=="switch":

                    pila.append("SENTENCIA_SWITCH")

                elif token=="variable":

                    pila.append("LLAMAR_FUNCION")


            if cabeza_pila=="ASIGNACION":

                pila.append("S","puntocoma" ,"VALOR" ,"igual" ,"variable" ,"TIPO_VARIABLE")


            if cabeza_pila=="TIPO_VARIABLE":

                if token=="var":

                    pila.append("var")

                elif token=="let":

                    pila.append("let")

                elif token=="const":

                    pila.append("const")


            if cabeza_pila=="VALOR":

                if token=="variable":

                    pila.append("variable")

                elif token=="numero":

                    pila.append("numero")

                elif token=="string":

                    pila.append("string")

                elif token=="bool":

                    pila.append("bool")


            if cabeza_pila=="SENTENCIA_IF":

                if lista_tokens[i+2]=="variable":

                    pila.append("S","llaveB","S","llaveA","parB","variable","parA","if")

                elif lista_tokens[i+2]=="bool":

                    pila.append("S","llaveB","S","llaveA","parB","bool","parA","if")

            
            if cabeza_pila=="SENTENCIA_WHILE":

                if lista_tokens[i+2]=="variable":

                    pila.append("S","llaveB","S","llaveA","parB","variable","parA","while")

                elif lista_tokens[i+2]=="bool":

                    pila.append("S","llaveB","S","llaveA","parB","bool","parA","while")

            
            if cabeza_pila=="SENTENCIA_FOREACH":

                    pila.append("S","llaveB","S","llaveA","parB","variable","in","variable","parA","foreach")

            
            if cabeza_pila=="SENTENCIA_SWITCH":

                    pila.append("S","llaveB","SENTENCIA_CASE","llaveA","parB","variable","parA","switch")

            
            if cabeza_pila=="SENTENCIA_CASE":

                if token=="case":

                    pila.append("SENTENCIA_CASE","BREAK","S","dospuntos","VALOR","case")

                elif token=="default":

                    pila.append("BREAK","S","dospuntos","default")

                else:

                    print("nada")


            if cabeza_pila=="BREAK":

                if token=="break":

                    pila.append("puntocoma","break")

                else:

                    print("nada")


            if cabeza_pila=="DECLARAR_FUNCION":

                print("PENDIENTE")


            if cabeza_pila=="LLAMAR_FUNCION":

                pila.append("S","puntocoma","parB","")
                print("PENDIENTE")


            if cabeza_pila=="PARAMETRO":

                if token_sig=="coma":

                    pila.append("PARAMETRO","coma","variable")

                else:
                    
                    pila.append("variable")


            if cabeza_pila=="var" and token=="var":

                pila.pop()
                i+=1;

            if cabeza_pila=="let" and token=="let":

                pila.pop()
                i+=1;

            if cabeza_pila=="const" and token=="const":

                pila.pop()
                i+=1;

            if cabeza_pila=="variable" and token=="variable":

                pila.pop()
                i+=1;

            if cabeza_pila=="igual" and token=="igual":

                pila.pop()
                i+=1;

            if cabeza_pila=="numero" and token=="numero":

                pila.pop()
                i+=1;

            if cabeza_pila=="string" and token=="string":

                pila.pop()
                i+=1;

            if cabeza_pila=="bool" and token=="bool":

                pila.pop()
                i+=1;

            if cabeza_pila=="if" and token=="if":

                pila.pop()
                i+=1;

            if cabeza_pila=="while" and token=="while":

                pila.pop()
                i+=1;

            if cabeza_pila=="foreach" and token=="foreach":

                pila.pop()
                i+=1;

            if cabeza_pila=="switch" and token=="switch":

                pila.pop()
                i+=1;

            if cabeza_pila=="in" and token=="in":

                pila.pop()
                i+=1;

            if cabeza_pila=="case" and token=="case":

                pila.pop()
                i+=1;

            if cabeza_pila=="default" and token=="default":

                pila.pop()
                i+=1;

            if cabeza_pila=="break" and token=="break":

                pila.pop()
                i+=1;

            if cabeza_pila=="parA" and token=="parA":

                pila.pop()
                i+=1;

            if cabeza_pila=="parB" and token=="parB":

                pila.pop()
                i+=1;

            if cabeza_pila=="llaveA" and token=="llaveA":

                pila.pop()
                i+=1;

            if cabeza_pila=="llaveB" and token=="llaveB":

                pila.pop()
                i+=1;

            if cabeza_pila=="dospuntos" and token=="dospuntos":

                pila.pop()
                i+=1;

            if cabeza_pila=="puntocoma" and token=="puntocoma":

                pila.pop()
                i+=1;

            if cabeza_pila=="coma" and token=="coma":

                pila.pop()
                i+=1;

            if cabeza_pila=="#" and token_sig=="#":

                pila.pop()
                i+=1;

                estado="q3"


        elif estado=="q3":

            print("COMOOOOOOOO")


    if pila:
        print("ES VALIDO")
    
    else:
        print("NO ES VALIDO :-(")

   
#AFD DIVERSOS
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

        3. Validar con AP

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

                print("No se ha ingresado un script")

                AFD(open("test.js").read())
            
        elif opcion=="3":

            if archivo:

                if lista_tokens:

                    AP()

                else:

                    print("No se ha hecho el análisis léxico")

            else:
                
                print("No se ha ingresado un script")

                AP(AFD(open("test.js").read()))

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

