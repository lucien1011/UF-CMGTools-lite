

##########################################################
##       CONFIGURATION FOR SUSY SS TREES       ##
## skim condition: >= 2 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg
import re

# ____________________________________________________________________________________________________ ||
# LOAD ALL ANALYZERS

from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

# ____________________________________________________________________________________________________ ||
# SET OPTIONS AND REDEFINE CONFIGURATION

analysis                        = "susy"
runQCDBM                        = False 
runFRMC                         = False
saveSuperClusterVariables       = False
removeJetReCalibration          = False
removeJecUncertainty            = False
doMETpreprocessor               = False
skipT1METCorr                   = False
forcedSplitFactor               = -1
forcedFineSplitFactor           = -1
isTest                          = True 
selectedEvents                  = ""
keepLHEWeights                  = False
fast                            = True
test                            = None

isolation = "miniIso"
sample = "main"

if analysis not in ['susy',]: raise RuntimeError, 'Analysis type unknown'
print 'Using analysis type: %s'%analysis

# ____________________________________________________________________________________________________ ||
# Lepton Skimming
ttHLepSkim.minLeptons           = 2
ttHLepSkim.maxLeptons           = 999
ttHLepSkim.requireSameSignPair  = True

susyCoreSequence.insert(susyCoreSequence.index(ttHLepSkim)+1,globalSkim)
susyCoreSequence.remove(ttHLepSkim)
globalSkim.selections = ["2lep5","1lep5_1tau18", "2tau18","1lep5[maxObj1]"]
#   [ lambda ev: 2<=sum([(lep.miniRelIso<0.4) for lep in ev.selectedLeptons]) ] 
#   ["2lep5[os:!DS_TTW_RA5_sync]_1lep50"]#, "1lep5_1tau18", "2tau18","2lep5_1met50"]

# ____________________________________________________________________________________________________ ||
# Lepton Isolation
lepAna.doMiniIsolation = True
lepAna.packedCandidates = 'packedPFCandidates'
lepAna.miniIsolationPUCorr = 'rhoArea'
lepAna.miniIsolationVetoLeptons = None # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones
lepAna.doIsolationScan = False

# Lepton Preselection
lepAna.loose_electron_id = "MVA_ID_NonTrig_Spring16_VLooseIdEmu"

if isolation == "miniIso": 
    lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
    lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
elif isolation == None:
    lepAna.loose_muon_isoCut     = lambda muon : True
    lepAna.loose_electron_isoCut = lambda elec : True
elif isolation == "absIso04":
    lepAna.loose_muon_isoCut     = lambda muon : muon.RelIsoMIV04*muon.pt() < 10 and muon.sip3D() < 8
    lepAna.loose_electron_isoCut = lambda elec : elec.RelIsoMIV04*elec.pt() < 10 and elec.sip3D() < 8
elif isolation == "Iperbolic":
    lepAna.loose_muon_isoCut     = lambda muon : muon.relIso03*muon.pt() < (20+300/muon.pt()) and  abs(muon.ip3D()) < 0.0175 and muon.sip3D() < 2.5
    lepAna.loose_electron_isoCut = lambda elec : elec.relIso03*elec.pt() < (20+300/elec.pt()) and  abs(elec.ip3D()) < 0.0175 and elec.sip3D() < 2.5
else:
    # nothing to do, will use normal relIso03
    pass

# ____________________________________________________________________________________________________ ||
# JetMET
jetAna.copyJetsByValue = True # do not remove this
metAna.copyMETsByValue = True # do not remove this

jetAna.cleanJetsFromLeptons = False
jetAna.cleanSelectedLeptons = True
jetAna.storeLowPtJets       = True
jetAna.jetEtaCentral        = jetAna.jetEta
jetAna.mcGT                 = "Spring16_25nsV8_MC"    
jetAna.dataGT               = "Spring16_25nsV8BCD_DATA Spring16_25nsV8E_DATA Spring16_25nsV8F_DATA Spring16_25nsV8_DATA"
jetAna.runsDataJEC          = [276811, 277420, 278802]
jetAna.doQG                 = False
jetAnaScaleUp.doQG          = False
jetAnaScaleDown.doQG        = False

