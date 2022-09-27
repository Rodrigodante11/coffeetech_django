let myChartTemperatura = null;
let myChartUmidade =null;
let myChartUmidadexTempo =null;
var temperatura =[]
var tempo = []
var umidade =[]

function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }

    return [bg_color, border_color];

}

function startTimer(duration, display){
    let timer = duration, minutes, seconds;

    setInterval(function (){
        minutes = parseInt(timer/60 , 10);
        seconds = parseInt(timer %60, 10),

         minutes = minutes < 10 ? "0" + minutes : minutes;
         seconds = seconds < 10 ? "0" + seconds : seconds;

         display.textContent = minutes + ":" + seconds;

         if(--timer < 0){
             timer= duration;
         }
    },1000);
}

function renderiza_dados(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json();
    }).then(function(data){

        document.getElementById('temperatura_atual').innerHTML = data.temperatura;
        document.getElementById('umidade_atual').innerHTML = data.umidade;
        document.getElementById('power_atual').innerHTML = data.power;
    });

}
window.onload = function () {
    if (null != document.querySelector('#idSenhaLogin')) {
        var password =document.getElementById('visibilityBtn');
        password.addEventListener("click", toggleVisibility);

        function toggleVisibility() {
            const passwordInput = document.getElementById("idSenhaLogin");

            if(passwordInput.type ==="password"){
                password.className = "fa-solid fa-eye fa-xl text-sm-left";
                passwordInput.type ="text";
            }else {
                password.className = "fa-solid fa-eye-slash fa-xl text-right";
                passwordInput.type ="password";
            }
        }
    }

    if (null != document.querySelector('#timer')) {
        var duration = parseInt(document.querySelector('#timer').innerHTML) * 60; //conversao para segundos
        var display = document.querySelector("#timer"); // Elemento para exibir o timer

        startTimer(duration, display); //inicia a funcao
    }
};

function renderiza_temperatura(){

    const ctx = document.getElementById('temperatura_atual_canvas').getContext('2d');

    if(document.getElementById('temperatura_atual').innerHTML==''){
        temperatura.push('0')
        tempo.push('0')
    }else{
        temperatura.push(document.getElementById('temperatura_atual').innerHTML)
        tempo.push(document.getElementById('timer').innerHTML)
    }

    let data = {
        labels: tempo,
        datasets: [{
            label: 'Temperatura',
            data: temperatura,
            backgroundColor: "#CB1EA8",
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    }
    const config = {
      type: 'line',
      data: data,
    };
    if (myChartTemperatura!=null){
        myChartTemperatura.destroy();
    }
    myChartTemperatura = new Chart(ctx, config);

}
function renderiza_umidade(){

    const ctx = document.getElementById('umidade_atual_canvas').getContext('2d');

    if(document.getElementById('umidade_atual').innerHTML==''){
        umidade.push('0')
        tempo.push('0')
    }else{
        umidade.push(document.getElementById('umidade_atual').innerHTML)
        tempo.push(document.getElementById('timer').innerHTML)
    }

    let data = {
        labels: tempo,
        datasets: [{
            label: 'Umidade',
            data: umidade,
            backgroundColor: "#CB1EA8",
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    }
    const config = {
      type: 'line',
      data: data,
    };
    if (myChartUmidade!=null){
        myChartUmidade.destroy();
    }
    myChartUmidade = new Chart(ctx, config);

}
// function temperatura_umidade_atual(){
//
//     const ctx = document.getElementById('temperatura_umidade_atual_canvas').getContext('2d');
//
//     if(document.getElementById('umidade_atual').innerHTML==''){
//         umidade.push('0')
//         temperatura.push('0')
//     }else{
//         umidade.push(document.getElementById('umidade_atual').innerHTML)
//         temperatura.push(document.getElementById('temperatura_atual').innerHTML)
//     }
//
//     let data = {
//         labels: temperatura,
//         datasets: [{
//             label: 'Umidade x Tempo',
//             data: umidade,
//             backgroundColor: "#CB1EA8",
//             borderColor: 'rgb(75, 192, 192)',
//             tension: 0.1
//         }]
//     }
//     const config = {
//       type: 'line',
//       data: data,
//     };
//     if (myChartUmidadexTempo!=null){
//         myChartUmidadexTempo.destroy();
//     }
//     myChartUmidadexTempo = new Chart(ctx, config);
//
// }