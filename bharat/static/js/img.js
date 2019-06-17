var x;
var h5=document.querySelector('h5');
function bansal(){
$.getJSON(" https://api.thingspeak.com/channels/641798/fields/1/last.json?api_key=T49ZYG8UVGE6L0D7&results=2",function(data){
	x=data['field1']
	console.log(x);
	if(x==='0'){
		$('img').attr('src','/static/images/Capture.png')
		h5.textContent="No chance of flood enjoy your life";
	}
	else if(x==='1'){
		$('img').attr('src','/static/images/alert1.jpg')
		h5.textContent="People of hisar are on alert";
	}
	else if(x==='2'){
		$('img').attr('src','/static/images/alert2.jpg');
		h5.textContent="People of hisar and rohtak are on alert";
	}
	else{
		$('img').attr('src','/static/images/alert3.jpg')
		h5.textContent="High level flood is alert in all area near dam"		
	}
});
}
setInterval(bansal,10000);