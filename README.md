# ✈️ SkyRoute S.R.L. - Sistema de Gestión de Pasajes Aéreos Por DevSigma SAS

---

## 🎯 Propósito del Sistema

SkyRoute es una aplicación de consola desarrollada en Python que permite gestionar de forma simple y eficiente la **venta de pasajes aéreos** para empresas.  
Este prototipo simula las funciones esenciales de una agencia, tales como:

- Registro y gestión de **clientes corporativos**.
- Administración de **destinos** y sus tarifas.
- Venta de pasajes asociada a cliente, destino y fecha.
- Consultas generales sobre las ventas.
- Función especial de **“Botón de Arrepentimiento”**, que permite anular una compra dentro del plazo legal establecido por la Ley 24.240 de Defensa al Consumidor (60 días hábiles).

---

## ⚙️ ¿Cómo instalar y ejecutar el programa?

1. ✅ Asegurate de tener **Python 3.6 o superior** instalado.
2. ✅ Descargá este repositorio o clonalo desde tu consola con:

   ```bash
   git clone https://github.com/Fabricio-Cocconi/SkyRoute.git
   ```

3. ✅ Ejecutá el programa desde la terminal con:

   ```bash
   python main.py
   ```

---

## 👥 Integrantes del equipo desarrollador

| Nombre                | Apellido               | DNI       |
|-----------------------|------------------------|-----------|
| Fabricio Andres       | Cocconi                | 46708260  |
| Gabriel               | Yoles Trucco           | 39935283  |
| Melina Belén          | Rico                   | 46707711  |
| Sofía Yasmín          | Hernandez              | 44078511  |
| Marta Alejandra       | Moretti Orlandi        | 25585612  |


---

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3  
- **Paradigma:** Programación imperativa  
- **Herramientas:** Consola, estructuras secuenciales, condicionales, ciclos, listas y diccionarios  
- **Base de Datos:** Simulada en memoria (listas) – versión inicial sin persistencia  

---

## 🧱 Modelo de Base de Datos

**Entidades principales:**

- `Cliente` (id_cliente, razon_social, cuit, correo)
- `Destino` (id_destino, ciudad, pais, costo_base)
- `Venta` (id_venta, id_cliente, id_destino, fecha_venta, estado)

**Relaciones:**

- Un cliente puede tener muchas ventas.
- Un destino puede estar asociado a muchas ventas.

---

## 🖼️ Diagrama Entidad-Relación (ER)


```markdown
![Diagrama ER del Sistema](C:\Users\Usuario\Desktop\ABP ciencias de datos\SkyRoute\SkyRoute\base de datos\Diagrama DER.jpg
```

---

## 📌 Estado del Proyecto

- 🧪 Prototipo inicial completo por consola.  
- 🧩 Próxima etapa: implementación con base de datos real (SQLite) y modularización.

---

## 🧑‍💻 Créditos

Este proyecto fue desarrollado como parte del **Módulo Programador**.  
**SkyRoute S.R.L.** es una empresa ficticia creada con fines educativos.
