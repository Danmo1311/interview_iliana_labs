import uuid

from models import Pedido, Restaurante, Producto, PedidoProducto
from db import session
from commands import PedidoCreate, PedidoProductoCommands, PedidoSalida, Factura, Estado


def nuevo_restaurante(restaurante):
    if not session.query(Restaurante).filter(
            Restaurante.id_restaurante == restaurante.id_restaurante
    ).first():
        db_restaurante = Restaurante(
            id_restaurante=restaurante.id_restaurante,
            nombre=restaurante.nombre,
            logo=restaurante.logo
        )
        session.add(db_restaurante)
        session.commit()
        session.refresh(db_restaurante)
        return db_restaurante
    else:
        return "el restaurante ya existe"


def añadir_pedido(pedido: PedidoCreate):
    producs = []
    if not session.query(Pedido).filter(
            Pedido.id_pedido == pedido.id_pedido, Pedido.cedula_cliente == pedido.cedula_cliente
    ).first():
        for producto in pedido.productos:
            if producto_bd := session.query(Producto).filter(
                    Producto.id_producto == producto.id_producto
            ).first():
                db_producto = PedidoProducto(
                    nombre=producto.nombre,
                    precio=producto_bd.precio,
                    cantidad=producto.cantidad,
                    observaciones=producto.observaciones,
                    para_llevar=producto.para_llevar,
                    estado=producto.estado,
                    id_pedido=producto.id_pedido,
                    id_producto=producto.id_producto
                )
                producs.append(db_producto)
        db_pedido = Pedido(
            id_pedido=pedido.id_pedido,
            cedula_cliente=pedido.cedula_cliente,
            pedido_productos=producs,
            estado=pedido.estado
        )
        session.add(db_pedido)
        session.commit()
        return pedido
    else:
        return "el pedido ya existe"


def añadir_producto(producto):
    if not session.query(Producto).filter(
            Producto.id_producto == producto.id_producto
    ).first():
        if session.query(Restaurante).filter(
                Restaurante.id_restaurante == producto.id_restaurante
        ).first():
            db_producto = Producto(
                id_producto=producto.id_producto,
                nombre=producto.nombre,
                descripcion=producto.descripcion,
                precio=producto.precio,
                imagen=producto.imagen,
                id_restaurante=producto.id_restaurante
            )
            session.add(db_producto)
            session.commit()
            session.refresh(db_producto)
            return db_producto
        else:
            return "el restaurante no existe"
    else:
        return "el producto ya existe"


def calcular_total(pedido):
    total = 0
    productos = []

    for producto in pedido.pedido_productos:
        producto_dict = {
            'id_producto': producto.id_producto,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'cantidad': producto.cantidad,
            'observaciones': producto.observaciones,
            'para_llevar': producto.para_llevar,
            'estado': producto.estado,
        }
        productos.append(producto_dict)
        total += producto.cantidad * producto.precio
    factura = Factura(
        id_factura=str(uuid.uuid4()),
        cedula_cliente=pedido.cedula_cliente,
        productos=productos,
        fecha=str(pedido.fecha),
        total=total
    )
    return factura

def obtener_todos_los_pedidos():
    productos = []
    pedidos_lista = []
    if pedido_resultado := (session.query(Pedido).all()):

        for pedido in pedido_resultado:
            if pedido.estado == Estado.Entregado:
                respuesta = calcular_total(pedido)
            else:
                for producto in pedido.pedido_productos:
                    producto = PedidoProductoCommands(
                        nombre=producto.nombre,
                        cantidad=producto.cantidad,
                        observaciones=producto.observaciones,
                        para_llevar=producto.para_llevar,
                        estado=producto.estado,
                        id_pedido=producto.id_pedido,
                        id_producto=producto.id_producto
                    )
                    productos.append(producto)
                respuesta = PedidoSalida(
                    id_pedido=pedido.id_pedido,
                    cedula_cliente=pedido.cedula_cliente,
                    productos=productos,
                    estado=pedido.estado,
                    fecha=str(pedido.fecha)
                )
            pedidos_lista.append(respuesta)

    else:
        return "no hay pedidos"
    return pedidos_lista


def obtener_un_pedido(id_pedido):
    if pedido := session.query(Pedido).filter(Pedido.id_pedido == id_pedido).first():
        return pedido
    else:
        return "el pedido no existe"


def listar_pedidos_restaurante(restaurante_id):
    if pedidos := session.query(Restaurante).filter(
            Restaurante.id_restaurante == restaurante_id, Pedido.id_producto == Producto.id_producto,
            Producto.id_restaurante == restaurante_id
    ).all():
        return pedidos


def cambiar_estado_pedido(id_pedido, estado):
    if pedido := session.query(Pedido).filter(
            Pedido.id_pedido == id_pedido
    ).first():
        pedido.estado = str(estado.value)
        session.commit()
        return pedido
    else:
        return "el pedido no existe"


def cambiar_estado_pedido_producto(id_pedido, id_producto, estado):
    pedido = session.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    cambiado = []
    if not pedido:
        return "El pedido no existe"

    for pedido_producto in pedido.pedido_productos:
        if pedido_producto.id_producto == id_producto:
            pedido_producto.estado = str(estado.value)
            cambiado.append(pedido_producto)
            session.commit()

    return pedido


def listar_restuarantes():
    if len(session.query(Restaurante).all()) > 0:
        return session.query(Restaurante).all()
    else:
        return "no hay restaurantes"


def listar_productos(restaurante_id):
    if productos := session.query(Producto).filter(
            Producto.id_restaurante == restaurante_id
    ).all():
        return productos
    else:
        return "no hay productos"
