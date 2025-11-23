# ==========================================
# SISTEMA DE GESTIÓN DE TAREAS (MENÚ SIMPLE)
# Usa: diccionarios, listas, pilas y matriz 2D
# ==========================================

# === ESTRUCTURAS DE DATOS GLOBALES ===

# DICCIONARIO: Almacena todas las tareas con su ID como clave
# Ejemplo: {1: {"titulo": "Hacer tarea", "estado": "pendiente", ...}}
tareas = {}

# LISTA (usada como PILA): Almacena IDs de tareas urgentes
# LIFO = Last In, First Out (el último en entrar es el primero en salir)
pila_urgentes = []

# CONTADOR: Genera IDs únicos e incrementales para cada tarea
next_id = 1


# ---------------------------
# FUNCIONES DEL SISTEMA
# ---------------------------

def agregar_tarea():
    """
    Crea una nueva tarea y la añade al diccionario.
    Valida que el título no esté vacío y la prioridad sea válida.
    """
    # Utilizamos GLOBAL para modificar una variable definida fuera de la función
    # Sin global, Python crearía una variable LOCAL nueva en lugar de modificar la existente
    global next_id
    
    print("\n--- AGREGAR TAREA ---")
    
    # INPUT: Captura datos del usuario
    # Utilizamos .STRIP() para eliminar espacios en blanco al inicio y final del texto
    # Ejemplo: "  hola  " se convierte en "hola"
    titulo = input("Título: ").strip()
    
    # Utilizamos .LOWER() para convertir todo el texto a minúsculas
    # Esto permite comparaciones sin importar cómo escribió el usuario (Alta, ALTA, alta)
    prioridad = input("Prioridad (alta, media, baja): ").strip().lower()
    
    # VALIDACIÓN 1: Título no vacío
    if titulo == "":
        print("Error: el título no puede estar vacío.")
        return  # Termina la función sin hacer nada
    
    # VALIDACIÓN 2: Prioridad válida
    # Utilizamos IN para verificar si un valor está dentro de una lista
    # Es más eficiente que hacer múltiples comparaciones con OR
    if prioridad not in ["alta", "media", "baja"]:
        print("Error: prioridad inválida.")
        return
    
    # CREAR TAREA: Estructura de diccionario anidado
    tareas[next_id] = {
        "titulo": titulo,
        "estado": "pendiente",      # Estado inicial por defecto
        "prioridad": prioridad,
        "urgente": False            # No es urgente por defecto
    }
    
    print(f"Tarea agregada con ID {next_id}.")
    next_id += 1  # Incrementa el ID para la siguiente tarea


def listar_tareas():
    """
    Muestra todas las tareas registradas en el sistema.
    Itera sobre el diccionario y muestra información básica.
    """
    print("\n--- LISTA DE TAREAS ---")
    
    # Verifica si hay tareas (diccionario vacío = False en Python)
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    # ITERACIÓN: Recorre cada tarea en el diccionario
    # Utilizamos .ITEMS() para obtener tanto la clave (id) como el valor (datos) simultáneamente
    # Alternativa: for id in tareas: (solo obtendría las claves)
    for id, datos in tareas.items():
        # f-string: Permite insertar variables dentro del texto con {}
        print(f"[{id}] {datos['titulo']} - Estado: {datos['estado']} - Prioridad: {datos['prioridad']}")


def cambiar_estado():
    """
    Modifica el estado de una tarea existente.
    Valida que el ID exista y el nuevo estado sea válido.
    """
    print("\n--- CAMBIAR ESTADO ---")
    
    # MANEJO DE EXCEPCIONES: try-except captura errores
    # Utilizamos TRY-EXCEPT para evitar que el programa se detenga si el usuario ingresa texto en lugar de número
    # Si falla int(), el código dentro de EXCEPT se ejecuta
    try:
        id = int(input("ID de tarea: "))  # Convierte texto a número entero
    except:
        print("ID inválido.")
        return
    
    # VALIDACIÓN 1: Verifica que el ID exista en el diccionario
    if id not in tareas:
        print("No existe una tarea con ese ID.")
        return
    
    nuevo = input("Nuevo estado (pendiente, en_progreso, completada): ").strip()
    
    # VALIDACIÓN 2: Estado válido
    if nuevo not in ["pendiente", "en_progreso", "completada"]:
        print("Estado inválido.")
        return
    
    # ACTUALIZACIÓN: Modifica el valor dentro del diccionario anidado
    tareas[id]["estado"] = nuevo
    print(f"Estado de la tarea {id} actualizado.")


