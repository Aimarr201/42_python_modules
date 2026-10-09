# ![42](https://img.shields.io/badge/-000000?style=for-the-badge&logo=42&logoColor=whit) Python Modules

Este repositorio contiene mi solución a los módulos de python del campus 42. El objetivo de este proyecto es aprender desde los conceptos más básicos de Python hasta la programación orientada a objetos, estructuración de paquetes, manejo de excepciones, manipulación de archivos y gestión de entornos.

## Estructura del Proyecto

El repositorio está dividido en 10 módulos principales (del 0 al 9). A continuación se detalla el contenido y objetivo de cada uno:

### [Module 0: Fundamentos](./module0)
Introducción a la sintaxis básica de Python.
- Variables y tipos de datos básicos.
- Estructuras de control (bucles `for` y `while`, condicionales).
- Funciones básicas e iteración/recursividad.

### [Module 1: Estructuras de Datos](./module1)
Profundización en las estructuras de datos nativas de Python.
- Listas, tuplas, conjuntos (`sets`) y diccionarios.
- Manipulación, análisis y estructuración de datos.

### [Module 2: Manejo de Excepciones](./module2)
Asegurando la robustez del código.
- Bloques `try`, `except` y `finally`.
- Lanzamiento de excepciones predefinidas (`raise`).
- Creación de errores personalizados (*Custom Exceptions*).

### [Module 3: Tipos Avanzados y Dato](./module3)
Gestión de datos más complejos.
- Sistemas de inventario y flujos de datos.
- Mapeo de sistemas de coordenadas.
- Seguimiento de logros y análisis de puntuaciones.

### [Module 4: Manejo de Archivos](./module4)
Operaciones de entrada y salida.
- Lectura y escritura de archivos en diferentes modos.
- Gestión de *streams* de datos.
- Creación de archivos y medidas básicas de seguridad en directorios.

### [Module 5: Pipelines de Datos](./module5)
Procesamiento eficiente de grandes flujos de datos.
- Creación de pipelines.
- Manejo de procesadores de datos.
- Uso de generadores y flujos para optimización de memoria.

### [Module 6: Módulos y Paquetes](./module6)
Estructuración correcta de proyectos grandes.
- Importaciones absolutas y relativas.
- Uso de archivos `__init__.py`.
- Creación de paquetes y subpaquetes.

### [Module 7: Programación Orientada a Objetos](./module7)
Diseño de software utilizando el paradigma de objetos.
- Clases, instancias y constructores.
- Herencia, polimorfismo y encapsulamiento.
- Implementación de clases abstractas

### [Module 8: Entornos y Configuración](./module8)
Preparación del proyecto para el mundo real.
- Creación de archivos `requirements.txt` y `pyproject.toml`.
- Uso de variables de entorno mediante `.env`.
- Gestión de `.gitignore` para omitir archivos sensibles.

## Instalación y Uso

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/42_python_modules.git
   cd 42_python_modules
   ```

2. **Crear y activar un entorno virtual** (Recomendado):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar dependencias** (para el Módulo 8):
   ```bash
   pip install module8/ex2/requirements.txt
   ```

4. **Ejecutar los ejercicios**:
   Puedes navegar a cada directorio y ejecutar los scripts directamente:
   ```bash
   python3 module0/ex00/ft_hello_garden.py
   ```

## Buenas Prácticas y Normas
Este proyecto está diseñado siguiendo las convenciones oficiales de estilo de Python PEP 8.
