from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.leptonJetReCleaner import bestZ1TL,minMllTL,passMllVeto
from ROOT import TFile,TH1F
import os

from CMGTools.TTHAnalysis.tools.functionsTTH import _ttH_idEmu_cuts_E2_obj,_soft_MuonId_2016ICHEP,_medium_MuonId_2016ICHEP
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import jetLepAwareJEC,ptRelv2

def _susy2lss_lepId_CBloose(lep):
        if abs(lep.pdgId()) == 13:
            if lep.pt() <= 5: return False
            return True #lep.mediumMuonId > 0
        elif abs(lep.pdgId()) == 11:
            if lep.pt() <= 7: return False
            if not (lep.passConversionVeto() and lep.gsfTrack().hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS) <= 1): 
                return False
            if not lep.mvaRun2("NonTrigSpring15MiniAOD") > -0.70+(-0.83+0.70)*(abs(lep.superCluster().eta())>0.8)+(-0.92+0.83)*(abs(lep.superCluster().eta())>1.479):
                return False
            if not _susy2lss_idEmu_cuts(lep): return False
            return True
        return False

def _susy2lss_lepConePt1015(lep):
    if lep.conept <= (10 if abs(lep.pdgId())==13 else 15): return False
    return True

def _susy2lss_lepId_loosestFO(lep):
    if not _susy2lss_lepId_CBloose(lep): return False
    if abs(lep.pdgId()) == 13:
        return _medium_MuonId_2016ICHEP(lep) > 0 and 2*(lep.innerTrack().ptError()/lep.innerTrack().pt() < 0.2) > 0
    elif abs(lep.pdgId()) == 11:
        return (lep.passConversionVeto() and lep.isGsfCtfScPixChargeConsistent()+lep.isGsfScPixChargeConsistent() > 1 and lep.gsfTrack().hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS) == 0)
    return False

def _susy2lss_lepId_tighterFO(lep):
    if not _susy2lss_lepId_loosestFO(lep): return False
    if abs(lep.pdgId())==11:
        if not lep.mvaRun2("NonTrigSpring15MiniAOD") > -0.155+(-0.56+0.155)*(abs(lep.superCluster().eta())>0.8)+(-0.76+0.56)*(abs(lep.superCluster().eta())>1.479):
            return False
        if not _susy2lss_idIsoEmu_cuts(lep): return False
    return True

def _susy2lss_lepId_inSituLoosestFO(lep):
    if not _susy2lss_lepId_loosestFO(lep): return False
    if abs(lep.pdgId)==11:
        if not lep.mvaIdSpring15 > -0.363+(-0.579+0.363)*(abs(lep.etaSc)>0.8)+(-0.623+0.579)*(abs(lep.etaSc)>1.479):
            return False
    return True

def _susy2lss_lepId_inSituTighterFO(lep):
    if not _susy2lss_lepId_loosestFO(lep): return False
    if abs(lep.pdgId)==11:
        if not lep.mvaIdSpring15 > 0.051+(-0.261-0.051)*(abs(lep.etaSc)>0.8)+(-0.403+0.261)*(abs(lep.etaSc)>1.479):
            return False
        if not _susy2lss_idIsoEmu_cuts(lep): return False
    return True

def _susy2lss_lepId_IPcuts(lep):
    if not lep.sip3D()<4: return False
    if not (abs(lep.dxy())<0.05): return False
    if not (abs(lep.dz())<0.1): return False
    return True

def _susy2lss_lepId_CB(lep):
    if not _susy2lss_lepId_CBloose(lep): return False
    if not _susy2lss_lepId_IPcuts(lep): return False
    if abs(lep.pdgId()) == 13:

        return _medium_MuonId_2016ICHEP(lep) > 0 and 2*(lep.innerTrack().ptError()/lep.innerTrack().pt() < 0.2) > 0
    elif abs(lep.pdgId()) == 11:
        if not (lep.passConversionVeto() and lep.isGsfCtfScPixChargeConsistent()+lep.isGsfScPixChargeConsistent() > 1 and lep.gsfTrack().hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS) == 0):
            return False
        return lep.mvaRun2("NonTrigSpring15MiniAOD") > 0.87+(0.60-0.87)*(abs(lep.superCluster().eta())>0.8)+(0.17-0.60)*(abs(lep.superCluster().eta())>1.479)
    return False

def _susy2lss_idEmu_cuts(lep):
    if (abs(lep.pdgId())!=11): return True
    if (lep.full5x5_sigmaIetaIeta()>=(0.011 if abs(lep.superCluster().eta())<1.479 else 0.031)): return False
    if (lep.hadronicOverEm()>=0.08): return False
    if (abs(lep.deltaEtaSuperClusterTrackAtVtx())>=0.01): return False
    if (abs(lep.deltaPhiSuperClusterTrackAtVtx())>=(0.04 if abs(lep.superCluster().eta())<1.479 else 0.08)): return False
    tempVar = abs((1.0/lep.ecalEnergy() - lep.eSuperClusterOverP()/lep.ecalEnergy()) if lep.ecalEnergy()>0. else 9e9)
    if (tempVar>=0.01): return False
    return True

