#!/bin/bash

# __________________________________________________________________________________________ ||
# July18 production
# __________________________________________________________________________________________ ||

#./heppy_crab.py -c BkgMC_2016_cfg.py -s T2_US_Florida -d HeppyTree -l July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c PrivSignal_SMS-T1qqqqL1000_2016_cfg.py -s T2_US_Florida -d HeppyTree -l PrivSig_T1qqqqL_1000_July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c PrivSignal_SMS-T1qqqqL_1500_2016_cfg.py -s T2_US_Florida -d HeppyTree -l PrivSig_T1qqqqL_1500_July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c PrivSignal_SMS-T1tbs_1000_2016_cfg.py -s T2_US_Florida -d HeppyTree -l PrivSig_T1tbs_1000_July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c PrivSignal_SMS-T1tbs_1500_2016_cfg.py -s T2_US_Florida -d HeppyTree -l PrivSig_T1tbs_1500_July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c run_Data2016_cfg.py -s T2_US_Florida -d HeppyTree -l Data2016_July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c MinorBkgMC_2016_cfg.py -s T2_US_Florida -d HeppyTree -l July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c QCD_2016_cfg.py -s T2_US_Florida -d HeppyTree -l July18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

# __________________________________________________________________________________________ ||
# Sept18 MC production (2 jets + 1 tight lepton)
# __________________________________________________________________________________________ ||

#./heppy_crab.py -c BkgMCv2_2016_cfg.py -s T2_US_Florida -d HeppyTree -l Sept18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 

#./heppy_crab.py -c Datav2_2016_cfg.py -s T2_US_Florida -d HeppyTree -l Sept18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt

./heppy_crab.py -c QCDv2_2016_cfg.py -s T2_US_Florida -d HeppyTree -l Sept18_v1 -v heppy_80X_RA5_Legacy -u treeProducerSusyRA5/tree.root,skimAnalyzerCount/SkimReport.txt 
