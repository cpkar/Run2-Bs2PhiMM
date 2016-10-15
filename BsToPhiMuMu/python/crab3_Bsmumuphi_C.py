from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_("General")
config.General.requestName = 'Bsmumuphi_2016C'
config.General.workArea = 'crab_projects_Bsmumuphi_2016C'
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/j/jmejiagu/public/data2015_RunII/new_compaskym/Bsmumuphi/CMSSW_8_1_0_pre9/src/Bphysics/BsToPhiMuMu/python/bstophimumu_Run2016.py'

config.section_("Data")
#config.Data.inputDataset = '/Charmonium/Run2016B-PromptReco-v2/AOD'
config.Data.inputDataset = '/Charmonium/Run2016C-PromptReco-v2/AOD'
#config.Data.inputDataset = '/Charmonium/Run2016D-PromptReco-v2/AOD'

config.Data.inputDBS =	'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt'
#config.Data.lumiMask = 'Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON_MuonPhys.txt'
#config.Data.runRange = 
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'CRAB3_Bsmumuphi_2016C'
config.Data.outLFNDirBase = '/store/user/'+getUsernameFromSiteDB()+'/Bsmumuphi_2016C/'

config.section_("Site")
#config.Site.storageSite = 'T3_MX_Cinvestav'
config.Site.storageSite = 'T2_CH_CERN'


