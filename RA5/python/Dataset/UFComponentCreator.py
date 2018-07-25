import PhysicsTools.HeppyCore.framework.config as cfg
from CMGTools.Production import eostools
from CMGTools.Production.dataset import createDataset, createMyDataset
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
from CMGTools.Production.dataset import getDatasetFromCache, writeDatasetToCache
import re,subprocess,os

uf_xrootd_prefix = "root://cmsio5.rc.ufl.edu//"

def list_gsiftp(path):
    prefix = "gsiftp://cmsio.rc.ufl.edu//"
    cmd = ["gfal-ls", prefix+path]
    output = subprocess.Popen(cmd,stdout=subprocess.PIPE).communicate()[0].split("\n")
    return output

class UFComponentCreator(ComponentCreator):
    def getFilesFromUF(self,name,dataset,path,pattern=".*root"):
        if "%" in path: path = path % dataset;
        try:
            files = getDatasetFromCache('UF%{path}%{pattern}.pck'.format(path = path.replace('/','_'), pattern = pattern))
        except IOError:
            files = [ uf_xrootd_prefix+path.replace("/cms/data","")+x for x in list_gsiftp(path) if re.match(pattern,x) ] 
            #files = [ 'gsiftp://cmsio.rc.ufl.edu//'+path+x for x in list_gsiftp(path)] 
            if len(files) == 0:
                raise RuntimeError, "ERROR making component %s: no files found under %s matching '%s'" % (name,path,pattern)
            writeDatasetToCache('UF%{path}%{pattern}.pck'.format(path = path.replace('/','_'), pattern = pattern), files)
        return files

    def makeMCComponentFromUF(self,name,dataset,path,pattern=".*root",xSec=1):
        component = cfg.MCComponent(
            dataset=dataset,
            name = name,
            files = self.getFilesFromUF(name,dataset,path,pattern),
            xSection = xSec,
            nGenEvents = 1,
            triggers = [],
            effCorrFactor = 1,
        )
        return component

