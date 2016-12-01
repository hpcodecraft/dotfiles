function removeFeedAds() {

  var str = 'Vorgeschlagener Beitrag';

  var strArr = ['Vorgeschlagener Beitrag', 'Personen, die du vielleicht kennst']
  var posts = document.querySelectorAll('div[data-testid=fbfeed_story]');

  for(var i = 0; i < posts.length; i++) {
    var post = posts[i],
        ads = null;

    for(var j = 0; j < strArr.length; j++) {
      if(ads !== null) break;
      ads = document.evaluate('//*[text()="' + strArr[j] + '"]', post, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null).snapshotItem(0);
    }

    if(ads !== null) {
      $(post).css('border', '1px solid red');
        //.remove();

    }
  }

}

// clearInterval(document.dotjstimer);
if(!document.dotjstimer) document.dotjstimer = setInterval(removeFeedAds, 5000);
