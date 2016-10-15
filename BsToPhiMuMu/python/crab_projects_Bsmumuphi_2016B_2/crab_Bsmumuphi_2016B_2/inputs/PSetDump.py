import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuple")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2016B/Charmonium/AOD/PromptReco-v2/000/273/158/00000/14E579B3-271A-E611-911E-02163E013584.root')
)
process.AODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoTracks_GsfGlobalElectronTest_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep recoPhotonCores_gedPhotonCore_*_*', 
        'keep recoPhotons_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'drop *_gedPhotons_valMapPFEgammaCandToPhoton_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'drop *_pfElectronTranslator_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep recoCaloClusters_pfElectronTranslator_*_*', 
        'keep recoPreshowerClusters_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_pfElectronTranslator_*_*', 
        'keep recoCaloClusters_pfPhotonTranslator_*_*', 
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*', 
        'keep recoSuperClusters_pfPhotonTranslator_*_*', 
        'keep recoPhotons_pfPhotonTranslator_*_*', 
        'keep recoPhotonCores_pfPhotonTranslator_*_*', 
        'keep recoConversions_pfPhotonTranslator_*_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*' ) )
)

process.AODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoTracks_GsfGlobalElectronTest_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep recoPhotonCores_gedPhotonCore_*_*', 
        'keep recoPhotons_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'drop *_gedPhotons_valMapPFEgammaCandToPhoton_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'drop *_pfElectronTranslator_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep recoCaloClusters_pfElectronTranslator_*_*', 
        'keep recoPreshowerClusters_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_pfElectronTranslator_*_*', 
        'keep recoCaloClusters_pfPhotonTranslator_*_*', 
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*', 
        'keep recoSuperClusters_pfPhotonTranslator_*_*', 
        'keep recoPhotons_pfPhotonTranslator_*_*', 
        'keep recoPhotonCores_pfPhotonTranslator_*_*', 
        'keep recoConversions_pfPhotonTranslator_*_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*' ) )
)

process.BeamSpotAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.BeamSpotFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.BeamSpotRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.CommonEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_logErrorHarvester_*_*')
)

process.DATAMIXEREventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep CSCDetIdCSCALCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCALCTDigi_*', 
        'keep CSCDetIdCSCCLCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCCLCTDigi_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_muonCSCDigis_MuonCSCComparatorDigi_*', 
        'keep CSCDetIdCSCCorrelatedLCTDigiMuonDigiCollection_csctfDigis_*_*', 
        'keep CSCDetIdCSCCorrelatedLCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCCorrelatedLCTDigi_*', 
        'keep CSCDetIdCSCRPCDigiMuonDigiCollection_muonCSCDigis_MuonCSCRPCDigi_*', 
        'keep CSCDetIdCSCStripDigiMuonDigiCollection_muonCSCDigis_MuonCSCStripDigi_*', 
        'keep CSCDetIdCSCWireDigiMuonDigiCollection_muonCSCDigis_MuonCSCWireDigi_*', 
        'keep DTLayerIdDTDigiMuonDigiCollection_muonDTDigis_*_*', 
        'keep PixelDigiedmDetSetVector_siPixelDigis_*_*', 
        'keep SiStripDigiedmDetSetVector_siStripDigis_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_muonRPCDigis_*_*', 
        'keep HBHEDataFramesSorted_hcalDigis_*_*', 
        'keep HFDataFramesSorted_hcalDigis_*_*', 
        'keep HODataFramesSorted_hcalDigis_*_*', 
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_*_*', 
        'keep QIE11DataFrameHcalDataFrameContainer_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep CastorDataFramesSorted_castorDigis_*_*', 
        'keep EBDigiCollection_ecalDigis_*_*', 
        'keep EEDigiCollection_ecalDigis_*_*', 
        'keep ESDigiCollection_ecalPreshowerDigis_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.DQMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_MEtoEDMConverter_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.DigiToRawFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*')
)

process.EITopPAGEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*')
)

process.EvtScalersAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*')
)

process.EvtScalersRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*')
)

process.FASTPUEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_famosSimHits_*_*', 
        'keep *_MuonSimHits_*_*', 
        'drop *_famosSimHits_VertexTypes_*', 
        'keep *_generalTracksBeforeMixing_*_*', 
        'drop *_generalTracksBeforeMixing_MVAValues_*', 
        'drop *_generalTracksBeforeMixing_QualityMasks_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*')
)

process.FEVTDEBUGEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_simCscTriggerPrimitiveDigis_*_*', 
        'keep *_simDtTriggerPrimitiveDigis_*_*', 
        'keep *_simRpcTriggerDigis_*_*', 
        'keep *_simRctDigis_*_*', 
        'keep *_simCsctfDigis_*_*', 
        'keep *_simCsctfTrackDigis_*_*', 
        'keep *_simDttfDigis_*_*', 
        'keep *_simGctDigis_*_*', 
        'keep *_simCaloStage1Digis_*_*', 
        'keep *_simCaloStage1FinalDigis_*_*', 
        'keep *_simCaloStage2Layer1Digis_*_*', 
        'keep *_simCaloStage2Digis_*_*', 
        'keep *_simGmtDigis_*_*', 
        'keep *_simGtDigis_*_*', 
        'keep *_cscTriggerPrimitiveDigis_*_*', 
        'keep *_dtTriggerPrimitiveDigis_*_*', 
        'keep *_rpcTriggerDigis_*_*', 
        'keep *_rctDigis_*_*', 
        'keep *_csctfDigis_*_*', 
        'keep *_csctfTrackDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gctDigis_*_*', 
        'keep *_gmtDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_gtEvmDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep *_simSiPixelDigis_*_*', 
        'keep *_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_trackingParticleRecoTrackAsssociation_*_*', 
        'keep *_assoc2secStepTk_*_*', 
        'keep *_assoc2thStepTk_*_*', 
        'keep *_assoc2GsfTracks_*_*', 
        'keep *_assocOutInConversionTracks_*_*', 
        'keep *_assocInOutConversionTracks_*_*', 
        'keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*', 
        'keep *_simEcalDigis_*_*', 
        'keep *_simEcalPreshowerDigis_*_*', 
        'keep *_simEcalTriggerPrimitiveDigis_*_*', 
        'keep *_simHcalDigis_*_*', 
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*', 
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*', 
        'keep *_simHcalTriggerPrimitiveDigis_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTDEBUGHLTEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(10485760),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_simCscTriggerPrimitiveDigis_*_*', 
        'keep *_simDtTriggerPrimitiveDigis_*_*', 
        'keep *_simRpcTriggerDigis_*_*', 
        'keep *_simRctDigis_*_*', 
        'keep *_simCsctfDigis_*_*', 
        'keep *_simCsctfTrackDigis_*_*', 
        'keep *_simDttfDigis_*_*', 
        'keep *_simGctDigis_*_*', 
        'keep *_simCaloStage1Digis_*_*', 
        'keep *_simCaloStage1FinalDigis_*_*', 
        'keep *_simCaloStage2Layer1Digis_*_*', 
        'keep *_simCaloStage2Digis_*_*', 
        'keep *_simGmtDigis_*_*', 
        'keep *_simGtDigis_*_*', 
        'keep *_cscTriggerPrimitiveDigis_*_*', 
        'keep *_dtTriggerPrimitiveDigis_*_*', 
        'keep *_rpcTriggerDigis_*_*', 
        'keep *_rctDigis_*_*', 
        'keep *_csctfDigis_*_*', 
        'keep *_csctfTrackDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gctDigis_*_*', 
        'keep *_gmtDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_gtEvmDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep *_simSiPixelDigis_*_*', 
        'keep *_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_trackingParticleRecoTrackAsssociation_*_*', 
        'keep *_assoc2secStepTk_*_*', 
        'keep *_assoc2thStepTk_*_*', 
        'keep *_assoc2GsfTracks_*_*', 
        'keep *_assocOutInConversionTracks_*_*', 
        'keep *_assocInOutConversionTracks_*_*', 
        'keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*', 
        'keep *_simEcalDigis_*_*', 
        'keep *_simEcalPreshowerDigis_*_*', 
        'keep *_simEcalTriggerPrimitiveDigis_*_*', 
        'keep *_simHcalDigis_*_*', 
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*', 
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*', 
        'keep *_simHcalTriggerPrimitiveDigis_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*', 
        'keep *_*_MergedTrackTruth_*', 
        'keep *_*_StripDigiSimLink_*', 
        'keep *_*_PixelDigiSimLink_*', 
        'keep *_*_MuonCSCStripDigiSimLinks_*', 
        'keep *_*_MuonCSCWireDigiSimLinks_*', 
        'keep *_*_RPCDigiSimLink_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTHLTALLEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep *_*_*_HLT' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTSIMEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep *_tcdsDigis_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.GENRAWEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep recoGenMETs_*_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_logErrorHarvester_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.GeneratorInterfaceAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.GeneratorInterfaceLHE = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep *_externalLHEProducer_LHEScriptOutput_*')
)

process.GeneratorInterfaceRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.GeneratorInterfaceRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497),
    HFdepthOneParameterB = cms.vdouble(-4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209),
    HFdepthTwoParameterA = cms.vdouble(0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593),
    HFdepthTwoParameterB = cms.vdouble(-2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06)
)

process.HLTDEBUGEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'keep *_logErrorHarvester_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.HLTDebugFEVT = cms.PSet(
    outputCommands = cms.vstring( ('drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.HLTDebugRAW = cms.PSet(
    outputCommands = cms.vstring( ('drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) )
)

process.HLTriggerAOD = cms.PSet(
    outputCommands = cms.vstring('drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.HLTriggerRAW = cms.PSet(
    outputCommands = cms.vstring('drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.HLTriggerRECO = cms.PSet(
    outputCommands = cms.vstring('drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*')
)

process.IOMCRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_randomEngineStateProducer_*_*')
)

process.L1TriggerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiSummary_lumiProducer_*_*')
)

process.L1TriggerFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simCscTriggerPrimitiveDigis_*_*', 
        'keep *_simDtTriggerPrimitiveDigis_*_*', 
        'keep *_simRpcTriggerDigis_*_*', 
        'keep *_simRctDigis_*_*', 
        'keep *_simCsctfDigis_*_*', 
        'keep *_simCsctfTrackDigis_*_*', 
        'keep *_simDttfDigis_*_*', 
        'keep *_simGctDigis_*_*', 
        'keep *_simCaloStage1Digis_*_*', 
        'keep *_simCaloStage1FinalDigis_*_*', 
        'keep *_simCaloStage2Layer1Digis_*_*', 
        'keep *_simCaloStage2Digis_*_*', 
        'keep *_simGmtDigis_*_*', 
        'keep *_simGtDigis_*_*', 
        'keep *_cscTriggerPrimitiveDigis_*_*', 
        'keep *_dtTriggerPrimitiveDigis_*_*', 
        'keep *_rpcTriggerDigis_*_*', 
        'keep *_rctDigis_*_*', 
        'keep *_csctfDigis_*_*', 
        'keep *_csctfTrackDigis_*_*', 
        'keep *_dttfDigis_*_*', 
        'keep *_gctDigis_*_*', 
        'keep *_gmtDigis_*_*', 
        'keep *_gtDigis_*_*', 
        'keep *_gtEvmDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*')
)

process.L1TriggerRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*')
)

process.L1TriggerRAWDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*')
)

process.L1TriggerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*')
)

process.LHEEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep *_externalLHEProducer_LHEScriptOutput_*'),
    splitLevel = cms.untracked.int32(0)
)

