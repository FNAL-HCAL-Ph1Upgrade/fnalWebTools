Guide to using FNAL web tools
=============================

This is a guide to using the custom FNAL web tools.

Homepage
--------

<img align="right" width="400" src="homepage.png" />

After setting up your ssh tunnel (see instructions [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/FNALHCalMicroTCATestStand#Login_Instructions)), visit http://cmsnghcal01.fnal.gov:16000/. You should see the main page with links to the other tools and assorted other links. 

browseSnippets
--------------

### Navigation pages
<img align="right" width="400" src="browseSnippets_dir.png" />

### Snippet display
<img align="right" width="400" src="browseSnippets_grandmaster.png" />

getCfgScript
------------

This tool queries the FNAL RunInfo database to get the full CFG script as compiled by the hcalSupervisor in a given run. (This is a rewritten version of the perl script `getCfgScript.cgi` that runs on the P5 machine `hcalmon`.)

### Splash page
<img align="right" width="400" src="getCfgScript_splash.png" />
Enter the run number of the run whose CFG script you would like to retrieve

### CFG script display
<img align="right" width="400" src="getCfgScript_cfg.png" />


diffCfgScripts
-------------

### Splash page
<img align="right" width="400" src="diffCfgScripts_splash.png" />

### Diff display
<img align="right" width="400" src="diffCfgScripts_diff.png" />
