from src.database import SessionLocal, init_db
from src.models import Cliente, Producto, Venta, TipoVehiculo
from datetime import datetime, timedelta
import random

def seed():
    init_db()
    db = SessionLocal()

    # Clientes
    clientes_nombres = ["Juan Pérez", "María García", "Luis Rodríguez", "Ana Martínez", "Carlos López"]
    clientes = []
    for nombre in clientes_nombres:
        cliente = Cliente(nombre=nombre, email=f"{nombre.replace(' ', '.').lower()}@example.com", telefono="555-010"+str(random.randint(0,9)))
        db.add(cliente)
        clientes.append(cliente)

    # Productos (Repuestos 2wh y 3wh)
    productos_data = [
        ("Kit de Arrastre Pulsar 200NS", TipoVehiculo.TWO_WHEELER, "Transmisión", 120000.0, 8000.0, 50),
        ("Llanta Delantera 80/90-17", TipoVehiculo.TWO_WHEELER, "Llantas", 150000.0, 10000.0, 30),
        ("Filtro de Aceite Boxer CT100", TipoVehiculo.TWO_WHEELER, "Motor", 15000.0, 2000.0, 100),
        ("Pastillas de Freno AKT 125", TipoVehiculo.TWO_WHEELER, "Frenos", 25000.0, 3000.0, 80),
        ("Eje Delantero Motocarro Torito", TipoVehiculo.THREE_WHEELER, "Chasis", 85000.0, 12000.0, 20),
        ("Cables de Bujía Motocarro RE", TipoVehiculo.THREE_WHEELER, "Eléctrico", 45000.0, 5000.0, 40),
        ("Batería 12V 9Ah", TipoVehiculo.TWO_WHEELER, "Eléctrico", 180000.0, 15000.0, 15),
        ("Espejo Retrovisor Universal", TipoVehiculo.TWO_WHEELER, "Accesorios", 35000.0, 5000.0, 60),
    ]

    productos = []
    for nombre, tipo, cat, precio, envio, stock in productos_data:
        prod = Producto(nombre=nombre, tipo_vehiculo=tipo, categoria=cat, precio=precio, costo_envio_base=envio, stock=stock)
        db.add(prod)
        productos.append(prod)

    db.commit() # Asegurar que tenemos IDs

    # Ventas Históricas (Simulación)
    vendedores = ["Pedro Gomez", "Beatriz Morales", "Juan Fernandez", "Maria Alfonso"]
    sucursales = ["Bogotá", "Medellín", "Cali", "Barranquilla"]
    metodos = ["Tarjeta de crédito", "Nequi", "Efectivo", "Transferencia"]

    for _ in range(50):
        cliente = random.choice(clientes)
        producto = random.choice(productos)
        cantidad = random.randint(1, 3)
        fecha = datetime.now() - timedelta(days=random.randint(1, 365))
        metodo_pago = random.choice(metodos)

        venta = Venta(
            cliente_id=cliente.id,
            producto_id=producto.id,
            cantidad=cantidad,
            precio_unitario=producto.precio,
            costo_envio=producto.costo_envio_base,
            fecha_venta=fecha,
            vendedor=random.choice(vendedores),
            sucursal=random.choice(sucursales),
            calificacion=random.randint(1, 5),
            metodo_pago=metodo_pago,
            cantidad_cuotas=random.randint(1, 12) if "Tarjeta" in metodo_pago else 1
        )
        db.add(venta)

    db.commit()
    db.close()
    print("Base de datos poblada exitosamente.")

if __name__ == "__main__":
    seed()
