var logo = $('#hplogo');

if(logo.is('img')) {
  $('#hplogo')
    .css({
      'width': '200px',
      'height': '200px',
      'margin-top': '31px',
      'padding-top': '0',
    })
    .attr('src', 'http://ponyfac.es/144/full');
}
else {
  $('#hplogo')
    .css({
      'width': '200px',
      'height': '200px',
      'margin-top': '-80px',
      'background-size': '200px 200px',
      'background-image': 'url(http://ponyfac.es/144/full)'
    })
    .find('div').remove();
}

$('#logo-sub').remove();