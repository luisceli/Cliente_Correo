const formLogin=document.querySelector('formLogin');

async function validarLogin(e){
    e.preventDefault();
    
    const usuario = formLogin.querySelector("#user").value;
    const clave = formLogin.querySelector("#pass").value;
    let validador =  await validarCredenciales(usuario,clave);
    if (validador.nombres != undefined) {
        localStorage.setItem("usuarioLocalUsuario",validador.usuario);
        localStorage.setItem("usuarioLocalClave",validador.clave);
        window.location = "correo.html";
    }else{
        alert( "usuario o contraseña incorrectos");
    }
}
