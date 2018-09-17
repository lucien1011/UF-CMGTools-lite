from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

leptonTypeSusyRA5 = NTupleObjectType("leptonTypeSusyRA5", baseObjectTypes = [ leptonTypeSusyExtraLight ], variables = [ 
        NTupleVariable("conePt", lambda x : x.conePt),
        NTupleVariable("isLoose", lambda x : x.isLoose, int,),
        NTupleVariable("isLooseVeto", lambda x : x.isLooseVeto, int,),
        NTupleVariable("isCleaning", lambda x : x.isCleaning, int,),
        NTupleVariable("isCleaningVeto", lambda x : x.isCleaningVeto, int,),
        NTupleVariable("isFake", lambda x : x.isFake, int,),
        NTupleVariable("isFakeVeto", lambda x : x.isFakeVeto, int,),
        NTupleVariable("isTight", lambda x : x.isTight, int,),
        NTupleVariable("isTightVeto", lambda x : x.isTightVeto, int,),
    ])

arrayType = NTupleObjectType("array", variables = [
        NTupleVariable("",    lambda x : x),
    ])

susyRA5_globalVariables = [
            
            NTupleVariable("Flag_badMuonMoriond2017",  lambda ev: ev.badMuonMoriond2017, int, help="bad muon found in event (Moriond 2017 filter)?"),
            NTupleVariable("Flag_badCloneMuonMoriond2017",  lambda ev: ev.badCloneMuonMoriond2017, int, help="clone muon found in event (Moriond 2017 filter)?"),
            NTupleVariable("badCloneMuonMoriond2017_maxPt",  lambda ev: max(mu.pt() for mu in ev.badCloneMuonMoriond2017_badMuons) if not ev.badCloneMuonMoriond2017 else 0, help="max pt of any clone muon found in event (Moriond 2017 filter)"),
            NTupleVariable("badNotCloneMuonMoriond2017_maxPt",  lambda ev: max((mu.pt() if mu not in ev.badCloneMuonMoriond2017_badMuons else 0) for mu in ev.badMuonMoriond2017_badMuons) if not ev.badMuonMoriond2017 else 0, help="max pt of any bad non-clone muon found in event (Moriond 2017 filter)"),

            NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
            NTupleVariable("rhoCN",  lambda ev: ev.rhoCN, float, help="fixed grid rho central neutral"),
            NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"), 

            ## ------- lheHT, needed for merging HT binned samples 
            NTupleVariable("lheHT", lambda ev : getattr(ev,"lheHT",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer"),
            NTupleVariable("lheHTIncoming", lambda ev : getattr(ev,"lheHTIncoming",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer (only LHE status<0 as mothers)"),
            NTupleVariable("Flag_badChargedHadronFilter", lambda ev: ev.badChargedHadron, help="bad charged hadron filter decision"),
            NTupleVariable("Flag_badMuonFilter", lambda ev: ev.badMuon, help="bad muon filter decision"),

            NTupleVariable("nJetSel", lambda ev: ev.nJetSel, help="nJetSel after LeptonJetRecleaner"),
            NTupleVariable("nDiscJetSel", lambda ev: ev.nDiscJetSel, help="nDiscJetSel after LeptonJetRecleaner"),
            NTupleVariable("nBJetLooseRA540", lambda ev: ev.nBJetLooseRA540, help="nBJetLooseRA540 after LeptonJetRecleaner"),
            NTupleVariable("nBJetMediumRA540", lambda ev: ev.nBJetMediumRA540, help="nBJetMediumRA540 after LeptonJetRecleaner"),
            NTupleVariable("nBJetLooseRA525", lambda ev: ev.nBJetLooseRA525, help="nBJetLooseRA525 after LeptonJetRecleaner"),
            NTupleVariable("nBJetMediumRA525", lambda ev: ev.nBJetMediumRA525, help="nBJetMediumRA525 after LeptonJetRecleaner"),
            NTupleVariable("nJetRA540", lambda ev: ev.nJetRA540, help="nJetRA540 after LeptonJetRecleaner"),
            NTupleVariable("nJetRA525", lambda ev: ev.nJetRA525, help="nJetRA525 after LeptonJetRecleaner"),
            NTupleVariable("htJet40", lambda ev: ev.htJet40, help="htJet40 after LeptonJetRecleaner"),
            NTupleVariable("htJet25", lambda ev: ev.htJet25, help="htJet25 after LeptonJetRecleaner"),
            NTupleVariable("mhtJet40", lambda ev: ev.mhtJet40, help="mhtJet40 after LeptonJetRecleaner"),
            NTupleVariable("mhtJet25", lambda ev: ev.mhtJet25, help="mhtJet25 after LeptonJetRecleaner"),
]

susyRA5_globalObjects = {
            "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after type 1 corrections"),
            }
susyRA5_globalObjects.update({
            # put more here
})

susyRA5_collections = {} 
susyRA5_collections.update({
            "genleps"           : NTupleCollection("genLep",     genParticleWithLinksType, 10, help="Generated leptons (e/mu) from W/Z decays"),                                                                                                
            "generatorSummary"  : NTupleCollection("GenPart", genParticleWithLinksType, 100 , help="Hard scattering particles, with ancestry and links"),
            "selectedLeptons"   : NTupleCollection("LepGood",  leptonTypeSusyRA5, 8, help="Leptons after the preselection"),
            "otherLeptons"      : NTupleCollection("LepOther", leptonTypeSusy, 8, help="Leptons after the preselection"),
            "cleanJets"         : NTupleCollection("Jet",     jetTypeSusyExtraLight, 15, help="Cental jets after full selection and cleaning, sorted by pt"),
            "discardedJets"     : NTupleCollection("DiscJet", jetTypeSusyExtraLight, 15, help="Jets discarted in the jet-lepton cleaning"),
            "discardedLeptons"  : NTupleCollection("DiscLep", leptonTypeSusy, 8, help="Leptons discarded in the jet-lepton cleaning"),
            "LHE_weights"       : NTupleCollection("LHEweight",  weightsInfoType, 1000, mcOnly=True, help="LHE weight info"),
            "JetSelIndex"       : NTupleCollection("JetSelIndex", arrayType, 15, help="Jet index after recleaning"),
})
