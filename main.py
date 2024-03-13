import random

# Estructuras de datos
bandas = []
equipos = []
programa = []

# Funciones
def generar_id():
    return random.randint(1, 100)

def agregar_banda():
    id_banda = generar_id()
    nombre = input("Nombre de la banda: ")
    genero = input("Género de la banda: ")
    clasificacion = input("Clasificación (amateur/intermedio/especial): ")

    if clasificacion == "amateur":
        tiempo = int(input("Tiempo de actuación (minutos): "))
        banda = {"id": id_banda, "nombre": nombre, "genero": genero, "clasificacion": clasificacion, "tiempo": tiempo}
    elif clasificacion == "intermedio":
        costo = float(input("Costo de la banda: "))
        banda = {"id": id_banda, "nombre": nombre, "genero": genero, "clasificacion": clasificacion, "costo": costo}
    elif clasificacion == "especial":
        banda = {"id": id_banda, "nombre": nombre, "genero": genero, "clasificacion": clasificacion}
    else:
        print("Clasificación no válida.")
        return

    bandas.append(banda)

def agregar_equipo():
    nombre_equipo = input("Nombre del equipo: ")
    equipos.append(nombre_equipo)

def agregar_programa():
    id_banda = int(input("ID de la banda a agregar al programa: "))
    banda = next((b for b in bandas if b["id"] == id_banda), None)
    if banda:
        programa.append(banda)
    else:
        print("Banda no encontrada.")

def modificar_programa():
    id_banda = int(input("ID de la banda que cancela: "))
    programa[:] = [b for b in programa if b["id"] != id_banda]

def buscar_info():
    id_banda = int(input("ID de la banda a buscar: "))
    banda = next((b for b in bandas if b["id"] == id_banda), None)
    if banda:
        print("Información de la banda:")
        print("ID:", banda["id"])
        print("Nombre:", banda["nombre"])
        print("Género:", banda["genero"])
        print("Clasificación:", banda["clasificacion"])
        if "tiempo" in banda:
            print("Tiempo de actuación:", banda["tiempo"], "minutos")
        elif "costo" in banda:
            print("Costo de la banda:", banda["costo"])
    else:
        print("Banda no encontrada.")

# Menú principal
while True:
    print("\n*** Menú Principal ***")
    print("1. Agregar banda")
    print("2. Agregar equipo")
    print("3. Agregar banda al programa")
    print("4. Modificar programa (cancelar banda)")
    print("5. Buscar información")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_banda()
    elif opcion == "2":
        agregar_equipo()
    elif opcion == "3":
        agregar_programa()
    elif opcion == "4":
        modificar_programa()
    elif opcion == "5":
        buscar_info()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")