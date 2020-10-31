import traceback

archivo=""

letra=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

digito=["0","1","2","3","4","5","6","7","8","9"]


tk={"if":"if",
    "while":"while",
    "switch":"switch",
    "case":"case",
    "break":"break",
    "default":"default",
    "foreach":"foreach",
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

    comilla, comentario=False, False

    i=0;
    for char in script:

        if char=="\n": #CONTEO DE LINEAS
            linea+=1
            columna=0

        columna+=1
        i+=1

        try:
            char_sig=script[i]

        except:
            char_sig="#"

        try:

            if char not in [" ","\n"] or comilla==True or comentario==True:


                if comentario:
                    
                    if char =="*" and char_sig=="/":

                        comentario=False

                    elif char!="*":        

                        lexema+=char

                elif comilla:
                    
                    if char in tk["comilla"]:
                        
                        lista_tokens.append("string")
                        lista_tokens.append("comilla")

                        comilla=False

                    else:              
                                  
                        lexema+=char
                                

                else:
                
                    if char not in "{}()=,;:'\"":

                        lexema+=char

                    if char_sig in letra+digito+["_"] and char not in "{}()=,;:'\"":

                        pass

                    elif estado==0:                

                        if char==tk["parA"]:
                            estado=1
                            token="parA"

                        elif char==tk["parB"]:
                            estado=1
                            token="parB"

                        elif char==tk["llaveA"]:
                            estado=1
                            token="llaveA"

                        elif char==tk["llaveB"]:
                            estado=1
                            token="llaveB"

                        elif char in tk["comilla"]:
                            comilla=True;

                            estado=1
                            token="comilla"

                        elif char==tk["igual"]:
                            estado=1

                            if char_sig==">":
                                token="asinc"   

                            else:
                                token="igual"

                        elif char==tk["coma"]:
                            estado=1
                            token="coma"

                        elif char==tk["puntocoma"]:
                            estado=1
                            token="puntocoma"

                        elif char==tk["dospuntos"]:
                            estado=1
                            token="dospuntos"
                        
                        elif lexema==tk["if"]:
                            estado=1
                            token="if"

                        elif lexema==tk["while"]:
                            estado=1
                            token="while"

                        elif lexema==tk["switch"]:
                            estado=1
                            token="switch"

                        elif lexema==tk["case"]:
                            estado=1
                            token="case"

                        elif lexema==tk["break"]:
                            estado=1
                            token="break"

                        elif lexema==tk["default"]:
                            estado=1
                            token="default"

                        elif lexema==tk["foreach"]:
                            estado=1
                            token="foreach"

                        elif lexema==tk["in"]:
                            estado=1
                            token="in"

                        elif lexema==tk["var"]:
                            estado=1
                            token="var"

                        elif lexema==tk["let"]:
                            estado=1
                            token="let"

                        elif lexema==tk["const"]:
                            estado=1
                            token="const"

                        elif Bool(lexema):
                            estado=1
                            token="bool"

                        elif Variable(lexema):
                            estado=1
                            token="variable"

                        elif Numero(lexema):
                            estado=1
                            token="numero"  

                        elif char=="/" and char_sig=="*":

                            comentario=True                              
                            estado=1        

                        else:

                            estado=-1


                    if estado==1:
                        
                        if token:
                            
                            lista_tokens.append(token)
                        
                        token, lexema="", ""
                        estado=0


                    elif estado==-1:

                        if token != "":
                            
                            lista_error.append(token)

                        token, lexema="", ""                    
                        estado=0
                    

        except Exception as e:
            
            traceback.print_exc()


    print(lista_tokens)        
    print(lista_error)        


# AP PARA ANÁLISIS SINTÁCTICO
def AP():

    estado, i="q0", 0

    pila=[]

    lista_tokens.append("#")

    while i<len(lista_tokens)-1:

        token, token_sig=lista_tokens[i], lista_tokens[i+1]

        try:
            cabeza_pila=pila[len(pila)-1]

        except:
            cabeza_pila="#"
          
        # print("PILA:  ",pila," |  TOKEN:  '"+token+"'  |  TOKEN_SIG:  '"+token_sig+"'",i)
        
        if estado=="q0":

            pila.append("#")
            estado="q1"

        elif estado=="q1":

            pila.append("S")
            estado="q2"

        elif estado=="q2":#CONSIDERAR USAR ELIF EN CABEZA_PILA

            if cabeza_pila=="S":
                
                pila.pop()

                if token in ["var","let","const"]:
                    
                    if lista_tokens[i+3] in ["variable","comilla","numero","bool"]:

                        pila.append("ASIGNACION")

                    elif lista_tokens[i+3]=="parA":

                        pila.append("DECLARAR_FUNCION")

                elif token=="if":
                    
                    pila.append("SENTENCIA_IF")

                elif token=="while":
                    
                    pila.append("SENTENCIA_WHILE")

                elif token=="foreach":
                    
                    pila.append("SENTENCIA_FOREACH")

                elif token=="switch":
                    
                    pila.append("SENTENCIA_SWITCH")

                elif token=="variable":
                    
                    pila.append("LLAMAR_FUNCION")


            elif cabeza_pila=="ASIGNACION":

                pila.pop()

                for elemento in ["S","puntocoma" ,"VALOR" ,"igual" ,"variable" ,"TIPO_VARIABLE"]:

                    pila.append(elemento)


            elif cabeza_pila=="TIPO_VARIABLE":
                
                pila.pop()

                if token=="var":

                    pila.append("var")

                elif token=="let":

                    pila.append("let")

                elif token=="const":

                    pila.append("const")


            elif cabeza_pila=="VALOR":
                
                pila.pop()

                if token=="variable":

                    pila.append("variable")

                elif token=="numero":

                    pila.append("numero")

                elif token=="comilla":

                    for elemento in ["comilla","string","comilla"]:

                        pila.append(elemento)

                elif token=="bool":

                    pila.append("bool")


            elif cabeza_pila=="SENTENCIA_IF":
                
                pila.pop()

                if lista_tokens[i+2]=="variable":

                    for elemento in ["S","llaveB","S","llaveA","parB","variable","parA","if"]:

                        pila.append(elemento)

                elif lista_tokens[i+2]=="bool":

                    for elemento in ["S","llaveB","S","llaveA","parB","bool","parA","if"]:

                        pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_WHILE":
                
                pila.pop()

                if lista_tokens[i+2]=="variable":

                    for elemento in ["S","llaveB","S","llaveA","parB","variable","parA","while"]:

                        pila.append(elemento)

                elif lista_tokens[i+2]=="bool":

                    for elemento in ["S","llaveB","S","llaveA","parB","bool","parA","while"]:

                        pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_FOREACH":
                
                pila.pop()

                for elemento in ["S","llaveB","S","llaveA","parB","variable","in","variable","parA","foreach"]:

                    pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_SWITCH":
                
                pila.pop()

                for elemento in ["S","llaveB","SENTENCIA_CASE","llaveA","parB","variable","parA","switch"]:

                    pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_CASE":
                
                pila.pop()

                if token=="case":

                    for elemento in ["SENTENCIA_CASE","BREAK","S","dospuntos","VALOR","case"]:

                        pila.append(elemento)

                elif token=="default":

                    for elemento in ["BREAK","S","dospuntos","default"]:

                        pila.append(elemento)


            elif cabeza_pila=="BREAK":
                
                pila.pop()

                if token=="break":

                    for elemento in ["puntocoma","break"]:

                        pila.append(elemento)


            elif cabeza_pila=="DECLARAR_FUNCION":
                
                pila.pop()

                if lista_tokens[i+4]=="variable":

                    for elemento in ["S","llaveB","S","llaveA","asinc","parB","PARAMETRO","parA","igual","variable","TIPO_VARIABLE"]:
                        
                        pila.append(elemento)

                elif lista_tokens[i+4]=="parB":
                    
                    for elemento in ["S","llaveB","S","llaveA","asinc","parB","parA","igual","variable","TIPO_VARIABLE"]:
                    
                        pila.append(elemento)


            elif cabeza_pila=="LLAMAR_FUNCION":
                
                pila.pop()
                
                if lista_tokens[i+2] in ["variable","comilla","numero","valor"]:

                    for elemento in ["S","puntocoma","parB","PARAMETRO","parA","variable"]:
                        
                        pila.append(elemento)

                elif lista_tokens[i+2]=="parB":
                    
                    for elemento in ["S","puntocoma","parB","parA","variable"]:
                    
                        pila.append(elemento)


            elif cabeza_pila=="PARAMETRO":
                
                pila.pop()
                                    
                if token_sig=="coma" or lista_tokens[i+3]=="coma":

                    for elemento in ["PARAMETRO","coma","VALOR"]:

                        pila.append(elemento)
                        
                else:                
                    
                    pila.append("VALOR")


            elif cabeza_pila=="var" and token=="var":
                
                pila.pop()
                i+=1;

            elif cabeza_pila=="let" and token=="let":

                pila.pop()
                i+=1;

            elif cabeza_pila=="const" and token=="const":

                pila.pop()
                i+=1;

            elif cabeza_pila=="variable" and token=="variable":

                pila.pop()
                i+=1;

            elif cabeza_pila=="igual" and token=="igual":

                pila.pop()
                i+=1;

            elif cabeza_pila=="asinc" and token=="asinc":

                pila.pop()
                i+=1;

            elif cabeza_pila=="numero" and token=="numero":

                pila.pop()
                i+=1;

            elif cabeza_pila=="string" and token=="string":

                pila.pop()
                i+=1;

            elif cabeza_pila=="bool" and token=="bool":

                pila.pop()
                i+=1;

            elif cabeza_pila=="comilla" and token=="comilla":

                pila.pop()
                i+=1;

            elif cabeza_pila=="if" and token=="if":

                pila.pop()
                i+=1;

            elif cabeza_pila=="while" and token=="while":

                pila.pop()
                i+=1;

            elif cabeza_pila=="foreach" and token=="foreach":

                pila.pop()
                i+=1;

            elif cabeza_pila=="switch" and token=="switch":

                pila.pop()
                i+=1;

            elif cabeza_pila=="in" and token=="in":

                pila.pop()
                i+=1;

            elif cabeza_pila=="case" and token=="case":

                pila.pop()
                i+=1;

            elif cabeza_pila=="default" and token=="default":

                pila.pop()
                i+=1;

            elif cabeza_pila=="break" and token=="break":

                pila.pop()
                i+=1;

            elif cabeza_pila=="parA" and token=="parA":

                pila.pop()
                i+=1;

            elif cabeza_pila=="parB" and token=="parB":

                pila.pop()
                i+=1;

            elif cabeza_pila=="llaveA" and token=="llaveA":

                pila.pop()
                i+=1;

            elif cabeza_pila=="llaveB" and token=="llaveB":

                pila.pop()
                i+=1;

            elif cabeza_pila=="dospuntos" and token=="dospuntos":

                pila.pop()
                i+=1;

            elif cabeza_pila=="puntocoma" and token=="puntocoma":

                pila.pop()
                i+=1;

            elif cabeza_pila=="coma" and token=="coma":

                pila.pop()
                i+=1;

            elif cabeza_pila=="#" and token_sig=="#":

                pila.pop()
                i+=1;

                estado="q3"

            else:

                print("=============================================")
                print("/////////////////// ERROR ///////////////////")
                print("=============================================\n")
                print("  Se esperaba "+cabeza_pila+"\n")
                input("Presiona enter para salir\n")
                break


        elif estado=="q3":

            pass

    print(pila)

    if pila in [["#"],["#","S"]]:
        print("ES VALIDO")
    
    else:
        print("NO ES VALIDO :-(")

    input("Presiona enter para terminar")
   
#AFD DIVERSOS
def Variable(lexema):

    if lexema in [""," ","\n","true","false"] or lexema in tk.values():
        return False

    estado=0

    for char in lexema.strip():
        
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

    for char in lexema.strip():

        if estado==0:

            if char in digito:
                estado=1

            else:
                estado=-1

        elif estado==1:

            if char in digito:
                estado=1

            elif char == tk["punto"]:
                estado=1

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

def Bool(lexema):

    if lexema in [""," ","\n"]:
        return False

    estado=0

    for char in lexema.strip():

        if estado==0:

            if char =="t":
                estado=1

            elif char=="f":
                estado=11

            else:
                estado=-1

        elif estado==1:

            if char =="r":
                estado=2

            else:
                estado=-1

        elif estado==2:

            if char =="u":
                estado=3

            else:
                estado=-1

        elif estado==3:

            if char =="e":
                estado=20

            else:
                estado=-1

        elif estado==11:

            if char =="a":
                estado=12

            else:
                estado=-1

        elif estado==12:

            if char =="l":
                estado=13

            else:
                estado=-1

        elif estado==13:

            if char =="s":
                estado=14

            else:
                estado=-1

        elif estado==14:

            if char =="e":
                estado=20

            else:
                estado=-1

        elif estado==20:

            if char:
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

            temp=open(directorio,encoding="utf8")

            if(temp):

                archivo=temp.read()
        
        elif opcion=="2":

            if archivo:

                AFD(archivo)

            else:

                print("No se ha ingresado un script")

                AFD(open("test.js",encoding="utf8").read())
            
        elif opcion=="3":

            if archivo:

                if lista_tokens:

                    AP()

                else:

                    print("No se ha hecho el análisis léxico")

            else:
                
                print("No se ha ingresado un script")

                AFD(open("last.js",encoding="utf8").read())
                AP()

        elif opcion=="4":

            print("op 4")

        elif opcion=="5":

            print(""".\n..\n...""")

            salir=True    

        else:

            print("Opción no reconocida")


#~~> EJECUCIÓN <~~

Basilisk()


