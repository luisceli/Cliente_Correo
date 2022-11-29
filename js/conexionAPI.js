var urlBase = 'http://127.0.0.1:8000';

export async  function ValidarCredenciales(usuario,clave)  {
    const respuesta = await fetch(urlBase+
    `/ValidarCredenciales/${usuario},${clave}`);
    let validador = await respuesta.json();
    return validador;
}

//trae una json con una lista de correos, tambien se especifica la pagina a listar por defecto trae 7 correos a la vez
export async  function listarCorreos(pag,usuario,clave)  {
    const respuesta = await fetch(urlBase+
    `/ListarCorreos/${pag},${usuario},${clave}`);
    let validador = await respuesta.json();
    return validador;
}

//recive json con la estructura y datos deel correo Asunto, De, Para, Contenido, Clave
export async function enviarCorreo(correo)  {
    const respuesta = await fetch(urlBase+
    `/enviarCorreo`,
    {method:'POST',
    body:JSON.stringify(correo),
    headers:{
        'Content-Type':'application/json'
    }});
    let validador = await respuesta.json();
    return validador;
}

