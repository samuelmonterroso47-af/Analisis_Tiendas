# 🏍️ Sistema Profesional de Gestión de Sala de Ventas (2wh & 3wh)

Este proyecto ha sido evolucionado de un análisis estático en Jupyter Notebook a una aplicación empresarial funcional diseñada específicamente para la venta de repuestos de motocicletas (2wh) y motocarros (3wh).

## 🚀 Nuevas Capacidades Empresariales

1.  **Arquitectura Modular**: Código organizado en módulos (`src/`) siguiendo estándares de ingeniería de software.
2.  **Base de Datos Relacional**: Implementación de SQLAlchemy con SQLite para gestionar:
    *   **Inventario**: Repuestos categorizados por tipo de vehículo (2wh/3wh).
    *   **CRM**: Seguimiento y registro de clientes.
    *   **Ventas**: Historial detallado con KPIs dinámicos.
3.  **Dashboard Interactivo**: Aplicación web construida con Streamlit para uso en tiempo real en la sala de ventas.
4.  **Analítica Avanzada**: Visualización automática de Ingresos, Mix de productos (Assortment) y Customer Experience (CX).

---

## 🛠️ Estructura del Proyecto

```text
.
├── data/               # Base de datos SQLite
├── src/                # Código fuente
│   ├── app.py          # Dashboard Streamlit (Frontend)
│   ├── models.py       # Definición de tablas DB
│   ├── database.py     # Configuración de conexión
│   ├── crm.py          # Lógica de clientes
│   ├── inventory.py    # Lógica de repuestos
│   └── analytics.py    # Cálculo de KPIs
├── tests/              # Pruebas automatizadas
└── README.md
```

---

## 💻 Instrucciones de Uso

### 1. Requisitos
* Python 3.10+
* Dependencias: `pip install sqlalchemy streamlit pandas plotly pytest`

### 2. Inicialización
El sistema ya cuenta con una base de datos poblada para demostración. Si desea reiniciar los datos, ejecute:
```bash
export PYTHONPATH=$PYTHONPATH:.
python3 src/seed_data.py
```

### 3. Ejecutar la Aplicación
Para iniciar el dashboard de sala de ventas:
```bash
streamlit run src/app.py
```

---

## 📈 KPIs Monitoreados (En Tiempo Real)
*   **Top-Line**: Ingresos brutos por sucursal y tipo de vehículo.
*   **Assortment**: Análisis de rotación por categoría de repuesto (Motor, Frenos, etc.).
*   **CX (Customer Experience)**: Calificación promedio de satisfacción del cliente.

**Autor**: [Jules - AI Software Engineer]
*Proyecto evolucionado para nivel empresarial.*