def _susy2lss_idEmu_cuts_obj(lep):
    if (abs(lep.pdgId())!=11): return True
    if (lep.full5x5_sigmaIetaIeta()>=(0.011 if abs(lep.superCluster().eta())<1.479 else 0.031)): return False
    if (lep.hadronicOverEm()>=0.08): return False
    if (abs(lep.deltaEtaSuperClusterTrackAtVtx())>=0.01): return False
    if (abs(lep.deltaPhiSuperClusterTrackAtVtx())>=(0.04 if abs(lep.superCluster().eta())<1.479 else 0.08)): return False
    if (abs((1.0/lep.ecalEnergy() - lep.eSuperClusterOverP()/lep.ecalEnergy()) if lep.ecalEnergy()>0. else 9e9)>=0.01): return False
    return True

def _susy2lss_idIsoEmu_cuts(lep):
    if (abs(lep.pdgId())!=11): return True
    if not _susy2lss_idEmu_cuts(lep): return False
    if (lep.ecalPFClusterIso()>=0.45*lep.pt()): return False
    if (lep.hcalPFClusterIso()>=0.25*lep.pt()): return False
    if (lep.dr03TkSumPt()>=0.2*lep.pt()): return False
    return True

def _susy2lss_idIsoEmu_cuts_obj(lep):
    if (abs(lep.pdgId())!=11): return True
    if not _susy2lss_idEmu_cuts_obj(lep): return False
    if (lep.ecalPFClusterIso()>=0.45*lep.pt()): return False
    if (lep.hcalPFClusterIso()>=0.25*lep.pt()): return False
    if (lep.dr03TkSumPt()>=0.2*lep.pt()): return False
    return True
    
def _susy2lss_multiIso(lep):
        if abs(lep.pdgId()) == 13: A,B,C = (0.16,0.76,7.2)
        else:                    A,B,C = (0.12,0.80,7.2)
        jetPtRatiov2 = lep.pt()/jetLepAwareJEC(lep).Pt() if hasattr(lep,'jet') else -1
        jetPtRelv2 = ptRelv2(lep) if hasattr(lep,'jet') else -1
        return lep.miniRelIso < A and (jetPtRatiov2 > B or jetPtRelv2 > C)

def _susy2lss_multiIso_relaxedForInSituApp(lep):
        if abs(lep.pdgId) == 13: A,B,C = (0.4,0.76,7.2)
        else:                    A,B,C = (0.4,0.80,7.2)
        return lep.miniRelIso < A and (1/lep.jetPtRatiov2 < (1/B + lep.miniRelIso) or ptRelv2(lep) if hasattr(lep,'jet') else -1 > C)

def conept_RA5(lep):
    if (abs(lep.pdgId())!=11 and abs(lep.pdgId())!=13):
        return lep.pt()
    A = 0.12 if (abs(lep.pdgId())==11) else 0.16
    B = 0.80 if (abs(lep.pdgId())==11) else 0.76
    C = 7.2 if (abs(lep.pdgId())==11) else 7.2
    jetPtRatiov2 = lep.pt()/jetLepAwareJEC(lep).Pt() if hasattr(lep,'jet') else -1
    jetPtRelv2 = ptRelv2(lep) if hasattr(lep,'jet') else -1
    if (jetPtRelv2>C):
        return lep.pt()*(1+max(lep.miniRelIso-A,0))
    else:
        return max(lep.pt(),lep.pt()/jetPtRatiov2*B)

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    tree.vectorTree = True
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf1 = LeptonChoiceRA5("Old", 
                lambda lep : lep.relIso03 < 0.5, 
                lambda lep : lep.relIso03 < 0.1 and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4))
            self.sf2 = LeptonChoiceRA5("PtRel", 
                lambda lep : lep.relIso03 < 0.4 or lep.jetPtRel > 5, 
                lambda lep : (lep.relIso03 < 0.1 or lep.jetPtRel > 14) and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4))
            self.sf3 = LeptonChoiceRA5("MiniIso", 
                lambda lep : lep.miniRelIso < 0.4, 
                lambda lep : lep.miniRelIso < 0.05 and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4))
            self.sf4 = LeptonChoiceRA5("PtRelJC", 
                lambda lep : lep.relIso03 < 0.4 or lep.jetPtRel > 5, 
                lambda lep : (lep.relIso03 < 0.1 or lep.jetPtRel > 14) and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4 and not (lep.jetPtRel > 5 and lep.pt*(1/lep.jetPtRatio-1) > 25)))
            self.sf5 = LeptonChoiceRA5("MiniIsoJC", 
                lambda lep : lep.miniRelIso < 0.4, 
                lambda lep : lep.miniRelIso < 0.05 and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4 and not (lep.jetDR > 0.5*10/min(50,max(lep.pt,200)) and lep.pt*(1/lep.jetPtRatio-1) > 25)))
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf1(ev)
            print self.sf2(ev)
            print self.sf3(ev)
            print self.sf4(ev)
            print self.sf5(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

        
