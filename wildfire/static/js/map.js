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
    'rgba(57, 133, 69, 0)',
    'rgba(44, 101, 75, 1)',
    'rgba(21, 66, 94, 1)',
    'rgba(0, 0, 200, 1)',
    'rgba(0, 0, 225, 1)',
    'rgba(0, 0, 240, 1)',
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
    zoom: 10,
    center: new google.maps.LatLng(37.7833, -122.4167),
     mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var posArray = new google.maps.MVCArray(pos);
  var negArray = new google.maps.MVCArray(neg);

  positiveMap = new google.maps.visualization.HeatmapLayer({
    data: posArray,
    radius: 20,
    gradient: positiveGradient,
    opacity: 8
  });
  negativeMap = new google.maps.visualization.HeatmapLayer({
    data: negArray,
    radius: 20,
    gradient: negativeGradient,
    opacity: 8
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
