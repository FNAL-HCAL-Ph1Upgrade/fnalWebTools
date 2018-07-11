#!/bin/env python

# cgi script for making a list of runs organized chronologically and grouped by their local runkey name
# this version is for FNAL. there is another version for P5.
# John Hakala 7/11/18

import mysql.connector

def getRunMaps(earliest):
  # this is the login info for connecting to the FNAL runinfo DB
  config = {
    'user': 'runinfoviewer',
    'password': '',
    'host': 'localhost',
    'database': 'fermiruninfo',
    'raise_on_warnings': True,
  }
  
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  
  # this is the appropriate SQL query for getting what we want from the runInfo DB
  query = '''
             SELECT runnumber, string_value, time
             FROM fermiruninfo.runsession_parameter 
             WHERE name LIKE "CMS.HCAL_LEVEL1%:LOCAL_RUNKEY_SELECTED" AND runnumber >= {};
          '''.format(earliest)
  cursor.execute(query)


  runMap = {}
  # runMap will have the structure:
  # {"name_of_runkey": [(run#, time), (run#, time), ...], "name_of_other_runkey": [(#, time), ...], ... }

  latestMap = []
  # latestMap will be ordered by age: ["runkey_name_of_latest_run", "second_most_recently_used_runkey", ...]

  for value in cursor:
    # value has the structure [runnumber, runkey_name, time] as per SQL query
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
    # return the splash page if no cgi arguments are passed
    body += '''
      <h2>Get all runs organized by local runkey since run:</h2>
      <form action="/cgi-bin/getRunTypes.cgi">
        <input type='number' name='first'>
        <input type='submit'>
      </form>
    '''
  
  else:
    # if it got a starting run number as a cgi argument, build the page
    runMap, latestMap = getRunMaps(form.getvalue('first'))
    
    diffButton = "<pre>\t \t \t \t \t \t<input type='button' onclick='goToDiff();' value='diff'></pre>\n"

    for runKey in latestMap:
      body += "\n    <tt>" + runKey + ": </tt>"
      
      # make a div for all the runs of a given run key, and add a JS toggle button for each div
      body += " <input type='button' value='toggle'" 
      body += " onclick='hide(" + '"' + runKey + '"' + ")'>"
      body += "\n    <div id='" + runKey +"'>"
      # put a diff button at the top of every group of runs
      body += diffButton

      for run in reversed(runMap[runKey]):
        # go through all the runs in a run key, put newest runs at the top.
        body += '      <pre>\t <input type="checkbox" value="{0}" onclick="tally();"> {0: >6} \t\t{1} </pre>\n'.format(run[0], run[1])
      body += "    </div><br>\n"
      
      # add a diff link button at the bottom too
    body += "    " + diffButton
  
  # now serve the page
  print "Content-type: text/html"
  print
  print """
<html>
  <head>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="/runTypeScripts.js"> </script>
    <style>
      pre {
        margin: 0;
      }
    </style>
  </head>
      """
  print"  <body>"
  print body
  print "  </body>"
  print "</html>"
