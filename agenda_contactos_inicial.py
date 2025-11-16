# --- agenda_contactos_completo_corregido.py ---

import os
import time
import datetime 

# --- Constantes ---
FILENAME = "contactos.txt"
SEPARATOR = ";"

# --- Funciones de Utilidad ---
def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresiona Enter para continuar...")

def pedir_fecha_valida():
    """
    Pide al usuario una fecha en formato DD MM AAAA y la valida.
    No permite continuar hasta que el formato sea correcto.
    """
    while True:
        fecha_str = input("Introduce la fecha (formato DD MM AAAA): ")
        try:
            # Usamos .strip() para limpiar la entrada antes de validar
            datetime.datetime.strptime(fecha_str.strip(), '%d %m %Y')
            return fecha_str.strip() # Devolvemos la fecha ya limpia
        # CORRECCIÓN: Se eliminó el error tipográfico "exce2pt"
        except ValueError:
            print("Error: Formato incorrecto. Por favor, use DD MM AAAA (ej: 30 11 2025).")

# --- Funciones Principales de la Agenda ---
def cargar_contactos():
    """
    Carga los contactos desde el archivo de texto.
    Cada contacto se guarda como un diccionario.
    """
    contactos = []
    try:
        with open(FILENAME, 'r') as f:
            for linea in f:
                if linea.strip():
                    partes = linea.strip().split(SEPARATOR)
                    if len(partes) == 5:
                        contacto = {
                            "nombre": partes[0], "telefono": partes[1], "correo": partes[2],
                            "nota": partes[3], "fecha": partes[4]
                        }
                        contactos.append(contacto)
    except FileNotFoundError:
        print(f"Advertencia: El archivo {FILENAME} no existía. Se ha creado uno nuevo.")
        open(FILENAME, 'w').close()
    return contactos

def guardar_contactos(contactos):
    """
    Guarda la lista de diccionarios de contactos en el archivo.
    """
    with open(FILENAME, 'w') as f:
        for contacto in contactos:
            linea = SEPARATOR.join([
                contacto["nombre"], contacto["telefono"], contacto["correo"],
                contacto["nota"], contacto["fecha"]
            ])
            f.write(linea + '\n')

def mostrar_menu():
    """Imprime el menú de opciones."""
    print("===== Gestor de Contactos =====")
    print("1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto por nombre")
    print("4. Actualizar fecha de reunión")
    print("5. Salir")
    print("===============================")

def mostrar_detalle_contacto(contacto):
    """Función auxiliar para mostrar un solo contacto formateado."""
    print("\n----------------------------------------")
    print(f"Nombre:          {contacto['nombre']}")
    print(f"Teléfono:        {contacto['telefono']}")
    print(f"Correo:          {contacto['correo']}")
    print(f"Nota:            {contacto['nota']}")
    print(f"Próxima Reunión: {contacto['fecha']}")
    print("----------------------------------------")

def agregar_contacto(contactos):
    """
    Pide los datos de un nuevo contacto, con validaciones mejoradas.
    """
    limpiar_pantalla()
    print("--- Agregar Nuevo Contacto ---")
    
    nombre = input("Nombre completo (obligatorio): ")
    if not nombre.strip():
        print("\nError: El nombre es un campo obligatorio. Operación cancelada.")
        return

    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    if not telefono.strip() and not correo.strip():
        print("\nError: Debes proporcionar al menos un teléfono o un correo electrónico.")
        print("Operación cancelada.")
        return

    print("\n")
    nota = input("Nota o descripción: ")
    
    fecha = "" # Valor por defecto si el usuario no quiere agregar fecha.
    while True:
        gestionar_fecha = input("¿Deseas registrar una fecha de reunión? (si/no): ").lower()
        if gestionar_fecha in ['si', 's']:
            fecha = pedir_fecha_valida()
            break
        elif gestionar_fecha in ['no', 'n']:
            break
        else:
            print("Opción no válida. Por favor, responde 'si' o 'no'.")

    nuevo_contacto = {
        "nombre": nombre.strip(), "telefono": telefono.strip(), "correo": correo.strip(),
        "nota": nota.strip(), "fecha": fecha
    }
    contactos.append(nuevo_contacto)
    guardar_contactos(contactos)
    print("\n¡Contacto agregado exitosamente!")

def listar_contactos(contactos):
    """
    Muestra una lista formateada de todos los contactos.
    NOTA: No limpia la pantalla, se espera que el llamador lo haga.
    """
    print("--- Lista de Contactos ---")
    if not contactos:
        print("No hay contactos guardados.")
    else:
        # Ordenamos los contactos por nombre
        contactos.sort(key=lambda c: c["nombre"].lower())
        for contacto in contactos:
            mostrar_detalle_contacto(contacto)

def buscar_contacto(contactos):
    """Busca un contacto por una parte de su nombre."""
    limpiar_pantalla()
    print("--- Buscar Contacto por Nombre ---")
    termino = input("Introduce el nombre o parte del nombre a buscar: ").lower()
    encontrados = []
    for contacto in contactos:
        if termino in contacto["nombre"].lower():
            encontrados.append(contacto)
    if not encontrados:
        print(f"\nNo se encontraron contactos que coincidan con '{termino}'.")
    else:
        print(f"\nSe encontraron {len(encontrados)} contactos:")
        # Se llama a listar_contactos para mostrar solo los encontrados
        listar_contactos(encontrados)

def actualizar_contacto(contactos):
    """Actualiza la fecha de reunión de un contacto existente."""
    limpiar_pantalla()
    print("--- Actualizar Fecha de Reunión ---")
    nombre_buscado = input("Introduce el nombre exacto del contacto a actualizar: ")

    contacto_a_actualizar = None
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre_buscado.lower():
            contacto_a_actualizar = contacto
            break

    if contacto_a_actualizar:
        print("\nContacto encontrado:")
        print(f"Nombre: {contacto_a_actualizar['nombre']}, Fecha actual: {contacto_a_actualizar['fecha']}")
        
        nueva_fecha = pedir_fecha_valida()
        
        contacto_a_actualizar["fecha"] = nueva_fecha
        guardar_contactos(contactos)
        print("\n¡Fecha de reunión actualizada exitosamente!")
    else:
        print(f"\nNo se encontró ningún contacto con el nombre '{nombre_buscado}'.")

# --- Bucle Principal de la Aplicación ---
def main():
    """Función principal que ejecuta el programa."""
    contactos = cargar_contactos()
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        # Opciones que requieren una acción inmediata
        if opcion == '1':
            agregar_contacto(contactos)
            pausar()
        elif opcion == '2':
            # Limpiamos justo antes de mostrar la lista completa
            limpiar_pantalla()
            listar_contactos(contactos)
            pausar()
        elif opcion == '3':
            # buscar_contacto limpia su propia pantalla internamente
            buscar_contacto(contactos)
            pausar()
        elif opcion == '4':
            # actualizar_contacto limpia su propia pantalla internamente
            actualizar_contacto(contactos)
            pausar()
        elif opcion == '5':
            print("\nGracias por usar el Gestor de Contactos. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 5.")
            time.sleep(2)

# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    main()