#!/bin/env python
from PhysicsTools.Heppy.analyzers.core.autovars import *
from PhysicsTools.Heppy.analyzers.objects.autophobj import *

##------------------------------------------  
## GEN PHOTON
##------------------------------------------  

slimGenPhotonType = NTupleObjectType("genPhoton", baseObjectTypes = [ fourVectorType ], mcOnly=True, variables = [
    NTupleVariable("drMinParton", lambda x : getattr(x,'drMinParton',-99.), float, help="Delta R between photon and hard partons"),
    NTupleVariable("isPrompt",    lambda x : getattr(x,'isPrompt',-99.),    float, help="Prompt photon flag"),
])


##------------------------------------------  
## GEN PARTICLE WITH LINKS
##------------------------------------------  

slimGenParticleWithLinksType = NTupleObjectType("genParticleWithLinks", baseObjectTypes = [ particleType ], mcOnly=True, variables = [
    NTupleVariable("charge",   lambda x : x.threeCharge()/3.0,                       float),
    NTupleVariable("motherId", lambda x : x.mother(0).pdgId() if x.mother(0) else 0, int, help="pdgId of the mother of the particle"),
    NTupleVariable("motherIndex", lambda x : x.motherIndex, int, help="index of the mother in the generatorSummary"),
    NTupleVariable("status",   lambda x : x.status(),                                int),
])


##------------------------------------------  
## PHOTON
##------------------------------------------  

slimPhotonType = NTupleObjectType("slimGamma", baseObjectTypes = [ fourVectorType ], variables = [
    #NTupleVariable("drMinParton",   lambda x : getattr(x, 'drMinParton', -1.0),              float, mcOnly=True, help="deltaR min between photon and parton"),
    NTupleVariable("sigmaIetaIeta", lambda x : x.full5x5_sigmaIetaIeta(),                                 float, help="sigmaIetaIeta for photons"),
#    NTupleVariable("chHadIso", lambda x : x.chargedHadronIso('rhoArea'), float, help="chargedHadronIsolation for photons with footprint removal and pile-up correction"),
#    NTupleVariable("phIso", lambda x : x.photonIso('rhoArea'), float, help="gammaIsolation for photons with footprint removal and pile-up correction"),
#    NTupleVariable("neuHadIso", lambda x : x.neutralHadronIso('rhoArea'), float, help="neutralHadronIsolation for photons with footprint removal and pile-up correction"),
    NTupleVariable("chHadIso",      lambda x : x.chargedHadronIso(),                                      float, help="chargedHadronIsolation for photons with footprint removal"),
    NTupleVariable("phIso",         lambda x : x.photonIso(),                                             float, help="gammaIsolation for photons with footprint removal"),
    NTupleVariable("neuHadIso",     lambda x : x.neutralHadronIso(),                                      float, help="neutralHadronIsolation for photons with footprint removal"),
    NTupleVariable("relIso",        lambda x : x.ftprRelIso03 if hasattr(x,'ftprRelIso03') else x.relIso, float, help="relativeIsolation for photons with footprint removal and pile-up correction"),
    NTupleVariable("mcMatchId",     lambda x : getattr(x, 'mcMatchId', -99),                   int, mcOnly=True, help="Match to source from hard scatter (pdgId of heaviest particle in chain, 25 for H, 6 for t, 23/24 for W/Z), zero if non-prompt or fake"),
    #NTupleVariable("isPrompt",      lambda x : x.isPrompt if hasattr(x,"isPrompt") else 0,     int, mcOnly=True, help="flag for prompt photons"),
])


##------------------------------------------  
## LEPTON
##------------------------------------------  

slimLeptonType = NTupleObjectType("slimLepton", baseObjectTypes = [ fourVectorType ], variables = [
    NTupleVariable("charge",     lambda x : x.charge(),  int),
    # Identification
    NTupleVariable("tightId",    lambda x : x.tightId(), int,                                   help="POG Tight ID (for electrons it's configured in the analyzer)"),
    # Isolations with the two radia
    NTupleVariable("relIso03",   lambda x : x.relIso03,                                         help="PF Rel Iso, R=0.3, pile-up corrected"),
    NTupleVariable("relIso04",   lambda x : x.relIso04,                                         help="PF Rel Iso, R=0.4, pile-up corrected"),
    NTupleVariable("miniRelIso", lambda x : x.miniRelIso if hasattr(x,'miniRelIso') else  -999, help="PF Rel miniRel, pile-up corrected"),
])


##------------------------------------------  
## JET
##------------------------------------------  

