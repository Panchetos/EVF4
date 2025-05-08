from fastapi import APIRouter, HTTPException

# Este es el router que debe existir y exportarse
actualizar_reglas = APIRouter()

@actualizar_reglas.put("/actualizar-reglas-orquestacion")
def actualizar(reglas: dict, token: str = "fake-token"):
    if token != "fake-token":
        raise HTTPException(status_code=403, detail="No autorizado")
    return {"mensaje": "Reglas de orquestación actualizadas correctamente"}