if not removeJecUncertainty:
    jetAna.addJECShifts = True
    jetAnaScaleDown.copyJetsByValue = True # do not remove this
    metAnaScaleDown.copyMETsByValue = True # do not remove this
    jetAnaScaleUp.copyJetsByValue = True # do not remove this
    metAnaScaleUp.copyMETsByValue = True # do not remove this
    susyCoreSequence.insert(susyCoreSequence.index(jetAna)+1, jetAnaScaleDown)
    susyCoreSequence.insert(susyCoreSequence.index(jetAna)+1, jetAnaScaleUp)
    susyCoreSequence.insert(susyCoreSequence.index(metAna)+1, metAnaScaleDown)
    susyCoreSequence.insert(susyCoreSequence.index(metAna)+1, metAnaScaleUp)
    jetAnaScaleDown.cleanJetsFromLeptons=False
    jetAnaScaleDown.cleanSelectedLeptons=True
    jetAnaScaleDown.storeLowPtJets=True
    jetAnaScaleDown.jetEtaCentral = jetAnaScaleDown.jetEta
    jetAnaScaleUp.cleanJetsFromLeptons=False
    jetAnaScaleUp.cleanSelectedLeptons=True
    jetAnaScaleUp.storeLowPtJets=True
    jetAnaScaleUp.jetEtaCentral = jetAnaScaleUp.jetEta
    jetAnaScaleDown.mcGT="Spring16_25nsV8_MC"    
    jetAnaScaleDown.dataGT   = "Spring16_25nsV8BCD_DATA Spring16_25nsV8E_DATA Spring16_25nsV8F_DATA Spring16_25nsV8_DATA"
    jetAnaScaleDown.runsDataJEC   = [276811, 277420, 278802]
    jetAnaScaleUp.mcGT="Spring16_25nsV8_MC"    
    jetAnaScaleUp.dataGT   = "Spring16_25nsV8BCD_DATA Spring16_25nsV8E_DATA Spring16_25nsV8F_DATA Spring16_25nsV8_DATA"
    jetAnaScaleUp.runsDataJEC   = [276811, 277420, 278802]

# ____________________________________________________________________________________________________ ||
# Photon
# Switch off slow photon MC matching
photonAna.do_mc_match = False

# ____________________________________________________________________________________________________ ||
# Tau
# Loose Tau configuration
tauAna.loose_ptMin = 20
tauAna.loose_etaMax = 2.3
tauAna.loose_decayModeID = "decayModeFindingNewDMs"
tauAna.loose_tauID = "decayModeFindingNewDMs"

# ____________________________________________________________________________________________________ ||
# ADDITIONAL ANALYZERS 
## Event Analyzer for susy multi-lepton (at the moment, it's the TTH one)
from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## JetTau analyzer, to be called (for the moment) once bjetsMedium are produced
from CMGTools.TTHAnalysis.analyzers.ttHJetTauAnalyzer import ttHJetTauAnalyzer
ttHJetTauAna = cfg.Analyzer(
    ttHJetTauAnalyzer, name="ttHJetTauAnalyzer",
    )

# ____________________________________________________________________________________________________ ||
### Insert the FatJet, SV, HeavyFlavour analyzers in the sequence
#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna), 
#                        ttHFatJetAna)
#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna), 
#                        ttHSVAna)
#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna), 
#                        ttHHeavyFlavourHadronAna)

### Insert declustering analyzer
#from CMGTools.TTHAnalysis.analyzers.ttHDeclusterJetsAnalyzer import ttHDeclusterJetsAnalyzer
#ttHDecluster = cfg.Analyzer(
#    ttHDeclusterJetsAnalyzer, name='ttHDecluster',
#    lepCut     = lambda lep,ptrel : lep.pt() > 10,
#    maxSubjets = 6, # for exclusive reclustering
#    ptMinSubjets = 5, # for inclusive reclustering
#    drMin      = 0.2, # minimal deltaR(l,subjet) required for a successful subjet match
#    ptRatioMax = 1.5, # maximum pt(l)/pt(subjet) required for a successful match
#    ptRatioDiff = 0.1,  # cut on abs( pt(l)/pt(subjet) - 1 ) sufficient to call a match successful
#    drMatch     = 0.02, # deltaR(l,subjet) sufficient to call a match successful
#    ptRelMin    = 5,    # maximum ptRelV1(l,subjet) sufficient to call a match successful
#    prune       = True, # also do pruning of the jets 
#    pruneZCut       = 0.1, # pruning parameters (usual value in CMS: 0.1)
#    pruneRCutFactor = 0.5, # pruning parameters (usual value in CMS: 0.5)
#    verbose     = 0,   # print out the first N leptons
#    jetCut = lambda jet : jet.pt() > 20,
#    mcPartonPtCut = 20,
#    mcLeptonPtCut =  5,
#    mcTauPtCut    = 15,
#    )
#susyCoreSequence.insert(susyCoreSequence.index(ttHFatJetAna)+1, ttHDecluster)

