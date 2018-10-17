import PhysicsTools.HeppyCore.framework.config as cfg
import os

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

TTWW = kreator.makeMCComponent("TTWW", "/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM", "CMS", ".*root", 7.83e-3)

samples = [
            TTWW,
        ]

for comp in samples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 10
