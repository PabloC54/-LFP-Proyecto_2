SimpleSQL CLI, 201901698

=====================
     GUÍA DE USO
=====================

-Ejecutar el archivo simplesqlcli.py, para esto es necesario Python 3.
En caso no se tuviera Python, se puede descargar en https://www.python.org/downloads/ .

-Se abrirá una linea de comandos, donde se pueden ejecutar los comandos propios de SimpleSQL CLI. Para consultar los comandos se puede ejecutar 'ayuda'



COMANDOS:

- Crear un set de archivos

Permite crear un conjunto donde ingresar datos con las mismas características.

Forma de uso:
                CREATE SET < ID >


- Cargar archivos en un set

Permite meter varios archivos dentro de un set creado, especificando el nombre del set y el directorio relativo.

Forma de uso:
                LOAD INTO < set_id > FILES < id >[, <id>]+


- Usar un set

Permite seleccionar un set especificando el nombre. Para los comandos de consulta es necesario seleccionar un set.

Forma de uso:
                USE SET <set_id>


- Seleccionar datos

Permite seleccionar uno o más (o todos) atributos en los archivos AON del set cargado.

Forma de uso:
                SELECT < atributo >[, <atributo>]+ [ WHERE < condiciones > ]
                
                SELECT * [ WHERE <condiciones> ]   


- Listar atributos

Permite listar los atributos de los registros cargados en el set.

Forma de uso:
                LIST ATTRIBUTES


- Cambiar el color de la consola

Permite cambiar el color del texto en consola, especificando el color.

Forma de uso:
                PRINT IN <color>


- Seleccionar el valor máximo

Permite mostrar el valor máximo especificado dentro de los registros cargados en el set seleccionado.

Forma de uso:
                MAX <atributo>


- Seleccionar el valor mínimo

Permite mostrar el valor mínimo especificado dentro de los registros cargados en el set seleccionado.

Forma de uso:
                MIN <atributo>


- Sumar valores

Permite mostrar la suma del valor/valores (o todos los valores) del atributo especificado, dentro de los registros cargados en el set seleccionado.

Forma de uso:
                SUM <atributo> [, <atributo> ] +  
                SUM *


  - Contar valores

Permite mostrar la cuenta de veces que el atributo especificado aparece, dentro de los registros cargados en el set seleccionado.

Forma de uso:
                COUNT <atributo> [, <atributo> ] +  
                COUNT *


- Reportar comando

Permite mostrar en un documento HTML (con el nombre especificado) la consulta del comando especificado.

Forma de uso:
                REPORT TO <id> <comando>


- Cargar script

Permite ejecutar comandos escritos en un documento SIQL.

Forma de uso:
                SCRIPT < direccion > [, < direccion > ]


- Reportar tokens

Permite mostrar los lexemas encontrados en la ejecución del programa, junto a su token correspondiente.

Forma de uso:
                 REPORT TOKENS



ARCHIVOS AON

Para escribir correctamente un archivo aon:


- Se debe escribir la apertura '(' del documento

- Se debe escribir la apertura '<' de un registro

- Se debe escribir la apertura '[' de un atributo

- Se debe escribir un nombre del atributo, no se puede dejar vacío

- Se debe escribir la cerradura ']' de un atributo

- Se debe escribir la igualación '=' del atributo y el valor

- Se debe escribir un valor string entre comillas '"', un número o un valor booleano

- Se puede cerrar el registro con la cerradura '>' de un registro, o se puede escribir otro atributo con una coma ',' y la apertura '[' de un atributo

- Si se cierra el registro, se puede escribir otro registro escribiendo una coma ',' y la apertura '<' de un registro, o se puede cerrar el documento con la cerradura ')' del documento



