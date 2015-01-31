var map, positiveMap, negativeMap, posArray, negArray;

var pos = [];
var neg = [];
// Todo: use map to keep track of tweets for different tags

var termMap = {}

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

function buildTweets(term) {
  for (var i = 0; i < tweets.length; i++) {
    if(term == null || term == tweets[i].searchterm) {
      if(!(tweets[i].searchterm in termMap)) {
        termMap[tweets[i].searchterm] = true;
      }

      if (tweets[i].lat != null && tweets[i].lng != null) {
        if (tweets[i].sentiment == "pos") {
          pos.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
        } else if (tweets[i].sentiment == "neg") {
          neg.push(new google.maps.LatLng(tweets[i].lat, tweets[i].lng));
        }
      }
    }
  }
}

function initialize() {

  var mapOptions = {
    zoom: 2,
    center: new google.maps.LatLng(51.5072, -0.1275),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    styles: mapStyle
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  setHeatMap(null);

  for (var key in termMap) {
    if (termMap.hasOwnProperty(key)) {
      $( "<option value=" + key + ">" + key + "</option>").appendTo( "#filter" );
    }
  }
}

function setHeatMap(term) {
  pos = [];
  neg = [];

  var posArray = new google.maps.MVCArray(pos);
  var negArray = new google.maps.MVCArray(neg);

  buildTweets(term);

  

  positiveMap = new google.maps.visualization.HeatmapLayer({
    data: posArray,
    radius: 25,
    gradient: positiveGradient,
    opacity: 0.5
  });
  negativeMap = new google.maps.visualization.HeatmapLayer({
    data: negArray,
    radius: 25,
    gradient: negativeGradient,
    opacity: 0.5
  });

  negativeMap.setMap(map);
  positiveMap.setMap(map);
}

function togglePositiveHeatmap() {
  positiveMap.setMap(positiveMap.getMap() ? null : map);
}
function toggleNegativeHeatmap() {
  negativeMap.setMap(negativeMap.getMap() ? null : map);
}

google.maps.event.addDomListener(window, 'load', initialize);


$( "#filter" )
  .change(function () {
    $( "#filter option:selected" ).each(function() {
      if($( this ).text() == "All") {
        setHeatMap(null);
      }
      else {
        setHeatMap($( this ).text());
      }
    });
}).change();
