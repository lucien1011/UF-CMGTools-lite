#!/bin/bash

#heppy TEST_01 run_BkgMC2016_cfg.py -N 1000 -f
#heppy TEST_Sig run_PrivSignalMC2016_cfg.py -N 1000 -f
#heppy TEST_Data run_Data2016_cfg.py -N 1000 -f -o test=1
#heppy SyncMC2016v5 run_BkgMC2016_cfg.py -f -o test="ra5-sync-mc"
#heppy TEST2016 run_BkgMC2016_cfg.py -f -o test="ra5-sync-mc" -N 100
#heppy TEST_DataV2 Datav2_2016_cfg.py -N 1000 -f -o test=1
heppy TEST_DataV2 Datav2_Run2016H_cfg.py -N 100 -f -o test=1
