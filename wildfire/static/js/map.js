var map, positiveMap, negativeMap;

var pos = [];
var neg = [];
// Todo: use map to keep track of tweets for different tags

for (var i = 0; i < tweets.length; i++) {
  if (tweets[i].lat != null && tweets[i].lng != null) {
    if (tweets[i].sentiment == "pos") {
      pos.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
    } else if (tweets[i].sentiment == "neg") {
      neg.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
    }
  }
}

function initialize() {
  var positiveGradient = [
    'rgba(55, 149, 245, 0)',
    'rgba(40, 80, 246, 1)',
    'rgba(30, 40, 247, 1)',
    'rgba(0, 0, 249, 1)',
    'rgba(0, 0, 250, 1)',
    'rgba(0, 0, 253, 1)',
    'rgba(0, 0, 255, 1)'
  ];

  var negativeGradient = [
    'rgba(245, 149, 55, 0)',
    'rgba(246, 80, 40, 1)',
    'rgba(247, 40, 30, 1)',
    'rgba(249, 0, 0, 1)',
    'rgba(250, 0, 0, 1)',
    'rgba(253, 0, 0, 1)',
    'rgba(255, 0, 0, 1)'
  ];


  var mapOptions = {
    zoom: 2,
    center: new google.maps.LatLng(51.5072, -0.1275),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    styles: mapStyle
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var posArray = new google.maps.MVCArray(pos);
  var negArray = new google.maps.MVCArray(neg);

  positiveMap = new google.maps.visualization.HeatmapLayer({
    data: posArray,
    radius: 20,
    gradient: positiveGradient,
    opacity: .5
  });
  negativeMap = new google.maps.visualization.HeatmapLayer({
    data: negArray,
    radius: 20,
    gradient: negativeGradient,
    opacity: .5
  });

  positiveMap.setMap(map);
  negativeMap.setMap(map);
}

function togglePositiveHeatmap() {
  positiveMap.setMap(positiveMap.getMap() ? null : map);
}
function toggleNegativeHeatmap() {
  negativeMap.setMap(negativeMap.getMap() ? null : map);
}

google.maps.event.addDomListener(window, 'load', initialize);
