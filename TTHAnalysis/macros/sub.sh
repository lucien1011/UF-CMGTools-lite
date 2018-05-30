#!/bin/bash

bsub -q 1nh  /afs/cern.ch/work/k/klo/SUSY/RA5/Heppy/CMSSW_8_0_25/src/CMGTools/TTHAnalysis/macros/lxbatch_runner.sh /afs/cern.ch/work/k/klo/SUSY/RA5/Heppy/CMSSW_8_0_25/src/CMGTools/TTHAnalysis/macros /afs/cern.ch/work/k/klo/SUSY/RA5/Heppy/CMSSW_8_0_25 python ./prepareEventVariablesFriendTreeRA5.py -N 500000 -T sf -t tree root://cms-xrd-global.cern.ch//store/user/cheidegg/sea/12/2017-02-24-11-30-00_2lss_bkg/ /eos/cms/store/user/klo/SUSY/RA5/HeppyTree/2016/MC/ --vector -m  'leptonJetReCleanerSusyRA5'    -I  'CMGTools.TTHAnalysis.tools.multilepFriendTreeProducersToCleanup'
