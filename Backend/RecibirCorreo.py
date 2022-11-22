import imaplib
import email
from email.header import decode_header
from getpass import getpass

# Datos del usuario
#username = input("Correo: ")
#password = getpass("Password: ")
#username = 'marcelolatino.mx@gmail.com'
#password = 'himlbcjvrjroplpl'

def conexionCorreo (username,password):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    try:
        imap.login(username, password)
    except:
        return False
    return imap

def listaCorreos (pag,username,password):
    imap = conexionCorreo(username,password)
    n = 2
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

                    item = {'Asunto':subject,'De':from_,'fecha':'25/12/2022'}
                    Respuesta["Correos"].append(item)

                    #print("Subject:", subject)
                    #print("From:", from_)
        return Respuesta     
    else:
        return False


def leerCorreos (imap):
    N = 1
    status, mensajes = imap.select("INBOX")
    mensajes = int(mensajes[0])
    for i in range(mensajes, mensajes - N, -1):
        try:
            res, mensaje = imap.fetch(str(i), "(RFC822)")
        except:
            break
        for respuesta in mensaje:
            if isinstance(respuesta, tuple):
                # Obtener el contenido
                mensaje = email.message_from_bytes(respuesta[1])
                # decodificar el contenido
                subject = decode_header(mensaje["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # convertir a string
                    subject = subject.decode()
                # de donde viene el correo
                from_ = mensaje.get("From")
                
                print("Subject:", subject)
                print("From:", from_)
                print("Mensaje obtenido con exito")
                # si el correo es html
                if mensaje.is_multipart():
                    # Recorrer las partes del correo
                    for part in mensaje.walk():
                        # Extraer el contenido
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        if content_type == "text/plain":
                            try:
                                # el cuerpo del correo
                                body = part.get_payload(decode=True).decode()
                                #print("Body",body)
                            except:
                                pass
                            if "attachment" not in content_disposition:
                                # Mostrar el cuerpo del correo
                                print(body)
                            elif "attachment" in content_disposition:
        #                         # download attachment
                                nombre_archivo = part.get_filename()
                                if nombre_archivo:
                                    if not os.path.isdir(subject):
                                        # crear una carpeta para el mensaje
                                        os.mkdir(subject)
                                    ruta_archivo = os.path.join(subject, nombre_archivo)
                                    # download attachment and save it
                                    open(ruta_archivo, "wb").write(part.get_payload(decode=True))
    imap.close()
    imap.logout()


cx = conexionCorreo (username,password)
if (not cx == False):
    listaCorreos(cx,1)
else:
    print('sdaqdas')


