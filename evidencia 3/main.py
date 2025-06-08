from gestion_clientes import agregar_cliente, listar_clientes, eliminar_cliente
from gestion_destino import agregar_destino, listar_destinos, eliminar_destino
from gestion_ventas import registrar_venta, listar_ventas
from boton_de_arrepentimiento import ejecutar_boton_arrepentimiento

def menu():
    while True:
        print("\n--- SkyRoute - Menú Principal ---")
        print("1. Administrar Clientes")
        print("2. Administrar Destinos")
        print("3. Administrar Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_destinos()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            print("Gracias por utilizar SkyRoute. 🛫")
            break
        else:
            print("Opción inválida.")

def menu_clientes():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Eliminar Cliente")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def menu_destinos():
    while True:
        print("\n--- Gestión de Destinos ---")
        print("1. Agregar Destino")
        print("2. Listar Destinos")
        print("3. Eliminar Destino")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_destino()
        elif opcion == "2":
            listar_destinos()
        elif opcion == "3":
            eliminar_destino()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def menu_ventas():
    while True:
        print("\n--- Gestión de Ventas ---")
        print("1. Registrar Venta")
        print("2. Mostrar Ventas")
        print("3. Botón de Arrepentimiento")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            ejecutar_boton_arrepentimiento()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
