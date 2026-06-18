import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, TipoVehiculo
from src.inventory import listar_productos, buscar_producto
from src.crm import registrar_cliente, listar_clientes

# Setup database para pruebas
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_registrar_cliente(db):
    cliente = registrar_cliente(db, "Test User", "test@example.com", "123456")
    assert cliente.id is not None
    assert len(listar_clientes(db)) == 1

def test_buscar_producto_vacio(db):
    res = buscar_producto(db, "Inexistente")
    assert len(res) == 0
