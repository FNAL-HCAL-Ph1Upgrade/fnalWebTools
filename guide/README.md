Guide to using FNAL web tools
=============================

This is a guide to using the custom FNAL web tools.

Homepage
--------

This page serves as the launch pad for using the FNAL web tools.

![homepage](homepage.png#right =400x)

After setting up your ssh tunnel (see instructions [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/FNALHCalMicroTCATestStand#Login_Instructions)), visit http://cmsnghcal01.fnal.gov:16000/. You should see the main page with links to the other tools and assorted other links. 



browseSnippets
--------------

This tool allows one to browse the FNALfakeCfgCVS snippets via the web.

### Navigation pages
![snippetDir](browseSnippets_dir.png#right =400x)

Links with names of snippets/directories in the (fake) CfgCVS will be displayed, along with a label indicating if the link corresponds to a snippet or a directory.


### Snippet display
![snippetDispl](browseSnippets_grandmaster.png#right =400x)

After navigating through directories, when you click on a link to a file, the content of that snippet will be displayed.



getCfgScript
------------

This tool queries the FNAL RunInfo database to get the full CFG script as compiled by the hcalSupervisor in a given run. (This is a rewritten version of the perl script `getCfgScript.cgi` that runs on the P5 machine `hcalmon`.)


### Splash page

![cfgSplash](getCfgScript_splash.png#right =400x)

Enter the run number of the run whose CFG script you would like to retrieve


### CFG script display

![cfgDispl](getCfgScript_cfg.png#right =400x)

Click "Submit query" and you will see a display of the CFG script used for that run.



diffCfgScripts
-------------

This tool also queries the FNAL RunInfo database, but retrieves the CFG scripts for two runs and runs a diff on them.


### Splash page
![diffSplash](diffCfgScripts_splash.png#right =400x)

To see the differences between the CFG scripts used for two runs, enter their two run numbers. 

### Diff display
![diffDispl](diffCfgScripts_diff.png#right =400x)

Click "Submit query" and you will see a diff of the two runs' CFG scripts.
