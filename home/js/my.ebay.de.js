/**
 * User script for "My Ebay" page
 * Hides Ads
 */

$(function() {
  console.log('My Ebay script ready');

  // hide stuff
  var selectors = [
    '#GlobalNavigation > div:eq(1) > div:first',
    '#iconLegend ~ div',
    '#SupportiveNavigation > div > div:eq(2)',

  ];

  function tick() {
    if(selectors.length > 0) {
      var selector = selectors[0];

      if($(selector).length > 0) {

        $(selector)
          //.css('border', '2px solid red')
          .remove();

        selectors.shift();
      }
    }
  }


  setInterval(tick, 50);
});