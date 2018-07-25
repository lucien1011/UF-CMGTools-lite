from CMGTools.RA5.Dataset.UFComponentCreator import *

k = UFComponentCreator()

T1tbs_1000 = k.makeMCComponentFromUF(
        "SMS-T1tbs_mGluino1000",
        "/SMS-T1tbs_mGluino1000",
        "/cms/data/store/user/klo/RA5/T1tbs_Moriond17_MINIAODSIM/v1/SMS-T1tbs_mGluino1000_GEN-SIM/PUMoriond17-Realistic50ns13TeVCollision-80X_mc2015_realistic_v1-MINIAODSIM/180719_080357/0000/",
        xSec = 0.0243547,
        )

T1tbs_1500 = k.makeMCComponentFromUF(
        "SMS-T1tbs_mGluino1500",
        "/SMS-T1tbs_mGluino1500",
        "/cms/data/store/user/klo/RA5/T1tbs_Moriond17_MINIAODSIM/v1/SMS-T1tbs_mGluino1500_GEN-SIM/PUMoriond17-Realistic50ns13TeVCollision-80X_mc2015_realistic_v1-MINIAODSIM/180719_080022/0000/",
        xSec = 0.000394612,
        )

samples = [
        T1tbs_1000,
        T1tbs_1500,
        ]

for comp in samples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 10
