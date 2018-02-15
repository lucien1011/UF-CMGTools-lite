from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

##__________________________________________________________________||
## turn off LHE info for now, as it slows everything down
genAna.makeLHEweights = False

##__________________________________________________________________||
## Muons
## Choose medium point from https://indico.cern.ch/event/357213/contribution/2/material/slides/0.pdf
## other things in https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonId2015
mu_id_loose     = "POG_ID_Loose"
mu_id_selection = "POG_ID_Tight"
lepAna.loose_muon_pt               = 10.
lepAna.loose_muon_eta              = 2.5
lepAna.loose_muon_id               = mu_id_loose
lepAna.loose_muon_dxy              = 999.
lepAna.loose_muon_dz               = 999.
lepAna.loose_muon_relIso           = 0.12
lepAna.mu_isoCorr                  = "rhoArea"
lepAna.loose_muon_isoCut           = lambda muon : muon.miniRelIso < 0.2

##__________________________________________________________________||
## Electrons
## Choose loose point from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
ele_id_selection = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Tight'
ele_id_loose     = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Loose'
ele_id_veto      = 'POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto'
ele_ea      = "Spring15_25ns_v1"
ele_ea_50ns = "Spring15_50ns_v1"
lepAna.loose_electron_id           = ele_id_loose
lepAna.loose_electron_pt           = 10
lepAna.loose_electron_eta          = 2.5
lepAna.loose_electron_dxy          = 0.118
lepAna.loose_electron_dz           = 0.822
lepAna.loose_electron_relIso       = 0.12
lepAna.loose_electron_isoCut       = lambda electron : electron.miniRelIso < 0.1
lepAna.loose_electron_lostHits     = 1
# ttHLepAna.inclusive_electron_lostHits = 999 # no cut
lepAna.ele_isoCorr                 = "rhoArea"
lepAna.ele_tightId                 = "Cuts_2012"
lepAna.doMiniIsolation = True
lepAna.miniIsolationPUCorr = None #Will use the correction defined for the individual objects

##__________________________________________________________________||
## Photons (used for the veto)
pho_id_loose                       = "POG_SPRING15_25ns_Loose"
pho_id_selection                   = "POG_SPRING15_25ns_Tight"
pho_id_selection_fakeEnriched      = "POG_SPRING15_25ns_Tight_noChaHadIso_noSigmaIEtaIEta"
pho_ea = "PHYS14_25ns_v1"
pho_id_loose_50ns                  = "POG_SPRING15_50ns_Loose"
pho_id_selection_50ns              = "POG_SPRING15_50ns_Tight"
pho_id_selection_fakeEnriched_50ns = "POG_SPRING15_50ns_Tight_noChaHadIso_noSigmaIEtaIEta"
pho_ea_50ns = "PHYS14_50ns_v1"
photonAna.ptMin                       = 25
photonAna.etaMax                      = 2.5
photonAna.gammaID                     = pho_id_loose
photonAna.rhoPhoton                   = 'fixedGridRhoFastjetAll'
photonAna.gamma_isoCorr               = 'rhoArea'
photonAna.checkGen                    = True

##__________________________________________________________________||
# Jets (for event variables do apply the jetID and not PUID yet)
jet_pt_selection = 40.
jet_eta_selection = 3.
jet_jec_mcGT   = "Summer16_23Sep2016V3_MC"
jet_jec_fsGT   = "Spring16_FastSimV1_MC"
jet_jec_dataGT = [(1,"Summer16_23Sep2016BCDV3_DATA"),(276831,"Summer16_23Sep2016EFV3_DATA"),(278802,"Summer16_23Sep2016GV3_DATA"),(280919,"Summer16_23Sep2016HV3_DATA")]
jet_jec_mcGT_50ns   = "76X_mcRun2_asymptotic_v12"
jet_jec_dataGT_50ns = "76X_dataRun2_v15_Run2015D_50ns"
jet_residuals = True 
jetAna.jetEta          = 5.
jetAna.jetEtaCentral   = jet_eta_selection
jetAna.jetPt           = 10.0
jetAna.jetID           = "POG_PFID_Loose"
jetAna.cleanAllJets    = True
jetAna.alwaysCleanPhotons     = True
jetAna.cleanGenJetsFromPhoton = True
jetAna.addJECShifts           = True
jetAna.smearJets       = False
jetAna.calculateType1METCorrection  = True
jetAna.doPuId  = True
#jetAna.jetCol = 'selectedUpdatedPatJets'

##__________________________________________________________________||
## Isolated Track
# those are the cuts for the nonEMu
isoTrackAna.setOff          = False
isoTrackAna.candidates      = 'packedPFCandidates'
isoTrackAna.candidatesTypes = 'std::vector<pat::PackedCandidate>'
isoTrackAna.ptMin           = 10 ### for pion
isoTrackAna.ptMinEMU        = 10 ### for EMU
isoTrackAna.dzMax           = 0.05
isoTrackAna.isoDR           = 0.3
isoTrackAna.ptPartMin       = 0
isoTrackAna.dzPartMax       = 0.05
isoTrackAna.maxAbsIso       = 8
isoTrackAna.doRelIsolation  = True
isoTrackAna.MaxIsoSum       = 0.1
isoTrackAna.MaxIsoSumEMU    = 0.1
isoTrackAna.doSecondVeto    = False
isoTrackAna.doPrune         = False

##__________________________________________________________________||
metAna.doMetNoMu = True
metAna.doMetNoEle = True
metAna.doMetNoPhoton = True
metAna.doMetNoMuEle = True
metAna.recalibrate = 'type1'
metAna.applyJetSmearing = True
metAna.fallbackLabel = None

##__________________________________________________________________||
from CMGTools.RPV.treeContent.baseContent import *
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyRPV',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the
                                   # TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyRPV_globalVariables,
     globalObjects = susyRPV_globalObjects,
     collections = susyRPV_collections,
     isCompressed = 9
)

from CMGTools.RPV.RPVEventSelector import *
rpvEvtSelector = cfg.Analyzer(
    RPVEventSelector,name="RPVEventSelector",
    )

##__________________________________________________________________||
sequence = susyCoreSequence
sequence = cfg.Sequence(sequence)

sequence.remove(susyScanAna)
#sequence.append(rpvEvtSelector)
sequence.append(treeProducer)
