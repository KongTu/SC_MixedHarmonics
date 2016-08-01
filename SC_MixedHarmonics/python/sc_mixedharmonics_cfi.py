import FWCore.ParameterSet.Config as cms

import HLTrigger.HLTfilters.hltHighLevel_cfi
hltHM = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
hltHM.HLTPaths = ['HLT_PAPixelTracks_Multiplicity100_v*',
                  'HLT_PAPixelTracks_Multiplicity130_v*',
                  'HLT_PAPixelTracks_Multiplicity160_v*'
                  #'HLT_PAPixelTracks_Multiplicity190_v*',
                  #'HLT_PAPixelTracks_Multiplicity220_v*'
]

hltHM.andOr = cms.bool(True)
hltHM.throw = cms.bool(False)
				
ana = cms.EDAnalyzer('SC_MixedHarmonics',
                                                  vertexName = cms.InputTag('offlinePrimaryVertices'),
                		  						  trackName = cms.InputTag('generalTracks'),
                                                  towerName = cms.InputTag("towerMaker"),
                                                  offlineDCA = cms.untracked.double(3.0),
                                                  offlineptErr = cms.untracked.double(0.1),
				  		  offlinenhits = cms.untracked.double(0),
						  offlineChi2 = cms.untracked.double(999.9),
						  useCentrality = cms.untracked.bool(False),
                                                  reverseBeam = cms.untracked.bool(False),
						  doEffCorrection = cms.untracked.bool(False),
						  Nmin = cms.untracked.int32(1),
                                                  Nmax = cms.untracked.int32(10000),
                                                  vzLow = cms.untracked.double(0.0),
                                                  vzHigh = cms.untracked.double(15.0),
                                                  ptLow = cms.untracked.double(0.3),
						  ptHigh = cms.untracked.double(3.0),
						 
						  etaTracker = cms.untracked.double(2.4),
						  etaLowHF = cms.untracked.double(4.4),
                                                  etaHighHF = cms.untracked.double(5.0),
                                                  etaBins = cms.untracked.vdouble(-2.4,-2.3,-2.2,-2.1,-2,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,
                                                                                  -1.3,-1.2,-1.1,-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,
                                                                                  -0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,
                                                                                  1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4),
                                                  dEtaBins = cms.untracked.vdouble(0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,
                                                                                   1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.2,
                                                                                   2.4,2.6,2.8,3.0,3.4,3.8,4.2,4.8),
						  ptBins = cms.untracked.vdouble(
                                                                      0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
                                                                      0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95,
                                                                      1.0, 1.05, 1.1, 1.15, 1.2,
                                                                      1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
                                                                      2.5, 3.0, 4.0, 5.0, 7.5, 10.0, 12.0, 15.0,
                                                                      20.0, 25.0, 30.0, 45.0, 60.0, 90.0, 120.0, 
                                                                      180.0, 300.0, 500.0
                                                                      )

)

