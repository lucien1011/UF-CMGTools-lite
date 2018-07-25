from CMGTools.RA5.Dataset.UFComponentCreator import *

k = UFComponentCreator()

T1qqqqL_1000 = k.makeMCComponentFromUF(
        "SMS-T1qqqqL_mGluino1000",
        "/SMS-T1qqqqL_mGluino1000",
        "/cms/data/store/user/klo/RA5/T1qqqqL_Moriond17_MINIAODSIM/v1/SMS-T1qqqqL_mGluino1000_GEN-SIM/PUMoriond17-Realistic50ns13TeVCollision-80X_mc2015_realistic_v1-MINIAODSIM/180719_113742/0000/",
        xSec = 0.0243547,
        )

T1qqqqL_1500 = k.makeMCComponentFromUF(
        "SMS-T1qqqqL_mGluino1500",
        "/SMS-T1qqqqL_mGluino1500",
        "/cms/data/store/user/klo/RA5/T1qqqqL_Moriond17_MINIAODSIM/v1/SMS-T1qqqqL_mGluino1500_GEN-SIM/PUMoriond17-Realistic50ns13TeVCollision-80X_mc2015_realistic_v1-MINIAODSIM/180719_113805/0000/",
        xSec = 0.000394612,
        )

samples = [
        T1qqqqL_1000,
        T1qqqqL_1500,
        ]

for comp in samples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 10
