// Cookie Clicker
$(function() {

  var productLimit = 200;

  // show that the script is running
  console.info('dotjs script enabled');

  // LOOP START
  var interval = setInterval(function() {

    // automatically click the big cookie
    $('#bigCookie').click();

    // automatically click season popups (reindeers)
    $('#seasonPopup').click();

    // automatically click golden cookies
    var bg = $('#goldenCookie').css('background');
    if(bg !== 'url(http://orteil.dashnet.org/cookieclicker/img/spookieCookie.png)') {
      $('#goldenCookie').click();
    }

    // automatically buy buildings until a specified count is reached (200 of each sort by default)
    var products = $('.product.enabled');
    products.each(function(){
	    var owned = $(this).find('.title.owned').html();
	    if(parseInt(owned) < productLimit) $(this).click();
    });

  }, 1);
  // LOOP END
})
