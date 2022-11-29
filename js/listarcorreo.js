import { listarCorreos } from "./conexionAPI.js";

 const listarcorreo = await listarCorreos(1, window.localStorage.getItem("Usuario"), window.localStorage.getItem("Clave"))

 //console.log( listarcorreo);

 listarcorreo.Correos.forEach(element => {
 //   console.log(element)
  document.querySelector('.tbody').innerHTML += `<tr ><td class="contenedor-asunto">${element.Asunto}</td> <td>${element.De}</td> <td class="contenido-msg">${element.Body}</td> <td>${element.Fecha}</td></tr>`    
 });



