import os
import PhysicsTools.HeppyCore.framework.config as cfg

##__________________________________________________________________||
import logging
# levels: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.basicConfig( level = logging.WARNING )

##__________________________________________________________________||
import CMGTools.RPV.components.components_RPV as cmps

componentList = [ ]
componentList.append(cmps.SMS_RPV_madgraphMLM)

##__________________________________________________________________||
from CMGTools.RPV.components.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

components = [kreator.makeMCComponent(**s) for s in componentList]
for comp in components:
    # comp.files = comp.files[1:3] # for batch submission test
    comp.splitFactor = len(comp.files)

##__________________________________________________________________||
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
test = getHeppyOption('test')
if test == "1" :
    components = [kreator.makeMCComponent(**s) for s in componentList]
    for comp in components:
        comp.files = comp.files[0:1]
        print comp.files
        comp.splitFactor = len(comp.files)
else: # for production
    components = [kreator.makeMCComponent(**s) for s in componentList]
    for comp in components:
        # comp.files = comp.files[1:3] # for batch submission test
        comp.splitFactor = min(len(comp.files), 1000)

##__________________________________________________________________||
from CMGTools.RPV.sequence import *
sequence = cfg.Sequence(sequence)

##__________________________________________________________________||
preprocessor = None

##__________________________________________________________________||
from CMGTools.RPV.framework.AtEvents import AtEvents
config = cfg.Config(components = components,
                    sequence = sequence,
                    preprocessor = preprocessor,
                    services = [],
                    events_class = AtEvents)

