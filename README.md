# Run2-Bs2PhiMM
Run2 Bs --> Phi(KK) mu+ mu- analysis

# How to build:
-------------
$ cmsrel CMSSW_8_0_24

$ cd CMSSW_8_0_24/src/

$ cmsenv

$ scram b

$ mkdir BpHaNa

$ cd BpHaNa

$ git clone https://github.com/nsahoo/Run2-Bs2PhiMM.git

$ cd ../

$ scram b 


# How to run:
-----------
$ cd Run2-Bs2PhiMM/BsToPhiMuMu/python/

for data, do

$ cmsRun bstophimumu_Run2016.py

for mc, do

$ cmsRun bstophimumu_2016_mc.py


If you have any queries, please write to nsahoo@cern.ch
