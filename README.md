FNAL web tools
--------------

This repo contains some web-based tools that can be used through [the FNAL teststand's tomcat server](http://cmsnghcal01.fnal.gov:16000/). They could also be reused on a similar teststand.

FNAL also runs a modified version of webHandsaw, which can be found here:
https://github.com/HCALRunControl/logViewer/tree/fnal

TODO: Also contained here are the modified tomcat server configuration files for allowing simple cgi scripts to run in a tomcat server.

The layout for these files when installed in the tomcat server is:
```
daqowner@cmsnghcal01 ~ # ls ~/tomcat/webapps/ROOT/
asf-logo-wide.svg  bg-middle.png    bg-nav.png	  favicon.ico		 fnalHomePage.css   fnalLogo.png      home.html  RELEASE-NOTES.txt  tomcat.gif	tomcat-power.gif  webHandsaw_black.png	webHandsaw.html  WEB-INF
bg-button.png	   bg-nav-item.png  bg-upper.png  FNALfakeCfgCVSbrowser  fnalLogo_gray.png  functionmanagers  index.jsp  tomcat.css	    tomcat.png	tomcat.svg	  webHandsaw.css	webHandsaw.png
daqowner@cmsnghcal01 ~ # ls ~/tomcat/webapps/ROOT/WEB-INF/
cgi  web.xml
daqowner@cmsnghcal01 ~ # ls ~/tomcat/webapps/ROOT/WEB-INF/cgi/
ansi2html.py  ansi2html.pyc  browseSnippets.cgi  diffCfgScripts.cgi  getCfgScript.cgi  logHtml.py  logHtml.pyc	viewLogs.cgi  webHandsaw_conf.ini
```
