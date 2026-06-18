import pandas as pd
from src.models import Venta, Producto
from sqlalchemy.orm import Session
from sqlalchemy import func

def obtener_df_ventas(db: Session):
    ventas = db.query(Venta).all()
    data = []
    for v in ventas:
        data.append({
            "id": v.id,
            "producto": v.producto.nombre,
            "categoria": v.producto.categoria,
            "tipo_vehiculo": v.producto.tipo_vehiculo.value,
            "precio": v.precio_unitario,
            "cantidad": v.cantidad,
            "total": v.precio_unitario * v.cantidad,
            "costo_envio": v.costo_envio,
            "fecha": v.fecha_venta,
            "vendedor": v.vendedor,
            "sucursal": v.sucursal,
            "calificacion": v.calificacion
        })
    return pd.DataFrame(data)

def calcular_kpis(df):
    if df.empty:
        return {
            "total_ingresos": 0,
            "ventas_por_sucursal": {},
            "calificacion_promedio": 0,
            "productos_estrella": []
        }

    kpis = {
        "total_ingresos": df["total"].sum(),
        "ventas_por_sucursal": df.groupby("sucursal")["total"].sum().to_dict(),
        "calificacion_promedio": df["calificacion"].mean(),
        "productos_estrella": df.groupby("producto")["cantidad"].sum().sort_values(ascending=False).head(5).index.tolist()
    }
    return kpis
