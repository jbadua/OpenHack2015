// Adding 500 Data Points
var map, positiveMap, negativeMap;

var pos = [];
var neg = [];
// Todo: use map to keep track of tweets for different tags

for (var i = 0; i < tweets.length; i++) {
  if (tweets[i].sentiment == "pos") {
    pos.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
  } else if (tweets[i].sentiment == "neg") {
    neg.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
  }
}

function initialize() {
  var positiveGradient = [
    'rgba(0, 0, 225, 0)',
    'rgba(0, 0, 240, 1)',
    'rgba(0, 0, 255, 1)'
  ];

  var negativeGradient = [
    'rgba(225, 0, 0, 0)',
    'rgba(240, 0, 0, 1)',
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
    gradient: positiveGradient
  });
  negativeMap = new google.maps.visualization.HeatmapLayer({
    data: negArray,
    radius: 20,
    gradient: negativeGradient
  });

  positiveMap.setMap(map);
  negativeMap.setMap(map);
}

function toggleHeatmap() {
  positiveMap.setMap(positiveMap.getMap() ? null : map);
}

google.maps.event.addDomListener(window, 'load', initialize);
