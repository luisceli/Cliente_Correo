import { enviarCorreo } from "./conexionAPI.js";

//const asunto= document.querySelector('#asunto').value
 //console.log(asunto)
async function redactarCorreo(){
    let correo={}
        correo.Asunto= document.querySelector("#asunto").value
  // console.log(asunto)
    //console.log("hola")
        correo.De = localStorage.getItem("Usuario")
    correo.Para=document.querySelector("#para").value
    correo.Contenido = document.querySelector("#msg").value
    correo.Clave=localStorage.getItem("Clave")
   // console.log(correo)

    await enviarCorreo(correo)

    document.querySelector("#asunto").value=""
    document.querySelector("#para").value=""
    document.querySelector("#msg").value=""
    
    alert("Correo enviado")
}

const btn= document.querySelector('#btn-enviar')

btn.addEventListener('click',redactarCorreo)