def marcar_urgente():
    """
    Marca una tarea como urgente y la añade a la pila.
    La pila permite gestionar urgencias en orden LIFO.
    """
    print("\n--- MARCAR URGENTE ---")
    
    try:
        id = int(input("ID de tarea: "))
    except:
        print("ID inválido.")
        return
    
    if id not in tareas:
        print("No existe una tarea con ese ID.")
        return
    
    # Actualiza el estado de urgencia en el diccionario
    tareas[id]["urgente"] = True
    
    # OPERACIÓN DE PILA: append() añade al final (push)
    # Utilizamos .APPEND() para agregar elementos al final de una lista
    # En el contexto de pilas, esto es equivalente a "apilar" o "push"
    pila_urgentes.append(id)
    
    print(f"Tarea {id} marcada como urgente.")


def sacar_urgente():
    """
    Extrae la última tarea urgente de la pila (LIFO).
    Útil para atender urgencias en orden inverso al que llegaron.
    """
    print("\n--- SACAR URGENTE (PILA) ---")
    
    if not pila_urgentes:
        print("No hay tareas urgentes.")
        return
    
    # OPERACIÓN DE PILA: pop() extrae y elimina el último elemento
    # Utilizamos .POP() para sacar el último elemento de la lista (LIFO)
    # La diferencia con .append(): pop() REMUEVE el elemento, append() lo AÑADE
    id = pila_urgentes.pop()
    
    # Marca la tarea como no urgente
    tareas[id]["urgente"] = False
    
    print(f"Tarea urgente extraída: {tareas[id]['titulo']} (ID {id})")


def generar_tabla():
    """
    Crea una representación tabular (matriz 2D) de todas las tareas.
    Cada fila es una lista con los datos de una tarea.
    """
    print("\n--- TABLA 2D DE TAREAS ---")
    
    # MATRIZ 2D: Lista de listas (tabla)
    tabla = []
    
    for id, datos in tareas.items():
        # Cada fila es una lista con información de la tarea
        fila = [
            id,
            datos["titulo"],
            datos["estado"],
            datos["prioridad"],
            datos["urgente"]
        ]
        tabla.append(fila)  # Añade la fila a la tabla
        print(fila)  # Muestra la fila


# ---------------------------
# MENÚ PRINCIPAL
# ---------------------------

def menu():
    """
    Bucle principal del programa.
    Muestra opciones y ejecuta funciones según la elección del usuario.
    """
    while True:  # Bucle infinito hasta que se elija salir
        # Menú visual con triple comillas para texto multilínea
        print("""
===============================
   SISTEMA DE GESTIÓN DE TAREAS
===============================

1. Agregar tarea
2. Listar tareas
3. Cambiar estado
4. Marcar como urgente
5. Sacar tarea urgente (pila)
6. Mostrar tabla 2D
0. Salir
""")
        
        opcion = input("Elige una opción: ")
        
        # ESTRUCTURA CONDICIONAL: if-elif-else
        if opcion == "1":
            agregar_tarea()
        
        elif opcion == "2":
            listar_tareas()
        
        elif opcion == "3":
            cambiar_estado()
        
        elif opcion == "4":
            marcar_urgente()
        
        elif opcion == "5":
            sacar_urgente()
        
        elif opcion == "6":
            generar_tabla()
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break  # Rompe el bucle while y termina el programa
        
        else:
            print("Opción inválida.")


# === PUNTO DE ENTRADA DEL PROGRAMA ===
# Ejecuta el menú cuando se corre el script
menu()