process.METSignificanceParams = cms.PSet(
    dRMatch = cms.double(0.4),
    jetThreshold = cms.double(15),
    jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
    jpar = cms.vdouble(1.2, 1.13, 1.03, 0.96, 1.08),
    pjpar = cms.vdouble(-1.9, 0.6383)
)

process.MEtoEDMConverterAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.MEtoEDMConverterFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MEtoEDMConverter_*_*')
)

process.MEtoEDMConverterRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.MINIAODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_slimmedPhotons_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons_*_*', 
        'keep *_slimmedTaus_*_*', 
        'keep *_slimmedTausBoosted_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs_*_*', 
        'keep *_slimmedMETsNoHF_*_*', 
        'keep *_slimmedMETsPuppi_*_*', 
        'keep *_slimmedSecondaryVertices_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep *_bunchSpacingProducer_*_*', 
        'keep double_fixedGridRhoAll__*', 
        'keep double_fixedGridRhoFastjetAll__*', 
        'keep double_fixedGridRhoFastjetAllCalo__*', 
        'keep double_fixedGridRhoFastjetCentral_*_*', 
        'keep double_fixedGridRhoFastjetCentralCalo__*', 
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*', 
        'keep double_fixedGridRhoFastjetCentralNeutral__*', 
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep patPackedTriggerPrescales_patTrigger_l1max_*', 
        'keep patPackedTriggerPrescales_patTrigger_l1min_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_*', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*')
)

process.MINIAODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_slimmedPhotons_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons_*_*', 
        'keep *_slimmedTaus_*_*', 
        'keep *_slimmedTausBoosted_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs_*_*', 
        'keep *_slimmedMETsNoHF_*_*', 
        'keep *_slimmedMETsPuppi_*_*', 
        'keep *_slimmedSecondaryVertices_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep *_bunchSpacingProducer_*_*', 
        'keep double_fixedGridRhoAll__*', 
        'keep double_fixedGridRhoFastjetAll__*', 
        'keep double_fixedGridRhoFastjetAllCalo__*', 
        'keep double_fixedGridRhoFastjetCentral_*_*', 
        'keep double_fixedGridRhoFastjetCentralCalo__*', 
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*', 
        'keep double_fixedGridRhoFastjetCentralNeutral__*', 
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep patPackedTriggerPrescales_patTrigger_l1max_*', 
        'keep patPackedTriggerPrescales_patTrigger_l1min_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_*', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_slimmedGenJets*_*_*', 
        'keep patPackedGenParticles_packedGenParticles_*_*', 
        'keep recoGenParticles_prunedGenParticles_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_*_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep GenRunInfoProduct_*_*_*', 
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*')
)

process.MIXINGMODULEEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_cfWriter_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.MicroEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons_*_*', 
        'keep *_slimmedTaus_*_*', 
        'keep *_slimmedTausBoosted_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs_*_*', 
        'keep *_slimmedMETsNoHF_*_*', 
        'keep *_slimmedMETsPuppi_*_*', 
        'keep *_slimmedSecondaryVertices_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep *_bunchSpacingProducer_*_*', 
        'keep double_fixedGridRhoAll__*', 
        'keep double_fixedGridRhoFastjetAll__*', 
        'keep double_fixedGridRhoFastjetAllCalo__*', 
        'keep double_fixedGridRhoFastjetCentral_*_*', 
        'keep double_fixedGridRhoFastjetCentralCalo__*', 
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*', 
        'keep double_fixedGridRhoFastjetCentralNeutral__*', 
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep patPackedTriggerPrescales_patTrigger_l1max_*', 
        'keep patPackedTriggerPrescales_patTrigger_l1min_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_*', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*')
)

process.MicroEventContentMC = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_slimmedPhotons_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons_*_*', 
        'keep *_slimmedTaus_*_*', 
        'keep *_slimmedTausBoosted_*_*', 
        'keep *_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs_*_*', 
        'keep *_slimmedMETsNoHF_*_*', 
        'keep *_slimmedMETsPuppi_*_*', 
        'keep *_slimmedSecondaryVertices_*_*', 
        'keep *_slimmedJetsAK8PFCHSSoftDropPacked_SubJets_*', 
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep *_bunchSpacingProducer_*_*', 
        'keep double_fixedGridRhoAll__*', 
        'keep double_fixedGridRhoFastjetAll__*', 
        'keep double_fixedGridRhoFastjetAllCalo__*', 
        'keep double_fixedGridRhoFastjetCentral_*_*', 
        'keep double_fixedGridRhoFastjetCentralCalo__*', 
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*', 
        'keep double_fixedGridRhoFastjetCentralNeutral__*', 
        'keep *_selectedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep patPackedTriggerPrescales_patTrigger_l1max_*', 
        'keep patPackedTriggerPrescales_patTrigger_l1min_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_*', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_slimmedGenJets*_*_*', 
        'keep patPackedGenParticles_packedGenParticles_*_*', 
        'keep recoGenParticles_prunedGenParticles_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_*_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep GenRunInfoProduct_*_*_*', 
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*')
)

process.PREMIXEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep recoGenMETs_*_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep RPCDetIdRPCDigiMuonDigiCollection_simMuonRPCDigis_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_*_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_*_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.PREMIXRAWEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'drop CrossingFramePlaybackInfoNew_mix_*_*', 
        'keep *_*_MergedTrackTruth_*', 
        'keep *_*_StripDigiSimLink_*', 
        'keep *_*_PixelDigiSimLink_*', 
        'keep *_*_MuonCSCStripDigiSimLinks_*', 
        'keep *_*_MuonCSCWireDigiSimLinks_*', 
        'keep *_*_RPCDigiSimLink_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_*_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWAODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoTracks_GsfGlobalElectronTest_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep recoPhotonCores_gedPhotonCore_*_*', 
        'keep recoPhotons_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'drop *_gedPhotons_valMapPFEgammaCandToPhoton_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'drop *_pfElectronTranslator_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep recoCaloClusters_pfElectronTranslator_*_*', 
        'keep recoPreshowerClusters_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_pfElectronTranslator_*_*', 
        'keep recoCaloClusters_pfPhotonTranslator_*_*', 
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*', 
        'keep recoSuperClusters_pfPhotonTranslator_*_*', 
        'keep recoPhotons_pfPhotonTranslator_*_*', 
        'keep recoPhotonCores_pfPhotonTranslator_*_*', 
        'keep recoConversions_pfPhotonTranslator_*_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*' ) )
)