# ____________________________________________________________________________________________________ ||
# TreeProducer
from CMGTools.RA5.analyzers.treeProducerSusyRA5 import * 

ttHLepSkim.allowLepTauComb = True
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        susyLeptonMatchAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        susyTauMatchAna)
leptonTypeSusyExtraLight.addVariables([
        NTupleVariable("mcUCSXMatchId", lambda x : x.mcUCSXMatchId if hasattr(x,'mcUCSXMatchId') else -1, mcOnly=True, help="MC truth matching a la UCSX"),
        ])
tauTypeSusy.addVariables([
        NTupleVariable("mcUCSXMatchId", lambda x : x.mcUCSXMatchId if hasattr(x,'mcUCSXMatchId') else -1, mcOnly=True, help="MC truth matching a la UCSX"),
        ])
photonAna.do_mc_match = True
susyRA5_collections.update({ # for conversion studies
        "selectedPhotons"    : NTupleCollection("PhoGood", photonTypeSusy, 10, help="Selected photons"),
        }) 
del susyRA5_collections["discardedJets"]
susyRA5_collections.update({"discardedJets"   : NTupleCollection("DiscJet", jetTypeSusySuperLight, 15, help="Jets discarted in the jet-lepton cleaning (JEC)")
                                        })

# for electron scale and resolution checks
if saveSuperClusterVariables:
    leptonTypeSusyExtraLight.addVariables([
            NTupleVariable("e5x5", lambda x: x.e5x5() if (abs(x.pdgId())==11 and hasattr(x,"e5x5")) else -999, help="Electron e5x5"),
            NTupleVariable("r9", lambda x: x.r9() if (abs(x.pdgId())==11 and hasattr(x,"r9")) else -999, help="Electron r9"),
            NTupleVariable("sigmaIetaIeta", lambda x: x.sigmaIetaIeta() if (abs(x.pdgId())==11 and hasattr(x,"sigmaIetaIeta")) else -999, help="Electron sigmaIetaIeta"),
            NTupleVariable("sigmaIphiIphi", lambda x: x.sigmaIphiIphi() if (abs(x.pdgId())==11 and hasattr(x,"sigmaIphiIphi")) else -999, help="Electron sigmaIphiIphi"),
            NTupleVariable("hcalOverEcal", lambda x: x.hcalOverEcal() if (abs(x.pdgId())==11 and hasattr(x,"hcalOverEcal")) else -999, help="Electron hcalOverEcal"),
            NTupleVariable("full5x5_e5x5", lambda x: x.full5x5_e5x5() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_e5x5")) else -999, help="Electron full5x5_e5x5"),
            NTupleVariable("full5x5_r9", lambda x: x.full5x5_r9() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_r9")) else -999, help="Electron full5x5_r9"),
            NTupleVariable("full5x5_sigmaIetaIeta", lambda x: x.full5x5_sigmaIetaIeta() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_sigmaIetaIeta")) else -999, help="Electron full5x5_sigmaIetaIeta"),
            NTupleVariable("full5x5_sigmaIphiIphi", lambda x: x.full5x5_sigmaIphiIphi() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_sigmaIphiIphi")) else -999, help="Electron full5x5_sigmaIphiIphi"),
            NTupleVariable("full5x5_hcalOverEcal", lambda x: x.full5x5_hcalOverEcal() if (abs(x.pdgId())==11 and hasattr(x,"full5x5_hcalOverEcal")) else -999, help="Electron full5x5_hcalOverEcal"),
            NTupleVariable("correctedEcalEnergy", lambda x: x.correctedEcalEnergy() if (abs(x.pdgId())==11 and hasattr(x,"correctedEcalEnergy")) else -999, help="Electron correctedEcalEnergy"),
            NTupleVariable("eSuperClusterOverP", lambda x: x.eSuperClusterOverP() if (abs(x.pdgId())==11 and hasattr(x,"eSuperClusterOverP")) else -999, help="Electron eSuperClusterOverP"),
            NTupleVariable("ecalEnergy", lambda x: x.ecalEnergy() if (abs(x.pdgId())==11 and hasattr(x,"ecalEnergy")) else -999, help="Electron ecalEnergy"),
            NTupleVariable("superCluster_rawEnergy", lambda x: x.superCluster().rawEnergy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.rawEnergy"),
            NTupleVariable("superCluster_preshowerEnergy", lambda x: x.superCluster().preshowerEnergy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.preshowerEnergy"),
            NTupleVariable("superCluster_correctedEnergy", lambda x: x.superCluster().correctedEnergy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.correctedEnergy"),
            NTupleVariable("superCluster_energy", lambda x: x.superCluster().energy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.energy"),
            NTupleVariable("superCluster_clustersSize", lambda x: x.superCluster().clustersSize() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.clustersSize"),
            NTupleVariable("superCluster_seed.energy", lambda x: x.superCluster().seed().energy() if (abs(x.pdgId())==11 and hasattr(x,"superCluster")) else -999, help="Electron superCluster.seed.energy"),
])

if not removeJecUncertainty:
    susyRA5_globalObjects.update({
            "met_jecUp" : NTupleObject("met_jecUp", metType, help="PF E_{T}^{miss}, after type 1 corrections (JEC plus 1sigma)"),
            "met_jecDown" : NTupleObject("met_jecDown", metType, help="PF E_{T}^{miss}, after type 1 corrections (JEC minus 1sigma)"),
            })
    susyRA5_collections.update({
            "cleanJets_jecUp"       : NTupleCollection("Jet_jecUp",     jetTypeSusyExtraLight, 15, help="Cental jets after full selection and cleaning, sorted by pt (JEC plus 1sigma)"),
            "cleanJets_jecDown"     : NTupleCollection("Jet_jecDown",     jetTypeSusyExtraLight, 15, help="Cental jets after full selection and cleaning, sorted by pt (JEC minus 1sigma)"),
            "discardedJets_jecUp"   : NTupleCollection("DiscJet_jecUp", jetTypeSusySuperLight if analysis=='susy' else jetTypeSusyExtraLight, 15, help="Jets discarted in the jet-lepton cleaning (JEC +1sigma)"),
            "discardedJets_jecDown" : NTupleCollection("DiscJet_jecDown", jetTypeSusySuperLight if analysis=='susy' else jetTypeSusyExtraLight, 15, help="Jets discarted in the jet-lepton cleaning (JEC -1sigma)"),
            })

# ____________________________________________________________________________________________________ ||
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyRA5',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susyRA5_globalVariables,
     globalObjects = susyRA5_globalObjects,
     collections = susyRA5_collections,
)

# ____________________________________________________________________________________________________ ||
## histo counter
susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
                        susyCounter)
susyScanAna.doLHE=False # until a proper fix is put in the analyzer

# ____________________________________________________________________________________________________ ||
# HBHE new filter
from CMGTools.TTHAnalysis.analyzers.hbheAnalyzer import hbheAnalyzer
hbheAna = cfg.Analyzer(
    hbheAnalyzer, name="hbheAnalyzer", IgnoreTS4TS5ifJetInLowBVRegion=False
    )
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),hbheAna)
treeProducer.globalVariables.append(NTupleVariable("hbheFilterNew50ns", lambda ev: ev.hbheFilterNew50ns, int, help="new HBHE filter for 50 ns"))
treeProducer.globalVariables.append(NTupleVariable("hbheFilterNew25ns", lambda ev: ev.hbheFilterNew25ns, int, help="new HBHE filter for 25 ns"))
treeProducer.globalVariables.append(NTupleVariable("hbheFilterIso", lambda ev: ev.hbheFilterIso, int, help="HBHE iso-based noise filter"))
treeProducer.globalVariables.append(NTupleVariable("Flag_badChargedHadronFilter", lambda ev: ev.badChargedHadron, help="bad charged hadron filter decision"))
treeProducer.globalVariables.append(NTupleVariable("Flag_badMuonFilter", lambda ev: ev.badMuon, help="bad muon filter decision"))


# ____________________________________________________________________________________________________ ||
#additional MET quantities
metAna.doTkMet = False
#treeProducer.globalVariables.append(NTupleVariable("met_trkPt", lambda ev : ev.tkMet.pt() if  hasattr(ev,'tkMet') else  0, help="tkmet p_{T}"))
#treeProducer.globalVariables.append(NTupleVariable("met_trkPhi", lambda ev : ev.tkMet.phi() if  hasattr(ev,'tkMet') else  0, help="tkmet phi"))

if not skipT1METCorr:
    if doMETpreprocessor: 
        print "WARNING: you're running the MET preprocessor and also Type1 MET corrections. This is probably not intended."
    jetAna.calculateType1METCorrection = True
    metAna.recalibrate = "type1"
    jetAnaScaleUp.calculateType1METCorrection = True
    metAnaScaleUp.recalibrate = "type1"
    jetAnaScaleDown.calculateType1METCorrection = True
    metAnaScaleDown.recalibrate = "type1"

# ____________________________________________________________________________________________________ ||
# SAMPLES AND TRIGGERS
from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import *
triggerFlagsAna.triggerBits = {
    'DoubleMu' : triggers_mumu_iso,
    'DoubleMuSS' : triggers_mumu_ss,
    'DoubleMuNoIso' : triggers_mumu_noniso + triggers_mu27tkmu8,
    'DoubleEl' : triggers_ee + triggers_doubleele33 + triggers_doubleele33_MW,
    'MuEG'     : triggers_mue + triggers_mu30ele30,
    'DoubleMuHT' : triggers_mumu_ht,
    'DoubleElHT' : triggers_ee_ht,
    'MuEGHT' : triggers_mue_ht,
    'TripleEl' : triggers_3e,
    'TripleMu' : triggers_3mu,
    'TripleMuA' : triggers_3mu_alt,
    'DoubleMuEl' : triggers_2mu1e,
    'DoubleElMu' : triggers_2e1mu,
    'SingleMu' : triggers_1mu_iso,
    'SingleEl'     : triggers_1e,
    'SOSHighMET' : triggers_SOS_highMET,
    'SOSDoubleMuLowMET' : triggers_SOS_doublemulowMET,
    'SOSTripleMu' : triggers_SOS_tripleMu,
    'LepTau' : triggers_leptau,
    'MET' : triggers_metNoMu90_mhtNoMu90 + triggers_htmet,
    'HT' : triggers_pfht,
    'MonoJet80MET90' : triggers_Jet80MET90,
    'MonoJet80MET120' : triggers_Jet80MET120,
    #'METMu5' : triggers_MET120Mu5,
    }
triggerFlagsAna.unrollbits = True
triggerFlagsAna.saveIsUnprescaled = True
triggerFlagsAna.checkL1Prescale = True

from CMGTools.RA5.Dataset.SMS_T1qqqqL_Run2016 import *
from CMGTools.HToZZ4L.tools.configTools import printSummary, configureSplittingFromTime, cropToLumi, prescaleComponents, insertEventSelector

samples = [
            T1qqqqL_1000,
            ]
   
if not keepLHEWeights:
    selectedComponents = samples #samples_2l +samples_1l
else:
    selectedComponents = samples_LHE

if removeJetReCalibration:
    jetAna.recalibrateJets = False
    jetAnaScaleUp.recalibrateJets = False
    jetAnaScaleDown.recalibrateJets = False

if getHeppyOption("noLepSkim",False):
    if globalSkim in sequence:
        globalSkim.selection = []
    if ttHLepSkim in sequence:
        ttHLepSkim.minLeptons=0 

if forcedSplitFactor>0 or forcedFineSplitFactor>0:
    if forcedFineSplitFactor>0 and forcedSplitFactor!=1: raise RuntimeError, 'splitFactor must be 1 if setting fineSplitFactor'
    for c in selectedComponents:
        if forcedSplitFactor>0: c.splitFactor = forcedSplitFactor
        if forcedFineSplitFactor>0: c.fineSplitFactor = forcedFineSplitFactor

# ____________________________________________________________________________________________________ ||
# SEQUENCE
sequence = cfg.Sequence(susyCoreSequence+[
        ttHJetTauAna,
        ttHEventAna,
        treeProducer,
    ])
preprocessor = None

# ____________________________________________________________________________________________________ ||
#-------- HOW TO RUN -----------
if test == '1':
    comp = selectedComponents[0]
    comp.files = comp.files[:1]
    comp.splitFactor = 1
    comp.fineSplitFactor = 1
    selectedComponents = [ comp ]
elif test == '2':
    from CMGTools.Production.promptRecoRunRangeFilter import filterWithCollection
    for comp in selectedComponents:
        if comp.isData: comp.files = filterWithCollection(comp.files, [274315,275658,276363,276454])
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1
elif test == '3':
    for comp in selectedComponents:
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 4
elif test == '5':
    for comp in selectedComponents:
        comp.files = comp.files[:5]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1
elif test == "ra5-sync-mc":
    comp = cfg.MCComponent( files = ["root://eoscms.cern.ch//store/mc/RunIISpring16MiniAODv1/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/6E02CA07-BA02-E611-A59E-14187741208F.root"], name="TTW_RA5_sync" )
    comp.triggers = []
    comp.splitFactor = 1
    comp.fineSplitFactor = 1
    selectedComponents = [ comp ]
    sequence.remove(jsonAna)
elif test == '80X-MC':
    what = getHeppyOption("sample","TTLep")
    if what == "TTLep":
        TTLep_pow = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
        selectedComponents = [ TTLep_pow ]
        comp = selectedComponents[0]
        comp.triggers = []
        comp.files = [ '/store/mc/RunIISpring16MiniAODv1/TTTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/00000/002606A5-C909-E611-85DA-44A8423D7E31.root' ]
        tmpfil = os.path.expandvars("/tmp/$USER/002606A5-C909-E611-85DA-44A8423D7E31.root")
        if not os.path.exists(tmpfil):
            os.system("xrdcp root://eoscms//eos/cms%s %s" % (comp.files[0],tmpfil))
        comp.files = [ tmpfil ]
        if not getHeppyOption("single"): comp.fineSplitFactor = 4
    else: raise RuntimeError, "Unknown MC sample: %s" % what
elif test != None:
    raise RuntimeError, "Unknown test %r" % test

## FAST mode: pre-skim using reco leptons, don't do accounting of LHE weights (slow)"
## Useful for large background samples with low skim efficiency
if fast:
    susyCounter.doLHE = False
    from CMGTools.TTHAnalysis.analyzers.ttHFastLepSkimmer import ttHFastLepSkimmer
    fastSkim = cfg.Analyzer(
        ttHFastLepSkimmer, name="ttHFastLepSkimmer2lep",
        muons = 'slimmedMuons', muCut = lambda mu : mu.pt() > 3 and mu.isLooseMuon(),
        electrons = 'slimmedElectrons', eleCut = lambda ele : ele.pt() > 5,
        minLeptons = 2, 
    )
    if jsonAna in sequence:
        sequence.insert(sequence.index(jsonAna)+1, fastSkim)
    else:
        sequence.insert(sequence.index(skimAnalyzer)+1, fastSkim)
if not keepLHEWeights:
    if "LHE_weights" in treeProducer.collections: treeProducer.collections.pop("LHE_weights")
    if lheWeightAna in sequence: sequence.remove(lheWeightAna)
    susyCounter.doLHE = False

## Auto-AAA
from CMGTools.RootTools.samples.autoAAAconfig import *
if not getHeppyOption("isCrab"):
    autoAAA(selectedComponents)

## output histogram
outputService=[]
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='treeProducerSusyRA5/tree.root',
    option='recreate'
    )    
outputService.append(output_service)

# print summary of components to process
printSummary(selectedComponents)

# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload if not preprocessor else Events
EOSEventsWithDownload.aggressive = 2 # always fetch if running on Wigner
if getHeppyOption("nofetch") or getHeppyOption("isCrab"):
    event_class = Events
    if preprocessor: preprocessor.prefetch = False
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = outputService, 
                     preprocessor = preprocessor, 
                     events_class = event_class)
