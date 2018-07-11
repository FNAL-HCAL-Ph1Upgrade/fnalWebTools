#!/bin/env python

import mysql.connector

def getRunMaps(earliest):
  config = {
    'user': 'runinfoviewer',
    'password': '',
    'host': 'localhost',
    'database': 'fermiruninfo',
    'raise_on_warnings': True,
  }
  
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  
  query = '''
             SELECT runnumber, string_value, time
             FROM fermiruninfo.runsession_parameter 
             WHERE name LIKE "CMS.HCAL_LEVEL1%:LOCAL_RUNKEY_SELECTED" AND runnumber >= {};
          '''.format(earliest)
  cursor.execute(query)
  runMap = {}
  latestMap = []
  for value in cursor:
    if not str(value[1]) in runMap.keys():
      runMap[str(value[1])] = []
    else:
      latestMap.remove(str(value[1]))
    latestMap.insert(0, str(value[1]))
    runMap[str(value[1])].append((value[0], value[2]))
  cnx.close()
  return runMap, latestMap

if __name__ == "__main__":
  import cgi
  import cgitb; cgitb.enable() # for troubleshooting
  form = cgi.FieldStorage()
  body = ""
  if not form.getvalue('first'):
    body += '''
      <h2>Get all runs organized by local runkey since run:</h2>
      <form action="/cgi-bin/getRunTypes.cgi">
        <input type='number' name='first'>
        <input type='submit'>
      </form>
    '''
  
  else:
    body += "<pre>"
    runMap, latestMap = getRunMaps(form.getvalue('first'))
    
    body += "\t \t \t \t \t \t<input type='button' onclick='goToDiff();' value='diff'>"
    for runKey in latestMap:
      body += "<br><br>" + runKey + ":"
      body += " <input type='button' value='toggle'" 
      body += " onclick='hide(" + '"' + runKey + '"' + ")'>"
      body += "<div id='" + runKey +"'>"
      for run in reversed(runMap[runKey]):
        body += '<br>\t <input type="checkbox" value="{0}" onclick="tally();"> {0: >6} \t\t{1}'.format(run[0], run[1])
      body += "</div>"
      body += "<br><br>\t \t \t \t \t \t<input type='button' onclick='goToDiff();' value='diff'>"
    body+="</pre>"
  
  print "Content-type: text/html"
  print
  print "<html><head>"
  print """
  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  <script>
  function goToDiff() {
    var runNumbers = $(':checkbox:checked');
    if (runNumbers.length == 2) {
      window.location.href='/cgi-bin/diffCfgScripts.cgi?runX=' + $(runNumbers[0]).val() + '&runY=' + $(runNumbers[1]).val(); 
    }
    else if (runNumbers.length != 2) { tally(); }
  }
  </script>
  <script>
  function tally() {
    if ($(':checkbox:checked').length > 2) {
      $(":checkbox").prop('checked', false);
    }
  }
  </script> 
  <script>
  function hide(divID) {
    var x = document.getElementById(divID);
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }  
  }
  </script>
 
      """
  print" </head><body>"
  print body
  print "</body></html>"
