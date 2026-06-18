from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import enum

Base = declarative_base()

class TipoVehiculo(enum.Enum):
    TWO_WHEELER = "2wh"
    THREE_WHEELER = "3wh"

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100))
    telefono = Column(String(20))
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    ventas = relationship("Venta", back_populates="cliente")

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    tipo_vehiculo = Column(Enum(TipoVehiculo), nullable=False)
    categoria = Column(String(100)) # e.g., Motor, Frenos, Transmisión
    precio = Column(Float, nullable=False)
    costo_envio_base = Column(Float, default=0.0)
    stock = Column(Integer, default=0)

    ventas = relationship("Venta", back_populates="producto")

class Venta(Base):
    __tablename__ = 'ventas'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    producto_id = Column(Integer, ForeignKey('productos.id'))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    costo_envio = Column(Float, nullable=False)
    fecha_venta = Column(DateTime, default=datetime.utcnow)
    vendedor = Column(String(100))
    sucursal = Column(String(100))
    calificacion = Column(Integer) # 1-5
    metodo_pago = Column(String(50))
    cantidad_cuotas = Column(Integer, default=1)

    cliente = relationship("Cliente", back_populates="ventas")
    producto = relationship("Producto", back_populates="ventas")
