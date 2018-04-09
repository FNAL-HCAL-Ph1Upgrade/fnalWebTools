#!/bin/env python

import cgi
import cgitb; cgitb.enable() # for troubleshooting
import mysql.connector

form = cgi.FieldStorage()
body = ""
if not form.getvalue('runX') or not form.getvalue('runY'):
  body += '''
    <h2>Diff CfgScripts between two runs:</h2>
    <form action="/cgi-bin/diffCfgScripts.cgi">
      <input type='number' name='runX'>
      <input type='number' name='runY'>
      <input type='submit'>
    </form>
  '''

else:
  runNumberX = int(form.getvalue('runX'))
  runNumberY = int(form.getvalue('runY'))
  if runNumberX < runNumberY :
    (earlierRun, laterRun) = (runNumberX, runNumberY) 
  else:
    (earlierRun, laterRun) = (runNumberY, runNumberX) 
  
  config = {
    'user': 'runinfoviewer',
    'password': '',
    'host': 'localhost',
    'database': 'fermiruninfo',
    'raise_on_warnings': True,
  }
  
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  
  queryEarlierRun = ("SELECT VALUE FROM fermiruninfo.runsession_string WHERE runsession_parameter_id=(select id from fermiruninfo.runsession_parameter where runnumber={} and (name LIKE 'CMS.%:CFGDOC_TXT') LIMIT 1)".format(earlierRun))
  cursor.execute(queryEarlierRun)
  earlierCfgScript = ""
  for value in cursor:
    earlierCfgScript += value[0]
  cursor = cnx.cursor()
  
  queryLaterRun = ("SELECT VALUE FROM fermiruninfo.runsession_string WHERE runsession_parameter_id=(select id from fermiruninfo.runsession_parameter where runnumber={} and (name LIKE 'CMS.%:CFGDOC_TXT') LIMIT 1)".format(laterRun))
  cursor.execute(queryLaterRun)
  laterCfgScript = ""
  for value in cursor:
    laterCfgScript += value[0]
  cnx.close()

  earlierCfgScript = earlierCfgScript.splitlines()
  laterCfgScript = laterCfgScript.splitlines()
  import difflib
  htmlDiffer = difflib.HtmlDiff(wrapcolumn=90)
  body = htmlDiffer.make_table(earlierCfgScript, laterCfgScript, "", "", True)


print "Content-type: text/html"
print
print "<html><head>"
print """
  <style>
    body {
       font-family: Consolas,monaco,monospace; 
    }
    table {
      font-size: 12px;
    }
    .diff td{
       padding-right: 8px;
     }
    .diff_add {
      background-color: #ddffdd;
    }
    .diff_chg {
      background-color: #ffffbb;
    }
    .diff_sub {
      background-color: #ffdddd;
    }
  </style>
"""
print "</head><body>"
print body
print "</body></html>"
