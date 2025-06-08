from conexion_base_de_datos import conectar
from datetime import datetime

def registrar_venta():
    cuit = input("CUIT del cliente: ")
    ciudad = input("Ciudad destino: ")
    fecha = datetime.now()  # ← usa hora exacta del sistema

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_cliente FROM cliente WHERE cuit = %s", (cuit,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente no encontrado.")
        conexion.close()
        return

    cursor.execute("SELECT d.id_destino FROM destino d JOIN ciudad ci ON d.id_ciudad = ci.id_ciudad WHERE ci.descripcion = %s", (ciudad,))
    destino = cursor.fetchone()
    if not destino:
        print("Destino no encontrado.")
        conexion.close()
        return

    cursor.execute("""
        INSERT INTO venta (id_cliente, id_destino, fecha, estado, fecha_anulacion, arrepent)
        VALUES (%s, %s, %s, 'Activa', NULL, FALSE)
    """, (cliente[0], destino[0], fecha))

    conexion.commit()
    conexion.close()
    print(f"Venta registrada con fecha y hora exacta: {fecha.strftime('%Y-%m-%d %H:%M:%S')}")


def listar_ventas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT 
            v.id_venta,
            cl.razon_social,
            ci.descripcion AS ciudad,
            p.descripcion AS pais,
            v.fecha,
            v.estado,
            v.fecha_anulacion,
            v.arrepent
        FROM venta v
        JOIN cliente cl ON v.id_cliente = cl.id_cliente
        JOIN destino d ON v.id_destino = d.id_destino
        JOIN ciudad ci ON d.id_ciudad = ci.id_ciudad
        JOIN pais p ON ci.id_pais = p.id_pais
        ORDER BY v.fecha DESC
    """)

    ventas = cursor.fetchall()

    if ventas:
        print("\n--- Listado de Ventas ---")
        for v in ventas:
            print(f"ID Venta: {v[0]}")
            print(f"Cliente: {v[1]}")
            print(f"Destino: {v[2]}, {v[3]}")
            print(f"Fecha: {v[4]}")
            print(f"Estado: {v[5]}")
            print(f"Anulación: {v[6] if v[6] else 'No anulada'}")
            print(f"Botón de Arrepentimiento: {'Sí' if v[7] else 'No'}")
            print("-" * 40)
    else:
        print("No hay ventas registradas.")

    conexion.close()