process.RAWDEBUGEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWDEBUGHLTEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECODEBUGHLTEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECOEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECOSIMHLTEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWSIMEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RAWSIMHLTEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*', 
        'keep *_hltAK4CaloJetsIDPassed_*_*', 
        'keep *_hltAK4CaloJets_*_*', 
        'keep *_hltAK4PFJetsCorrected_*_*', 
        'keep *_hltAK4PFJetsForTaus_*_*', 
        'keep *_hltAK4PFJets_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaEtaEERechitsToDigis_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegionalLowPU_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*', 
        'keep *_hltAlCaEtaRecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaEtaRecHitsFilter_*_*', 
        'keep *_hltAlCaPhiSymStream_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigisLowPU_*_*', 
        'keep *_hltAlCaPi0EERechitsToDigis_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEBonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegionalLowPU_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*', 
        'keep *_hltAlCaPi0RecHitsFilterEEonly_*_*', 
        'keep *_hltAlCaPi0RecHitsFilter_*_*', 
        'keep *_hltBLifetimeL25AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL25TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3AssociatorbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3BJetTagsbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeL3TagInfosbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet110Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet20Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet40Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5L3FilterByDR_*_*', 
        'keep *_hltBSoftMuonDiJet70Mu5SelL3BJetTagsByDR_*_*', 
        'keep *_hltBSoftMuonMu5L3_*_*', 
        'keep *_hltCSVJetTagSingleTopEle27_*_*', 
        'keep *_hltCSVJetTagSingleTopIsoMu24_*_*', 
        'keep *_hltCaloJetCorrectedRegional_*_*', 
        'keep *_hltCaloJetCorrected_*_*', 
        'keep *_hltCaloJetL1FastJetCorrected_*_*', 
        'keep *_hltCaloStage2Digis_*_*', 
        'keep *_hltCleanedCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCleanedHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*', 
        'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFindingIsolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackFinding_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5Isolation_*_*', 
        'keep *_hltConvPFTausTightIsoTrackPt5_*_*', 
        'keep *_hltConvPFTausTightIso_*_*', 
        'keep *_hltConvPFTausTrackFindingLooseIsolation_*_*', 
        'keep *_hltConvPFTausTrackFinding_*_*', 
        'keep *_hltConvPFTaus_*_*', 
        'keep *_hltCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltCsc2DRecHits_*_*', 
        'keep *_hltCscSegments_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltDoublePFTau25TrackPt5_*_*', 
        'keep *_hltDoublePFTau25_*_*', 
        'keep *_hltDoublePFTauTightIso45Track5_*_*', 
        'keep *_hltDoublePFTauTightIso45Track_*_*', 
        'keep *_hltDt4DSegments_*_*', 
        'keep *_hltEcalPhiSymFilter_*_*', 
        'keep *_hltEcalRecHitAll_*_*', 
        'keep *_hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*', 
        'keep *_hltEle27WP85PixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltFEDSelectorLumiPixels_*_*', 
        'keep *_hltFastPVPixelTracksMerger_*_*', 
        'keep *_hltFastPVPixelTracksRecover_*_*', 
        'keep *_hltFastPVPixelTracks_*_*', 
        'keep *_hltFastPVPixelVertices3D_*_*', 
        'keep *_hltFastPVPixelVertices_*_*', 
        'keep *_hltFastPixelBLifetimeL3TagInfos_*_*', 
        'keep *_hltFastPrimaryVertex_*_*', 
        'keep *_hltFilterDoubleIsoPFTau45Trk5LeadTrack5IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterL2EtCutDoublePFIsoTau45Trk5_*_*', 
        'keep *_hltFilterL2EtCutSingleIsoPFTau35Trk20MET70_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20LeadTrackPt20_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET60LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltFilterSingleIsoPFTau35Trk20MET70LeadTrack20IsolationL1HLTMatched_*_*', 
        'keep *_hltGmtStage2Digis_*_*', 
        'keep *_hltGoodOnlinePVs_*_*', 
        'keep *_hltGtStage2Digis_*_*', 
        'keep *_hltHICaloJetCorrected_*_*', 
        'keep *_hltHICaloJetIDPassed_*_*', 
        'keep *_hltHIGoodLooseTracks_*_*', 
        'keep *_hltHIPixel3PrimTracks_*_*', 
        'keep *_hltHISelectedVertex_*_*', 
        'keep *_hltHISiPixelClusters_*_*', 
        'keep *_hltHITIPTCorrectorHB_*_*', 
        'keep *_hltHITIPTCorrectorHE_*_*', 
        'keep *_hltHiCorrectedIslandBarrelSuperClustersHI_*_*', 
        'keep *_hltHiCorrectedIslandEndcapSuperClustersHI_*_*', 
        'keep *_hltHiIslandSuperClustersHI_*_*', 
        'keep *_hltIsolPixelTrackProdHB_*_*', 
        'keep *_hltIsolPixelTrackProdHE_*_*', 
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter1Merged_*_*', 
        'keep *_hltIter1PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter2Merged_*_*', 
        'keep *_hltIter2PFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltIter3Merged_*_*', 
        'keep *_hltIter4Merged_*_*', 
        'keep *_hltIterativeCone5PileupSubtractionCaloJets_*_*', 
        'keep *_hltL1HLTSingleIsoPFTau35Trk20Met60JetsMatch_*_*', 
        'keep *_hltL1IsoElectronTrackIsol_*_*', 
        'keep *_hltL1NonIsoElectronTrackIsol_*_*', 
        'keep *_hltL1SeededRecoEcalCandidate_*_*', 
        'keep *_hltL1sDoubleTauJet44Eta2p17orDoubleJet64Central_*_*', 
        'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*', 
        'keep *_hltL1sL1EG18er_*_*', 
        'keep *_hltL1sL1ETM36ORETM40_*_*', 
        'keep *_hltL1sL1Jet52ETM30_*_*', 
        'keep *_hltL1sL1SingleEG12_*_*', 
        'keep *_hltL1sL1SingleEG15_*_*', 
        'keep *_hltL1sL1SingleEG18orL1SingleEG20_*_*', 
        'keep *_hltL1sL1SingleMu10_*_*', 
        'keep *_hltL1sL1SingleMu14Eta2p1_*_*', 
        'keep *_hltL1sMu16Eta2p1_*_*', 
        'keep *_hltL2MuonCandidatesNoVtx_*_*', 
        'keep *_hltL2MuonCandidates_*_*', 
        'keep *_hltL2MuonSeeds_*_*', 
        'keep *_hltL2Muons_*_*', 
        'keep *_hltL2TauJets_*_*', 
        'keep *_hltL3MuonCandidates_*_*', 
        'keep *_hltL3MuonsIOHit_*_*', 
        'keep *_hltL3MuonsLinksCombination_*_*', 
        'keep *_hltL3MuonsOIHit_*_*', 
        'keep *_hltL3MuonsOIState_*_*', 
        'keep *_hltL3Muons_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*', 
        'keep *_hltL3NoFiltersNoVtxMuons_*_*', 
        'keep *_hltL3SecondaryVertexTagInfos_*_*', 
        'keep *_hltL3TkFromL2OICombination_*_*', 
        'keep *_hltL3TkTracksFromL2IOHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIHit_*_*', 
        'keep *_hltL3TkTracksFromL2OIState_*_*', 
        'keep *_hltL3TkTracksFromL2_*_*', 
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*', 
        'keep *_hltL3TrackCandidateFromL2OIState_*_*', 
        'keep *_hltL3TrajSeedIOHit_*_*', 
        'keep *_hltL3TrajSeedOIHit_*_*', 
        'keep *_hltL3TrajSeedOIState_*_*', 
        'keep *_hltL3TrajectorySeed_*_*', 
        'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopEle27_*_*', 
        'keep *_hltLeadingCentralJets30SingleTopIsoMu24_*_*', 
        'keep *_hltMet_*_*', 
        'keep *_hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter_*_*', 
        'keep *_hltMuTrackJpsiCtfTrackCands_*_*', 
        'keep *_hltMuTrackJpsiPixelTrackCands_*_*', 
        'keep *_hltMuonCSCDigis_*_*', 
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*', 
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*', 
        'keep *_hltMuonDTDigis_*_*', 
        'keep *_hltMuonRPCDigis_*_*', 
        'keep *_hltOnlineBeamSpot_*_*', 
        'keep *_hltOnlinePrimaryVertices_*_*', 
        'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*', 
        'keep *_hltOverlapFilterIsoEle20MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15IsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15MediumIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu15TightIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*', 
        'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*', 
        'keep *_hltPFJetForBtag_*_*', 
        'keep *_hltPFTau15TrackLooseIso_*_*', 
        'keep *_hltPFTau15Track_*_*', 
        'keep *_hltPFTau15_*_*', 
        'keep *_hltPFTau20IsoMuVertex_*_*', 
        'keep *_hltPFTau20TrackLooseIso_*_*', 
        'keep *_hltPFTau20Track_*_*', 
        'keep *_hltPFTau20_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*', 
        'keep *_hltPFTau25TrackPt5MediumIsolation_*_*', 
        'keep *_hltPFTau25TrackPt5_*_*', 
        'keep *_hltPFTau25_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*', 
        'keep *_hltPFTau35TrackPt20LooseIso_*_*', 
        'keep *_hltPFTau35TrackPt20_*_*', 
        'keep *_hltPFTau35Track_*_*', 
        'keep *_hltPFTau35_*_*', 
        'keep *_hltPFTauEleVertex20_*_*', 
        'keep *_hltPFTauJetTracksAssociator_*_*', 
        'keep *_hltPFTauMediumIso20TrackMediumIso_*_*', 
        'keep *_hltPFTauMediumIso20Track_*_*', 
        'keep *_hltPFTauMediumIso20_*_*', 
        'keep *_hltPFTauMediumIso35Track_*_*', 
        'keep *_hltPFTauMediumIso35_*_*', 
        'keep *_hltPFTauTagInfo_*_*', 
        'keep *_hltPFTauTightIso20TrackTightIso_*_*', 
        'keep *_hltPFTauTightIso20Track_*_*', 
        'keep *_hltPFTauTightIso20_*_*', 
        'keep *_hltPFlowTrackSelectionHighPurity_*_*', 
        'keep *_hltParticleFlowForTaus_*_*', 
        'keep *_hltParticleFlow_*_*', 
        'keep *_hltPixelMatch3HitElectronsActivity_*_*', 
        'keep *_hltPixelMatch3HitElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchCleanElectronsL1Seeded_*_*', 
        'keep *_hltPixelMatchElectronsActivity_*_*', 
        'keep *_hltPixelMatchElectronsL1Iso_*_*', 
        'keep *_hltPixelMatchElectronsL1NonIso_*_*', 
        'keep *_hltPixelMatchElectronsL1Seeded_*_*', 
        'keep *_hltPixelTracks_*_*', 
        'keep *_hltPixelVertices3DbbPhi_*_*', 
        'keep *_hltPixelVertices_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC4_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidateSC5_*_*', 
        'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*', 
        'keep *_hltRpcRecHits_*_*', 
        'keep *_hltSelector4CentralJetsL1FastJet_*_*', 
        'keep *_hltSelector8CentralJetsL1FastJet_*_*', 
        'keep *_hltSelectorJets20L1FastJet_*_*', 
        'keep *_hltSiPixelCluster_*_*', 
        'keep *_hltSiPixelClusters_*_*', 
        'keep *_hltSiStripClusters_*_*', 
        'keep *_hltSiStripRawToClustersFacility_*_*', 
        'keep *_hltSingleMu15L3Filtered15_*_*', 
        'keep *_hltSingleMuIsoL1s14L3IsoFiltered15eta2p1_*_*', 
        'keep *_hltSingleMuIsoL3IsoFiltered15_*_*', 
        'keep *_hltTowerMakerForAll_*_*', 
        'keep *_hltTowerMakerForMuons_*_*', 
        'keep *_hltTriggerSummaryAOD_*_*', 
        'keep *_hltTriggerSummaryRAW_*_*', 
        'keep *_hltTrimmedPixelVertices_*_*', 
        'keep *_hltVerticesL3_*_*', 
        'keep *_hltVerticesPFSelector_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajSeedOIHit_*_*', 
        'keep L3MuonTrajectorySeeds_hltHIL3TrajectorySeed_*_*', 
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*', 
        'keep LumiScalerss_hltScalersRawToDigi_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIHit_*_*', 
        'keep TrackCandidates_hltHIL3TrackCandidateFromL2OIState_*_*', 
        'keep TrackingRecHitsOwned_hltL3Muons_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep recoCaloJets_*_*_*', 
        'keep recoCaloMETs_*_*_*', 
        'keep recoCaloMETs_hltMet_*_*', 
        'keep recoCompositeCandidates_*_*_*', 
        'keep recoElectrons_*_*_*', 
        'keep recoIsolatedPixelTrackCandidates_*_*_*', 
        'keep recoMETs_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoPFTaus_*_*_*', 
        'keep recoRecoChargedCandidates_*_*_*', 
        'keep recoRecoChargedCandidates_hltHIL3MuonCandidates_*_*', 
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1IsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsoHLTClusterShape_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonEcalIsol_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalForHE_*_*', 
        'keep recoRecoEcalCandidatesToValuefloatAssociation_hltL1NonIsolatedPhotonHcalIsol_*_*', 
        'keep recoRecoEcalCandidates_*_*_*', 
        'keep recoRecoEcalCandidates_hltL1IsoRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hltL1NonIsoRecoEcalCandidate_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIHit_*_*', 
        'keep recoTrackExtras_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3MuonsOIHit_*_*', 
        'keep recoTracks_hltHIL3MuonsOIState_*_*', 
        'keep recoTracks_hltHIL3Muons_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIHit_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2OIState_*_*', 
        'keep recoTracks_hltHIL3TkTracksFromL2_*_*', 
        'keep triggerTriggerEventWithRefs_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep triggerTriggerFilterObjectWithRefs_*_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECODEBUGEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECOEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECOSIMEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*' ) ),
    splitLevel = cms.untracked.int32(0)
)

process.REDIGIEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('drop *', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'drop *_randomEngineStateProducer_*_*')
)

process.REGENEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*')
)

process.REPACKRAWEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop FEDRawDataCollection_*_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'drop FEDRawDataCollection_source_*_*', 
        'drop FEDRawDataCollection_rawDataCollector_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.REPACKRAWSIMEventContent = cms.PSet(
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = cms.untracked.vstring('drop *', 
        'drop FEDRawDataCollection_*_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*', 
        'keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*', 
        'keep recoGenMETs_*_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep *_MEtoEDMConverter_*_*', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'drop FEDRawDataCollection_source_*_*', 
        'drop FEDRawDataCollection_rawDataCollector_*_*'),
    splitLevel = cms.untracked.int32(0)
)

process.RESIMEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring('drop *', 
        'keep *_randomEngineStateProducer_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenRunInfoProduct_generator_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_generator_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep edmHepMCProduct_generatorSmeared_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep *_genParticles_*_*')
)

process.RecoBTagAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*')
)

process.RecoBTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*')
)

process.RecoBTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfGhostTrackVertexTagInfos_*_*', 
        'keep *_pfGhostTrackBJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*')
)

process.RecoBTauAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoBTauFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoBTauRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoCTPPSAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep TotemFEDInfos_totemRPRawToDigi_*_*', 
        'keep TotemTriggerCounters_totemTriggerRawToDigi_*_*', 
        'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemVFATStatusedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer_*_*', 
        'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer_*_*', 
        'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder_*_*', 
        'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter_*_*')
)

process.RecoCTPPSFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep TotemFEDInfos_totemRPRawToDigi_*_*', 
        'keep TotemTriggerCounters_totemTriggerRawToDigi_*_*', 
        'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemVFATStatusedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer_*_*', 
        'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer_*_*', 
        'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder_*_*', 
        'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter_*_*')
)

process.RecoCTPPSRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep TotemFEDInfos_totemRPRawToDigi_*_*', 
        'keep TotemTriggerCounters_totemTriggerRawToDigi_*_*', 
        'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemVFATStatusedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer_*_*', 
        'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer_*_*', 
        'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder_*_*', 
        'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter_*_*')
)

process.RecoEcalAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*')
)

process.RecoEcalFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_selectDigi_*_*', 
        'keep *_reducedEcalRecHitsEB_*_*', 
        'keep *_reducedEcalRecHitsEE_*_*', 
        'keep *_reducedEcalRecHitsES_*_*', 
        'keep *_interestingEcalDetId*_*_*', 
        'keep *_ecalWeightUncalibRecHit_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep *_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5*_*_*', 
        'keep *_correctedMulti5x5*_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*')
)

process.RecoEcalRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*')
)

process.RecoEgammaAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep recoPhotonCores_gedPhotonCore_*_*', 
        'keep recoPhotons_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'drop *_gedPhotons_valMapPFEgammaCandToPhoton_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*')
)

