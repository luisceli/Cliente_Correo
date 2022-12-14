from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI as fast
import RecibirCorreo as rc
import baseModels as bm
import enviarCorreos as ec

app = fast()

origins = [

    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''@app.post("/InUsuario")
def ingresarUsuario (usuario: mE.usuario):
    inUsu(usuario.dict())
    return True'''


@app.get("/ValidarCredenciales/{user},{pas}")
def validarUsuario(user, pas):
    respuesta = rc.validarCredenciales(user, pas)

    return respuesta


@app.get("/ListarCorreos/{pag},{user},{pas}")
def validarUsuario(pag, user, pas):
    pag = int(pag)
    respuesta = rc.listaCorreos(pag, user, pas)
    return respuesta


@app.post("/enviarCorreo")
def ingresarUsuario(correo: bm.Correo):
    jcorreo = correo.dict()
    print(correo.dict())
    respuesta = ec.EnvairCorreo(
        jcorreo['Asunto'], jcorreo['De'], jcorreo['Para'], jcorreo['Contenido'], jcorreo['Clave'])
    return True
