#!/bin/bash

#./prepareEventVariablesFriendTreeRA5.py /cms/data//store/user/klo/RA5/NTuples/2016/HeppyTree/ /raid/raid7/lucien/SUSY/RA5/Test/ -d TBar_tch_powheg -m leptonJetReCleanerSusyRA5 -I CMGTools.TTHAnalysis.tools.multilepFriendTreeProducersToCleanup -j 0
./prepareEventVariablesFriendTreeRA5.py root://t3se01.psi.ch:1094//store/user/cheidegg/sea/12/2017-02-24-11-30-00_2lss_bkg/ /eos/cms/store/user/klo/SUSY/RA5/HeppyTree/2016/MC/ -m leptonJetReCleanerSusyRA5 -I CMGTools.TTHAnalysis.tools.multilepFriendTreeProducersToCleanup -j 1 --queue 8nh
