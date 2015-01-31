var map, pointarray, positiveMap, negativeMap;
var positive = [];
var negative = [];
for (var i = 0; i < positiveTweets.length; i++) {
  var str = positiveTweets[i];
  var obj = JSON.parse(str);
  if (obj['lat'] != null && obj['lng'] != null) {
    positive.push(new google.maps.LatLng(obj['lat'], obj['lng']));
  }
}
for (var i = 0; i < negativeTweets.length; i++) {
  var str = negativeTweets[i];
  var obj = JSON.parse(str);
  if (obj['lat'] != null && obj['lng'] != null) {
    negative.push(new google.maps.LatLng(obj['lat'], obj['lng']));
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
    zoom: 13,
    center: new google.maps.LatLng(37.774546, -122.433523),
     mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var pointArray = new google.maps.MVCArray(positive);

  positiveMap = new google.maps.visualization.HeatmapLayer({
    data: pointArray,
    radius: 20,
    gradient: positiveGradient
  });

  positiveMap.setMap(map);

  var pointArray2 = new google.maps.MVCArray(negative);

  negativeMap = new google.maps.visualization.HeatmapLayer({
    data: pointArray2,
    radius: 20,
    gradient: negativeGradient
  });

  negativeMap.setMap(map);
}

function toggleHeatmap() {
  positiveMap.setMap(positiveMap.getMap() ? null : map);
}

google.maps.event.addDomListener(window, 'load', initialize);
