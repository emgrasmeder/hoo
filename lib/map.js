var MapboxClient = require('mapbox');
var token = process.env.MAPBOX_ACCESS_TOKEN;
var client = new MapboxClient(token);
client.geocodeForward('chester NJ', function(err, res) {
  console.log(err);
  console.log(res);
});

