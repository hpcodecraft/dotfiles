$(function() {
  console.info("%c.js\t\t" + "%czelluloid.de script loaded", "color: #FF1493; font-weight: bold", "color: black");
  setInterval(cleanUp, 1000);
  cleanUp();
});

function cleanUp() {
  $('.zRectangle').remove();
}
