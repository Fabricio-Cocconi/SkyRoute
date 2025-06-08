from conexion_base_de_datos import conectar

def agregar_destino():
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    try:
        costo = float(input("Costo base ($): "))
    except ValueError:
        print("⚠️ El costo debe ser un número.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    # Insertar país si no existe
    cursor.execute("SELECT id_pais FROM pais WHERE descripcion = %s", (pais,))
    resultado_pais = cursor.fetchone()
    if resultado_pais:
        id_pais = resultado_pais[0]
    else:
        cursor.execute("INSERT INTO pais (descripcion) VALUES (%s)", (pais,))
        id_pais = cursor.lastrowid

    # Insertar ciudad si no existe
    cursor.execute("SELECT id_ciudad FROM ciudad WHERE descripcion = %s AND id_pais = %s", (ciudad, id_pais))
    resultado_ciudad = cursor.fetchone()
    if resultado_ciudad:
        id_ciudad = resultado_ciudad[0]
    else:
        cursor.execute("INSERT INTO ciudad (descripcion, id_pais) VALUES (%s, %s)", (ciudad, id_pais))
        id_ciudad = cursor.lastrowid

    # Insertar destino
    cursor.execute("INSERT INTO destino (id_ciudad, costo) VALUES (%s, %s)", (id_ciudad, costo))

    conexion.commit()
    conexion.close()
    print("Destino agregado exitosamente.")

def listar_destinos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT d.id_destino, ci.descripcion AS ciudad, p.descripcion AS pais, d.costo
        FROM destino d
        JOIN ciudad ci ON d.id_ciudad = ci.id_ciudad
        JOIN pais p ON ci.id_pais = p.id_pais
    """)
    for row in cursor.fetchall():
        print(row)
    conexion.close()

def eliminar_destino():
    try:
        id_destino = int(input("Ingrese el ID del destino a eliminar: "))
    except ValueError:
        print("⚠️ El ID debe ser un número.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    # Verificar si hay ventas asociadas al destino
    cursor.execute("SELECT COUNT(*) FROM venta WHERE id_destino = %s", (id_destino,))
    ventas_asociadas = cursor.fetchone()[0]

    if ventas_asociadas > 0:
        print("❌ No se puede eliminar el destino porque tiene ventas asociadas.")
    else:
        cursor.execute("DELETE FROM destino WHERE id_destino = %s", (id_destino,))
        conexion.commit()
        print("✅ Destino eliminado correctamente.")

    conexion.close()
