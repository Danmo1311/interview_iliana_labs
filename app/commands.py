from enum import Enum
from typing import List

from pydantic import BaseModel


class Commands(BaseModel):
    pass


class PedidoProductoCommands(Commands):
    nombre: str
    cantidad: int
    observaciones: str = None
    para_llevar: bool
    estado: str = 'En espera'
    id_pedido: int
    id_producto: int


class PedidoCreate(Commands):
    id_pedido: int
    cedula_cliente: int
    productos: List[PedidoProductoCommands]
    estado: str = 'En espera'


class Estado(str, Enum):
    En_espera = 'En espera'
    En_preparacion = 'En preparacion'
    En_camino = 'En camino'
    Entregado = 'Entregado'
    Cancelado = 'Cancelado'


class EstadoPedido(Commands):
    estado: Estado


class Factura(Commands):
    id_factura: str
    cedula_cliente: int
    productos: List[PedidoProductoCommands]
    fecha: str
    total: float


class PedidoSalida(Commands):
    id_pedido: int
    cedula_cliente: int
    productos: List[PedidoProductoCommands]
    estado: str
    fecha: str


class Restaurante(Commands):
    id_restaurante: int
    nombre: str
    logo: str


class Producto(Commands):
    id_producto: int
    nombre: str
    descripcion: str
    precio: float
    imagen: str
    id_restaurante: int
