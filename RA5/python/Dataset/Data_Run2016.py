import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- Zero Tesla run  ----------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
#json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
json                            = os.environ['CMSSW_BASE']+ '/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt' # 36.46 /fb

run_range = (273158, 284044)
label = "_runs%s_%s"%(run_range[0], run_range[1])

### ----------------------------- Run2016B 23Sep2016 ----------------------------------------

JetHT_Run2016B_23Sep2016          = kreator.makeDataComponent("JetHT_Run2016B_23Sep2016"         , "/JetHT/Run2016B-23Sep2016-v3/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_23Sep2016          = kreator.makeDataComponent("HTMHT_Run2016B_23Sep2016"         , "/HTMHT/Run2016B-23Sep2016-v3/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_23Sep2016            = kreator.makeDataComponent("MET_Run2016B_23Sep2016"           , "/MET/Run2016B-23Sep2016-v3/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016B_23Sep2016", "/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016B_23Sep2016"    , "/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_23Sep2016   = kreator.makeDataComponent("SinglePhoton_Run2016B_23Sep2016"  , "/SinglePhoton/Run2016B-23Sep2016-v3/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_23Sep2016       = kreator.makeDataComponent("DoubleEG_Run2016B_23Sep2016"      , "/DoubleEG/Run2016B-23Sep2016-v3/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_23Sep2016        = kreator.makeDataComponent("MuonEG_Run2016B_23Sep2016"        , "/MuonEG/Run2016B-23Sep2016-v3/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_23Sep2016     = kreator.makeDataComponent("DoubleMuon_Run2016B_23Sep2016"    , "/DoubleMuon/Run2016B-23Sep2016-v3/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016B_23Sep2016     = kreator.makeDataComponent("Tau_Run2016B_23Sep2016"    , "/Tau/Run2016B-23Sep2016-v3/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016B_23Sep2016 = [JetHT_Run2016B_23Sep2016, HTMHT_Run2016B_23Sep2016, MET_Run2016B_23Sep2016, SingleElectron_Run2016B_23Sep2016, SingleMuon_Run2016B_23Sep2016, SinglePhoton_Run2016B_23Sep2016, DoubleEG_Run2016B_23Sep2016, MuonEG_Run2016B_23Sep2016, DoubleMuon_Run2016B_23Sep2016, Tau_Run2016B_23Sep2016]

### ----------------------------- Run2016C 23Sep2016 ----------------------------------------

JetHT_Run2016C_23Sep2016          = kreator.makeDataComponent("JetHT_Run2016C_23Sep2016"         , "/JetHT/Run2016C-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016C_23Sep2016          = kreator.makeDataComponent("HTMHT_Run2016C_23Sep2016"         , "/HTMHT/Run2016C-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016C_23Sep2016            = kreator.makeDataComponent("MET_Run2016C_23Sep2016"           , "/MET/Run2016C-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016C_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016C_23Sep2016", "/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016C_23Sep2016"    , "/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016C_23Sep2016   = kreator.makeDataComponent("SinglePhoton_Run2016C_23Sep2016"  , "/SinglePhoton/Run2016C-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016C_23Sep2016       = kreator.makeDataComponent("DoubleEG_Run2016C_23Sep2016"      , "/DoubleEG/Run2016C-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016C_23Sep2016         = kreator.makeDataComponent("MuonEG_Run2016C_23Sep2016"        , "/MuonEG/Run2016C-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016C_23Sep2016     = kreator.makeDataComponent("DoubleMuon_Run2016C_23Sep2016"    , "/DoubleMuon/Run2016C-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016C_23Sep2016            = kreator.makeDataComponent("Tau_Run2016C_23Sep2016"           , "/Tau/Run2016C-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016C_23Sep2016 = [JetHT_Run2016C_23Sep2016, HTMHT_Run2016C_23Sep2016, MET_Run2016C_23Sep2016, SingleElectron_Run2016C_23Sep2016, SingleMuon_Run2016C_23Sep2016, SinglePhoton_Run2016C_23Sep2016, DoubleEG_Run2016C_23Sep2016, MuonEG_Run2016C_23Sep2016, DoubleMuon_Run2016C_23Sep2016, Tau_Run2016C_23Sep2016]


### ----------------------------- Run2016D 23Sep2016 v2 ----------------------------------------

JetHT_Run2016D_23Sep2016          = kreator.makeDataComponent("JetHT_Run2016D_23Sep2016"         , "/JetHT/Run2016D-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016D_23Sep2016          = kreator.makeDataComponent("HTMHT_Run2016D_23Sep2016"         , "/HTMHT/Run2016D-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016D_23Sep2016            = kreator.makeDataComponent("MET_Run2016D_23Sep2016"           , "/MET/Run2016D-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016D_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016D_23Sep2016", "/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016D_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016D_23Sep2016"    , "/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016D_23Sep2016   = kreator.makeDataComponent("SinglePhoton_Run2016D_23Sep2016"  , "/SinglePhoton/Run2016D-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016D_23Sep2016       = kreator.makeDataComponent("DoubleEG_Run2016D_23Sep2016"      , "/DoubleEG/Run2016D-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016D_23Sep2016         = kreator.makeDataComponent("MuonEG_Run2016D_23Sep2016"        , "/MuonEG/Run2016D-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016D_23Sep2016     = kreator.makeDataComponent("DoubleMuon_Run2016D_23Sep2016"    , "/DoubleMuon/Run2016D-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016D_23Sep2016            = kreator.makeDataComponent("Tau_Run2016D_23Sep2016"           , "/Tau/Run2016D-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016D_23Sep2016 = [JetHT_Run2016D_23Sep2016, HTMHT_Run2016D_23Sep2016, MET_Run2016D_23Sep2016, SingleElectron_Run2016D_23Sep2016, SingleMuon_Run2016D_23Sep2016, SinglePhoton_Run2016D_23Sep2016, DoubleEG_Run2016D_23Sep2016, MuonEG_Run2016D_23Sep2016, DoubleMuon_Run2016D_23Sep2016, Tau_Run2016D_23Sep2016]

### ----------------------------- Run2016E 23Sep2016 v2 ----------------------------------------

JetHT_Run2016E_23Sep2016          = kreator.makeDataComponent("JetHT_Run2016E_23Sep2016"         , "/JetHT/Run2016E-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016E_23Sep2016          = kreator.makeDataComponent("HTMHT_Run2016E_23Sep2016"         , "/HTMHT/Run2016E-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016E_23Sep2016            = kreator.makeDataComponent("MET_Run2016E_23Sep2016"           , "/MET/Run2016E-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016E_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016E_23Sep2016", "/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016E_23Sep2016"    , "/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016E_23Sep2016   = kreator.makeDataComponent("SinglePhoton_Run2016E_23Sep2016"  , "/SinglePhoton/Run2016E-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016E_23Sep2016       = kreator.makeDataComponent("DoubleEG_Run2016E_23Sep2016"      , "/DoubleEG/Run2016E-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016E_23Sep2016         = kreator.makeDataComponent("MuonEG_Run2016E_23Sep2016"        , "/MuonEG/Run2016E-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016E_23Sep2016     = kreator.makeDataComponent("DoubleMuon_Run2016E_23Sep2016"    , "/DoubleMuon/Run2016E-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016E_23Sep2016            = kreator.makeDataComponent("Tau_Run2016E_23Sep2016"           , "/Tau/Run2016E-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016E_23Sep2016 = [JetHT_Run2016E_23Sep2016, HTMHT_Run2016E_23Sep2016, MET_Run2016E_23Sep2016, SingleElectron_Run2016E_23Sep2016, SingleMuon_Run2016E_23Sep2016, SinglePhoton_Run2016E_23Sep2016, DoubleEG_Run2016E_23Sep2016, MuonEG_Run2016E_23Sep2016, DoubleMuon_Run2016E_23Sep2016, Tau_Run2016E_23Sep2016]


### ----------------------------- Run2016F 23Sep2016 v1 ----------------------------------------

JetHT_Run2016F_23Sep2016          = kreator.makeDataComponent("JetHT_Run2016F_23Sep2016"         , "/JetHT/Run2016F-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016F_23Sep2016          = kreator.makeDataComponent("HTMHT_Run2016F_23Sep2016"         , "/HTMHT/Run2016F-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016F_23Sep2016            = kreator.makeDataComponent("MET_Run2016F_23Sep2016"           , "/MET/Run2016F-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016F_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016F_23Sep2016", "/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016F_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016F_23Sep2016"    , "/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016F_23Sep2016   = kreator.makeDataComponent("SinglePhoton_Run2016F_23Sep2016"  , "/SinglePhoton/Run2016F-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016F_23Sep2016       = kreator.makeDataComponent("DoubleEG_Run2016F_23Sep2016"      , "/DoubleEG/Run2016F-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016F_23Sep2016         = kreator.makeDataComponent("MuonEG_Run2016F_23Sep2016"        , "/MuonEG/Run2016F-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016F_23Sep2016     = kreator.makeDataComponent("DoubleMuon_Run2016F_23Sep2016"    , "/DoubleMuon/Run2016F-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016F_23Sep2016            = kreator.makeDataComponent("Tau_Run2016F_23Sep2016"           , "/Tau/Run2016F-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016F_23Sep2016 = [JetHT_Run2016F_23Sep2016, HTMHT_Run2016F_23Sep2016, MET_Run2016F_23Sep2016, SingleElectron_Run2016F_23Sep2016, SingleMuon_Run2016F_23Sep2016, SinglePhoton_Run2016F_23Sep2016, DoubleEG_Run2016F_23Sep2016, MuonEG_Run2016F_23Sep2016, DoubleMuon_Run2016F_23Sep2016, Tau_Run2016F_23Sep2016]

### ----------------------------- Run2016G 23Sep2016 v1 ----------------------------------------

JetHT_Run2016G_23Sep2016          = kreator.makeDataComponent("JetHT_Run2016G_23Sep2016"         , "/JetHT/Run2016G-23Sep2016-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016G_23Sep2016          = kreator.makeDataComponent("HTMHT_Run2016G_23Sep2016"         , "/HTMHT/Run2016G-23Sep2016-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016G_23Sep2016            = kreator.makeDataComponent("MET_Run2016G_23Sep2016"           , "/MET/Run2016G-23Sep2016-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016G_23Sep2016 = kreator.makeDataComponent("SingleElectron_Run2016G_23Sep2016", "/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016G_23Sep2016     = kreator.makeDataComponent("SingleMuon_Run2016G_23Sep2016"    , "/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016G_23Sep2016   = kreator.makeDataComponent("SinglePhoton_Run2016G_23Sep2016"  , "/SinglePhoton/Run2016G-23Sep2016-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016G_23Sep2016       = kreator.makeDataComponent("DoubleEG_Run2016G_23Sep2016"      , "/DoubleEG/Run2016G-23Sep2016-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016G_23Sep2016        = kreator.makeDataComponent("MuonEG_Run2016G_23Sep2016"        , "/MuonEG/Run2016G-23Sep2016-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016G_23Sep2016     = kreator.makeDataComponent("DoubleMuon_Run2016G_23Sep2016"    , "/DoubleMuon/Run2016G-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016G_23Sep2016     = kreator.makeDataComponent("Tau_Run2016G_23Sep2016"    , "/Tau/Run2016G-23Sep2016-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016G_23Sep2016 = [JetHT_Run2016G_23Sep2016, HTMHT_Run2016G_23Sep2016, MET_Run2016G_23Sep2016, SingleElectron_Run2016G_23Sep2016, SingleMuon_Run2016G_23Sep2016, SinglePhoton_Run2016G_23Sep2016, DoubleEG_Run2016G_23Sep2016, MuonEG_Run2016G_23Sep2016, DoubleMuon_Run2016G_23Sep2016, Tau_Run2016G_23Sep2016]

### Summary of prompt reco
dataSamples_23Sep2016 = dataSamples_Run2016B_23Sep2016 + dataSamples_Run2016C_23Sep2016 + dataSamples_Run2016D_23Sep2016 + dataSamples_Run2016E_23Sep2016 + dataSamples_Run2016F_23Sep2016 + dataSamples_Run2016G_23Sep2016

### Dataset corresponding to the full Run2016 with re-reco + prompt
#dataSamples_23Sep2016PlusPrompt = dataSamples_23Sep2016 + dataSamples_Run2016H_v2 + dataSamples_Run2016H_v3

### ----------------------------- Run2016B v2 03Feb2017 ----------------------------------------

JetHT_Run2016B_03Feb2017_v2       = kreator.makeDataComponent("JetHT_Run2016B_03Feb2017_v2"      , "/JetHT/Run2016B-03Feb2017_ver2-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_03Feb2017_v2       = kreator.makeDataComponent("HTMHT_Run2016B_03Feb2017_v2"      , "/HTMHT/Run2016B-03Feb2017_ver2-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_03Feb2017_v2         = kreator.makeDataComponent("MET_Run2016B_03Feb2017_v2"        , "/MET/Run2016B-03Feb2017_ver2-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_03Feb2017_v2 = kreator.makeDataComponent("SingleElectron_Run2016B_03Feb2017_v2", "/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_03Feb2017_v2  = kreator.makeDataComponent("SingleMuon_Run2016B_03Feb2017_v2" , "/SingleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_03Feb2017_v2= kreator.makeDataComponent("SinglePhoton_Run2016B_03Feb2017_v2"  , "/SinglePhoton/Run2016B-03Feb2017_ver2-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_03Feb2017_v2    = kreator.makeDataComponent("DoubleEG_Run2016B_03Feb2017_v2"   , "/DoubleEG/Run2016B-03Feb2017_ver2-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_03Feb2017_v2     = kreator.makeDataComponent("MuonEG_Run2016B_03Feb2017_v2"     , "/MuonEG/Run2016B-03Feb2017_ver2-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_03Feb2017_v2  = kreator.makeDataComponent("DoubleMuon_Run2016B_03Feb2017_v2" , "/DoubleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016B_03Feb2017_v2  = kreator.makeDataComponent("Tau_Run2016B_03Feb2017_v2" , "/Tau/Run2016B-03Feb2017_ver2-v2/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016B_03Feb2017_v2 = [JetHT_Run2016B_03Feb2017_v2, HTMHT_Run2016B_03Feb2017_v2, MET_Run2016B_03Feb2017_v2, SingleElectron_Run2016B_03Feb2017_v2, SingleMuon_Run2016B_03Feb2017_v2, SinglePhoton_Run2016B_03Feb2017_v2, DoubleEG_Run2016B_03Feb2017_v2, MuonEG_Run2016B_03Feb2017_v2, DoubleMuon_Run2016B_03Feb2017_v2, Tau_Run2016B_03Feb2017_v2]

### ----------------------------- Run2016C 03Feb2017 ----------------------------------------

JetHT_Run2016C_03Feb2017          = kreator.makeDataComponent("JetHT_Run2016C_03Feb2017"         , "/JetHT/Run2016C-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016C_03Feb2017          = kreator.makeDataComponent("HTMHT_Run2016C_03Feb2017"         , "/HTMHT/Run2016C-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016C_03Feb2017            = kreator.makeDataComponent("MET_Run2016C_03Feb2017"           , "/MET/Run2016C-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016C_03Feb2017 = kreator.makeDataComponent("SingleElectron_Run2016C_03Feb2017", "/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_03Feb2017     = kreator.makeDataComponent("SingleMuon_Run2016C_03Feb2017"    , "/SingleMuon/Run2016C-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016C_03Feb2017   = kreator.makeDataComponent("SinglePhoton_Run2016C_03Feb2017"  , "/SinglePhoton/Run2016C-03Feb2017-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016C_03Feb2017       = kreator.makeDataComponent("DoubleEG_Run2016C_03Feb2017"      , "/DoubleEG/Run2016C-03Feb2017-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016C_03Feb2017         = kreator.makeDataComponent("MuonEG_Run2016C_03Feb2017"        , "/MuonEG/Run2016C-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016C_03Feb2017     = kreator.makeDataComponent("DoubleMuon_Run2016C_03Feb2017"    , "/DoubleMuon/Run2016C-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016C_03Feb2017            = kreator.makeDataComponent("Tau_Run2016C_03Feb2017"           , "/Tau/Run2016C-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016C_03Feb2017 = [JetHT_Run2016C_03Feb2017, HTMHT_Run2016C_03Feb2017, MET_Run2016C_03Feb2017, SingleElectron_Run2016C_03Feb2017, SingleMuon_Run2016C_03Feb2017, SinglePhoton_Run2016C_03Feb2017, DoubleEG_Run2016C_03Feb2017, MuonEG_Run2016C_03Feb2017, DoubleMuon_Run2016C_03Feb2017, Tau_Run2016C_03Feb2017]


### ----------------------------- Run2016D 03Feb2017 v2 ----------------------------------------

JetHT_Run2016D_03Feb2017          = kreator.makeDataComponent("JetHT_Run2016D_03Feb2017"         , "/JetHT/Run2016D-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016D_03Feb2017          = kreator.makeDataComponent("HTMHT_Run2016D_03Feb2017"         , "/HTMHT/Run2016D-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016D_03Feb2017            = kreator.makeDataComponent("MET_Run2016D_03Feb2017"           , "/MET/Run2016D-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016D_03Feb2017 = kreator.makeDataComponent("SingleElectron_Run2016D_03Feb2017", "/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016D_03Feb2017     = kreator.makeDataComponent("SingleMuon_Run2016D_03Feb2017"    , "/SingleMuon/Run2016D-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016D_03Feb2017   = kreator.makeDataComponent("SinglePhoton_Run2016D_03Feb2017"  , "/SinglePhoton/Run2016D-03Feb2017-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016D_03Feb2017       = kreator.makeDataComponent("DoubleEG_Run2016D_03Feb2017"      , "/DoubleEG/Run2016D-03Feb2017-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016D_03Feb2017         = kreator.makeDataComponent("MuonEG_Run2016D_03Feb2017"        , "/MuonEG/Run2016D-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016D_03Feb2017     = kreator.makeDataComponent("DoubleMuon_Run2016D_03Feb2017"    , "/DoubleMuon/Run2016D-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016D_03Feb2017            = kreator.makeDataComponent("Tau_Run2016D_03Feb2017"           , "/Tau/Run2016D-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016D_03Feb2017 = [JetHT_Run2016D_03Feb2017, HTMHT_Run2016D_03Feb2017, MET_Run2016D_03Feb2017, SingleElectron_Run2016D_03Feb2017, SingleMuon_Run2016D_03Feb2017, SinglePhoton_Run2016D_03Feb2017, DoubleEG_Run2016D_03Feb2017, MuonEG_Run2016D_03Feb2017, DoubleMuon_Run2016D_03Feb2017, Tau_Run2016D_03Feb2017]

### ----------------------------- Run2016E 03Feb2017 v2 ----------------------------------------

JetHT_Run2016E_03Feb2017          = kreator.makeDataComponent("JetHT_Run2016E_03Feb2017"         , "/JetHT/Run2016E-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016E_03Feb2017          = kreator.makeDataComponent("HTMHT_Run2016E_03Feb2017"         , "/HTMHT/Run2016E-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016E_03Feb2017            = kreator.makeDataComponent("MET_Run2016E_03Feb2017"           , "/MET/Run2016E-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016E_03Feb2017 = kreator.makeDataComponent("SingleElectron_Run2016E_03Feb2017", "/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_03Feb2017     = kreator.makeDataComponent("SingleMuon_Run2016E_03Feb2017"    , "/SingleMuon/Run2016E-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016E_03Feb2017   = kreator.makeDataComponent("SinglePhoton_Run2016E_03Feb2017"  , "/SinglePhoton/Run2016E-03Feb2017-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016E_03Feb2017       = kreator.makeDataComponent("DoubleEG_Run2016E_03Feb2017"      , "/DoubleEG/Run2016E-03Feb2017-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016E_03Feb2017         = kreator.makeDataComponent("MuonEG_Run2016E_03Feb2017"        , "/MuonEG/Run2016E-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016E_03Feb2017     = kreator.makeDataComponent("DoubleMuon_Run2016E_03Feb2017"    , "/DoubleMuon/Run2016E-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016E_03Feb2017            = kreator.makeDataComponent("Tau_Run2016E_03Feb2017"           , "/Tau/Run2016E-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016E_03Feb2017 = [JetHT_Run2016E_03Feb2017, HTMHT_Run2016E_03Feb2017, MET_Run2016E_03Feb2017, SingleElectron_Run2016E_03Feb2017, SingleMuon_Run2016E_03Feb2017, SinglePhoton_Run2016E_03Feb2017, DoubleEG_Run2016E_03Feb2017, MuonEG_Run2016E_03Feb2017, DoubleMuon_Run2016E_03Feb2017, Tau_Run2016E_03Feb2017]


### ----------------------------- Run2016F 03Feb2017 v1 ----------------------------------------

JetHT_Run2016F_03Feb2017          = kreator.makeDataComponent("JetHT_Run2016F_03Feb2017"         , "/JetHT/Run2016F-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016F_03Feb2017          = kreator.makeDataComponent("HTMHT_Run2016F_03Feb2017"         , "/HTMHT/Run2016F-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016F_03Feb2017            = kreator.makeDataComponent("MET_Run2016F_03Feb2017"           , "/MET/Run2016F-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016F_03Feb2017 = kreator.makeDataComponent("SingleElectron_Run2016F_03Feb2017", "/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016F_03Feb2017     = kreator.makeDataComponent("SingleMuon_Run2016F_03Feb2017"    , "/SingleMuon/Run2016F-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016F_03Feb2017   = kreator.makeDataComponent("SinglePhoton_Run2016F_03Feb2017"  , "/SinglePhoton/Run2016F-03Feb2017-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016F_03Feb2017       = kreator.makeDataComponent("DoubleEG_Run2016F_03Feb2017"      , "/DoubleEG/Run2016F-03Feb2017-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016F_03Feb2017         = kreator.makeDataComponent("MuonEG_Run2016F_03Feb2017"        , "/MuonEG/Run2016F-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016F_03Feb2017     = kreator.makeDataComponent("DoubleMuon_Run2016F_03Feb2017"    , "/DoubleMuon/Run2016F-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016F_03Feb2017            = kreator.makeDataComponent("Tau_Run2016F_03Feb2017"           , "/Tau/Run2016F-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016F_03Feb2017 = [JetHT_Run2016F_03Feb2017, HTMHT_Run2016F_03Feb2017, MET_Run2016F_03Feb2017, SingleElectron_Run2016F_03Feb2017, SingleMuon_Run2016F_03Feb2017, SinglePhoton_Run2016F_03Feb2017, DoubleEG_Run2016F_03Feb2017, MuonEG_Run2016F_03Feb2017, DoubleMuon_Run2016F_03Feb2017, Tau_Run2016F_03Feb2017]

### ----------------------------- Run2016G 03Feb2017 v1 ----------------------------------------

JetHT_Run2016G_03Feb2017          = kreator.makeDataComponent("JetHT_Run2016G_03Feb2017"         , "/JetHT/Run2016G-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016G_03Feb2017          = kreator.makeDataComponent("HTMHT_Run2016G_03Feb2017"         , "/HTMHT/Run2016G-03Feb2017-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016G_03Feb2017            = kreator.makeDataComponent("MET_Run2016G_03Feb2017"           , "/MET/Run2016G-03Feb2017-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016G_03Feb2017 = kreator.makeDataComponent("SingleElectron_Run2016G_03Feb2017", "/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016G_03Feb2017     = kreator.makeDataComponent("SingleMuon_Run2016G_03Feb2017"    , "/SingleMuon/Run2016G-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016G_03Feb2017   = kreator.makeDataComponent("SinglePhoton_Run2016G_03Feb2017"  , "/SinglePhoton/Run2016G-03Feb2017-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016G_03Feb2017       = kreator.makeDataComponent("DoubleEG_Run2016G_03Feb2017"      , "/DoubleEG/Run2016G-03Feb2017-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016G_03Feb2017        = kreator.makeDataComponent("MuonEG_Run2016G_03Feb2017"        , "/MuonEG/Run2016G-03Feb2017-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016G_03Feb2017     = kreator.makeDataComponent("DoubleMuon_Run2016G_03Feb2017"    , "/DoubleMuon/Run2016G-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016G_03Feb2017     = kreator.makeDataComponent("Tau_Run2016G_03Feb2017"    , "/Tau/Run2016G-03Feb2017-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016G_03Feb2017 = [JetHT_Run2016G_03Feb2017, HTMHT_Run2016G_03Feb2017, MET_Run2016G_03Feb2017, SingleElectron_Run2016G_03Feb2017, SingleMuon_Run2016G_03Feb2017, SinglePhoton_Run2016G_03Feb2017, DoubleEG_Run2016G_03Feb2017, MuonEG_Run2016G_03Feb2017, DoubleMuon_Run2016G_03Feb2017, Tau_Run2016G_03Feb2017]

### ----------------------------- Run2016H 03Feb2017_ver2-v1 ----------------------------------------

JetHT_Run2016H_03Feb2017_v2          = kreator.makeDataComponent("JetHT_Run2016H_03Feb2017_v2"         , "/JetHT/Run2016H-03Feb2017_ver2-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016H_03Feb2017_v2          = kreator.makeDataComponent("HTMHT_Run2016H_03Feb2017_v2"         , "/HTMHT/Run2016H-03Feb2017_ver2-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016H_03Feb2017_v2            = kreator.makeDataComponent("MET_Run2016H_03Feb2017_v2"           , "/MET/Run2016H-03Feb2017_ver2-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016H_03Feb2017_v2 = kreator.makeDataComponent("SingleElectron_Run2016H_03Feb2017_v2", "/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016H_03Feb2017_v2     = kreator.makeDataComponent("SingleMuon_Run2016H_03Feb2017_v2"    , "/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016H_03Feb2017_v2   = kreator.makeDataComponent("SinglePhoton_Run2016H_03Feb2017_v2"  , "/SinglePhoton/Run2016H-03Feb2017_ver2-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016H_03Feb2017_v2       = kreator.makeDataComponent("DoubleEG_Run2016H_03Feb2017_v2"      , "/DoubleEG/Run2016H-03Feb2017_ver2-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016H_03Feb2017_v2        = kreator.makeDataComponent("MuonEG_Run2016H_03Feb2017_v2"        , "/MuonEG/Run2016H-03Feb2017_ver2-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016H_03Feb2017_v2     = kreator.makeDataComponent("DoubleMuon_Run2016H_03Feb2017_v2"    , "/DoubleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016H_03Feb2017_v2     = kreator.makeDataComponent("Tau_Run2016H_03Feb2017_v2"    , "/Tau/Run2016H-03Feb2017_ver2-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016H_03Feb2017_v2 = [JetHT_Run2016H_03Feb2017_v2, HTMHT_Run2016H_03Feb2017_v2, MET_Run2016H_03Feb2017_v2, SingleElectron_Run2016H_03Feb2017_v2, SingleMuon_Run2016H_03Feb2017_v2, SinglePhoton_Run2016H_03Feb2017_v2, DoubleEG_Run2016H_03Feb2017_v2, MuonEG_Run2016H_03Feb2017_v2, DoubleMuon_Run2016H_03Feb2017_v2, Tau_Run2016H_03Feb2017_v2]

### ----------------------------- Run2016H 03Feb2017_ver3-v1 ----------------------------------------

JetHT_Run2016H_03Feb2017_v3          = kreator.makeDataComponent("JetHT_Run2016H_03Feb2017_v3"         , "/JetHT/Run2016H-03Feb2017_ver3-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016H_03Feb2017_v3          = kreator.makeDataComponent("HTMHT_Run2016H_03Feb2017_v3"         , "/HTMHT/Run2016H-03Feb2017_ver3-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016H_03Feb2017_v3            = kreator.makeDataComponent("MET_Run2016H_03Feb2017_v3"           , "/MET/Run2016H-03Feb2017_ver3-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016H_03Feb2017_v3 = kreator.makeDataComponent("SingleElectron_Run2016H_03Feb2017_v3", "/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016H_03Feb2017_v3     = kreator.makeDataComponent("SingleMuon_Run2016H_03Feb2017_v3"    , "/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016H_03Feb2017_v3   = kreator.makeDataComponent("SinglePhoton_Run2016H_03Feb2017_v3"  , "/SinglePhoton/Run2016H-03Feb2017_ver3-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016H_03Feb2017_v3       = kreator.makeDataComponent("DoubleEG_Run2016H_03Feb2017_v3"      , "/DoubleEG/Run2016H-03Feb2017_ver3-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016H_03Feb2017_v3        = kreator.makeDataComponent("MuonEG_Run2016H_03Feb2017_v3"        , "/MuonEG/Run2016H-03Feb2017_ver3-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016H_03Feb2017_v3     = kreator.makeDataComponent("DoubleMuon_Run2016H_03Feb2017_v3"    , "/DoubleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016H_03Feb2017_v3     = kreator.makeDataComponent("Tau_Run2016H_03Feb2017_v3"    , "/Tau/Run2016H-03Feb2017_ver3-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016H_03Feb2017_v3 = [JetHT_Run2016H_03Feb2017_v3, HTMHT_Run2016H_03Feb2017_v3, MET_Run2016H_03Feb2017_v3, SingleElectron_Run2016H_03Feb2017_v3, SingleMuon_Run2016H_03Feb2017_v3, SinglePhoton_Run2016H_03Feb2017_v3, DoubleEG_Run2016H_03Feb2017_v3, MuonEG_Run2016H_03Feb2017_v3, DoubleMuon_Run2016H_03Feb2017_v3, Tau_Run2016H_03Feb2017_v3]

### Summary of 03Feb2017
dataSamples_03Feb2017 = dataSamples_Run2016B_03Feb2017_v2 + dataSamples_Run2016C_03Feb2017 + dataSamples_Run2016D_03Feb2017 + dataSamples_Run2016E_03Feb2017 + dataSamples_Run2016F_03Feb2017 + dataSamples_Run2016G_03Feb2017 + dataSamples_Run2016H_03Feb2017_v2 + dataSamples_Run2016H_03Feb2017_v3


#dataSamples = dataSamples_23Sep2016 + dataSamples_03Feb2017
dataSamples = dataSamples_03Feb2017
samples = dataSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