slimJetType = NTupleObjectType("slimJet", baseObjectTypes = [fourVectorType], variables = [
    #NTupleVariable("newId",         lambda x : x.jetID("POG_PFID_13TeV") ,        int, mcOnly=False, help="POG Loose jet ID for 13 TeV"),  
    NTupleVariable("puId",          lambda x : getattr(x, 'puJetIdPassed', -99),  int, mcOnly=False, help="puId (full MVA, loose WP, 5.3.X training on AK5PFchs: the only thing that is available now)"),
    NTupleVariable("btagCSV",       lambda x : x.btag('pfCombinedInclusiveSecondaryVertexV2BJetTags'), help="CSV-IVF v2 discriminator"),
    NTupleVariable("rawPt",         lambda x : x.pt() * x.rawFactor(), help="p_{T} before JEC"),
    NTupleVariable("mcPt",          lambda x : x.mcJet.pt() if getattr(x,"mcJet",None) else 0., mcOnly=True, help="p_{T} of associated gen jet"),
    NTupleVariable("partonFlavour", lambda x : x.partonFlavour(),                 int, mcOnly=True, help="purely parton-based flavour"),
    NTupleVariable("hadronFlavour", lambda x : x.hadronFlavour(),                 int, mcOnly=True, help="hadron flavour (ghost matching to B/C hadrons)"),
    NTupleVariable("corr_JECUp",    lambda x : getattr(x, 'corrJECUp', -99),    float, help=""),
    NTupleVariable("corr_JECDown",  lambda x : getattr(x, 'corrJECDown', -99),  float, help=""),
    NTupleVariable("corr",          lambda x : getattr(x, 'corr', -99),         float, help=""),
    NTupleVariable("chHEF",         lambda x : x.chargedHadronEnergyFraction(), float, mcOnly = False, help="chargedHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("neHEF",         lambda x : x.neutralHadronEnergyFraction(), float, mcOnly = False, help="neutralHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("phEF",          lambda x : x.photonEnergyFraction(),        float, mcOnly = False, help="photonEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("eEF",           lambda x : x.electronEnergyFraction(),      float, mcOnly = False, help="electronEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("muEF",          lambda x : x.muonEnergyFraction(),          float, mcOnly = False, help="muonEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("HFHEF",         lambda x : x.HFHadronEnergyFraction(),      float, mcOnly = False, help="HFHadronEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("HFEMEF",        lambda x : x.HFEMEnergyFraction(),          float, mcOnly = False, help="HFEMEnergyFraction (relative to corrected jet energy)"),
    #NTupleVariable('btagDeepCSVProbUdsg', lambda x : x.bDiscriminator('pfDeepCSVJetTags:probudsg'), float, help="DeepFlavour probudsg flag"),
    #NTupleVariable('btagDeepCSVProbB'   , lambda x : x.bDiscriminator('pfDeepCSVJetTags:probb'   ), float, help="DeepFlavour probb flag"),
    #NTupleVariable('btagDeepCSVProbC'   , lambda x : x.bDiscriminator('pfDeepCSVJetTags:probc'   ), float, help="DeepFlavour probc flag"),
    #NTupleVariable('btagDeepCSVProbBb'  , lambda x : x.bDiscriminator('pfDeepCSVJetTags:probbb'  ), float, help="DeepFlavour probbb flag"),
    #NTupleVariable('btagDeepCSVProbCc'  , lambda x : x.bDiscriminator('pfDeepCSVJetTags:probcc'  ), float, help="DeepFlavour probcc flag"),
])


slimJetFwdType = NTupleObjectType("slimJetFwd", baseObjectTypes = [fourVectorType], variables = [
    NTupleVariable("chHEF",        lambda x : x.chargedHadronEnergyFraction(), float, mcOnly = False, help="chargedHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("phEF",         lambda x : x.photonEnergyFraction(),        float, mcOnly = False,help="photonEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("eEF",          lambda x : x.electronEnergyFraction(),      float, mcOnly = False,help="electronEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("muEF",         lambda x : x.muonEnergyFraction(),          float, mcOnly = False,help="muonEnergyFraction (relative to corrected jet energy)"),
])


##------------------------------------------  
## MET
##------------------------------------------  
  
slimMetType = NTupleObjectType("slimMet", baseObjectTypes = [ twoVectorType ], variables = [
    NTupleVariable("genPt",  lambda x : x.genMET().pt()  if x.genMET() else 0, mcOnly=True ),
    NTupleVariable("genPhi", lambda x : x.genMET().phi() if x.genMET() else 0, mcOnly=True ),
    NTupleVariable("genEta", lambda x : x.genMET().eta() if x.genMET() else 0, mcOnly=True ),
])


##------------------------------------------  
## FAT JETS
##------------------------------------------  
slimFatJetType = NTupleObjectType("fatJet",  baseObjectTypes = [ fourVectorType ], variables = [
    NTupleVariable("softDropMass", lambda x : x.userFloat("ak8PFJetsCHSSoftDropMass"), float, help="soft-drop mass"),
    NTupleVariable("prunedMass",  lambda x : x.userFloat("ak8PFJetsCHSPrunedMass"),  float, help="pruned mass"),
    NTupleVariable("tau1",         lambda x : x.userFloat("NjettinessAK8:tau1"),       float, help="1-subjettiness"),
    NTupleVariable("tau2",         lambda x : x.userFloat("NjettinessAK8:tau2"),       float, help="2-subjettiness"),
    NTupleVariable("tau3",         lambda x : x.userFloat("NjettinessAK8:tau3"),       float, help="3-subjettiness"),
    NTupleVariable("nSubJets", lambda x : x.nSubJets, help="no. subjets per AK8 jet"),
])

slimSubJetType = NTupleObjectType("subJet", baseObjectTypes = [ fourVectorType ], variables = [
    NTupleVariable("btagCSV", lambda x : x.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"), float, help="sub-jet b-tag"),
    NTupleVariable("hadronFlavour", lambda x : x.hadronFlavour(), int,     mcOnly=True, help="hadron flavour (ghost matching to B/C hadrons)"),
])
