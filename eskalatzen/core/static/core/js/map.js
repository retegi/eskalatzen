
var map = L.map('map').setView([43.039787, -2.215118], 13);

var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

var marker = L.marker([43.299135, -1.819246]).addTo(map)
    .bindPopup('<b>Pikoketa</b><br />I am a popup.').openPopup();

var marker = L.marker([43.244703, -1.805695]).addTo(map)
    .bindPopup('<b>Aritxulegi</b><br />I am a popup.').openPopup();

//var circle = L.circle([43.3207, -1.98445], {
//    color: 'red',
//    fillColor: '#f03',
//    fillOpacity: 0.5,
//    radius: 500
//}).addTo(map).bindPopup('I am a circle.');

//var polygon = L.polygon([
//    [51.509, -0.08],
//    [51.503, -0.06],
//    [51.51, -0.047]
//]).addTo(map).bindPopup('I am a polygon.');


//var popup = L.popup()
//    .setLatLng([43.3207, -1.98445])
//    .setContent('I am a standalone popup.')
//    .openOn(map);

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent('You clicked the map at ' + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);