function startTimer(duration, display){
    var timer = duration, minutes, seconds;

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

window.onload = function () {
    var password =document.getElementById('visibilityBtn')
    password.addEventListener("click", toggleVisibility)

    function toggleVisibility() {
        const passwordInput = document.getElementById("idSenhaLogin")

        if(passwordInput.type ==="password"){
            password.className = "fa-solid fa-eye fa-xl text-sm-left"
            passwordInput.type ="text"
        }else {
            password.className = "fa-solid fa-eye-slash fa-xl text-right"
            passwordInput.type ="password"
        }
    }
    // var duration =parseInt(document.querySelector('#timer').innerHTML) *60 ; //conversao para segundos
    // var display= document.querySelector("#timer"); // Elemento para exibir o timer
    //
    // startTimer(duration, display); //inicia a funcao

}