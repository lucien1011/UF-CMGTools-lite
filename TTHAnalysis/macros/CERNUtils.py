import subprocess

def isRootFile(fileName):
    return fileName.endswith(".root")

def listdir_psi(path,selection=isRootFile):
    cmd = ["gfal-ls", path]
    output = subprocess.Popen(cmd,stdout=subprocess.PIPE).communicate()[0]
    return [l for l in output.split('\n') if selection(l)]
