# SkyRoute - Sistema de Gestión de Pasajes

clientes = []
destinos = []
ventas = []

print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")

opcion = 0
while opcion != 8:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Botón de Arrepentimiento")
    print("6. Ver Reporte General")
    print("7. Acerca del Sistema")
    print("8. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        subopcion = 0
        while subopcion != 5:
            print("\n-- GESTIONAR CLIENTES --")
            print("1. Ver Clientes")
            print("2. Agregar Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")
            subopcion = int(input("Seleccione una opción: "))

            if subopcion == 1:
                print("Listado de Clientes:")
                for cliente in clientes:
                    print(cliente)

            elif subopcion == 2:
                razon_social = input("Ingrese razón social: ")
                cuit = input("Ingrese CUIT: ")
                correo = input("Ingrese correo electrónico: ")
                cliente = {"razon_social": razon_social, "cuit": cuit, "correo": correo}
                clientes.append(cliente)
                print("Cliente agregado:", cliente)

            elif subopcion == 3:
                cuit = input("Ingrese CUIT del cliente a modificar: ")
                for cliente in clientes:
                    if cliente["cuit"] == cuit:
                        cliente["razon_social"] = input("Nueva razón social: ")
                        cliente["correo"] = input("Nuevo correo: ")
                        print("Cliente modificado:", cliente)
                        break
                else:
                    print("Cliente no encontrado.")

            elif subopcion == 4:
                cuit = input("Ingrese CUIT del cliente a eliminar: ")
                for cliente in clientes:
                    if cliente["cuit"] == cuit:
                        clientes.remove(cliente)
                        print("Cliente eliminado.")
                        break
                else:
                    print("Cliente no encontrado.")

    elif opcion == 2:
        subopcion = 0
        while subopcion != 4:
            print("\n-- GESTIONAR DESTINOS --")
            print("1. Ver Destinos")
            print("2. Agregar Destino")
            print("3. Eliminar Destino")
            print("4. Volver al Menú Principal")
            subopcion = int(input("Seleccione una opción: "))

            if subopcion == 1:
                print("Listado de Destinos:")
                for destino in destinos:
                    print(destino)

            elif subopcion == 2:
                ciudad = input("Ingrese ciudad: ")
                pais = input("Ingrese país: ")
                costo = float(input("Ingrese costo base: "))
                destino = {"ciudad": ciudad, "pais": pais, "costo": costo}
                destinos.append(destino)
                print("Destino agregado:", destino)

            elif subopcion == 3:
                ciudad = input("Ingrese ciudad del destino a eliminar: ")
                for destino in destinos:
                    if destino["ciudad"] == ciudad:
                        destinos.remove(destino)
                        print("Destino eliminado.")
                        break
                else:
                    print("Destino no encontrado.")

    elif opcion == 3:
        print("\n-- GESTIONAR VENTAS --")
        cuit = input("Ingrese CUIT del cliente: ")
        ciudad = input("Ingrese ciudad destino: ")
        fecha = input("Ingrese fecha de venta (dd/mm/aaaa): ")
        for cliente in clientes:
            if cliente["cuit"] == cuit:
                for destino in destinos:
                    if destino["ciudad"] == ciudad:
                        venta = {
                            "cliente": cuit,
                            "destino": ciudad,
                            "fecha": fecha,
                            "costo": destino["costo"],
                            "estado": "Activa"
                        }
                        ventas.append(venta)
                        print("Venta registrada:", venta)
                        break
                else:
                    print("Destino no encontrado.")
                break
        else:
            print("Cliente no encontrado.")

    elif opcion == 4:
        print("\n-- CONSULTAR VENTAS --")
        if len(ventas) == 0:
            print("No hay ventas registradas.")
        else:
            for venta in ventas:
                print(venta)

    elif opcion == 5:
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        cuit = input("Ingrese CUIT del cliente: ")
        ciudad = input("Ingrese ciudad del destino: ")
        for venta in ventas:
            if venta["cliente"] == cuit and venta["destino"] == ciudad and venta["estado"] == "Activa":
                venta["estado"] = "Anulada"
                print("Venta anulada por botón de arrepentimiento:", venta)
                break
        else:
            print("No se encontró una venta activa reciente para anular.")

    elif opcion == 6:
        print("\n-- REPORTE GENERAL --")
        print("Clientes registrados:", len(clientes))
        print("Destinos registrados:", len(destinos))
        print("Total de ventas:", len(ventas))
        activas = sum(1 for v in ventas if v["estado"] == "Activa")
        anuladas = sum(1 for v in ventas if v["estado"] == "Anulada")
        print("Ventas activas:", activas)
        print("Ventas anuladas:", anuladas)

    elif opcion == 7:
        print("\n-- ACERCA DEL SISTEMA --")
        print("SkyRoute S.R.L. - Sistema de Gestión de Pasajes")
        print("Versión: Prototipo Inicial por Consola")
        print("Desarrollado por el equipo de estudiantes - Módulo Programador")

    elif opcion == 8:
        print("Saliendo del sistema... ¡Gracias por utilizar SkyRoute!")

    else:
        print("Opción inválida. Intente nuevamente.")
