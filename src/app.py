import streamlit as st
import pandas as pd
import plotly.express as px
from src.database import SessionLocal
from src.inventory import listar_productos, buscar_producto
from src.crm import listar_clientes, registrar_cliente
from src.analytics import obtener_df_ventas, calcular_kpis
from src.models import TipoVehiculo

st.set_page_config(page_title="Sistema Pro Repuestos 2wh/3wh", layout="wide")

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        pass # Handle closure carefully in streamlit

st.title("📊 Gestión Empresarial de Sala de Ventas - Repuestos")

db = get_db()

menu = ["Dashboard Analytics", "Ventas e Inventario", "Seguimiento de Clientes"]
choice = st.sidebar.selectbox("Menú Principal", menu)

if choice == "Dashboard Analytics":
    st.header("Análisis Estratégico en Tiempo Real")
    df_ventas = obtener_df_ventas(db)
    kpis = calcular_kpis(df_ventas)

    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Totales", f"${kpis['total_ingresos']:,.2f}")
    col2.metric("Calificación Promedio CX", f"{kpis['calificacion_promedio']:.2f} ⭐")
    col3.metric("Top Producto", kpis['productos_estrella'][0] if kpis['productos_estrella'] else "N/A")

    st.subheader("Ventas por Sucursal")
    fig_sucursal = px.bar(df_ventas, x="sucursal", y="total", color="tipo_vehiculo",
                         title="Facturación Bruta por Ubicación y Tipo de Vehículo")
    st.plotly_chart(fig_sucursal, use_container_width=True)

    st.subheader("Mix de Productos (Assortment)")
    fig_mix = px.pie(df_ventas, names="categoria", values="cantidad", title="Distribución de Ventas por Categoría")
    st.plotly_chart(fig_mix, use_container_width=True)

elif choice == "Ventas e Inventario":
    st.header("📦 Consulta de Stock y Ventas")

    busqueda = st.text_input("Buscar repuesto por nombre:")
    if busqueda:
        prods = buscar_producto(db, busqueda)
    else:
        tipo_filtro = st.radio("Filtrar por tipo:", ["Todos", "2wh", "3wh"])
        if tipo_filtro == "2wh":
            prods = listar_productos(db, TipoVehiculo.TWO_WHEELER)
        elif tipo_filtro == "3wh":
            prods = listar_productos(db, TipoVehiculo.THREE_WHEELER)
        else:
            prods = listar_productos(db)

    df_prods = pd.DataFrame([{
        "ID": p.id,
        "Nombre": p.nombre,
        "Tipo": p.tipo_vehiculo.value,
        "Categoría": p.categoria,
        "Precio": p.precio,
        "Stock": p.stock
    } for p in prods])

    st.table(df_prods)

elif choice == "Seguimiento de Clientes":
    st.header("👥 CRM y Fidelización")

    with st.expander("Registrar Nuevo Cliente"):
        nombre = st.text_input("Nombre Completo")
        email = st.text_input("Email")
        tel = st.text_input("Teléfono")
        if st.button("Guardar Cliente"):
            registrar_cliente(db, nombre, email, tel)
            st.success(f"Cliente {nombre} registrado!")

    st.subheader("Lista de Clientes")
    clientes = listar_clientes(db)
    st.dataframe(pd.DataFrame([{
        "ID": c.id,
        "Nombre": c.nombre,
        "Email": c.email,
        "Teléfono": c.telefono,
        "Registro": c.fecha_registro
    } for c in clientes]))

db.close()
