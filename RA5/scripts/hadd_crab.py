import os,ROOT,argparse

# ____________________________________________________________________ ||
lucien_t2_area = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
printInputFiles = False
outputFileName = "treeProducerSusyRA5.root"
selectionStr = outputFileName.replace(".root","")

parser = argparse.ArgumentParser()
parser.add_argument("--inputDir",action="store")
parser.add_argument("--outputDir",action="store",default=lucien_t2_area)

# ____________________________________________________________________ ||
def list_rootfiles(inputDir,selection=lambda x: True):
    rootfiles = []
    timeFolderNames = [ time_folder for time_folder in os.listdir(inputDir) if os.path.isdir(os.path.join(inputDir,time_folder)) ]
    for time_folder in timeFolderNames:
        blockFolderNames = [ block_folder for block_folder in os.listdir(os.path.join(inputDir,time_folder)) if os.path.isdir(os.path.join(inputDir,time_folder,block_folder)) ]
        for block_folder in blockFolderNames:
            filePaths = [ os.path.join(inputDir,time_folder,block_folder,n) for n in os.listdir(os.path.join(inputDir,time_folder,block_folder)) if selection(n) ]
            rootfiles.extend(filePaths)
    return rootfiles

# ____________________________________________________________________ ||
option = parser.parse_args()

# ____________________________________________________________________ ||
sampleFolderNames = [ n for n in os.listdir(option.inputDir) if os.path.isdir(os.path.join(option.inputDir,n)) ]
for sampleFolderName in sampleFolderNames:
    outputfolderPath = os.path.join(option.outputDir,sampleFolderName)
    inputfolderPath = os.path.join(option.inputDir,sampleFolderName)
    if not os.path.exists(outputfolderPath):
        os.makedirs(outputfolderPath)
    inputRootFiles = list_rootfiles(inputfolderPath,selection=lambda x: selectionStr in x)
    inputRootFiles.sort()
    print "-"*20
    print "Input folder: "+inputfolderPath
    print "Output folder: "+outputfolderPath
    if printInputFiles: print "Sample "+sampleFolderName+", going to hadd the following files: "+", ".join(inputRootFiles)
    cmd = 'hadd -f '+os.path.join(outputfolderPath,outputFileName)+' '+" ".join(inputRootFiles)
    os.system(cmd)