process.RecoEgammaFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_gsfElectronCores_*_*', 
        'keep *_gsfElectrons_*_*', 
        'keep *_uncleanedOnlyGsfElectronCores_*_*', 
        'keep *_uncleanedOnlyGsfElectrons_*_*', 
        'keep *_eidRobustLoose_*_*', 
        'keep *_eidRobustTight_*_*', 
        'keep *_eidRobustHighEnergy_*_*', 
        'keep *_eidLoose_*_*', 
        'keep *_eidTight_*_*', 
        'keep *_egmGedGsfElectronPF*Isolation_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
        'keep *_egmPhotonIDs_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'keep *_conversions_*_*', 
        'keep *_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotonsTmp_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep *_photonCore_*_*', 
        'keep *_photons_*_*', 
        'keep *_mustachePhotonCore_*_*', 
        'keep *_mustachePhotons_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_allConversionsOldEG_*_*', 
        'keep *_ckfOutInTracksFrom*Conversions_*_*', 
        'keep *_ckfInOutTracksFrom*Conversions_*_*', 
        'keep *_uncleanedOnlyAllConversions_*_*', 
        'keep *_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep *_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*')
)

process.RecoEgammaRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*')
)

process.RecoGenJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenJets_*_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4GenJets_*_*', 
        'keep *_ak8GenJets_*_*', 
        'keep *_ak4GenJetsNoNu_*_*', 
        'keep *_ak8GenJetsNoNu_*_*', 
        'keep *_genParticle_*_*')
)

process.RecoGenMETAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoGenMETFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoGenMETRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoHcalNoiseAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('drop recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*')
)

process.RecoHcalNoiseFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*')
)

process.RecoHcalNoiseRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*')
)

process.RecoJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'drop doubles_*Jets_rhos_*', 
        'drop doubles_*Jets_sigmas_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*')
)

process.RecoJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloJets_*_*_*', 
        'keep recoPFJets_*_*_*', 
        'keep recoTrackJets_*_*_*', 
        'keep recoJPTJets_*_*_*', 
        'keep recoBasicJets_*_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_kt4JetTracksAssociatorAtVertex_*_*', 
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_kt4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*', 
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*', 
        'keep *_ak7JetExtender_*_*', 
        'keep *_*JetID_*_*', 
        'keep *_kt4CaloJets_*_*', 
        'keep *_kt6CaloJets_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak5CaloJets_*_*', 
        'keep *_ak7CaloJets_*_*', 
        'keep *_kt4PFJets_*_*', 
        'keep *_kt6PFJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak5PFJets_*_*', 
        'keep *_ak7PFJets_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep *_kt4TrackJets_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ca*Mass_*_*', 
        'keep *_ak*Mass_*_*')
)

process.RecoJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*')
)

process.RecoLocalCaloAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_castorreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*')
)

process.RecoLocalCaloFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HBHERecHitsSorted_hbheprerecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalMultiFitUncalibRecHit_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*')
)

process.RecoLocalCaloRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCDataFramesSorted_castorDigis_*_*', 
        'keep ZDCRecHitsSorted_zdcreco_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*')
)

process.RecoLocalMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_dt4DSegments_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*')
)

process.RecoLocalMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*')
)

process.RecoLocalMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*')
)

process.RecoLocalTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep ClusterSummary_clusterSummaryProducer_*_*')
)

process.RecoLocalTrackerFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*')
)

process.RecoLocalTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*')
)

process.RecoMETAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'drop recoHcalNoiseRBXs_*_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMETFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMETRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*')
)

process.RecoMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*')
)

process.RecoMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoMuonIsolationAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoMuonIsolationFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoMuonIsolationParamGlobal = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muParamGlobalIsoDepositGsTk_*_*', 
        'keep *_muParamGlobalIsoDepositCalEcal_*_*', 
        'keep *_muParamGlobalIsoDepositCalHcal_*_*', 
        'keep *_muParamGlobalIsoDepositCtfTk_*_*', 
        'keep *_muParamGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muParamGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muParamGlobalIsoDepositJets_*_*')
)

process.RecoMuonIsolationRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*')
)

process.RecoParticleFlowAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('drop CaloTowersSorted_towerMakerPF_*_*', 
        'drop *_pfElectronTranslator_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep recoCaloClusters_pfElectronTranslator_*_*', 
        'keep recoPreshowerClusters_pfElectronTranslator_*_*', 
        'keep recoSuperClusters_pfElectronTranslator_*_*', 
        'keep recoCaloClusters_pfPhotonTranslator_*_*', 
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*', 
        'keep recoSuperClusters_pfPhotonTranslator_*_*', 
        'keep recoPhotons_pfPhotonTranslator_*_*', 
        'keep recoPhotonCores_pfPhotonTranslator_*_*', 
        'keep recoConversions_pfPhotonTranslator_*_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*')
)

process.RecoParticleFlowFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*')
)

process.RecoParticleFlowRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*')
)

process.RecoPixelVertexingFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*')
)

process.RecoPixelVertexingRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*')
)

process.RecoTauTagAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*')
)

process.RecoTauTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*')
)

process.RecoTauTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*')
)

process.RecoTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTracks_ctfPixelLess_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*')
)

process.RecoTrackerFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*')
)

process.RecoTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*')
)

process.RecoVertexAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*')
)

process.RecoVertexFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*')
)

process.RecoVertexRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*')
)

process.SimCalorimetryAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimCalorimetryFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simEcalDigis_*_*', 
        'keep *_simEcalPreshowerDigis_*_*', 
        'keep *_simEcalTriggerPrimitiveDigis_*_*', 
        'keep *_simHcalDigis_*_*', 
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*', 
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*', 
        'keep *_simHcalTriggerPrimitiveDigis_*_*')
)

process.SimCalorimetryRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep EBSrFlagsSorted_simEcalDigis_*_*', 
        'keep EESrFlagsSorted_simEcalDigis_*_*')
)

process.SimCalorimetryRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimG4CoreAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimG4CoreRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_g4SimHits_*_*', 
        'keep edmHepMCProduct_source_*_*')
)

process.SimG4CoreRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep edmHepMCProduct_source_*_*', 
        'keep SimTracks_g4SimHits_*_*', 
        'keep SimVertexs_g4SimHits_*_*')
)

process.SimGeneralAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*')
)

process.SimGeneralFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *_trackingtruthprod_*_*', 
        'drop *_electrontruth_*_*', 
        'keep *_mix_MergedTrackTruth_*', 
        'keep CrossingFramePlaybackInfoNew_*_*_*')
)

process.SimGeneralRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep CrossingFramePlaybackInfoNew_*_*_*', 
        'keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*')
)

process.SimGeneralRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep PileupSummaryInfos_*_*_*', 
        'keep int_*_bunchSpacing_*')
)

process.SimMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimMuonFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*')
)

process.SimMuonRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*')
)

process.SimMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*')
)

process.SimTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_allTrackMCMatch_*_*')
)

process.SimTrackerDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*', 
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*')
)

process.SimTrackerFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simSiPixelDigis_*_*', 
        'keep *_simSiStripDigis_*_*', 
        'drop *_mix_simSiPixelDigis*_*', 
        'drop *_mix_simSiStripDigis*_*', 
        'keep *_allTrackMCMatch_*_*', 
        'keep *_trackingParticleRecoTrackAsssociation_*_*', 
        'keep *_assoc2secStepTk_*_*', 
        'keep *_assoc2thStepTk_*_*', 
        'keep *_assoc2GsfTracks_*_*', 
        'keep *_assocOutInConversionTracks_*_*', 
        'keep *_assocInOutConversionTracks_*_*')
)

process.SimTrackerRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_allTrackMCMatch_*_*')
)

process.SimTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_allTrackMCMatch_*_*')
)

process.TcdsEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_tcdsDigis_*_*')
)

process.TrackingToolsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoTracks_GsfGlobalElectronTest_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*')
)

process.TrackingToolsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep *_electronGsfTracks_*_*')
)

process.TrackingToolsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*')
)

process.ecalLocalRecoAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.ecalLocalRecoFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ecalMultiFitUncalibRecHit_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*')
)

process.ecalLocalRecoRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.untracked.string(''),
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0),
    deleteAfterCopy = cms.untracked.bool(True)
)


process.ak4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4JPTL1FastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4JPTL1FastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1OffsetCorrector")
)


process.ak4PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFPuppiL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFPuppiL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFPuppiL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PFPuppiL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4PFPuppiResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2L3Residual')
)


process.ak4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L3Absolute')
)


process.caloMetT1 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"))
)


process.caloMetT1T2 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"), cms.InputTag("corrCaloMetType2"))
)


process.cleanMuonTriggerMatchHLT0 = cms.EDProducer("PATTriggerMatcherDRLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('path("HLT_DoubleMu4_LowMassNonResonantTrk_Displaced*",0,0)'),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("cleanPatMuons")
)


process.cleanPatElectrons = cms.EDProducer("PATElectronCleaner",
    checkOverlaps = cms.PSet(
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatElectrons")
)


process.cleanPatJets = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        ),
        photons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatPhotons")
        ),
        taus = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatTaus")
        ),
        tkIsoElectrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string('pt > 10 && trackIso < 3'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatJets")
)


process.cleanPatMuons = cms.EDProducer("PATMuonCleaner",
    checkOverlaps = cms.PSet(

    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatMuons")
)


process.cleanPatMuonsTriggerMatch = cms.EDProducer("PATTriggerMatchMuonEmbedder",
    matches = cms.VInputTag("cleanMuonTriggerMatchHLT0"),
    src = cms.InputTag("cleanPatMuons")
)


process.cleanPatPhotons = cms.EDProducer("PATPhotonCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('bySuperClusterSeed'),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatPhotons")
)


process.cleanPatTaus = cms.EDProducer("PATTauCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("cleanPatMuons")
        )
    ),
    finalCut = cms.string('pt > 18. & abs(eta) < 2.3'),
    preselection = cms.string('tauID("decayModeFinding") > 0.5 & tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5 & tauID("againstMuonTight3") > 0.5 & tauID("againstElectronVLooseMVA6") > 0.5'),
    src = cms.InputTag("selectedPatTaus")
)


process.cleanPatTrackCands = cms.EDProducer("PATGenericParticleCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.3),
            pairCut = cms.string('0.5 < ele.pt/part.pt < 1.5'),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(True),
            deltaR = cms.double(0.3),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("cleanPatMuons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("selectedPatTrackCands")
)


process.corrCaloMetType1 = cms.EDProducer("CaloJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4CaloL2L3Corrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    src = cms.InputTag("ak4CaloJets"),
    srcMET = cms.InputTag("caloMetM"),
    type1JetPtThreshold = cms.double(20.0)
)


process.corrCaloMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrCaloMetType1","type2"), cms.InputTag("muCaloMetCorr")),
    type2CorrFormula = cms.string('A + B*TMath::Exp(-C*x)'),
    type2CorrParameter = cms.PSet(
        A = cms.double(2.0),
        B = cms.double(1.3),
        C = cms.double(0.1)
    )
)


process.corrPfMetType1 = cms.EDProducer("PFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelRes = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("ak4PFJetsCHS"),
    type1JetPtThreshold = cms.double(15.0)
)


process.corrPfMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrPfMetType1","type2"), cms.InputTag("corrPfMetType1","offset"), cms.InputTag("pfCandMETcorr")),
    type2CorrFormula = cms.string('A'),
    type2CorrParameter = cms.PSet(
        A = cms.double(1.4)
    )
)


process.elPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedAllPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedElectronsPFBRECO"),
    trackType = cms.string('candidate')
)


process.elPFIsoValueCharged03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositCharged"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAll"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPU"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.electronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons")
)


