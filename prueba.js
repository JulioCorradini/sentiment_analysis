function enviarAlertaAPython() {
    var mensaje = {
        "mensaje": "Coneccion correcta"
    };
    fetch("http://localhost:5000/analisis", {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(mensaje)
    }).then (response=>response.json())
    .then (data=>console.log(data))
    .catch(error=>console.log(error))
}