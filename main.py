from fastapi import FastAPI
from auth import autenticar_usuario, autorizar_acceso
from services import (
    orquestar_servicio,
    obtener_info_servicio,
    registrar_servicio
)
from reglas import actualizar_reglas

app = FastAPI()

# Incluir rutas
app.include_router(autenticar_usuario)
app.include_router(autorizar_acceso)
app.include_router(orquestar_servicio)
app.include_router(obtener_info_servicio)
app.include_router(registrar_servicio)
app.include_router(actualizar_reglas)