process.hpsPFTauChargedIsoPtSum = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByLoosePileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(True),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByMediumPileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(True),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(1.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(True),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByRawPileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauDiscriminationByTightPileupWeightedIsolation3Hits = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(True),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(0.8),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauFootprintCorrection = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawFootprintCorrection = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauNeutralIsoPtSum = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauNeutralIsoPtSumWeight = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(True),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauPUcorrPtSum = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(True),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(True),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.hpsPFTauPhotonPtSumOutsideSignalCone = cms.EDProducer("PFRecoTauDiscriminationByIsolation",
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    UseAllPFCandsForWeights = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    applyFootprintCorrection = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
    applyRelativeSumPtCut = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    applySumPtCut = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.double(0.5),
    footprintCorrections = cms.VPSet(cms.PSet(
        offset = cms.string('0.0'),
        selection = cms.string('decayMode() = 0')
    ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ), 
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ), 
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ), 
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
    maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
    maximumOccupancy = cms.uint32(0),
    maximumSumPtCut = cms.double(2.5),
    minTauPtForNoIso = cms.double(-99.0),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(0.5),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    relativeSumPtCut = cms.double(0.0),
    relativeSumPtOffset = cms.double(0.0),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1.0),
    storeRawPUsumPt = cms.bool(False),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool(True),
    storeRawSumPt = cms.bool(False),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.isoDeposits = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag(""),
    trackType = cms.string('candidate')
)


process.muCaloMetCorr = cms.EDProducer("MuonMETcorrInputProducer",
    src = cms.InputTag("muons"),
    srcMuonCorrections = cms.InputTag("muonMETValueMapProducer","muCorrData")
)


process.muPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedAllPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositGammaPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositNeutralPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositPUPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedMuonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.muPFIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositCharged"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAll"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring('0.0001', 
            'Threshold(0.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGamma"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutral"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(1.0)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04 = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPU"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04PFBRECO = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring('0.01', 
            'Threshold(0.5)'),
        weight = cms.string('1')
    ))
)


process.muonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("muons")
)


process.packedGenParticles = cms.EDProducer("PATPackedGenParticleProducer",
    inputCollection = cms.InputTag("prunedGenParticlesWithStatusOne"),
    inputOriginal = cms.InputTag("genParticles"),
    inputVertices = cms.InputTag("offlinePrimaryVertices"),
    map = cms.InputTag("prunedGenParticles"),
    maxRapidity = cms.double(6)
)


process.particleFlowPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlow")
)


process.patAODTrackCandsUnfiltered = cms.EDProducer("ConcreteChargedCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("generalTracks")
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(True),
    addGenMatch = cms.bool(False),
    addPFClusterIso = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        eidLoose = cms.InputTag("eidLoose"),
        eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
        eidRobustLoose = cms.InputTag("eidRobustLoose"),
        eidRobustTight = cms.InputTag("eidRobustTight"),
        eidTight = cms.InputTag("eidTight")
    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(False),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag(""),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("elPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04PFIdPAT")
    ),
    isolationValuesNoPFId = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04NoPFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04NoPFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04NoPFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04NoPFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04NoPFIdPAT")
    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patHemispheres = cms.EDProducer("PATHemisphereProducer",
    combinationMethod = cms.int32(3),
    maxElectronEta = cms.double(5),
    maxJetEta = cms.double(5),
    maxMuonEta = cms.double(5),
    maxPhotonEta = cms.double(5),
    maxTauEta = cms.double(-1),
    minElectronEt = cms.double(7),
    minJetEt = cms.double(30),
    minMuonEt = cms.double(7),
    minPhotonEt = cms.double(200000),
    minTauEt = cms.double(1000000),
    patElectrons = cms.InputTag("cleanLayer1Electrons"),
    patJets = cms.InputTag("cleanLayer1Jets"),
    patMets = cms.InputTag("layer1METs"),
    patMuons = cms.InputTag("cleanLayer1Muons"),
    patPhotons = cms.InputTag("cleanLayer1Photons"),
    patTaus = cms.InputTag("cleanLayer1Taus"),
    seedMethod = cms.int32(3)
)


process.patJetCharge = cms.EDProducer("JetChargeProducer",
    exp = cms.double(1.0),
    src = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    var = cms.string('Pt')
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak4PFJetsCHS"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","algorithmicPartons"),
    rParam = cms.double(0.4)
)


process.patJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacy")
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak4PFJetsCHS"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag(""),
    JetPartonMapSource = cms.InputTag(""),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleInclusiveSecondaryVertexHighEffBJetTags"), 
        cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("softPFMuonBJetTags"), cms.InputTag("softPFElectronBJetTags"), cms.InputTag("pfCombinedMVAV2BJetTags"), 
        cms.InputTag("pfCombinedCvsLJetTags"), cms.InputTag("pfCombinedCvsBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag(""),
    genPartonMatch = cms.InputTag(""),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactors")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsCHS"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMETs = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag(""),
    metSource = cms.InputTag("pfMetT1"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.2, 1.13, 1.03, 0.96, 1.08),
        pjpar = cms.vdouble(-1.9, 0.6383)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("selectedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("packedPFCandidates"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(True),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(False),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPfEcalEnergy = cms.bool(True),
    embedPickyMuon = cms.bool(True),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(True),
    embedTrack = cms.bool(False),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag(""),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("muPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoValueChargedAll04PAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04PAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04PAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoValuePU04PAT"),
        pfPhotons = cms.InputTag("muPFIsoValueGamma04PAT")
    ),
    muonSource = cms.InputTag("muons"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    resolutions = cms.PSet(

    ),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(True),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(False),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag(""),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("phPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("phPFIsoValueGamma04PFIdPAT")
    ),
    photonIDSources = cms.PSet(
        PhotonCutBasedIDLoose = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDLoose"),
        PhotonCutBasedIDTight = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDTight")
    ),
    photonSource = cms.InputTag("gedPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTaus = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenMatch = cms.bool(False),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag(""),
    genParticleMatch = cms.InputTag(""),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6LooseElectronRejection"),
        againstElectronMVA6Raw = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejection"),
        againstElectronMVA6category = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejection","category"),
        againstElectronMediumMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6MediumElectronRejection"),
        againstElectronTightMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6TightElectronRejection"),
        againstElectronVLooseMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6VLooseElectronRejection"),
        againstElectronVTightMVA6 = cms.InputTag("hpsPFTauDiscriminationByMVA6VTightElectronRejection"),
        againstMuonLoose3 = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection3"),
        againstMuonTight3 = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection3"),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.InputTag("hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits"),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw"),
        byIsolationMVArun2v1DBnewDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw"),
        byIsolationMVArun2v1DBoldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw"),
        byIsolationMVArun2v1PWdR03oldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw"),
        byIsolationMVArun2v1PWnewDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw"),
        byIsolationMVArun2v1PWoldDMwLTraw = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw"),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits"),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT"),
        byLooseIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT"),
        byLooseIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT"),
        byLooseIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT"),
        byLooseIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT"),
        byLooseIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT"),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits"),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT"),
        byMediumIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT"),
        byMediumIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT"),
        byMediumIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT"),
        byMediumIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT"),
        byMediumIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT"),
        byPhotonPtSumOutsideSignalCone = cms.InputTag("hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone"),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits"),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT"),
        byTightIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT"),
        byTightIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT"),
        byTightIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT"),
        byTightIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT"),
        byTightIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT"),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT"),
        byVLooseIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT"),
        byVLooseIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT"),
        byVLooseIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT"),
        byVLooseIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT"),
        byVLooseIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT"),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT"),
        byVTightIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT"),
        byVTightIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT"),
        byVTightIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT"),
        byVTightIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT"),
        byVTightIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT"),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT"),
        byVVTightIsolationMVArun2v1DBnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT"),
        byVVTightIsolationMVArun2v1DBoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT"),
        byVVTightIsolationMVArun2v1PWdR03oldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT"),
        byVVTightIsolationMVArun2v1PWnewDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT"),
        byVVTightIsolationMVArun2v1PWoldDMwLT = cms.InputTag("hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT"),
        chargedIsoPtSum = cms.InputTag("hpsPFTauChargedIsoPtSum"),
        chargedIsoPtSumdR03 = cms.InputTag("hpsPFTauChargedIsoPtSumdR03"),
        decayModeFinding = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
        decayModeFindingNewDMs = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
        footprintCorrection = cms.InputTag("hpsPFTauFootprintCorrection"),
        footprintCorrectiondR03 = cms.InputTag("hpsPFTauFootprintCorrectiondR03"),
        neutralIsoPtSum = cms.InputTag("hpsPFTauNeutralIsoPtSum"),
        neutralIsoPtSumWeight = cms.InputTag("hpsPFTauNeutralIsoPtSumWeight"),
        neutralIsoPtSumWeightdR03 = cms.InputTag("hpsPFTauNeutralIsoPtSumWeightdR03"),
        neutralIsoPtSumdR03 = cms.InputTag("hpsPFTauNeutralIsoPtSumdR03"),
        photonPtSumOutsideSignalCone = cms.InputTag("hpsPFTauPhotonPtSumOutsideSignalCone"),
        photonPtSumOutsideSignalConedR03 = cms.InputTag("hpsPFTauPhotonPtSumOutsideSignalConedR03"),
        puCorrPtSum = cms.InputTag("hpsPFTauPUcorrPtSum")
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducer"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrackCands = cms.EDProducer("PATGenericParticleProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addQuality = cms.bool(False),
    addResolutions = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedCaloTower = cms.bool(False),
    embedCombinedMuon = cms.bool(False),
    embedGenMatch = cms.bool(False),
    embedGsfTrack = cms.bool(False),
    embedMultipleTracks = cms.bool(False),
    embedStandAloneMuon = cms.bool(False),
    embedSuperCluster = cms.bool(False),
    embedTrack = cms.bool(False),
    genParticleMatch = cms.InputTag("REPLACE_ME"),
    isoDeposits = cms.PSet(

    ),
    qualitySource = cms.InputTag("REPLACE_ME"),
    resolutions = cms.PSet(

    ),
    src = cms.InputTag("patAODTrackCands"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrigger = cms.EDProducer("PATTriggerProducer",
    l1GtReadoutRecordInputTag = cms.InputTag("gtDigis"),
    l1GtRecordInputTag = cms.InputTag("gtDigis"),
    l1GtTriggerMenuLiteInputTag = cms.InputTag("gtDigis"),
    l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
    onlyStandAlone = cms.bool(True),
    processName = cms.string('HLT')
)


process.pfCandMETcorr = cms.EDProducer("PFCandMETcorrInputProducer",
    src = cms.InputTag("pfCandsNotInJetsForMetCorr")
)


process.pfCandsNotInJetsForMetCorr = cms.EDProducer("PFCandidateFromFwdPtrProducer",
    src = cms.InputTag("pfCandsNotInJetsPtrForMetCorr")
)


process.pfCandsNotInJetsPtrForMetCorr = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrForMetCorr"),
    verbose = cms.untracked.bool(False)
)


process.pfJetsPtrForMetCorr = cms.EDProducer("PFJetFwdPtrProducer",
    src = cms.InputTag("ak4PFJets")
)


process.pfMetT0pc = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"))
)


process.pfMetT0pcT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT0pcT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0pcT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0pcTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rt = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"))
)


process.pfMetT0rtT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT0rtT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT0rtT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rtT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rtT2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT0rtTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetXYMult"))
)


process.pfNoJet = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("pfNoElectronJME"),
    enable = cms.bool(True),
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrs"),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUpIsoPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECO"),
    verbose = cms.untracked.bool(False)
)


