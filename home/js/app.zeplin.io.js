$(function() {
  setTimeout(killUselessStuff, 2500);
});

function killUselessStuff() {
  $('#intercom-container').remove();
}
