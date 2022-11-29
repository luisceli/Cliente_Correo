import { ValidarCredenciales } from "./conexionAPI.js";

const formLogin=document.querySelector('#formLogin');


formLogin.addEventListener("submit",validarLogin);
async function validarLogin(e){
    e.preventDefault();
    
    const usuario = formLogin.querySelector("#user").value;
    const clave = formLogin.querySelector("#pass").value;


    let validador =  await ValidarCredenciales(usuario,clave);
    console.log(validador)
    if (validador != false) {
        window.localStorage.setItem("Usuario",usuario);
        window.localStorage.setItem("Clave",clave);
        window.location = "correo.html";
    }else{
        alert( "usuario o contraseña incorrectos");
    }

}
