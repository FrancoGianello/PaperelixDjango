let unfold = document.querySelector('.unfold');
let fold = document.querySelector('.fold');
let contenidoDesplegable = document.querySelector('#desplegableExt');


function verMas() {
    // contenidoDesplegable.innerHTML="";
    // for (const [key, value] of Object.entries(productoActual.extendido)) {
    //     contenidoDesplegable.innerHTML+=`<strong>${key}:</strong> ${value}<br><br>`
    // }

    contenidoDesplegable.classList.remove("folded");
    contenidoDesplegable.classList.add("unfolded");
    unfold.style.display="none";
    fold.style.display="block";
}

function verMenos() {
    contenidoDesplegable.classList.remove("unfolded");
    contenidoDesplegable.classList.add("folded");
    unfold.style.display="block";
    fold.style.display="none";
}