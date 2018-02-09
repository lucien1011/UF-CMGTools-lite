from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *
from CMGTools.RPV.objects.phobj import *

susyRPV_collections = {
    "cleanJets"       : NTupleCollection("jet",                slimJetType, 100, help="all jets (w/ x-cleaning, w/ ID applied w/o PUID applied pt > 25 (JEC up) |eta| < 3) , sorted by pt", filter=lambda l : l.pt()/l.corr*l.corrJECUp>25  ),

    # Photons
    "selectedPhotons" : NTupleCollection("gamma", slimPhotonType, 50, help="photons with pt > 25 and loose cut based ID"),

    # Leptons
    "selectedMuons"     : NTupleCollection("muon", slimLeptonType, 50, help="Muons selected by the analysis"),
    "selectedElectrons" : NTupleCollection("ele",  slimLeptonType, 50, help="Electrons selected by the analysis"),
    "selectedTaus"      : NTupleCollection("tau",  tauTypeSusy,    50, help="Taus after the preselection"),

    # Isotracks
    "selectedIsoTrack" : NTupleCollection("isoTrack", isoTrackType, 50, help="isoTrack, sorted by pt"),

    #Gen collections
    "cleanGenJets"      : NTupleCollection("genJet",    fourVectorType,                10, mcOnly=True, help="Generated jets (cleaned)", filter=lambda j : j.pt()>15 ),
    "genPhotons"        : NTupleCollection("genPhoton", slimGenPhotonType,             10, mcOnly=True, help="Generated photons"),
    "genleps"           : NTupleCollection("genLep",    slimGenParticleWithLinksType,  10, mcOnly=True, help="Generated leptons (e/mu) from W/Z decays"),
    "generatorSummary"  : NTupleCollection("GenPart",   slimGenParticleWithLinksType, 100, mcOnly=True, help="Hard scattering particles, with ancestry and links"),
    #"genParticles"     : NTupleCollection("allGenPart", genParticleWithMotherId, 200, help="all pruned genparticles"),

    }

susyRPV_globalVariables = [
    #NTupleVariable("nVert", lambda ev: ev.nVert, int, help="Number of good vertices"),
    ]

susyRPV_globalObjects = {
    "met"         : NTupleObject("met",            slimMetType, help="PF E_{T}^{miss}, after type 1 corrections"),
    }
