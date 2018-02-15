import operator 
import itertools
import copy

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
from PhysicsTools.HeppyCore.utils.deltar import *
import PhysicsTools.HeppyCore.framework.config as cfg

class RPVEventSelector( Analyzer ):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(RPVEventSelector,self).__init__(cfg_ana,cfg_comp,looperName)

    def declareHandles(self):
        super(RPVEventSelector, self).declareHandles()

    def beginLoop(self, setup):
        super(RPVEventSelector,self).beginLoop( setup )

    def process(self, event):
        self.readCollections( event.input )
        nSelectedMuons = len(event.selectedMuons)
        return nSelectedMuons == 2


