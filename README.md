FNAL web tools
--------------

This repo contains some web-based tools that can be used through [the FNAL teststand's tomcat server](http://cmsnghcal01.fnal.gov:16000/). They could also be reused on a similar teststand. Please see the [guide](guide/README.md) for an overview of the functionalities and usage.

FNAL also runs a modified version of webHandsaw, which can be found here:
https://github.com/HCALRunControl/logViewer/tree/fnal

Also contained here is (are) the modified tomcat server configuration file(s) for allowing simple cgi scripts to run in a tomcat server.

The layout for these files when installed in the tomcat server is:
```
daqowner@cmsnghcal01 ~ # ls ~/tomcat/webapps/ROOT/
asf-logo-wide.svg  bg-upper.png		  fnalLogo.png	     tomcat.css        webHandsaw_black.png
bg-button.png	   favicon.ico		  functionmanagers   tomcat.gif        webHandsaw.css
bg-middle.png	   FNALfakeCfgCVSbrowser  home.html	     tomcat.png        webHandsaw.html
bg-nav-item.png    fnalHomePage.css	  index.jsp	     tomcat-power.gif  webHandsaw.png
bg-nav.png	   fnalLogo_gray.png	  RELEASE-NOTES.txt  tomcat.svg        WEB-INF

### note: some of these files are default tomcat files, RCMS-related files, and webHandsaw files


daqowner@cmsnghcal01 ~ # ls ~/tomcat/webapps/ROOT/WEB-INF/
cgi  web.xml


daqowner@cmsnghcal01 ~ # ls ~/tomcat/webapps/ROOT/WEB-INF/cgi/
ansi2html.py   browseSnippets.cgi  getCfgScript.cgi  logHtml.pyc   webHandsaw_conf.ini
ansi2html.pyc  diffCfgScripts.cgi  logHtml.py	     viewLogs.cgi


daqowner@cmsnghcal01 ~ # ls ~/tomcat/conf
Catalina	 catalina.properties  logging.properties  server.xml.cmshcal4  tomcat-users.xml  web.xml
catalina.policy  context.xml	      server.xml	  server.xml.default   tomcat-users.xsd
```
