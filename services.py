from fastapi import APIRouter, Depends, HTTPException

orquestar_servicio = APIRouter()
obtener_info_servicio = APIRouter()
registrar_servicio = APIRouter()

@orquestar_servicio.post("/orquestar")
def orquestar(servicio_destino: str, parametros_adicionales: dict, token: str = "fake-token"):
    return {"mensaje": f"Orquestando servicio {servicio_destino} con {parametros_adicionales}"}

@obtener_info_servicio.get("/informacion-servicio/{id}")
def obtener_info(id: str, token: str = "fake-token"):
    return {"id": id, "info": "Información simulada del servicio"}

@registrar_servicio.post("/registrar-servicio")
def registrar(nombre: str, descripcion: str, endpoints: list[str], token: str = "fake-token"):
    return {"mensaje": f"Servicio {nombre} registrado correctamente"}
