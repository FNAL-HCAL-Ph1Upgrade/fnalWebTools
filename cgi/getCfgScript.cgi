#!/bin/env python

import cgi
import cgitb; cgitb.enable() # for troubleshooting
import mysql.connector

form = cgi.FieldStorage()
body = ""
if not form.getvalue('run'):
  body += '''
    <h2>Get CfgScript from run:</h2>
    <form action="/cgi-bin/getCfgScript.cgi">
      <input type='number' name='run'>
      <input type='submit'>
    </form>
  '''

else:
  runNumber = int(form.getvalue('run'))
  
  config = {
    'user': 'runinfoviewer',
    'password': '',
    'host': 'localhost',
    'database': 'fermiruninfo',
    'raise_on_warnings': True,
  }
  
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  
  body += "<pre>"
  query = ("SELECT VALUE FROM fermiruninfo.runsession_string WHERE runsession_parameter_id=(select id from fermiruninfo.runsession_parameter where runnumber={} and (name LIKE 'CMS.%:CFGDOC_TXT') LIMIT 1)".format(runNumber))
  cursor.execute(query)
  for value in cursor:
    body += value[0]
  cnx.close()
  body += "</pre>"


print "Content-type: text/html"
print
print "<html><body>"
print body
print "</body></html>"
