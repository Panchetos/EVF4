from fastapi import APIRouter, HTTPException

autenticar_usuario = APIRouter()
autorizar_acceso = APIRouter()

@autenticar_usuario.post("/autenticar-usuario")
def login(nombre_usuario: str, contrasena: str):
    if nombre_usuario == "admin" and contrasena == "1234":
        return {"token": "fake-token", "rol": "Administrador"}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")

@autorizar_acceso.post("/autorizar-acceso")
def autorizar(recursos: list[str], rol_usuario: str):
    if rol_usuario in ["Administrador", "Orquestador"]:
        return {"autorizado": True}
    return {"autorizado": False}
