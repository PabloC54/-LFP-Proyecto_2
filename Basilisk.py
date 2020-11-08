import traceback, webbrowser
from graphviz import Digraph

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
    "asinc":"=>",
    "variable":"una variable que varia",
    "string":"un texto",
    "numero":"una cantidad numerica",
    "bool":"un valor booleano"
}

tk_d={"if":"Sentencia que corre dependiendo de una condicional",
    "while":"Sentencia que se ejecuta en bucle hasta cumplir cierta condición",
    "switch":"Sentencia que tiene varias ramas de ejecución",
    "case":"Posible instrucción en una sentencia switch",
    "break":"Termina la instrucción de una sentencia case",
    "default":"Secuencia que corre como última opción en una sentencia switch",
    "foreach":"Secuencia que itera en una coleccion de datos",
    "in":"Palabra reservada",
    "dospuntos":"Indica el inicio del bloque de código de una sentencia case",
    "comilla":"Indica el inicio y el cierre de un valor string",
    "coma":"Separa los distintos parámetros con los que se llama a una función",
    "punto":"Separa la parte entera y la parte decimal de un número no entero",
    "var":"Declaración de variable tipo var",
    "let":"Declaración de variable tipo let",
    "const":"Declaración de variable tipo const",
    "igual":"Separa la variable a asignar del valor asignado",
    "puntocoma":"Indica el fin de una sentencia simple",
    "parA":"Indica el inicio de ingreso de parámetros, condición...",
    "parB":"Indica el fin de ingreso de parámetros, condición...",
    "llaveA":"Indica el inicio de un bloque de codigo",
    "llaveB":"Indica el fin fin de un bloque de codigo",
    "asinc":"Separa la asignación de función a una variable",
    "variable":"Un valor sujeto a cambios",
    "string":"Una cadena de texto, números, símbolos...",
    "numero":"Una cantidad numérica",
    "bool":"Un valor booleano"
}

terminales=tk.keys()

no_terminales=["S","ASIGNACION","SENTENCIA_IF","SENTENCIA_WHILE","SENTENCIA_FOREACH","SENTENCIA_SWITCH","DECLARAR_FUNCION","LLAMAR_FUNCION","TIPO_VARIABLE","VALOR","SENTENCIA_CASE","SENTENCIA_DEFAULT","BREAK","PARAMETRO"]



# AFD PARA ANÁLISIS LÉXICO
def AFD(script):

    lista_tokens,lista_reporte, lista_error=[],[],[]
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

                        lista_reporte.append(["Comentario",lexema,"Comentario multilinea","( "+str(linea)+", "+str(columna)+" )"])

                        lexema=""
                        comentario=False


                    elif char!="*" and char!="/":        

                        lexema+=char

                elif comilla:
                    
                    if char in tk["comilla"]:

                        lista_reporte.append(["string",lexema,tk_d["string"],"( "+str(linea)+", "+str(columna-1)+" )"])
                        lista_reporte.append(["comilla",char,tk_d["comilla"],"( "+str(linea)+", "+str(columna)+" )"])                        
                        lista_tokens.append("string")
                        lista_tokens.append("comilla")

                        lexema=""
                        comilla=False

                    else:              
                                  
                        lexema+=char
                                

                else:
                
                    if char in letra+digito+["_","'",'"']:

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

                            if lexema:

                                lista_reporte.append([token,lexema,tk_d[token],"( "+str(linea)+", "+str(columna)+" )"])

                            else:

                                 lista_reporte.append([token,char,tk_d[token],"( "+str(linea)+", "+str(columna)+" )"])
                                 
                        
                        token, lexema="", ""
                        estado=0


                    elif estado==-1:

                        if lexema not in ">/*" and char not in ">/*":

                            if lexema:

                                lista_error.append([lexema,"( "+str(linea)+", "+str(columna)+" )"])

                            else:

                                lista_error.append([char,"( "+str(linea)+", "+str(columna)+" )"])
                                 

                        token, lexema="", ""                    
                        estado=0
                    

        except Exception as e:
            
            traceback.print_exc()

    print(lista_tokens)
    print(lista_error)
  

    #===//==> R E P O R T E S <==//===

    if lista_reporte:

        Report(lista_reporte,"reporte_tokens",["Token","Lexema","Descripción","Línea y columna"])   

    if lista_error:

        Report(lista_error,"reporte_error",["Lexema","Línea y columna"])   


    return lista_tokens


