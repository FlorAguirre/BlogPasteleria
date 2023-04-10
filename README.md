# Blog de Pastelería - Recetas

IMPORTANTE - 
PARA EL FUNCIONAMIENTO CORRECTO DE LA PAGINA WEB SE DEBERA DESCARGAR POR TERMINAR LOS SIGUIENTES CONCEPTOS:
- CKEDITOR (pip install django-ckeditor )
- PILLOW (Python -m pip install Pillow)

** Hay cuatro videos a modo explicativo de como funciona la pagina. Los videos son: "Video1",;"Video2", "Video3","Video4" **

## Descripción

El blog esta dedicado a la creación de recetas como artículos, categorías y productos. El usuario podrá cargar recetas, productos o categorías y luego podrá también realizar una busqueda de productos y recetas.

## Funcionamiento

Antes de visualizar la página de Inicio el usuario deberá iniciar sesión o registrarse

1. En la página de Inicio (NavBar), se encuentrán los siguientes botones:
- **Crear Receta**: El boton lleva una pagina donde se encuentra el formulario para cargar una receta. Una vez cargada la receta, la misma aparecerá en el listado de recetas con un mensaje de que se guardo exitosamente.

- **Crear Producto**: El boton lleva una pagina donde se encuentra el formulario para cargar un producto. Una vez cargada la categoría, la misma aparecerá en el listado de productos con un mensaje de que se guardo exitosamente.


2. En la página de Categorías (NavBar), se podrá encontrar el listado de las categorías existentes en la base de datos.

3. En la página de Recetas (NavBar), se podrá encontrar el listado de las recetas existentes en la base de datos. Las mismas tienen las opciones de editar, borrar y ver. En la sección de Ver, se podrá dejar comentarios entre usuarios.

4. En la página de Productos (NavBar), se podrá encontrar el listado de los productos existentes en la base de datos. Los mismos tienen las opciones de editar, borrar y ver. 

5. En la página de Acerca de, se podrá encontrar la información sobre el creador del blog.

6. Si iniciaste sesión como SuperUsuario podrás ver la página de Usuarios, donde se listan los usuarios que estan registrados. El SuperUsuario puede editar los permisos de los usuarios.

7. En la página de Buscar, se podrá buscar productos o recetas.

- **Buscar Receta**: El boton lleva a una pagina donde se encuentra el formulario para ingresar el nombre de la receta que se esta buscando. Una vez ingresado, se rediccionará a una pagina donde se figurará la receta encontrada (si es que existe en la base de datos)
- **Buscar Producto**: El boton lleva a una pagina donde se encuentra el formulario para ingresar el nombre del producto que se esta buscando. Una vez ingresado, se rediccionará a una pagina donde se figurará el producto encontrado (si es que existe en la base de datos)

8. En la sección de Agregar Receta..., se podrá visualizar un formulario para crear una nueva receta

9. En la sección de Agregar Categoría..., se podrá visualizar un formulario para crear una nueva categoría

10. En la sección de Agregar Categoría Producto..., se podrá visualizar un formulario para crear un nuevo producto

11. En la sección de Perfil, se podrá visualizar el Perfil del usuario. El mismo se puede editar y se guarda en la base de datos.

12. Selección del Avatar, se deberá hacer click en la imagen del avatar para poder seleccionar un avatar diferente.


