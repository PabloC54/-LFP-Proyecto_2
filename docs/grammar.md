    =====> A L F A B E T O <=====
    
    
        >>> TERMINALES <<<
        
    var  let  const  variable  numero  string  bool  if  while  foreach  switch  case
    in  default  break  igual  parA  parB  llaveA  llaveB  dospuntos  puntocoma  coma
    
        
        >>> NO TERMINALES <<<
        
    S  ASIGNACION  SENTENCIA_IF  SENTENCIA_WHILE  SENTENCIA_FOREACH
    SENTENCIA_SWITCH  DECLARAR_FUNCION  LLAMAR_FUNCION  TIPO_VARIABLE
    VALOR  SENTENCIA_CASE  SENTENCIA_DEFAULT  BREAK  PARAMETRO
    
    
    =====> G R A M Á T I C A <=====
    
    
    S ~~> ASIGNACION
        | SENTENCIA_IF
        | SENTENCIA_WHILE
        | SENTENCIA_FOREACH
        | SENTENCIA_SWITCH
        | DECLARAR_FUNCION
        | LLAMAR_FUNCION
        | ɛ
        
    
    ASIGNACION ~~> TIPO_VARIABLE variable igual VALOR puntocoma S
    
    TIPO_VARIABLE ~~> var
                    | let
                    | const
    
    VALOR ~~> variable
            | numero
            | comilla string comilla
            | bool

    SENTENCIA_IF ~~> if parA variable parB llaveA S llaveB S
                    | if parA bool parB llaveA S llaveB S
    
    SENTENCIA_WHILE ~~> while parA variable parB llaveA S llaveB S
                        | while parA bool parB llaveA S llaveB S
    
    SENTENCIA_FOREACH ~~> foreach parA variable in variable parB llaveA S llaveB S
    
    SENTENCIA_SWITCH ~~> switch parA variable parB llaveA SENTENCIA_CASE llaveB S
    
    SENTENCIA_CASE ~~> case VALORdospuntos S BREAK SENTENCIA_CASE
                     | default VALORdospuntos S BREAK
                     | ɛ
                                
    BREAK ~~> break puntocoma
            | ɛ
    
    DECLARAR_FUNCION ~~> TIPO_VARIABLE variable igual parA PARAMETRO parB asinc llaveA S llaveB S
                       | TIPO_VARIABLE variable igual parA parB asinc llaveA S llaveB S
    
    LLAMAR_FUNCION ~~> variable parA PARAMETRO parB puntocoma S
                        | variable parA parB puntocoma S
    
    PARAMETRO ~~> VALOR
                | VALOR coma PARAMETRO
      
