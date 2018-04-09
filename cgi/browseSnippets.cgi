#!/bin/env python

import cgi
import cgitb; cgitb.enable() # for troubleshooting
import os

thisPage = "/cgi-bin/browseSnippets.cgi"
fakeCVSbrowser = "/FNALfakeCfgCVSbrowser"
fakeCVSreal = "/home/daqowner/FNALfakeCfgCVS"

form = cgi.FieldStorage()
body = ""
if not form.getvalue('path'):
  body += '''
    <h2>FNAL snippet browser</h2>
    <a href="{0}?path={1}">{2}</a>
  '''.format(thisPage, fakeCVSbrowser, fakeCVSreal)

else:
  body+="<ul>"
  path = str(form.getvalue('path'))
  realName = path.replace(fakeCVSbrowser, fakeCVSreal)
  if not path.split("/")[1] == fakeCVSbrowser[1:]:
    body+="invalid path:%s" % path
    body += "[" + path.split("/")[1] + "]"
    body += "[" + path.split("/")[1] + "]"
  elif not os.path.exists(realName):
    body+="path %s not found!" % path
  else:
    dirlist = os.listdir(realName)
    body+= "<h2>%s</h2>"%realName
    for item in dirlist:
      if os.path.isfile("{0}/{1}/pro".format(realName, item)):
        body+= "<li>file: <a href='{2}/{1}/pro'>{0}/{1}/pro</a></li>".format(realName, item, path)
      elif os.path.isdir(realName):
        body+= "<li>dir: <a href='{2}?path={3}/{1}'>{0}/{1}</a></li>".format(realName, item, thisPage, path)
      else:
        body+=item
  body+="</ul>"
        
print "Content-type: text/html"
print
print "<html><head>"
print '<link rel="stylesheet" type="text/css" href="/fnalHomePage.css">'
print "</head><body>"
print body
print "</body></html>"
