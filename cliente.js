/*function enviarTexto() {
    var textoIngresado = document.getElementById("textoInput").value;

    // Enviar el texto al servidor Python
    fetch('/analisis', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texto: textoIngresado }),
    })
    .then(response => response.json())
    .then(data => {
        // Mostrar el nuevo dato en la página HTML
        document.getElementById("resultado").innerText = "Valoración: " + data.valoracion;
    });
}*/