const estado = document.getElementById("mensaje");
const input = document.getElementById("id_ip");
const ip = "152.162.0.0"


input.addEventListener('change', (e) => {
    const ip = e.target.value;
    console.log(ip)

    function validarIP(ip) {
        const regex = /^(\d{1,3}\.){3}\d{1,3}$/;
        return regex.test(ip);
    }

    if (validarIP(ip)) {
        estado.textContent = 'La dirección IP es válida...'

    } else {
        estado.textContent = '\La dirección IP es inválida... \Tener en cuenta que el rango total de direcciones IP oscila entre 0.0.0.0 y 255.255.255.255. ' + 'Si guarda no funcionará...'
    }

})
;
