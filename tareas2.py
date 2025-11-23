# ==========================================
# SISTEMA DE GESTIÓN DE TAREAS (MENÚ SIMPLE)
# Usa: diccionarios, listas, pilas y matriz 2D
# ==========================================

tareas = {}            # Diccionario principal
pila_urgentes = []     # Pila (LIFO) para urgentes
next_id = 1            # Contador de IDs


# ---------------------------
# FUNCIONES
# ---------------------------

def agregar_tarea():
    global next_id

    print("\n--- AGREGAR TAREA ---")
    titulo = input("Título: ").strip()
    prioridad = input("Prioridad (alta, media, baja): ").strip().lower()

    if titulo == "":
        print("Error: el título no puede estar vacío.")
        return

    if prioridad not in ["alta", "media", "baja"]:
        print("Error: prioridad inválida.")
        return

    tareas[next_id] = {
        "titulo": titulo,
        "estado": "pendiente",
        "prioridad": prioridad,
        "urgente": False
    }

    print(f"Tarea agregada con ID {next_id}.")
    next_id += 1


def listar_tareas():
    print("\n--- LISTA DE TAREAS ---")

    if not tareas:
        print("No hay tareas registradas.")
        return

    for id, datos in tareas.items():
        print(f"[{id}] {datos['titulo']} - Estado: {datos['estado']} - Prioridad: {datos['prioridad']}")


def cambiar_estado():
    print("\n--- CAMBIAR ESTADO ---")
    try:
        id = int(input("ID de tarea: "))
    except:
        print("ID inválido.")
        return
    
    if id not in tareas:
        print("No existe una tarea con ese ID.")
        return

    nuevo = input("Nuevo estado (pendiente, en_progreso, completada): ").strip()

    if nuevo not in ["pendiente", "en_progreso", "completada"]:
        print("Estado inválido.")
        return

    tareas[id]["estado"] = nuevo
    print(f"Estado de la tarea {id} actualizado.")


def marcar_urgente():
    print("\n--- MARCAR URGENTE ---")
    try:
        id = int(input("ID de tarea: "))
    except:
        print("ID inválido.")
        return
    
    if id not in tareas:
        print("No existe una tarea con ese ID.")
        return

    tareas[id]["urgente"] = True
    pila_urgentes.append(id)      # Guardamos solo el ID en la pila
    print(f"Tarea {id} marcada como urgente.")


def sacar_urgente():
    print("\n--- SACAR URGENTE (PILA) ---")

    if not pila_urgentes:
        print("No hay tareas urgentes.")
        return

    id = pila_urgentes.pop()
    tareas[id]["urgente"] = False
    print(f"Tarea urgente extraída: {tareas[id]['titulo']} (ID {id})")


def generar_tabla():
    print("\n--- TABLA 2D DE TAREAS ---")

    tabla = []
    for id, datos in tareas.items():
        fila = [id, datos["titulo"], datos["estado"], datos["prioridad"], datos["urgente"]]
        tabla.append(fila)
        print(fila)  # imprimiendo fila por fila


# ---------------------------
# MENÚ PRINCIPAL
# ---------------------------

def menu():
    while True:
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
            break

        else:
            print("Opción inválida.")


# Ejecutar menú
menu()