process.pfNoPileUpPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpPFBRECO"),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpIsoPFBRECO = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpPFBRECO = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.phPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedAllPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(False),
        SCMatch_Veto = cms.bool(True),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositGammaPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(False),
        SCMatch_Veto = cms.bool(True),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositNeutralPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositPUPFBRECO = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("pfSelectedPhotonsPFBRECO"),
    trackType = cms.string('candidate')
)


process.phPFIsoValueCharged03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositCharged"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositCharged"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAll"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAll"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGamma"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPFBRECO"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutral"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPU"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFId = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPU"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFIdPFBRECO = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPFBRECO"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.photonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedPhotons")
)


process.prunedGenParticles = cms.EDProducer("GenParticlePruner",
    select = cms.vstring('drop  *', 
        '++keep abs(pdgId) == 11 || abs(pdgId) == 13 || abs(pdgId) == 15', 
        'keep abs(pdgId) == 12 || abs(pdgId) == 14 || abs(pdgId) == 16', 
        'drop   status == 2', 
        '+keep pdgId == 22 && status == 1 && (pt > 10 || isPromptFinalState())', 
        '+keep abs(pdgId) == 11 && status == 1 && (pt > 3 || isPromptFinalState())', 
        'keep++ abs(pdgId) == 15', 
        'drop  status > 30 && status < 70 ', 
        'drop  pdgId == 21 && pt < 5', 
        'drop   status == 2 && abs(pdgId) == 21', 
        'keep abs(pdgId) == 23 || abs(pdgId) == 24 || abs(pdgId) == 25 || abs(pdgId) == 6 || abs(pdgId) == 37 ', 
        'keep abs(pdgId) == 310 && abs(eta) < 2.5 && pt > 1 ', 
        '+keep abs(pdgId) == 13 && status == 1', 
        'keep (4 <= abs(pdgId) <= 5)', 
        'keep (1 <= abs(pdgId) <= 3 || pdgId = 21) & (status = 2 || status = 11 || status = 71 || status = 72) && pt>5', 
        'keep (400 < abs(pdgId) < 600) || (4000 < abs(pdgId) < 6000)', 
        'keep abs(pdgId) == 333', 
        'keep abs(pdgId) == 443 || abs(pdgId) == 100443 || abs(pdgId) == 10441 || abs(pdgId) == 20443 || abs(pdgId) == 445 || abs(pdgId) == 30443', 
        'keep abs(pdgId) == 553 || abs(pdgId) == 100553 || abs(pdgId) == 200553 || abs(pdgId) == 10551 || abs(pdgId) == 20553 || abs(pdgId) == 555', 
        'keep abs(pdgId) = 10411 || abs(pdgId) = 10421 || abs(pdgId) = 10413 || abs(pdgId) = 10423 || abs(pdgId) = 20413 || abs(pdgId) = 20423 || abs(pdgId) = 10431 || abs(pdgId) = 10433 || abs(pdgId) = 20433', 
        'keep abs(pdgId) = 10511 || abs(pdgId) = 10521 || abs(pdgId) = 10513 || abs(pdgId) = 10523 || abs(pdgId) = 20513 || abs(pdgId) = 20523 || abs(pdgId) = 10531 || abs(pdgId) = 10533 || abs(pdgId) = 20533 || abs(pdgId) = 10541 || abs(pdgId) = 10543 || abs(pdgId) = 20543', 
        'keep (1000001 <= abs(pdgId) <= 1000039 ) || ( 2000001 <= abs(pdgId) <= 2000015)', 
        'keep pdgId = 2212', 
        'keep status == 3 || ( 21 <= status <= 29) || ( 11 <= status <= 19)', 
        'keep isHardProcess() || fromHardProcessFinalState() || fromHardProcessDecayed() || fromHardProcessBeforeFSR() || (statusFlags().fromHardProcess() && statusFlags().isLastCopy())'),
    src = cms.InputTag("prunedGenParticlesWithStatusOne")
)


process.prunedGenParticlesWithStatusOne = cms.EDProducer("GenParticlePruner",
    select = cms.vstring('drop  *', 
        '++keep abs(pdgId) == 11 || abs(pdgId) == 13 || abs(pdgId) == 15', 
        'keep abs(pdgId) == 12 || abs(pdgId) == 14 || abs(pdgId) == 16', 
        'drop   status == 2', 
        '+keep pdgId == 22 && status == 1 && (pt > 10 || isPromptFinalState())', 
        '+keep abs(pdgId) == 11 && status == 1 && (pt > 3 || isPromptFinalState())', 
        'keep++ abs(pdgId) == 15', 
        'drop  status > 30 && status < 70 ', 
        'drop  pdgId == 21 && pt < 5', 
        'drop   status == 2 && abs(pdgId) == 21', 
        'keep abs(pdgId) == 23 || abs(pdgId) == 24 || abs(pdgId) == 25 || abs(pdgId) == 6 || abs(pdgId) == 37 ', 
        'keep abs(pdgId) == 310 && abs(eta) < 2.5 && pt > 1 ', 
        '+keep abs(pdgId) == 13 && status == 1', 
        'keep (4 <= abs(pdgId) <= 5)', 
        'keep (1 <= abs(pdgId) <= 3 || pdgId = 21) & (status = 2 || status = 11 || status = 71 || status = 72) && pt>5', 
        'keep (400 < abs(pdgId) < 600) || (4000 < abs(pdgId) < 6000)', 
        'keep abs(pdgId) == 333', 
        'keep abs(pdgId) == 443 || abs(pdgId) == 100443 || abs(pdgId) == 10441 || abs(pdgId) == 20443 || abs(pdgId) == 445 || abs(pdgId) == 30443', 
        'keep abs(pdgId) == 553 || abs(pdgId) == 100553 || abs(pdgId) == 200553 || abs(pdgId) == 10551 || abs(pdgId) == 20553 || abs(pdgId) == 555', 
        'keep abs(pdgId) = 10411 || abs(pdgId) = 10421 || abs(pdgId) = 10413 || abs(pdgId) = 10423 || abs(pdgId) = 20413 || abs(pdgId) = 20423 || abs(pdgId) = 10431 || abs(pdgId) = 10433 || abs(pdgId) = 20433', 
        'keep abs(pdgId) = 10511 || abs(pdgId) = 10521 || abs(pdgId) = 10513 || abs(pdgId) = 10523 || abs(pdgId) = 20513 || abs(pdgId) = 20523 || abs(pdgId) = 10531 || abs(pdgId) = 10533 || abs(pdgId) = 20533 || abs(pdgId) = 10541 || abs(pdgId) = 10543 || abs(pdgId) = 20543', 
        'keep (1000001 <= abs(pdgId) <= 1000039 ) || ( 2000001 <= abs(pdgId) <= 2000015)', 
        'keep pdgId = 2212', 
        'keep status == 3 || ( 21 <= status <= 29) || ( 11 <= status <= 19)', 
        'keep isHardProcess() || fromHardProcessFinalState() || fromHardProcessDecayed() || fromHardProcessBeforeFSR() || (statusFlags().fromHardProcess() && statusFlags().isLastCopy())', 
        'keep    status == 1'),
    src = cms.InputTag("genParticles")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.tauGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadrons"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("genParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauIsoDepositPFCandidates = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammas = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.patAODTrackCands = cms.EDFilter("CandViewSelector",
    cut = cms.string('pt > 0.4'),
    src = cms.InputTag("patAODTrackCandsUnfiltered")
)


process.pfAllChargedHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfPileUpAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13),
    src = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.selectedPatElectrons = cms.EDFilter("PATElectronSelector",
    cut = cms.string(''),
    src = cms.InputTag("patElectrons")
)


process.selectedPatJets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    src = cms.InputTag("patJets")
)


process.selectedPatMuons = cms.EDFilter("PATMuonSelector",
    cut = cms.string(''),
    src = cms.InputTag("patMuons")
)


process.selectedPatPhotons = cms.EDFilter("PATPhotonSelector",
    cut = cms.string(''),
    src = cms.InputTag("patPhotons")
)


process.selectedPatTaus = cms.EDFilter("PATTauSelector",
    cut = cms.string(''),
    src = cms.InputTag("patTaus")
)


process.selectedPatTrackCands = cms.EDFilter("PATGenericParticleSelector",
    cut = cms.string('pt > 0.4'),
    src = cms.InputTag("patTrackCands")
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring('oneProng0Pi0', 
        'oneProng1Pi0', 
        'oneProng2Pi0', 
        'oneProngOther', 
        'threeProng0Pi0', 
        'threeProng1Pi0', 
        'threeProngOther', 
        'rare'),
    src = cms.InputTag("tauGenJets")
)


process.MEtoMEComparitor = cms.EDAnalyzer("MEtoMEComparitor",
    Diffgoodness = cms.double(0.1),
    KSgoodness = cms.double(0.9),
    MEtoEDMLabel = cms.string('MEtoEDMConverter'),
    OverAllgoodness = cms.double(0.9),
    autoProcess = cms.bool(True),
    dirDepth = cms.uint32(1),
    lumiInstance = cms.string('MEtoEDMConverterLumi'),
    processNew = cms.string('RERECO'),
    processRef = cms.string('HLT'),
    runInstance = cms.string('MEtoEDMConverterRun')
)


process.cleanPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("cleanPatElectrons"), cms.InputTag("cleanPatMuons"), cms.InputTag("cleanPatTaus"), cms.InputTag("cleanPatPhotons"), cms.InputTag("cleanPatJets")),
    logName = cms.untracked.string('cleanPatCandidates|PATSummaryTables')
)


process.ntuple = cms.EDAnalyzer("BsToPhiMuMu",
    BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    BsMass = cms.untracked.double(5.36677),
    BsMaxMass = cms.untracked.double(6.0),
    BsMinMass = cms.untracked.double(4.7),
    BsMinVtxCl = cms.untracked.double(0.01),
    BuildBsToPhiMuMu = cms.untracked.bool(True),
    GenParticlesLabel = cms.InputTag("genParticles"),
    IsMonteCarlo = cms.untracked.bool(False),
    KaonMass = cms.untracked.double(0.493677),
    KaonMassErr = cms.untracked.double(1.6e-05),
    KeepGENOnly = cms.untracked.bool(False),
    LastFilterNames = cms.vstring('hltLowMassNonResonantTkVertexFilter'),
    MuMuMaxDca = cms.untracked.double(0.5),
    MuMuMaxInvMass = cms.untracked.double(4.8),
    MuMuMinCosAlphaBs = cms.untracked.double(0.9),
    MuMuMinInvMass = cms.untracked.double(1.0),
    MuMuMinLxySigmaBs = cms.untracked.double(3.0),
    MuMuMinPt = cms.untracked.double(6.9),
    MuMuMinVtxCl = cms.untracked.double(0.1),
    MuonLabel = cms.InputTag("cleanPatMuonsTriggerMatch"),
    MuonMass = cms.untracked.double(0.10565837),
    MuonMassErr = cms.untracked.double(3.5e-09),
    MuonMaxDcaBs = cms.untracked.double(2.0),
    MuonMaxEta = cms.untracked.double(2.2),
    MuonMinPt = cms.untracked.double(3.5),
    PhiMaxMass = cms.untracked.double(1.04),
    PhiMinMass = cms.untracked.double(1.0),
    TrackLabel = cms.InputTag("cleanPatTrackCands"),
    TriggerNames = cms.vstring('HLT_DoubleMu4_LowMassNonResonantTrk_Displaced'),
    TriggerResultsLabel = cms.InputTag("TriggerResults","","HLT"),
    TrkMaxR = cms.untracked.double(110.0),
    TrkMaxZ = cms.untracked.double(280.0),
    TrkMinDcaSigBs = cms.untracked.double(0.8),
    TrkMinPt = cms.untracked.double(0.4),
    TruthMatchKaonMaxR = cms.untracked.double(0.3),
    TruthMatchMuonMaxR = cms.untracked.double(0.004),
    VertexLabel = cms.InputTag("offlinePrimaryVertices")
)


