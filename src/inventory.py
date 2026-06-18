from src.models import Producto, TipoVehiculo
from sqlalchemy.orm import Session

def listar_productos(db: Session, tipo: TipoVehiculo = None):
    query = db.query(Producto)
    if tipo:
        query = query.filter(Producto.tipo_vehiculo == tipo)
    return query.all()

def buscar_producto(db: Session, termino: str):
    return db.query(Producto).filter(Producto.nombre.ilike(f"%{termino}%")).all()

def actualizar_stock(db: Session, producto_id: int, cantidad: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto and producto.stock >= cantidad:
        producto.stock -= cantidad
        db.commit()
        return True
    return False
