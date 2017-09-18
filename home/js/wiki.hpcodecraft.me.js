$(function() {
  if(location.pathname === '/spiele-keys') {

    var bullet = ':Pentagram:';
    var button = $('<button id="steam-export">Export for Steam</button>');

    button
      .css({
        margin: '20px'
      })
      .on('click', function() {
        var list = createList(bullet);
        var textarea = $('<textarea id="steam-export-textarea">'+list+'</textarea>');
        textarea.css({
          width: '100%',
          height: '500px',
          fontFamily: '"Lucida Console", Monaco, monospace',
          fontSize: '10px'
        });

        $('.codowiki_west_header').after(textarea);
        textarea.focus().select();
      });

    $('#dokuwiki__sitetools').after(button);
  }
});

function createList(bullet) {
  var list = [];
  var table = $('table.inline').first();
  table.find('tr').each(function(i, row) {
    if(i === 0) return;

    var cells = $(row).find('td');
    var name = cells.first().html();
    if(name === undefined) return;
    var key = cells.next().html();

    if($(key).is('a')) name += ' (Humble Bundle gift link)';
    list.push(bullet + ' ' + name);
  });

  return list.join('\n');
}
