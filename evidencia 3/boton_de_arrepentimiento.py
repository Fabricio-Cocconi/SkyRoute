# boton_arrepentimiento.py
from conexion_base_de_datos import conectar
from datetime import datetime, timedelta, date

def ejecutar_boton_arrepentimiento():
    cuit = input("CUIT del cliente: ")
    ciudad = input("Ciudad del destino: ")

    conexion = conectar()
    cursor = conexion.cursor()

    #selecciona todos los datos de la venta que coincidan con cuit y ciudad y muestra solo la ultima venta realizada por fecha y hora
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

    venta = cursor.fetchone() #crea una tupla con los datos de la ultima venta

    if venta:
        id_venta, fecha, arrepent = venta
        #si es date (sin hora) la convierte a datetime
        if isinstance(fecha, date) and not isinstance(fecha, datetime):
            from datetime import time
            fecha_venta = datetime.combine(fecha, time(0, 0))
        else:
            fecha_venta = fecha  #ya estaba como datetime
            
        ahora = datetime.now()
        diferencia = ahora - fecha_venta

        if arrepent: #si ya se uso el boton para esa venta, muestra el mensaje
            print("\n❌ Ya se utilizó el botón de arrepentimiento para esta venta. No es posible anularla nuevamente.")
        else: #si no, y si pasó menos de 1 minuto, actualiza el estado a "Anulada" en venta, muestra fecha actual y arrepent se cambia a TRUE para id_venta de la venta seleccionada
            if diferencia <= timedelta(minutes=1):
                    cursor.execute("""
                        UPDATE venta
                        SET estado = 'Anulada', fecha_anulacion = %s, arrepent = TRUE
                        WHERE id_venta = %s
                    """, (ahora, id_venta))
                    conexion.commit()
                    print("\n✅ La venta ha sido anulada exitosamente mediante el botón de arrepentimiento.")
            else:
                print("\n❌ Se acabó el tiempo máximo para anular la venta por botón de arrepentimiento.")
    else:
        print("\n❌ No se encontró una venta correspondiente a ese cliente y ciudad.")

    conexion.close()