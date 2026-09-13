# 🛒 SuperMarket POS

Sistema de Punto de Venta (POS) de escritorio para supermercados, desarrollado en **Python** con **Tkinter** y **SQLite3**. Incluye gestión de ventas, inventario, clientes, proveedores y generación de facturas en PDF.

## ✨ Funcionalidades

- 🔐 **Login y registro de usuarios** con contraseñas cifradas (SHA-256) y clave de administrador.
- 🛍️ **Módulo de ventas** con selección de cliente, productos y cálculo automático de totales.
- 📦 **Gestión de inventario** con control de stock y fotos de productos.
- 👥 **Gestión de clientes y proveedores** (registro, modificación y eliminación).
- 🧾 **Generación de facturas en PDF** con ReportLab.
- 📊 **Reportes** de ventas.
- 🖥️ **Interfaz escalable** que se adapta al tamaño de la ventana.

## 🛠️ Tecnologías

- **Python 3**
- **Tkinter** — interfaz gráfica
- **SQLite3** — base de datos
- **Pillow (PIL)** — manejo de imágenes
- **ReportLab** — generación de PDFs

## 📋 Requisitos

- Python 3.8 o superior
- Las dependencias de `requirements.txt`

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/mlly2319/supermarket-pos.git
cd supermarket-pos

1. (Opcional) Crea un entorno virtual:
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac

2. Instala las dependencias:
pip install -r requirements.txt

3. Configura la clave de asministrador:
Copia el archivo .env.example a .env y edítalo:
CLAVE_ADMIN=tu_clave_secreta

4. Ejecuta el programa:
python index.py

📁 Estructura del proyecto
supermarket-pos/
├── index.py              # Punto de entrada
├── manager.py            # Ventana principal y navegación
├── login_window.py       # Login, registro e inicio
├── container.py          # Contenedor de pantallas
├── container_clientes.py # Contenedor de clientes
├── ventas.py             # Módulo de ventas
├── ventasclientes.py     # Ventas por cliente
├── inventario.py         # Gestión de inventario
├── proveedor.py          # Gestión de proveedores
├── cliente.py            # Gestión de clientes
├── reportes.py           # Reportes
├── utils.py              # Utilidades
├── scaler.py             # Escalado de interfaz
├── .env.example          # Plantilla de configuración
└── requirements.txt      # Dependencias

📝 Notas
La base de datos database.db no se incluye en el repositorio. Se crea automáticamente al ejecutar el programa.
La carpeta fotos/ se crea automáticamente para las imágenes de los productos.
El proyecto está pensado para Windows (usa os.startfile y ctypes.windll).

👩‍💻 Autora
Merly Torres

📄 Licencia
Este proyecto es de uso libre con fines educativos.
