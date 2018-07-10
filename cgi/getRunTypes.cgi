#!/bin/env python

import cx_Oracle

def getRunMaps(earliest):
  # this is commented since it's for the mysql db at FNAL
  #config = {
  #  'user': 'runinfoviewer',
  #  'password': '',
  #  'host': 'localhost',
  #  'database': 'fermiruninfo',
  #  'raise_on_warnings': True,
  #}
  #
  #cnx = mysql.connector.connect(**config)

  # borrowed from RunInfoDiffer
  password_file = open("RunInfoDiffer/database_pwd.txt","r")
  password = password_file.readline().split("\n")[0]
  password_file.close()
  database = "cms_hcl_runinfo/%s@cms_rcms" % password

  cnx = cx_Oracle.connect(database)
  cursor = cnx.cursor()
  
  #query = '''
  #           SELECT runnumber, string_value
  #           FROM runsession_parameter 
  #           WHERE name LIKE "CMS.HCAL_LEVEL1%:LOCAL_RUNKEY_SELECTED" AND runnumber >= {};
  #        '''.format(earliest)
  query =  'SELECT runnumber, string_value '
  query += 'FROM runsession_parameter '
  query += "WHERE name LIKE 'CMS.HCAL_LEVEL_1%:LOCAL_RUNKEY_SELECTED' AND runnumber >= {}".format(earliest)
  cursor.execute(query)
  runMap = {}
  latestMap = []
  for value in cursor:
    if not str(value[1]) in runMap.keys():
      runMap[str(value[1])] = []
    else:
      latestMap.remove(str(value[1]))
    latestMap.insert(0, str(value[1]))
    runMap[str(value[1])].append(value[0])
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
        <input type='number' name='first' value='318000'>
        <input type='submit'>
      </form>
    '''
  
  else:
    body += "<pre>"
    runMap, latestMap = getRunMaps(form.getvalue('first'))
    
    body += "\t \t \t <input type='button' onclick='goToDiff();' value='diff'>"
    for runKey in latestMap:
      body += "<br><br>" + runKey + ":"
      for run in reversed(runMap[runKey]):
        body += '<br>\t \t <input type="checkbox" value="{0}" onclick="tally();"> {0} '.format(run)
      body += "<input type='button' onclick='goToDiff();' value='diff'>"
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
      window.location.href='/cgi-bin/RunInfoDiffer/complete_Diff.py?runnumber1='+ $(runNumbers[0]).val() + '&runnumber2=' + $(runNumbers[1]).val() + '&partition=HCAL_HO&partition=HCAL_HF&partition=HCAL_HBHE&partition=HCAL_Laser'
    }
    else if (runNumbers.length != 2) { tally(); }
  }</script><script>
  function tally() {
    if ($(':checkbox:checked').length > 2) {
      $(":checkbox").prop('checked', false);
    }
  }
  </script> 
  """
  print" </head><body>"
  print body
  print "</body></html>"
