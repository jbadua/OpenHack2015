// Adding 500 Data Points
var map, positiveMap, negativeMap;

var pos = [];
var neg = [];
// Todo: use map to keep track of tweets for different tags

for (var i = 0; i < tweets.length; i++) {
  if(tweets[i].sentiment == "pos") {
    pos.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
  } else if(tweets[i].sentiment == "neg") {
    neg.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
  }
}

function initialize() {
  var positiveGradient = [
    'rgba(225, 0, 0, 0)',
    'rgba(240, 0, 0, 1)',
    'rgba(255, 0, 0, 1)'
  ];
  var negativeGradient = [
    'rgba(0, 0, 225, 0)',
    'rgba(0, 0, 240, 1)',
    'rgba(0, 0, 255, 1)'
  ];

  var mapOptions = {
    zoom: 13,
    center: new google.maps.LatLng(37.774546, -122.433523),
     mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var posArray = new google.maps.MVCArray(pos);

  positiveMap = new google.maps.visualization.HeatmapLayer({
    data: posArray,
    radius: 20,
    gradient: positiveGradient
  });

  positiveMap.setMap(map);

  var negArray = new google.maps.MVCArray(neg);

  negativeMap = new google.maps.visualization.HeatmapLayer({
    data: negArray,
    radius: 20,
    gradient: negativeGradient
  });

  negativeMap.setMap(map);
}

function toggleHeatmap() {
  positiveMap.setMap(positiveMap.getMap() ? null : map);
}

function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  positiveMap.set('gradient', positiveMap.get('gradient') ? null : gradient);
}

function changeRadius() {
  positiveMap.set('radius', positiveMap.get('radius') ? null : 20);
}

function changeOpacity() {
  positiveMap.set('opacity', positiveMap.get('opacity') ? null : 0.2);
}

google.maps.event.addDomListener(window, 'load', initialize);
