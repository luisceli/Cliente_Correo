from pydantic import BaseModel

class Correo(BaseModel):
       
    Asunto : str
    De : str
    Para : str
    Contenido : str
    Clave : str
