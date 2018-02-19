# Short recipe for CMGTools 

For the general recipe, [follow these instructions](https://twiki.cern.ch/twiki/bin/view/CMS/CMGToolsReleasesExperimental).

--------------

#### Set up CMSSW and the base git

```
cmsrel CMSSW_8_0_25
cd CMSSW_8_0_25/src
cmsenv
git cms-init
```

#### Add the central cmg-cmssw repository to get the Heppy 80X branch

```
git remote add UF-Heppy git@github.com:lucien1011/UF-Heppy.git -f -t heppy_80X_RPV
```

#### Configure the sparse checkout, and get the base heppy packages

```
cp /afs/cern.ch/user/c/cmgtools/public/sparse-checkout_80X_heppy .git/info/sparse-checkout
git checkout -b heppy_80X_RPV UF-Heppy/heppy_80X_RPV
```

#### Now get the CMGTools subsystem from the cmgtools-lite repository

```
git clone -o UF-CMGTools-lite git@github.com:lucien1011/UF-CMGTools-lite.git -b heppy_80X_RPV CMGTools
cd CMGTools
```

#### Add your fork, and push the 80X branch to it (optional)

```
git remote add origin  git@github.com:YOUR_GITHUB_REPOSITORY/cmgtools-lite.git
git push -u origin heppy_80X_RPV
```

#### Compile

```
cd $CMSSW_BASE/src
scram b -j 8
```

#### To produce ntuples

```
cd $CMSSW_BASE/CMGTools/RPV/cfg/
heppy TEST_01 run_RPV_cfg.py -N 100 -o test=1 # To run over 100 events for testing purpose
```
