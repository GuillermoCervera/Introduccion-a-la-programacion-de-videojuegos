# Portfolio

60% de la Nota Final

- Primera Convocatoria 28/05/2021
- Segunda Convocatoria 09/07/2021

Para hacer las entregas hay que hacer un tag al repositorio en una fecha anterior a la fecha de entrega de la actividad, y pegar el enlace al tag del repositorio en la actividad de blackboard.

# Actividad 1

Peso - 30% del PortFolio

- Fecha de Entrega 28/05/2021

1. Crear un programa en el cual se vea un personaje caminando. Se provee el fichero "res/walking_animation.png", que tiene una secuencia de una animación para un personaje andando a izquierda y a derecha. Usando dicha animación el personaje deberá andar de izquierda a derecha de la pantalla, y cuando llegue al borde deberá dar la vuelta. Intentando usar el mejor método posible.

2. Crear un programa que use una fuente bitmap para pintar un texto en pantalla. En la dirección https://github.com/ianhan/BitmapFonts hay multitud de fuentes rasterizadas usadas en los tiempos de la demo scene. Usando una de ellas a libre elección escribir en pantalla un párrafo cualquiera en una línea que haga scroll por pantalla. Intentando mantener en memoría el mínimo número de surfaces posibles y usando subsurfaces.

# Actividad 2

Peso - 30% del PortFolio

- Fecha de Entrega 28/05/2021

Desarrollar el algoritmo de A Star. En clase se ha explicado el funcionamiento del algoritmo A* para encontrar el camino más corto entre dos puntos. En la carpeta *a_star* hay un fichero a_star.py que contiene código fuente de apoyo y un maze.bmp que contiene el diseño de un laberinto de prueba.

En el código adjunto se incluye el prototipo de una función *calc_path*, que debe implementar el algoritmo A*. Este algoritmo debe usar la clase *Node* (para cada nodo que se recorre) definida en el mismo fichero como apoyo, y al final del algoritmo estos nodos tendrán cada uno el padre desde el que fueron alcanzados. De esta manera, la función ya implementada *return_path* será capaz de determinar el camino, una vez se cumpla la condición de salida (haber llegado al final). También se proveen tres funciones para distintas heurísticas, se puede usar libremente cualquiera de ellas.

Se provee también de toda la infraestructura para cargar el fichero del laberinto, y construirlo como una lista bidimensional (que se deberá usar para conocer el entorno, por filas, columnas), donde el primer nivel son las filas y luego las columnas. En cada punto del laberinto se tiene un 0 si esa baldosa es transitable, o un 1 si es una pared. Al clickar sobre el mapa una vez, se determina el punto de salida, y otro click determina el punto de finalización, y en ese momento se llama a la función para calcular el camino más corto.