
const archivo = document.querySelector('#archivo')
const imagen = document.querySelector('#imagen-file')


archivo.addEventListener('change', () =>{
    let reader = new FileReader();

        reader.onload = function(e){
            imagen.src = `${e.target.result}`
        }

        reader.readAsDataURL(archivo.files[0]);
})
