# Blog de Pastelería - Recetas

IMPORTANTE - 
PARA EL FUNCIONAMIENTO CORRECTO DE LA PAGINA WEB SE DEBERA DESCARGAR POR TERMINAR LOS SIGUIENTES CONCEPTOS:
- CKEDITOR (pip install django-ckeditor )
- PILLOW (Python -m pip install Pillow)

** Hay dos videos a modo explicativo de como funciona la pagina. Los videos son: "Crear" y "Buscar" **

## Descripción

El blog esta dedicado a la creación de recetas como artículos, categorías y productos. El usuario podrá cargar recetas, productos o categorías y luego podrá también realizar una busqueda de productos y recetas.

## Funcionamiento

1. En la página de Inicio (NavBar), se encuentrán los siguientes botones:
- **Crear Receta**: El boton lleva una pagina donde se encuentra el formulario para cargar una receta. Una vez cargada la receta, la misma aparecerá en el listado de recetas con un mensaje de que se guardo exitosamente.
- **Crear Categoría**: El boton lleva una pagina donde se encuentra el formulario para cargar una categoría. Una vez cargada la categoría, la misma aparecerá en el listado de categorías con un mensaje de que se guardo exitosamente.
- **Crear Producto**: El boton lleva una pagina donde se encuentra el formulario para cargar un producto. Una vez cargada la categoría, la misma aparecerá en el listado de productos con un mensaje de que se guardo exitosamente.

- **Buscar Receta**: El boton lleva a una pagina donde se encuentra el formulario para ingresar el nombre de la receta que se esta buscando. Una vez ingresado, se rediccionará a una pagina donde se figurará la receta encontrada (si es que existe en la base de datos)
- **Buscar Producto**: El boton lleva a una pagina donde se encuentra el formulario para ingresar el nombre del producto que se esta buscando. Una vez ingresado, se rediccionará a una pagina donde se figurará el producto encontrado (si es que existe en la base de datos)


2. En la página de Categorías (NavBar), se podrá encontrar el listado de las categorías existentes en la base de datos.

3. En la página de Categorías Recetas (NavBar), se podrá encontrar el listado de las recetas existentes en la base de datos.

4. En la página de Categorías Productos (NavBar), se podrá encontrar el listado de los productos existentes en la base de datos.


## Requisitos de la entrega:

1. Link de GitHub con el proyecto totalmente subido a la plataforma: https://github.com/FlorAguirre/BlogRecetas

2. Herencia de HTML. (Se encuentrán en todos los HTML)

3. Por lo menos 3 clases en models: Se han creado models de 
- Product
- Article
- Category
- Page

4. Un formulario para buscar algo en la BD: Realice dos formularios para busqueda en la base de datos:
- Para Productos
- Para Recetas

5. Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades: Hecho.