process.patCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("patElectrons"), cms.InputTag("patMuons"), cms.InputTag("patTaus"), cms.InputTag("patPhotons"), cms.InputTag("patJets"), 
        cms.InputTag("patMETs")),
    logName = cms.untracked.string('patCandidates|PATSummaryTables')
)


process.selectedPatCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(cms.InputTag("selectedPatElectrons"), cms.InputTag("selectedPatMuons"), cms.InputTag("selectedPatTaus"), cms.InputTag("selectedPatPhotons"), cms.InputTag("selectedPatJets")),
    logName = cms.untracked.string('selectedPatCanddiates|PATSummaryTables')
)


process.ak4L1JPTOffsetCorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4L1JPTOffsetCorrector)


process.ak4PFL1L2L3CorrectorChain = cms.Sequence(process.ak4PFL1OffsetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL1L2L3Corrector)


process.ak4PFCHSL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastjetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL1FastL2L3ResidualCorrector)


process.patJetFlavourId = cms.Sequence(process.patJetPartons+process.patJetFlavourAssociation)


process.ak4PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1FastjetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL1FastL2L3Corrector)


process.ak4CaloL1L2L3CorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL1L2L3Corrector)


process.endOfProcess_withComparison = cms.Sequence(process.MEtoEDMConverter+process.MEtoMEComparitor)


process.ak4PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL1FastL2L3Corrector)


process.cleanPatCandidates = cms.Sequence(process.cleanPatMuons+process.cleanPatElectrons+process.cleanPatPhotons+process.cleanPatTaus+process.cleanPatJets+process.cleanPatCandidateSummary)


process.ak4PFPuppiL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1OffsetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL1L2L3ResidualCorrector)


process.electronPFIsolationDepositsPFBRECOSequence = cms.Sequence(process.elPFIsoDepositChargedPFBRECO+process.elPFIsoDepositChargedAllPFBRECO+process.elPFIsoDepositGammaPFBRECO+process.elPFIsoDepositNeutralPFBRECO+process.elPFIsoDepositPUPFBRECO)


process.ak4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL1FastL2L3ResidualCorrector)


process.ak4JPTL1L2L3CorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL1L2L3Corrector)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastjetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL1FastL2L3ResidualCorrector)


process.patJetFlavourIdLegacy = cms.Sequence(process.patJetPartonsLegacy+process.patJetPartonAssociationLegacy+process.patJetFlavourAssociationLegacy)


process.pfNoPileUpIsoPFBRECOSequence = cms.Sequence(process.pfPileUpIsoPFBRECO+process.pfNoPileUpIsoPFBRECO)


process.ak4PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL2L3ResidualCorrector)


process.pfSortByTypePFBRECOSequence = cms.Sequence(process.pfAllNeutralHadronsPFBRECO+process.pfAllChargedHadronsPFBRECO+process.pfAllPhotonsPFBRECO+process.pfAllChargedParticlesPFBRECO+process.pfPileUpAllChargedParticlesPFBRECO+process.pfAllNeutralHadronsAndPhotonsPFBRECO)


process.updateHPSPFTaus = cms.Sequence()


process.selectedPatCandidates = cms.Sequence(process.selectedPatElectrons+process.selectedPatMuons+process.selectedPatTaus+process.selectedPatPhotons+process.selectedPatJets+process.selectedPatCandidateSummary)


process.ak4JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak4JPTL1FastjetCorrector+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL1FastL2L3Corrector)


process.ak4PFCHSL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL2L3Corrector)


process.patCaloTauDiscrimination = cms.Sequence()


process.photonPFIsolationDepositsPFBRECOSequence = cms.Sequence(process.phPFIsoDepositChargedPFBRECO+process.phPFIsoDepositChargedAllPFBRECO+process.phPFIsoDepositGammaPFBRECO+process.phPFIsoDepositNeutralPFBRECO+process.phPFIsoDepositPUPFBRECO)


process.ak4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL1FastL2L3Corrector)


process.ak4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1OffsetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL1L2L3ResidualCorrector)


process.ak4JPTL2L3ResidualCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL2L3ResidualCorrector)


process.ak4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL6SLBCorrector+process.ak4PFL1FastL2L3L6Corrector)


process.photonPFIsolationDepositsPATSequence = cms.Sequence(process.phPFIsoDepositChargedPAT+process.phPFIsoDepositChargedAllPAT+process.phPFIsoDepositGammaPAT+process.phPFIsoDepositNeutralPAT+process.phPFIsoDepositPUPAT)


process.ak4TrackL2L3CorrectorChain = cms.Sequence(process.ak4TrackL2RelativeCorrector+process.ak4TrackL3AbsoluteCorrector+process.ak4TrackL2L3Corrector)


process.patShrinkingConePFTauDiscrimination = cms.Sequence()


process.ak4PFPuppiL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL2L3ResidualCorrector)


process.ak4JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1FastjetCorrector+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL1FastL2L3ResidualCorrector)


process.ak4PFL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL6SLBCorrector+process.ak4PFL2L3L6Corrector)


process.pfNoPileUpPFBRECOSequence = cms.Sequence(process.pfPileUpPFBRECO+process.pfNoPileUpPFBRECO)


process.patPFTauIsolation = cms.Sequence(process.tauIsoDepositPFCandidates+process.tauIsoDepositPFChargedHadrons+process.tauIsoDepositPFNeutralHadrons+process.tauIsoDepositPFGammas)


process.endOfProcess = cms.Sequence(process.MEtoEDMConverter)


process.ak4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL1FastL2L3ResidualCorrector)


process.electronPFIsolationDepositsPATSequence = cms.Sequence(process.elPFIsoDepositChargedPAT+process.elPFIsoDepositChargedAllPAT+process.elPFIsoDepositGammaPAT+process.elPFIsoDepositNeutralPAT+process.elPFIsoDepositPUPAT)


process.ak4CaloL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL6SLBCorrector+process.ak4CaloL2L3L6Corrector)


process.ak4PFPuppiL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastjetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL1FastL2L3Corrector)


process.ak4JPTL2L3CorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL2L3Corrector)


process.ak4CaloL2L3CorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL2L3Corrector)


process.ak4JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL1L2L3ResidualCorrector)


process.pfPhotonIsolationPATSequence = cms.Sequence(process.photonPFIsolationDepositsPATSequence+process.phPFIsoValueCharged03PFIdPAT+process.phPFIsoValueChargedAll03PFIdPAT+process.phPFIsoValueGamma03PFIdPAT+process.phPFIsoValueNeutral03PFIdPAT+process.phPFIsoValuePU03PFIdPAT+process.phPFIsoValueCharged04PFIdPAT+process.phPFIsoValueChargedAll04PFIdPAT+process.phPFIsoValueGamma04PFIdPAT+process.phPFIsoValueNeutral04PFIdPAT+process.phPFIsoValuePU04PFIdPAT)


process.patFixedConePFTauDiscrimination = cms.Sequence()


process.patJetCorrections = cms.Sequence(process.patJetCorrFactors)


process.muonPFIsolationDepositsPATSequence = cms.Sequence(process.muPFIsoDepositChargedPAT+process.muPFIsoDepositChargedAllPAT+process.muPFIsoDepositGammaPAT+process.muPFIsoDepositNeutralPAT+process.muPFIsoDepositPUPAT)


process.muonPFIsolationPATSequence = cms.Sequence(process.muonPFIsolationDepositsPATSequence+process.muPFIsoValueCharged03PAT+process.muPFMeanDRIsoValueCharged03PAT+process.muPFSumDRIsoValueCharged03PAT+process.muPFIsoValueChargedAll03PAT+process.muPFMeanDRIsoValueChargedAll03PAT+process.muPFSumDRIsoValueChargedAll03PAT+process.muPFIsoValueGamma03PAT+process.muPFMeanDRIsoValueGamma03PAT+process.muPFSumDRIsoValueGamma03PAT+process.muPFIsoValueNeutral03PAT+process.muPFMeanDRIsoValueNeutral03PAT+process.muPFSumDRIsoValueNeutral03PAT+process.muPFIsoValueGammaHighThreshold03PAT+process.muPFMeanDRIsoValueGammaHighThreshold03PAT+process.muPFSumDRIsoValueGammaHighThreshold03PAT+process.muPFIsoValueNeutralHighThreshold03PAT+process.muPFMeanDRIsoValueNeutralHighThreshold03PAT+process.muPFSumDRIsoValueNeutralHighThreshold03PAT+process.muPFIsoValuePU03PAT+process.muPFMeanDRIsoValuePU03PAT+process.muPFSumDRIsoValuePU03PAT+process.muPFIsoValueCharged04PAT+process.muPFMeanDRIsoValueCharged04PAT+process.muPFSumDRIsoValueCharged04PAT+process.muPFIsoValueChargedAll04PAT+process.muPFMeanDRIsoValueChargedAll04PAT+process.muPFSumDRIsoValueChargedAll04PAT+process.muPFIsoValueGamma04PAT+process.muPFMeanDRIsoValueGamma04PAT+process.muPFSumDRIsoValueGamma04PAT+process.muPFIsoValueNeutral04PAT+process.muPFMeanDRIsoValueNeutral04PAT+process.muPFSumDRIsoValueNeutral04PAT+process.muPFIsoValueGammaHighThreshold04PAT+process.muPFMeanDRIsoValueGammaHighThreshold04PAT+process.muPFSumDRIsoValueGammaHighThreshold04PAT+process.muPFIsoValueNeutralHighThreshold04PAT+process.muPFMeanDRIsoValueNeutralHighThreshold04PAT+process.muPFSumDRIsoValueNeutralHighThreshold04PAT+process.muPFIsoValuePU04PAT+process.muPFMeanDRIsoValuePU04PAT+process.muPFSumDRIsoValuePU04PAT)


process.pfElectronIsolationPATSequence = cms.Sequence(process.electronPFIsolationDepositsPATSequence+process.elPFIsoValueCharged03PFIdPAT+process.elPFIsoValueChargedAll03PFIdPAT+process.elPFIsoValueGamma03PFIdPAT+process.elPFIsoValueNeutral03PFIdPAT+process.elPFIsoValuePU03PFIdPAT+process.elPFIsoValueCharged04PFIdPAT+process.elPFIsoValueChargedAll04PFIdPAT+process.elPFIsoValueGamma04PFIdPAT+process.elPFIsoValueNeutral04PFIdPAT+process.elPFIsoValuePU04PFIdPAT+process.elPFIsoValueCharged03NoPFIdPAT+process.elPFIsoValueChargedAll03NoPFIdPAT+process.elPFIsoValueGamma03NoPFIdPAT+process.elPFIsoValueNeutral03NoPFIdPAT+process.elPFIsoValuePU03NoPFIdPAT+process.elPFIsoValueCharged04NoPFIdPAT+process.elPFIsoValueChargedAll04NoPFIdPAT+process.elPFIsoValueGamma04NoPFIdPAT+process.elPFIsoValueNeutral04NoPFIdPAT+process.elPFIsoValuePU04NoPFIdPAT)


process.muonPFIsolationDepositsPFBRECOSequence = cms.Sequence(process.muPFIsoDepositChargedPFBRECO+process.muPFIsoDepositChargedAllPFBRECO+process.muPFIsoDepositGammaPFBRECO+process.muPFIsoDepositNeutralPFBRECO+process.muPFIsoDepositPUPFBRECO)


process.ak4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL6SLBCorrector+process.ak4CaloL1FastL2L3L6Corrector)


process.ak4PFCHSL1L2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1OffsetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL1L2L3Corrector)