# AP PARA ANÁLISIS SINTÁCTICO
def AP(lista_tokens):

    lista_procedimientos=[]
    # vacio="\u03BB"
    vacio="lambda"
    estado, i="q0", 0
    pila=[]

    lista_tokens.append("#")

    while i<len(lista_tokens)-1 or pila:

        token, token_sig="",""

        try:
            token, token_sig=lista_tokens[i], lista_tokens[i+1]

        except: pass

        tam=10

        if i+tam>=len(lista_tokens):
            tam=len(lista_tokens)-i

        entrada_temp=lista_tokens[i:i+tam]        
        pila_temp=pila[::-1].copy()
        
        print("      \x1b[4;30;47m"+"  PILA  "+"\x1b[0m\n",pila_temp,"\n\n      \x1b[4;30;47m"+"  ENTRADA  "+"\x1b[0m\n",entrada_temp,"\n")

        if pila:
            cabeza_pila=pila[len(pila)-1]
        else:
            cabeza_pila=vacio

        estado_inicial, simbolo_entrada, simbolo_salida=estado,"",""   

        if estado=="q0":

            simbolo_entrada=vacio
            simbolo_salida="#"

            pila.append("#")
            estado="q1"

        elif estado=="q1":
            
            simbolo_entrada=vacio
            simbolo_salida="S"
            cabeza_pila=vacio

            pila.append("S")
            estado="q2"

        elif estado=="q2":

            if cabeza_pila=="S":
                
                simbolo_entrada=vacio
                
                pila.pop()

                if token in ["var","let","const"]:
                    
                    if lista_tokens[i+3] in ["variable","comilla","numero","bool"]:

                        simbolo_salida="ASIGNACION"
                        pila.append("ASIGNACION")

                    elif lista_tokens[i+3]=="parA":

                        simbolo_salida="DECLARAR FUNCION"
                        pila.append("DECLARAR_FUNCION")

                elif token=="if":
                    
                    simbolo_salida="SENTENCIA_IF"
                    pila.append("SENTENCIA_IF")

                elif token=="while":
                    
                    simbolo_salida="SENTENCIA_WHILE"
                    pila.append("SENTENCIA_WHILE")

                elif token=="foreach":
                    
                    simbolo_salida="SENTENCIA_FOREACH"
                    pila.append("SENTENCIA_FOREACH")

                elif token=="switch":
                    
                    simbolo_salida="SENTENCIA_SWITCH"
                    pila.append("SENTENCIA_SWITCH")

                elif token=="variable":

                    simbolo_salida="SENTENCIA_FUNCION"
                    pila.append("LLAMAR_FUNCION")


            elif cabeza_pila=="ASIGNACION":

                simbolo_entrada=vacio

                pila.pop()

                for elemento in ["S","puntocoma" ,"VALOR" ,"igual" ,"variable" ,"TIPO_VARIABLE"]:

                    simbolo_salida=elemento+" "+simbolo_salida
                    pila.append(elemento)


            elif cabeza_pila=="TIPO_VARIABLE":
                
                simbolo_entrada=vacio

                pila.pop()

                if token=="var":

                    simbolo_salida="var"
                    pila.append("var")

                elif token=="let":

                    simbolo_salida="let"
                    pila.append("let")

                elif token=="const":

                    simbolo_salida="const"
                    pila.append("const")


            elif cabeza_pila=="VALOR":

                simbolo_entrada=vacio
                
                pila.pop()

                if token=="variable":

                    simbolo_salida="variable"
                    pila.append("variable")

                elif token=="numero":

                    simbolo_salida="numero"
                    pila.append("numero")

                elif token=="comilla":

                    for elemento in ["comilla","string","comilla"]:

                        simbolo_salida=elemento+" "+simbolo_salida
                        pila.append(elemento)

                elif token=="bool":

                    simbolo_salida="bool"
                    pila.append("bool")


            elif cabeza_pila=="SENTENCIA_IF":
                
                simbolo_entrada=vacio
                
                pila.pop()

                if lista_tokens[i+2]=="variable":

                    for elemento in ["S","llaveB","S","llaveA","parB","variable","parA","if"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)

                elif lista_tokens[i+2]=="bool":

                    for elemento in ["S","llaveB","S","llaveA","parB","bool","parA","if"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_WHILE":

                simbolo_entrada=vacio
                
                pila.pop()

                if lista_tokens[i+2]=="variable":

                    for elemento in ["S","llaveB","S","llaveA","parB","variable","parA","while"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)

                elif lista_tokens[i+2]=="bool":

                    for elemento in ["S","llaveB","S","llaveA","parB","bool","parA","while"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_FOREACH":
                
                simbolo_entrada=vacio
                
                pila.pop()

                for elemento in ["S","llaveB","S","llaveA","parB","variable","in","variable","parA","foreach"]:

                    simbolo_salida=elemento+" "+simbolo_salida

                    pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_SWITCH":
                
                simbolo_entrada=vacio
                
                pila.pop()

                for elemento in ["S","llaveB","SENTENCIA_CASE","llaveA","parB","variable","parA","switch"]:

                    simbolo_salida=elemento+" "+simbolo_salida

                    pila.append(elemento)

            
            elif cabeza_pila=="SENTENCIA_CASE":
                
                simbolo_entrada=vacio
                
                pila.pop()

                if token=="case":

                    for elemento in ["SENTENCIA_CASE","BREAK","S","dospuntos","VALOR","case"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)

                elif token=="default":

                    for elemento in ["BREAK","S","dospuntos","default"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)


            elif cabeza_pila=="BREAK":
                
                simbolo_entrada=vacio
                
                pila.pop()

                if token=="break":

                    for elemento in ["puntocoma","break"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)


            elif cabeza_pila=="DECLARAR_FUNCION":
                
                simbolo_entrada=vacio
                
                pila.pop()

                if lista_tokens[i+4]=="variable":

                    for elemento in ["S","llaveB","S","llaveA","asinc","parB","PARAMETRO","parA","igual","variable","TIPO_VARIABLE"]:

                        simbolo_salida=elemento+" "+simbolo_salida
                        
                        pila.append(elemento)

                elif lista_tokens[i+4]=="parB":
                    
                    for elemento in ["S","llaveB","S","llaveA","asinc","parB","parA","igual","variable","TIPO_VARIABLE"]:

                        simbolo_salida=elemento+" "+simbolo_salida
                    
                        pila.append(elemento)


            elif cabeza_pila=="LLAMAR_FUNCION":
                
                simbolo_entrada=vacio
                
                pila.pop()
                
                if lista_tokens[i+2] in ["variable","comilla","numero","valor"]:

                    for elemento in ["S","puntocoma","parB","PARAMETRO","parA","variable"]:

                        simbolo_salida=elemento+" "+simbolo_salida
                        
                        pila.append(elemento)

                elif lista_tokens[i+2]=="parB":
                    
                    for elemento in ["S","puntocoma","parB","parA","variable"]:

                        simbolo_salida=elemento+" "+simbolo_salida
                    
                        pila.append(elemento)


            elif cabeza_pila=="PARAMETRO":
                
                simbolo_entrada=vacio
                
                pila.pop()
                                    
                if token_sig=="coma" or lista_tokens[i+3]=="coma":

                    for elemento in ["PARAMETRO","coma","VALOR"]:

                        simbolo_salida=elemento+" "+simbolo_salida

                        pila.append(elemento)
                        
                else:                
                    
                    pila.append("VALOR")


            elif cabeza_pila=="var" and token=="var":

                simbolo_entrada="var"
                simbolo_salida=vacio
                
                pila.pop()
                i+=1;

            elif cabeza_pila=="let" and token=="let":

                simbolo_entrada="let"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="const" and token=="const":

                simbolo_entrada="const"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="variable" and token=="variable":

                simbolo_entrada="variable"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="igual" and token=="igual":

                simbolo_entrada="igual"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="asinc" and token=="asinc":

                simbolo_entrada="asinc"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="numero" and token=="numero":

                simbolo_entrada="numero"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="string" and token=="string":

                simbolo_entrada="string"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="bool" and token=="bool":

                simbolo_entrada="bool"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="comilla" and token=="comilla":

                simbolo_entrada="comilla"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="if" and token=="if":

                simbolo_entrada="if"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="while" and token=="while":

                simbolo_entrada="while"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="foreach" and token=="foreach":

                simbolo_entrada="foreach"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="switch" and token=="switch":

                simbolo_entrada="switch"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="in" and token=="in":

                simbolo_entrada="in"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="case" and token=="case":

                simbolo_entrada="case"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="default" and token=="default":

                simbolo_entrada="default"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="break" and token=="break":

                simbolo_entrada="break"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="parA" and token=="parA":

                simbolo_entrada="parA"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="parB" and token=="parB":

                simbolo_entrada="parB"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="llaveA" and token=="llaveA":

                simbolo_entrada="llaveA"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="llaveB" and token=="llaveB":

                simbolo_entrada="llaveB"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="dospuntos" and token=="dospuntos":

                simbolo_entrada="dospuntos"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="puntocoma" and token=="puntocoma":

                simbolo_entrada="puntocoma"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="coma" and token=="coma":

                simbolo_entrada="coma"
                simbolo_salida=vacio

                pila.pop()
                i+=1;

            elif cabeza_pila=="#":

                simbolo_entrada=vacio
                simbolo_salida=vacio

                pila.pop()
                i+=1;

                estado="q3"

            else:

                print("=========================================================")
                print("//////////////////////// ERROR //////////////////////////")
                print("=========================================================\n")
                print("  Se esperaba '"+cabeza_pila+"'. Se recibió '"+token+"'  ["+str(i)+"]")
                print("\n=========================================================")
                break

        elif estado=="q3":

            pass

        estado_final=estado
        
        transicion_temp= "("+estado_inicial+","+simbolo_entrada+","+cabeza_pila+";"+estado_final+","+simbolo_salida+")"
        print("      \x1b[4;30;47m"+"  TRANSICIÓN  "+"\x1b[0m\n",transicion_temp+"\n")

        lista_procedimientos.append([pila_temp,entrada_temp,transicion_temp])

        input(".. [ Presiona enter ] ..\n\n")


    if pila==[]:
        print("\x1b[6;30;42m"+"  ANÁLISIS SINTÁCTICO REALIZADO CON ÉXITO, ENTRADA VÁLIDA  "+"\x1b[0m\n")
        lista_procedimientos.append(["--","--","ACEPTACION"])
    
    else:
        print("\x1b[6;30;41m"+"  ANÁLISIS SINTÁCTICO FALLIDO, ENTRADA NO VÁLIDA  "+"\x1b[0m\n")
        lista_procedimientos.append(["--","--","NO VÁLIDO"])
        

    Report(lista_procedimientos,"procedimiento_pila",["Pila","Entrada","Transición"])
   

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


# GENERADOR DE REPORTES
def Report(lista, nombre, encabezado):

    html_file = open(nombre+".html", "w")

    html_file.write(  # ENCABEZADO
        "<!DOCTYPE html>\n"
        + "\t<html>\n"
        + "\t\t<head>\n"
        + "\t\t\t<title>"+nombre+"</title>\n"
        + "\t\t\t<link rel='stylesheet' type='text/css' href='style.css'/>\n"
        + "\t\t</head>\n"
        + "\t\t<body>\n"
    )

    html_file.write( # ENCABEZADO DE LA TABLA
        "\t\t\t<table class='container'>\n"
        + "\t\t\t\t<thead>\n"  
        + "\t\t\t\t\t<tr>\n")

    for elemento in encabezado:

        html_file.write("\t\t\t\t\t\t<th><h1>{}</h1></th>\n".format(elemento))

    html_file.write( # CUERPO DE LA TABLA
        "\t\t\t\t\t</tr>\n"
        + "\t\t\t\t</thead>\n\n"
        +"\t\t\t\t<tbody>\n") 


    for tupla in lista:

        html_file.write("\t\t\t\t\t<tr>\n")

        for elemento in tupla:

            html_file.write("\t\t\t\t\t\t<td>{}</td>\n".format(elemento))

        html_file.write("\t\t\t\t\t</tr>\n\n")

    html_file.write(
        "\t\t\t\t</tbody>\n"
        + "\t\t\t</table>\n"
        + "\t\t</body>\n"
        + "\t</html>")
        

    webbrowser.open(nombre+".html") 

# GENERADOR DE DIAGRAMA DE BLOQUES DE CÓDIGO
def Bloques(lista_tokens):

    grafo=Digraph(name="quepedoooo")
    
    with grafo.subgraph(name='cluster_0') as c:
        c.attr(style='filled', color='lightgrey')
        c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])

    with grafo.subgraph(name='cluster_1') as c:
        c.attr(style='filled', color='lightgrey')
        c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])

    grafo.edge('a0', 'b0')

    grafo.render('Grafo', view=True)

