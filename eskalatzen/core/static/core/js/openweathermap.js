
var input = document.querySelector('.input_text');
var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var wind = document.querySelector('.wind');
var desc = document.querySelector('.desc');
var clouds = document.querySelector('.clouds');
var button= document.querySelector('.submit');


button.addEventListener('click', function(name){
fetch('https://api.openweathermap.org/data/2.5/weather?q='+input.value+'&units=metric&appid=32ce3717017406682b290a5dd99fbc99')
.then(response => response.json())
.then(data => {
  var tempValue = data['main']['temp'];
  var windValue = data['wind']['speed'];
  var nameValue = data['name'];
  var descValue = data['weather'][0]['description'];

  main.innerHTML = nameValue;
  desc.innerHTML = "Desc - "+descValue;
  temp.innerHTML = "Temp - "+tempValue;
  wind.innerHTML = "Wind - "+windValue;
  input.value ="";

})

.catch(err => alert("Wrong city name!"));
})