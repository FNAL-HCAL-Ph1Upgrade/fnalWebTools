Guide to using FNAL web tools
=============================

This is a guide to using the custom FNAL web tools.

Homepage
--------
<img src='homepage.png' width=400px align="right"/>

This page serves as the launch pad for using the FNAL web tools.

After setting up your ssh tunnel (see instructions [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/FNALHCalMicroTCATestStand#Login_Instructions)), visit http://cmsnghcal01.fnal.gov:16000/. You should see the main page with links to the other tools and assorted other links. 
<br><br><br><br><br>


browseSnippets
--------------

<img src='browseSnippets_dir.png' width=400px align="right"/>

This tool allows one to browse the FNALfakeCfgCVS snippets via the web.

### Navigation pages

Links with names of snippets/directories in the (fake) CfgCVS will be displayed, along with a label indicating if the link corresponds to a snippet or a directory.

<br>

### Snippet display

<img src='browseSnippets_grandmaster.png' width=400px align="right"/>

<br><br>

After navigating through directories, when you click on a link to a file, the content of that snippet will be displayed.
<br><br><br><br>


getCfgScript
------------

<img src='getCfgScript_splash.png' width=400px align="right"/>

This tool queries the FNAL RunInfo database to get the full CFG script as compiled by the hcalSupervisor in a given run. (This is a rewritten version of the perl script `getCfgScript.cgi` that runs on the P5 machine `hcalmon`.)

### Splash page

Enter the run number of the run whose CFG script you would like to retrieve
<br><br><br><br>


### CFG script display

<img src='getCfgScript_cfg.png' width=400px align="right"/>

<br><br>

Click "Submit query" and you will see a display of the CFG script used for that run.
<br><br><br><br><br><br><br>


diffCfgScripts
-------------
<img src='diffCfgScripts_splash.png' width=400px align="right"/>

This tool also queries the FNAL RunInfo database, but retrieves the CFG scripts for two runs and runs a diff on them.

### Splash page

To see the differences between the CFG scripts used for two runs, enter their two run numbers. 
<br><br><br><br>

### Diff display
<img src='diffCfgScripts_diff.png' width=400px align="right"/>

<br><br>

Click "Submit query" and you will see a diff of the two runs' CFG scripts.
