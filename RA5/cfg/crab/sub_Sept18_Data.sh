#!/bin/bash

# __________________________________________________________________________________________ ||
# Sept18 MC production (2 jets + 1 tight lepton)
# __________________________________________________________________________________________ ||

#./heppy_crab.py -c Datav2_2016_cfg.py -s T2_US_Florida -d HeppyTree -l Sept18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt

./heppy_crab.py -c Datav2_Run2016H_cfg.py -s T2_US_Florida -d HeppyTree -l Sept18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt
