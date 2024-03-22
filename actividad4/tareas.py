# Importamos la librería datetime para manejar fechas
from datetime import datetime

# Definimos la estructura de datos para almacenar las tareas
tareas = []

# Función para agregar una nueva tarea
def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (formato YYYY-MM-DD): ")
    tarea = {
        "descripcion": descripcion,
        "fecha_limite": datetime.strptime(fecha_limite, "%Y-%m-%d"),
        "estado": "pendiente",
    }
    tareas.append(tarea)

# Función para listar todas las tareas
def listar_tareas():
    for tarea in tareas:
        print(f"ID: {tareas.index(tarea)}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')}")
        print(f"Estado: {tarea['estado']}")
        print("---")

# Función para completar una tarea
def completar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
    tareas[id_tarea]["estado"] = "completada"

# Función para eliminar una tarea
def eliminar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
    del tareas[id_tarea]

# Menú principal
while True:
    print("**Sistema de gestión de tareas**")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        listar_tareas()
    elif opcion == 3:
        completar_tarea()
    elif opcion == 4:
        eliminar_tarea()
    elif opcion == 5:
        break
    else:
        print("Opción no válida.")

print("¡Hasta luego!")


# Agregar tareas:

def agregar_tarea():
  descripcion = input("Ingrese la descripción de la tarea: ")
  fecha_limite = input("Ingrese la fecha límite (formato YYYY-MM-DD): ")
  tarea = {
    "descripcion": descripcion,
    "fecha_limite": datetime.strptime(fecha_limite, "%Y-%m-%d"),
    "estado": "pendiente",
  }
  tareas.append(tarea)

# Se agregó la validación para fechas incorrectas
  try:
    datetime.strptime(fecha_limite, "%Y-%m-%d")
  except ValueError:
    print("Fecha límite inválida. Intente de nuevo.")
    return

  #Listar Tareas:

  def listar_tareas():
   for indice, tarea in enumerate(tareas):
    print(f"ID: {indice}")
    print(f"Descripción: {tarea['descripcion']}")
    print(f"Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')}")
    print(f"Estado: {tarea['estado']}")
    print("---")

 #Completar tareas:

  def completar_tarea():
   id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
  try:
    tareas[id_tarea]["estado"] = "completada"
  except IndexError:
    print("ID de tarea inválido.")

 # Eliminar tareas:

    def eliminar_tarea():
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
  try:
        del tareas[id_tarea]
  except IndexError:
        print("ID de tarea inválido.")  
   

# Implementar funcion para editar una tarea:   
def editar_tarea(id_tarea):
  """
  Función para editar una tarea.

  Parámetros:
    id_tarea: El ID de la tarea a editar.

  Retorno:
    None.
  """

  # Obtener la tarea a editar
  try:
    tarea = tareas[id_tarea]
  except IndexError:
    print(f"ID de tarea inválido: {id_tarea}")
    return

  # Solicitar la nueva descripción y fecha límite
  nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
  nueva_fecha_limite = input("Ingrese la nueva fecha límite (formato YYYY-MM-DD): ")

  # Validar la fecha límite
  try:
    datetime.strptime(nueva_fecha_limite, "%Y-%m-%d")
  except ValueError:
    print("Fecha límite inválida. Intente de nuevo.")
    return

  # Actualizar la información de la tarea
  tarea["descripcion"] = nueva_descripcion
  tarea["fecha_limite"] = datetime.strptime(nueva_fecha_limite, "%Y-%m-%d")

  # Mostrar un mensaje de confirmación
  print(f"Tarea con ID {id_tarea} actualizada correctamente.")