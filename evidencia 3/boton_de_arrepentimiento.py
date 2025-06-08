# boton_arrepentimiento.py
from conexion_base_de_datos import conectar
from datetime import datetime, timedelta

def ejecutar_boton_arrepentimiento():
    cuit = input("CUIT del cliente: ")
    ciudad = input("Ciudad del destino: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT v.id_venta, v.fecha, v.arrepent
        FROM venta v
        JOIN cliente c ON v.id_cliente = c.id_cliente
        JOIN destino d ON v.id_destino = d.id_destino
        JOIN ciudad ci ON d.id_ciudad = ci.id_ciudad
        WHERE c.cuit = %s AND ci.descripcion = %s
        ORDER BY v.fecha DESC
        LIMIT 1
    """, (cuit, ciudad))

    venta = cursor.fetchone()

    if venta:
        id_venta, fecha_venta, arrepent = venta
        ahora = datetime.now()

        if arrepent:
            print("\n❌ Ya se utilizó el botón de arrepentimiento para esta venta. No es posible anularla nuevamente.")
        else:
            cursor.execute("""
                UPDATE venta
                SET estado = 'Anulada', fecha_anulacion = %s, arrepent = TRUE
                WHERE id_venta = %s
            """, (ahora, id_venta))
            conexion.commit()
            print("\n✅ La venta ha sido anulada exitosamente mediante el botón de arrepentimiento.")
    else:
        print("\n❌ No se encontró una venta correspondiente a ese cliente y ciudad.")

    conexion.close()