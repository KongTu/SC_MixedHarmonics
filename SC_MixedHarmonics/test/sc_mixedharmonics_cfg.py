import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",ignoreTotal = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)
process.options   = cms.untracked.PSet( wantSummary =
cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("Configuration.StandardSequences.Digi_cff")
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.GlobalTag.globaltag = '75X_dataRun2_PromptHI_v3'

process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True),   # otherwise it won't filter the events
)

#Reject beam scraping events standard pp configuration
process.NoScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
'/store/hidata/HIRun2015/HIMinimumBias5/AOD/02May2016-v1/10000/006477CE-3326-E611-8C08-003048F317E6.root'
#'file:/afs/cern.ch/work/z/ztu/CME/CMSSW_7_5_8_patch3/src/CMEandCorrelation/ThreePointCorrelator/test/step2pp_RAW2DIGI_L1Reco_RECO_1.root'
#'/store/user/davidlw/EPOS_PbPb5TeV/Cent30100_DIGI-RECO_v1/160629_095734/0000/step2_FILTER_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_RECO_1.root'
#'root://xrootd-cms.infn.it//store/user/gsfs/Hydjet_Quenched_MinBias_5020GeV_750/Hydjet_30_100_w_pp_RECO_20160724/160725_221957/0000/step3_FILTER_RAW2DIGI_L1Reco_RECO_1.root'
)
)

process.load("SC_MixedHarmonics.SC_MixedHarmonics.sc_mixedharmonics_cfi")

#define the cuts

process.TFileService = cms.Service("TFileService",fileName = cms.string("test.root"))
process.p = cms.Path(  process.hfCoincFilter3 *
                       process.PAprimaryVertexFilter *
                       process.NoScraping *
                       process.ana
                        )