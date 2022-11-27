import imaplib
import email
from email.header import decode_header
import os
from datetime import datetime

# Datos del usuario
#username = input("Correo: ")
#password = getpass("Password: ")
username = 'marcelolatino.mx@gmail.com'
password = 'himlbcjvrjroplpl'

def conexionCorreo (username,password):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    try:
        imap.login(username, password)
    except:
        return False
    return imap

def listaCorreos (pag,username,password):
    imap = conexionCorreo(username,password)
    n = 1
    Respuesta = {'Correos':[]}
    status, mensajes = imap.select("INBOX")
    if(status=='OK'):
        minimo = n*pag
        maximo = int(mensajes[0])
        for i in range((maximo-(n*(pag-1))), maximo - minimo, -1):
            try:
                res, mensaje = imap.fetch(str(i), "(RFC822)")
            except:
                break
            for respuesta in mensaje:
                if isinstance(respuesta, tuple):
                    # Obtener el contenido
                    mensajeD = email.message_from_bytes(respuesta[1])
                    # decodificar el contenido
                    subject = decode_header(mensajeD["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # convertir a string
                        subject = subject.decode()
                    # de donde viene el correo
                    from_ = mensajeD.get("From")
                    fecha = mensajeD.get("Date")
                    fecha = datetime.strptime(fecha, '%a, %d %b %Y %H:%M:%S %z (%Z)')
                    

                    item = {'Asunto':subject,'De':from_,'Fecha':fecha.strftime("%d/%m/%Y")}
                    if mensajeD.is_multipart():
                    # Recorrer las partes del correo
                        for part in mensajeD.walk():
                            # Extraer el contenido
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if content_type == "text/plain":
                                try:
                                    # el cuerpo del correo
                                    body = part.get_payload(decode=True).decode()
                                except:
                                    pass
                                if "attachment" not in content_disposition:
                                    item["Body"] = body
                                    
                else:
                    # contenido del mensaje
                    content_type = mensajeD.get_content_type()
                    if content_type == "text/plain":
                        # cuerpo del mensaje
                        body = mensajeD.get_payload(decode=True).decode()
                        
                        item["Body"] = body
                
        Respuesta["Correos"].append(item)
        imap.close()
        imap.logout()
        return Respuesta     
    else:
        return False


'''cx = conexionCorreo (username,password)
if (not cx == False):
    lista = listaCorreos(1,username,password)
    print(lista)
else:
    print('sdaqdas')

'''
