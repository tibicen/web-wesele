// Contact Map
var contactMap = document.getElementById("mapa2");
if (contactMap) {
  var mymap = L.map('mapa2', { zoomControl: true }).setView([51.18, 16.9], 10);

  var OpenStreetMap_HOT = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
    // bounds: [[-75, -180], [81, 180]],
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, Tiles courtesy of <a href="http://hot.openstreetmap.org/" target="_blank">Humanitarian OpenStreetMap Team</a>'
});


var palac = new L.marker([51.24646,16.79723], { opacity: 1 });
palac.bindTooltip("Wesele", { permanent: true, className: "city-name", offset: [25, 0], direction: 'center' });
palac.bindPopup('W zabytkowym pałacyku Lenartowice odbędzie się ślub i wesele.<br><a href="https://goo.gl/maps/j1MrSKQsTLxZGAgZ8">Prowadź</a>');

var winnica = new L.marker([51.19573, 16.73738], { opacity: 1 });
winnica.bindTooltip("Winnica", { permanent: true, className: "city-name", offset: [-57, 5], direction: 'center' });
winnica.bindPopup('Noclegi w Winnicy Jaworek<br><a href="https://g.page/WinniceJaworek?share">Prowadź</a>');

var hotel = new L.marker([51.19621, 16.74518], { opacity: 1 });
hotel.bindTooltip("Hotel", { permanent: true, className: "city-name", offset: [20, 5], direction: 'center' });
hotel.bindPopup('Noclegi w Hotelu<br><a href="https://goo.gl/maps/6rCXnceAmqw8wfgx7">Prowadź</a>');



hotel.addTo(mymap);
winnica.addTo(mymap);
palac.addTo(mymap);
OpenStreetMap_HOT.addTo(mymap);
}