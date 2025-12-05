from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./base_datos.db"
motor = create_engine(DATABASE_URL, echo=True)

def crear_bd_y_tablas():
    SQLModel.metadata.create_all(motor)

def obtener_sesion():
    with Session(motor) as sesion:
        yield sesion