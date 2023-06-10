function getTlgmId (){
    let tg = window.Telegram.WebApp;
    return tg.initDataUnsafe.user.id
}
function sendData(){
    let tg = window.Telegram.WebApp;
	tg.sendData("some string that we need to send");
    //при клике на основную кнопку отправляем данные в строковом виде
}

