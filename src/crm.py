from src.models import Cliente, Venta
from sqlalchemy.orm import Session

def registrar_cliente(db: Session, nombre: str, email: str = None, telefono: str = None):
    cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def obtener_historial_cliente(db: Session, cliente_id: int):
    return db.query(Venta).filter(Venta.cliente_id == cliente_id).order_by(Venta.fecha_venta.desc()).all()

def listar_clientes(db: Session):
    return db.query(Cliente).all()
