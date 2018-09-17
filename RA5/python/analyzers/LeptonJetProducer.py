from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
import PhysicsTools.HeppyCore.framework.config as cfg

from CMGTools.RA5.analyzers.LeptonDefinition import LeptonDict

from CMGTools.RA5.analyzers.LeptonChoiceRA5 import _susy2lss_lepId_CBloose,_susy2lss_lepId_loosestFO,_susy2lss_lepId_IPcuts,_susy2lss_lepConePt1015,_susy2lss_lepId_tighterFO,_susy2lss_multiIso,_susy2lss_lepId_CB,_susy2lss_idIsoEmu_cuts,conept_RA5

import copy

class LeptonJetProducer(Analyzer):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(LeptonJetProducer,self).__init__(cfg_ana,cfg_comp,looperName)

    def beginLoop(self,setup):
        super(LeptonJetProducer,self).beginLoop( setup )
        self.leptonJetAlgo = LeptonDict["2016"]
        self.dictLabel = "_Mini"
        self.jecStrs = ["","_jecUp","_jecDown",]

    def process(self, event):
        event.leptonJetRet = self.leptonJetAlgo(event)

        for il,l in enumerate(event.selectedLeptons):
            l.conePt            = event.leptonJetRet["LepGood_conePt"][il]
            l.isLoose           = event.leptonJetRet["LepGood_isLooseOut"+self.dictLabel][il]
            l.isLooseVeto       = event.leptonJetRet["LepGood_isLooseVetoOut"+self.dictLabel][il]
            l.isCleaning        = event.leptonJetRet["LepGood_isCleaningOut"+self.dictLabel][il]
            l.isCleaningVeto    = event.leptonJetRet["LepGood_isCleaningVetoOut"+self.dictLabel][il]
            l.isFake            = event.leptonJetRet["LepGood_isFOOut"+self.dictLabel][il]
            l.isFakeVeto        = event.leptonJetRet["LepGood_isFOVetoOut"+self.dictLabel][il]
            l.isTight           = event.leptonJetRet["LepGood_isTightOut"+self.dictLabel][il]
            l.isTightVeto       = event.leptonJetRet["LepGood_isTightVetoOut"+self.dictLabel][il]
        
        for jecStr in self.jecStrs:
            setattr(event,"nJetSel"+jecStr,event.leptonJetRet["nJetSel"+self.dictLabel+jecStr])
            setattr(event,"nDiscJetSel"+jecStr,event.leptonJetRet["nDiscJetSel"+self.dictLabel+jecStr])
            setattr(event,"nBJetLooseRA540"+jecStr,event.leptonJetRet["nBJetLoose40"+self.dictLabel+jecStr])
            setattr(event,"nBJetMediumRA540"+jecStr,event.leptonJetRet["nBJetMedium40"+self.dictLabel+jecStr])
            setattr(event,"nBJetLooseRA525"+jecStr,event.leptonJetRet["nBJetLoose25"+self.dictLabel+jecStr])
            setattr(event,"nBJetMediumRA525"+jecStr,event.leptonJetRet["nBJetMedium25"+self.dictLabel+jecStr])  
            setattr(event,"nJetRA540"+jecStr,event.leptonJetRet["nJet40"+self.dictLabel+jecStr])  
            setattr(event,"nJetRA525"+jecStr,event.leptonJetRet["nJet25"+self.dictLabel+jecStr])  
            setattr(event,"htJet40"+jecStr,event.leptonJetRet["htJet40j"+self.dictLabel+jecStr])  
            setattr(event,"htJet25"+jecStr,event.leptonJetRet["htJet25j"+self.dictLabel+jecStr])  
            setattr(event,"mhtJet40"+jecStr,event.leptonJetRet["mhtJet40"+self.dictLabel+jecStr])  
            setattr(event,"mhtJet25"+jecStr,event.leptonJetRet["mhtJet25"+self.dictLabel+jecStr])            
        
        event.JetSelIndex = event.leptonJetRet["iJSel"+self.dictLabel]

        if event.leptonJetRet["nJet40"+self.dictLabel] < 2 and event.leptonJetRet["nJet40"+self.dictLabel+"_jecUp"] < 2 and event.leptonJetRet["nJet40"+self.dictLabel+"_jecDown"] < 2: return False
        if len([l for l in event.selectedLeptons if l.isTight]) < 1: return False

        return True
