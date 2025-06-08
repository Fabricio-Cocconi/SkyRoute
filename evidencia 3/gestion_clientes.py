from conexion_base_de_datos import conectar

def agregar_cliente():
    razon = input("Razón social: ")
    cuit = input("CUIT: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")

    conexion = conectar()
    cursor = conexion.cursor()

    # Insertar en contacto
    cursor.execute("INSERT INTO contacto (telefono, correo) VALUES (%s, %s)", (telefono, correo))
    id_contacto = cursor.lastrowid

    # Insertar en cliente
    cursor.execute("INSERT INTO cliente (razon_social, cuit, id_contacto) VALUES (%s, %s, %s)", (razon, cuit, id_contacto))

    conexion.commit()
    conexion.close()
    print("Cliente agregado exitosamente.")

def listar_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT c.id_cliente, c.razon_social, c.cuit, co.telefono, co.correo
        FROM cliente c
        LEFT JOIN contacto co ON c.id_contacto = co.id_contacto
    """)
    for row in cursor.fetchall():
        print(row)
    conexion.close()

def eliminar_cliente():
    cuit = input("Ingrese el CUIT del cliente a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()

    # Obtener id_cliente e id_contacto asociados
    cursor.execute("SELECT id_cliente, id_contacto FROM cliente WHERE cuit = %s", (cuit,))
    resultado = cursor.fetchone()

    if resultado:
        id_cliente, id_contacto = resultado

        # Eliminar cliente
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))

        # Verificar si el contacto está asociado a otro cliente
        cursor.execute("SELECT COUNT(*) FROM cliente WHERE id_contacto = %s", (id_contacto,))
        count = cursor.fetchone()[0]

        # Si no está asociado a nadie más, eliminar contacto
        if count == 0:
            cursor.execute("DELETE FROM contacto WHERE id_contacto = %s", (id_contacto,))

        conexion.commit()
        print("Cliente y contacto eliminados correctamente." if count == 0 else "Cliente eliminado. El contacto fue conservado porque está asociado a otro cliente.")
    else:
        print("❌ No se encontró un cliente con ese CUIT.")

    conexion.close()
