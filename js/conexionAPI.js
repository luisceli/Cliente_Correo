export async  function validarCredenciales(usuario,clave)  {
    const respuesta = await fetch(urlBase+
    `/validarUsuario/${usuario},${clave}`);
    let validador = await respuesta.json();
    return validador;
}

