# Arbol Fractal en Python (L-System) V1.

Este script utiliza la librería `turtle` en Python para dibujar un árbol fractal. El árbol se genera utilizando un sistema de L (Lindenmayer system), un método de modelado fractal que aplica reglas recursivas para crear formas complejas.

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>
<span><img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"/></span>

## Resultado
<img src="https://github.com/user-attachments/assets/3b66dfad-38f1-4421-9e88-afa9b2c3f18d" width="640px">

## Explicación del Código

### Importaciones
```python
from turtle import *
import time
import random
```
El código importa la librería `turtle` para dibujar gráficos, así como `time` y `random` para funciones de tiempo y generación de números aleatorios.

### Configuración Inicial
```python
speed(10)
rt(-90)
angle = 15
```
- `speed(10)`: Ajusta la velocidad de dibujo del turtle.
- `rt(-90)`: Rota el turtle 90 grados a la izquierda para que empiece a dibujar hacia arriba.
- `angle = 15`: Define el ángulo base de ramificación.

### Función Recursiva `y`
```python
def y(sz, level):
    if level > 0:
        colormode(255)
        if level < 3:
            pensize(7-level)
            largo = 0.8 * (sz + random.randrange(-15,5))
        else:
            pensize(int(level/1.1)+2)
            largo = 0.8 * (sz + random.randrange(0,16))

        pencolor(100, 200//level, 0)
        fd(sz)
        angulo = angle + random.randrange(-int(level*1.5),int(level*1.2))
        rt(angulo)
        
        y(largo, level-1)
        pencolor(100, 200//level, 0)
        lt( 2 * angulo )
        y(largo, level-1)
        pencolor(100, 200//level, 0)
        rt(angulo)
        fd(-sz)
```
Esta función es recursiva y se llama a sí misma para dibujar ramas del árbol. Los parámetros son:
- `sz`: El tamaño de la rama.
- `level`: El nivel de recursión.

Dentro de la función:
- `colormode(255)`: Ajusta el modo de color.
- `pensize(...)`: Ajusta el grosor del lápiz basado en el nivel.
- `pencolor(...)`: Cambia el color del lápiz.
- `fd(sz)`: Avanza el lápiz para dibujar una rama.
- `rt(angulo)`: Gira el lápiz a la derecha.
- `lt(2 * angulo)`: Gira el lápiz a la izquierda dos veces el ángulo.
- `fd(-sz)`: Retrocede el lápiz para volver a la base de la rama actual.

### Configuración de la Pantalla y Llamada Inicial
```python
setup(800, 480, 0, 0)
penup()
goto(0,-240)
pendown()
y(50, 13)
exitonclick()
```
- `setup(800, 480, 0, 0)`: Configura el tamaño de la ventana del dibujo.
- `penup()`, `goto(0,-240)`, `pendown()`: Posiciona el turtle en la base del árbol.
- `y(50, 13)`: Llama a la función `y` con un tamaño inicial de 50 y nivel de recursión de 13.
- `exitonclick()`: Espera un clic para cerrar la ventana del dibujo.

