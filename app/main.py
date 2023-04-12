from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from handlers import añadir_pedido, nuevo_restaurante, añadir_producto, obtener_todos_los_pedidos, obtener_un_pedido, \
    listar_pedidos_restaurante, cambiar_estado_pedido, listar_restuarantes, listar_productos,cambiar_estado_pedido_producto
import models
from db import session, engine
from models import Pedido
from commands import PedidoCreate, Restaurante, Producto, Estado

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/restaurantes/")
async def crear_restaurante(restaurante: Restaurante):
    return nuevo_restaurante(restaurante)


@app.get("/restaurantes/")
async def restaurantes():
    return listar_restuarantes()


@app.post("/restaurantes/productos/")
async def crear_producto(producto: Producto):
    return añadir_producto(producto)


@app.get("/restaurantes/{restaurante_id}/productos/")
async def productos(restaurante_id: int):
    return listar_productos(restaurante_id)


@app.post("/pedidos/")
async def crear_pedido(pedido: PedidoCreate):
    return añadir_pedido(pedido)


@app.get("/pedidos/")
async def pedidos():
    return obtener_todos_los_pedidos()


@app.get("/pedidos/{id_pedido}")
async def pedido(id_pedido: int):
    return obtener_un_pedido(id_pedido)


@app.get("/restaurantes/{restaurante_id}")
async def pedidos_por_restaurante(restaurante_id: int):
    return listar_pedidos_restaurante(restaurante_id)


@app.put("/pedidos/{id_pedido}/productos/{id_producto}")
async def actualizar_estado_producto_pedido(id_pedido: int, id_producto:int, estado: Estado):
    return cambiar_estado_pedido_producto(id_pedido=id_pedido, estado=estado, id_producto=id_producto)


@app.put("/pedidos/{id_pedido}")
async def actualizar_estado_pedido(id_pedido: int, estado: Estado):
    return cambiar_estado_pedido(id_pedido=id_pedido, estado=estado)
