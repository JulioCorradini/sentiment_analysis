async function capturarElTexto () {
    var texto = document.getElementById("texto").value;
    var data = {"texto": texto};
    
    try {
    
        await enviarElContenido(data);
    
        //await enviarAlertaAPython();
    
        //await recibirElContenido();
    } catch (error) {
        console.log(error);
    }

}

async function enviarElContenido(data) {
    
    return new Promise((resolve, reject) => {

        fetch("http://localhost:8080/texto", {
            method: "POST",
            headers: {
                "content-type": "application/json"
            },
            body: JSON.stringify(data)
        }).then (response=>response.json())
        .then (data=>console.log(data))
        .catch(error=>console.log(error));
    });
}

/*async function enviarElContenido(data) {
    
    return new Promise((resolve, reject) => {

        fetch("http://localhost:8080/texto", {
            method: "POST",
            headers: {
                "content-type": "application/json"
            },
            body: JSON.stringify(data)
        }).then (response=> {
            resolve();
        })
        .catch(error=> {
            reject(error);
        });
    });
}*/

async function enviarAlertaAPython() {
    //var mensaje = {"mensaje": "Coneccion correcta"}
    fetch("http://localhost:5000/analisis", {
        method: "POST",
        /*headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(mensaje)*/
    })//.then (response=>response.json())
    //.then (data=>console.log(data))
    .then(console.log("Solicitud enviada"))
    .catch(error=>console.log(error))
}

/*async function enviarAlertaAPython() {
    
    return new Promise((resolve, reject) => {
        var mensaje = {"mensaje": "Coneccion correcta"}
        fetch("http://localhost:5000/analisis", {
            method: "POST",
            headers: {
                "content-type": "application/json"
            },
            body: JSON.stringify(data)
        }).then (response=> {
            resolve();
        })
        .catch(error=> {
            reject(error);
        });
    });
}*/

async function recibirElContenido(){
    fetch("http://localhost:8080/analisisGET")
    .then(response=>response.text())
    .then(mensaje=>{
        var mensajeContainer = document.getElementById("mensaje-container");
        mensajeContainer.textContent = mensaje;
    })
    .catch(error=>console.log(error)); 
}

/*async function recibirElContenido() {
    
    return new Promise((resolve, reject) => {

        fetch("http://localhost:8080/analisisGET")
            .then(response=>response.text())
            .then (mensaje=>{
                var mensajeContainer = document.getElementById("mensaje-container");
                mensajeContainer.textContent = mensaje;
                resolve();
            })
            .catch(error=> {
                reject(error);
            });
    });
}*/