# MENU PRINCIPAL
def Basilisk():

    global archivo
    lista_tokens=[]

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

            if temp:

                archivo=temp.read()
                print("\nArchivo cargado con éxito")

            else:

                print("\nArchivo no encontrado\n")
        

        elif opcion=="2":

            if archivo:

                lista_tokens=AFD(archivo)

            else:

                print("No se ha ingresado un script\n")
                directorio=input("        Ingrese el directorio del script\n")
                    
                try:
                    archivo=open(directorio, encoding="utf8").read()
                    
                except:
                    print("\nArchivo no encontrado\n")   

                if archivo:    

                    lista_tokens=AFD(archivo)
            

        elif opcion=="3":

            if archivo:

                if lista_tokens:

                    AP(lista_tokens)

                else:

                    print("No se ha hecho el análisis léxico")
                        
                    lista_tokens=AFD(archivo)
                    AP(lista_tokens)

            else:
                
                print("No se ha ingresado un script")
                directorio=input("        Ingrese el directorio del script\n")

                try:
                    archivo=open(directorio, encoding="utf8").read()
                    
                except:
                    print("\nArchivo no encontrado\n")        

                if archivo:

                    lista_tokens=AFD(archivo)
                    AP(lista_tokens)



        elif opcion=="4":

            print("NO DISPONIBLE")


        elif opcion=="5":

            print(""".\n..\n...""")

            salir=True    

        else:

            if opcion:

                print("Opción no reconocida")


#==//==> EJECUCIÓN <==//==

Basilisk()

