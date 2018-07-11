function goToDiff() {
  var runNumbers = $(':checkbox:checked');
  if (runNumbers.length == 2) {
    window.location.href='/cgi-bin/diffCfgScripts.cgi?runX=' + $(runNumbers[0]).val() + '&runY=' + $(runNumbers[1]).val(); 
  }
  else if (runNumbers.length != 2) { tally(); }
}

function tally() {
  if ($(':checkbox:checked').length > 2) {
    $(":checkbox").prop('checked', false);
  }
}

function hide(divID) {
  $('#'+divID).toggle();
}
