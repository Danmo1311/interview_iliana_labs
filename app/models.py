from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurante(Base):
    __tablename__ = "restaurante"

    id_restaurante = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    logo = Column(String(255))

    productos = relationship("Producto", back_populates="restaurante")


class Pedido(Base):
    __tablename__ = "pedido"

    id_pedido = Column(Integer, primary_key=True, index=True)
    estado = Column(String(200))
    fecha = Column(DateTime, index=True, nullable=False, default=datetime.now())
    cedula_cliente = Column(Integer, nullable=False)
    pedido_productos = relationship("PedidoProducto", back_populates="pedido")


class Producto(Base):
    __tablename__ = "producto"

    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    descripcion = Column(String(255))
    precio = Column(Float)
    imagen = Column(String(255))
    id_restaurante = Column(Integer, ForeignKey("restaurante.id_restaurante"))

    restaurante = relationship("Restaurante", back_populates="productos")
    pedido_productos = relationship("PedidoProducto", back_populates="producto")


class PedidoProducto(Base):
    __tablename__ = "pedido_producto"

    id_pedido_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    precio = Column(Float)
    cantidad = Column(Integer)
    observaciones = Column(String(255))
    para_llevar = Column(Boolean)
    estado = Column(String(200))
    id_pedido = Column(Integer, ForeignKey("pedido.id_pedido"))
    id_producto = Column(Integer, ForeignKey("producto.id_producto"))

    pedido = relationship("Pedido", back_populates="pedido_productos")
    producto = relationship("Producto", back_populates="pedido_productos")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "observaciones": self.observaciones,
            "para_llevar": self.para_llevar,
            "estado": self.estado,
            "producto_id": self.producto_id,
            "pedido_id": self.pedido_id,
            "id_producto": self.producto.to_dict(),

        }