process.ak4PFPuppiL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL2L3Corrector)


process.ak4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL2L3ResidualCorrector)


process.ak4PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1OffsetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL1L2L3ResidualCorrector)


process.ak4PFL2L3CorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL2L3Corrector)


process.ak4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL1L2L3ResidualCorrector)


process.ak4PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL2L3ResidualCorrector)


process.ak4PFPuppiL1L2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1OffsetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL1L2L3Corrector)


process.patHPSPFTauDiscrimination = cms.Sequence(process.updateHPSPFTaus)


process.pfParticleSelectionPFBRECOSequence = cms.Sequence(process.pfNoPileUpIsoPFBRECOSequence+process.pfNoPileUpPFBRECOSequence+process.pfSortByTypePFBRECOSequence)


process.correctionTermsPfMetType1Type2 = cms.Sequence(process.pfJetsPtrForMetCorr+process.particleFlowPtrs+process.pfCandsNotInJetsPtrForMetCorr+process.pfCandsNotInJetsForMetCorr+process.pfCandMETcorr+process.ak4PFCHSL1FastL2L3ResidualCorrectorChain+process.ak4PFCHSL1FastL2L3Corrector+process.corrPfMetType1+process.corrPfMetType2)


process.correctionTermsCaloMet = cms.Sequence(process.ak4CaloL2L3CorrectorChain+process.corrCaloMetType1+process.muCaloMetCorr+process.corrCaloMetType2)


process.pfParticleSelectionForIsoSequence = cms.Sequence(process.particleFlowPtrs+process.pfParticleSelectionPFBRECOSequence)


process.patMETCorrections = cms.Sequence(process.correctionTermsCaloMet+process.caloMetT1+process.caloMetT1T2+process.correctionTermsPfMetType1Type2+process.pfMetT1+process.pfMetT1T2)


process.patPFCandidateIsoDepositSelection = cms.Sequence(process.pfNoPileUpIsoPFBRECOSequence+process.pfSortByTypePFBRECOSequence)


process.makePatTaus = cms.Sequence(process.patHPSPFTauDiscrimination+process.patPFCandidateIsoDepositSelection+process.patPFTauIsolation+process.tauMatch+process.tauGenJets+process.tauGenJetsSelectorAllHadrons+process.tauGenJetMatch+process.patTaus)


process.makePatJets = cms.Sequence(process.patJetCorrections+process.patJetCharge+process.patJetPartonMatch+process.patJetGenJetMatch+process.patJetFlavourIdLegacy+process.patJetFlavourId+process.patJets)


process.makePatMuons = cms.Sequence(process.pfParticleSelectionForIsoSequence+process.muonPFIsolationPATSequence+process.muonMatch+process.patMuons)


process.makePatElectrons = cms.Sequence(process.pfParticleSelectionForIsoSequence+process.pfElectronIsolationPATSequence+process.electronMatch+process.patElectrons)


process.makePatMETs = cms.Sequence(process.patMETCorrections+process.patMETs)


process.makePatPhotons = cms.Sequence(process.pfParticleSelectionForIsoSequence+process.pfPhotonIsolationPATSequence+process.photonMatch+process.patPhotons)


process.patCandidates = cms.Sequence(process.makePatElectrons+process.makePatMuons+process.makePatTaus+process.makePatPhotons+process.makePatJets+process.makePatMETs+process.patCandidateSummary)


process.p = cms.Path(process.ntuple)


process.DQMStore = cms.Service("DQMStore")


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('BsToPhiMuMu_2016B.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ak10PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL1Fastjet', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual')
)


process.ak10PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL1Offset', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual')
)


process.ak10PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute')
)


process.ak10PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual')
)


process.ak10PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2Relative')
)


process.ak10PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L3Absolute')
)


process.ak10PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak10PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL1Fastjet', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual')
)


process.ak10PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL1Offset', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual')
)


process.ak10PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL2Relative', 
        'ak10PFL3Absolute')
)


process.ak10PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual')
)


process.ak10PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2Relative')
)


process.ak10PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L3Absolute')
)


process.ak10PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2L3Residual')
)


process.ak1PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL1Fastjet', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual')
)


process.ak1PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL1Offset', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual')
)


process.ak1PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute')
)


process.ak1PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual')
)


process.ak1PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2Relative')
)


process.ak1PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak1PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL1Fastjet', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual')
)


process.ak1PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL1Offset', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual')
)


process.ak1PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL2Relative', 
        'ak1PFL3Absolute')
)


process.ak1PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual')
)


process.ak1PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2Relative')
)


process.ak1PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L3Absolute')
)


process.ak1PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2L3Residual')
)


process.ak2PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL1Fastjet', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual')
)


process.ak2PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL1Offset', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual')
)


process.ak2PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute')
)


process.ak2PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual')
)


process.ak2PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2Relative')
)


process.ak2PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak2PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL1Fastjet', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual')
)


process.ak2PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL1Offset', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual')
)


process.ak2PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL2Relative', 
        'ak2PFL3Absolute')
)


process.ak2PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual')
)


process.ak2PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2Relative')
)


process.ak2PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L3Absolute')
)


process.ak2PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2L3Residual')
)


process.ak3PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL1Fastjet', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual')
)


process.ak3PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL1Offset', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual')
)


process.ak3PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute')
)


process.ak3PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual')
)


process.ak3PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2Relative')
)


process.ak3PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak3PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL1Fastjet', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual')
)


process.ak3PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL1Offset', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual')
)


process.ak3PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL2Relative', 
        'ak3PFL3Absolute')
)


process.ak3PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual')
)


process.ak3PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2Relative')
)


process.ak3PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L3Absolute')
)


process.ak3PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2L3Residual')
)


process.ak4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute')
)


process.ak4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB')
)


process.ak4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual')
)


process.ak4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute')
)


process.ak4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual')
)


process.ak4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL2Relative', 
        'ak4CaloL3Absolute')
)


process.ak4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB')
)


process.ak4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual')
)


process.ak4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4JPTL1Fastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute')
)


process.ak4JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4JPTL1Fastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual')
)


process.ak4JPTL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute')
)


process.ak4JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual')
)


process.ak4JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute')
)


process.ak4JPTL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual')
)


process.ak4JPTL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak4PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute')
)


process.ak4PFCHSL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual')
)


process.ak4PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute')
)


process.ak4PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual')
)


process.ak4PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute')
)


process.ak4PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual')
)


process.ak4PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute')
)


process.ak4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB')
)


process.ak4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual')
)


process.ak4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute')
)


process.ak4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual')
)


process.ak4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL2Relative', 
        'ak4PFL3Absolute')
)


process.ak4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB')
)


process.ak4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual')
)


process.ak4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak4TrackL2Relative', 
        'ak4TrackL3Absolute')
)


process.ak4TrackL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4TrackL2Relative', 
        'ak4TrackL3Absolute')
)


process.ak4TrackL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL1Fastjet', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual')
)


process.ak5PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL1Offset', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual')
)


process.ak5PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute')
)


process.ak5PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual')
)


process.ak5PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2Relative')
)


process.ak5PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute')
)


process.ak5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual')
)


process.ak5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak6PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL1Fastjet', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual')
)


process.ak6PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL1Offset', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual')
)


process.ak6PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute')
)


process.ak6PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual')
)


process.ak6PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2Relative')
)


process.ak6PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL1Fastjet', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual')
)


process.ak6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL1Offset', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual')
)


process.ak6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL2Relative', 
        'ak6PFL3Absolute')
)


process.ak6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual')
)


process.ak6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2Relative')
)


process.ak6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L3Absolute')
)


process.ak6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2L3Residual')
)


process.ak7CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute')
)


process.ak7CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB')
)


process.ak7CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual')
)


process.ak7CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos")
)


process.ak7CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Fastjet', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7JPTL1Offset', 
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual')
)


process.ak7JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute')
)


process.ak7L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak7PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute')
)


process.ak7PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual')
)


process.ak7PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL1Offset', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual')
)


process.ak7PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute')
)


process.ak7PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual')
)


process.ak7PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2Relative')
)


process.ak7PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L3Absolute')
)


process.ak7PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak7PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute')
)


process.ak7PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB')
)


process.ak7PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual')
)


process.ak7PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos")
)


process.ak7PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2L3Residual')
)


process.ak8PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL1Fastjet', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual')
)


process.ak8PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL1Offset', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual')
)


process.ak8PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute')
)


process.ak8PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual')
)


process.ak8PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)


process.ak8PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak8PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL1Fastjet', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual')
)


process.ak8PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL1Offset', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual')
)


process.ak8PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL2Relative', 
        'ak8PFL3Absolute')
)


process.ak8PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual')
)


process.ak8PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)


process.ak8PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)


process.ak8PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2L3Residual')
)


process.ak9PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL1Fastjet', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual')
)


process.ak9PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL1Offset', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual')
)


process.ak9PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute')
)


process.ak9PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual')
)


process.ak9PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2Relative')
)


process.ak9PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak9PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL1Fastjet', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual')
)


process.ak9PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL1Offset', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual')
)


process.ak9PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL2Relative', 
        'ak9PFL3Absolute')
)


process.ak9PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual')
)


process.ak9PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2Relative')
)


process.ak9PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L3Absolute')
)


process.ak9PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2L3Residual')
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.ic5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ic5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute')
)


process.ic5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB')
)


process.ic5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual')
)


process.ic5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos")
)


process.ic5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ic5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute')
)


process.ic5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB')
)


process.ic5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual')
)


process.ic5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos")
)


process.ic5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2L3Residual')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.kt4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute')
)


process.kt4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB')
)


process.kt4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual')
)


process.kt4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos")
)


process.kt4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute')
)


process.kt4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB')
)


process.kt4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual')
)


process.kt4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos")
)


process.kt4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt6CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute')
)


process.kt6CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB')
)


process.kt6CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual')
)


process.kt6CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos")
)


process.kt6CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt6PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute')
)


process.kt6PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB')
)


process.kt6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual')
)


process.kt6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos")
)


process.kt6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2L3Residual')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('81X_dataRun2_v2'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497),
        HFdepthOneParameterB = cms.vdouble(-4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209),
        HFdepthTwoParameterA = cms.vdouble(0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593),
        HFdepthTwoParameterB = cms.vdouble(-2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06)
    ),
    HFRecalibration = cms.bool(False),
    hb = cms.PSet(
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        pedestal = cms.double(3.0),
        pedestalWidth = cms.double(0.55),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0)
    ),
    hbUpgrade = cms.PSet(
        gain = cms.vdouble(0.000280269058296),
        gainWidth = cms.vdouble(0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.333, 0.333, 0.333, 0.333),
        qieType = cms.int32(2)
    ),
    he = cms.PSet(
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        pedestal = cms.double(3.0),
        pedestalWidth = cms.double(0.79),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0)
    ),
    heUpgrade = cms.PSet(
        gain = cms.vdouble(0.000280269058296),
        gainWidth = cms.vdouble(0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.333, 0.333, 0.333, 0.333),
        qieType = cms.int32(2)
    ),
    hf = cms.PSet(
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        pedestal = cms.double(3.0),
        pedestalWidth = cms.double(0.84),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0)
    ),
    hfUpgrade = cms.PSet(
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1)
    ),
    ho = cms.PSet(
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        pedestal = cms.double(11.0),
        pedestalWidth = cms.double(0.57),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0)
    ),
    iLumi = cms.double(-1.0),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False)
)


process.prefer("es_hardcode")

