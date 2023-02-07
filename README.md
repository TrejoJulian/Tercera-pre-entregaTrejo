# Tercera-pre-entregaTrejo

Link de la pagina de inicio: http://127.0.0.1:8000/AppVeterinaria/inicio/

# Vistas:

El proyecto cuenta con varias vistas detalladas a continuación:

## Inicio:

Url: http://127.0.0.1:8000/AppVeterinaria/inicio/

Se trata del inicio de la aplicación, donde podemos observar las secciones: Profesionales, Pacientes, y Visitas, cada una con 3 botones que nos llevarán al listado, formulario de creación y formulario de busqueda de cada clase del modelo con el mismo nombre. También se cuenta con una nav bar que nos permite volver al inicio siempre tocando en "App Veterinaria" en la esquina superior izquierda.

## Ver Profesionales, Ver Pacientes, Ver Visitas:

### Urls:
1. http://127.0.0.1:8000/AppVeterinaria/profesionales/
2. http://127.0.0.1:8000/AppVeterinaria/pacientes/
3. http://127.0.0.1:8000/AppVeterinaria/visitas/

Estas vistas muestran el listado de los profesionales, pacientes y visitas creadas hasta el momento.

## Buscar Profesionales, Buscar Pacientes, Buscar Visitas:

### Urls:
1. http://127.0.0.1:8000/AppVeterinaria/buscarProfesional/
2. http://127.0.0.1:8000/AppVeterinaria/buscarPaciente/
3. http://127.0.0.1:8000/AppVeterinaria/buscarVisita/

Estas vistas contienen una barra de busqueda para buscar por nombre del profesional, nombre del paciente y nombre del paciente respectivamente.

## Vistas de resultados:

Estas vistas son similares a las vistas de Ver Profesionales, Pacientes y Visitas, a diferencia que se mostrarán solamente los resultados que contengan lo buscado en la vista de busqueda.

## Agregar Profesionales, Agregar Pacientes, Agregar Visitas:

### Urls:
1. http://127.0.0.1:8000/AppVeterinaria/agregarProfesional/
2. http://127.0.0.1:8000/AppVeterinaria/agregarPaciente/
3. http://127.0.0.1:8000/AppVeterinaria/agregarVisita/

Estas vistas muestran un formulario de Django donde se podrá ingresar la informacion necesaria para dar de alta nuevos Profesionales, Pacientes y Visitas. Aclaración: En esta vista una vez enviado el formulario habrá que volver manualmente al inicio clickeando en "App Veterinaria" en la nav bar porque en clase no terminamos de ver como redireccionar a otra pagina una vez enviado el formulario de Django.

# Datos para ingresar a admin:
Usuario: kaiser
Password: kaiser



