**ATENCION**


Para poder ejecutar el siguiente proyecyto en sistemas operativos basados en Debian se requeiren las siguientes dependencias:
- psycopg2==2.9.9
- psycopg2-binary==2.9.9

Tambien se requieren instalar los siguientes componenetes:
- libpq-dev
- postgresql


# ¿Cuales son el top 5 de caracteristicas de arquitectura del diseño actual de tu proyecto?

1. Agilidad:
        El código está dividido en funciones y métodos más pequeños y específicos lo que mejora la modularidad y facilita el mantenimiento y la comprensión del codigo.

2. Seguridad:
        Se utilizó una declaración with para garantizar el cierre adecuado de la conexión y el cursor, lo que ayuda a prevenir posibles problemas de seguridad relacionados con la gestion de recursos. 

3. Mantenibilidad:
        De igual manera se implementaron lineas de codigo que nos ayudan a minimizar la taza de errores y capacidad de mantenimineto, un ejemplo seria una cláusula IF NOT EXISTS al crear la tabla para evitar errores en caso de que la tabla ya exista, mejorando así la capacidad de ejecutar el script de inicialización varias veces sin problemas.

4. Escalabilidad:
        Debido a que el proyecto se programo en Ubuntu server, con ayuda de la integracion de un WEB SERVER GATEWAY INTERFACE se pueden controlar de una manera mas facil las interacciones de los usuarios con el servidor

5. Recuperabilidad:
        Usando el modelo vista-controlador y la utilizacion de entornos virtuales en python, asi como los requisitos listados en un listado de texto se puede hacer un rollback en caso necesario 

# Si la aplicacion migrara a una arquitectura de microservicios, ¿Cuales serian el top 5 de caracteristicas de arquitectura?

1. Tolerancia a fallos
        Debido a que la arquitectura de microservicios se basa en la idea de que los fallos son inevitables. Cada microservicio debe ser diseñado para ser resiliente y tolerante a fallos 
        por lo que el proyecto es mas facil de mantener y corregir errores debido a su modularidad
2. Escalabilidad
        Esto permite una gestión eficiente de los recursos y una escalabilidad mas especifica, ya que solo los servicios que experimentan una carga adicional necesitan escalar, en lugar de escalar toda la aplicación monolítica

3. Reusabilidad
        La implementacion de la base de datos y los modulos que se utilizan permiten al proyecto una facil reutilizacion de componentes para el mismo proyexto o para uno nuevo

4. Rendimiento
        Las caracterizticas del proyecto permiten que los componentes que interactuan entre si puedan seguir funcionando a pesar que se modifiquen las dependencias

5. Usabilidad 
        La aplicacion es adecuada para su utilizacion en caso que se vaya a cambiar
