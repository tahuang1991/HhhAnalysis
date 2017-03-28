import FWCore.ParameterSet.Config as cms
import os
import sys

process = cms.Process("DiHiggsAnalyzer")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.source = cms.Source("PoolSource",
  secondaryFileNames = cms.untracked.vstring(),
  fileNames = cms.untracked.vstring(
#  'file:/fdata/hepx/store/user/lpernie/TEST_LOCALLY/DYJETS_7A385961-C6D9-E611-85B2-0025905B85BC.root'
  'file:/fdata/hepx/store/user/lpernie/TEST_LOCALLY/Run2016D-23Sep2016_MINIAOD_12B2DEA9-B68C-E611-99A4-0CC47A1DF810.root'
  )
)

process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(100000) 
)

process.MessageLogger = cms.Service("MessageLogger", 
    destinations = cms.untracked.vstring("cout"), 
    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR"))
)

import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt
process.hltfilter = cms.EDFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v*',
  ),
  hltResults = cms.InputTag( "TriggerResults","","HLT"),
  #l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tResults = cms.InputTag( "" ),
  l1tIgnoreMask = cms.bool( False ),
  l1techIgnorePrescales = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool(True)    
)

print sys.argv
sample = 0#int(sys.argv[1])
print "sample",sample

process.DiHiggsWWBBAna = cms.EDAnalyzer('DiHiggsWWBBAnalyzer',
  verbose = cms.untracked.int32(0),
  #enum {Data = 0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, TTbar, DYJets, DY0Jets, DY1Jets, DY2Jets};//add other background
  SampleType = cms.untracked.int32(sample),
  #genParticles = cms.InputTag("genParticles"),
  genParticles = cms.InputTag("prunedGenParticles"),#minAOD
  #muons = cms.InputTag("cleanPatPFMuonsTriggerMatch"),
  muons = cms.InputTag("slimmedMuons"),
  electrons = cms.InputTag("slimmedElectrons"),
  genjets = cms.InputTag("slimmedGenJets"), # For miniAOD
  #genjets = cms.InputTag("ak4GenJetsNoNu"),
  #genjets = cms.InputTag("ak4GenJets"),
  jets = cms.InputTag("slimmedJets"),
  mets = cms.InputTag("slimmedMETs"),
  beamSpot = cms.InputTag("offlineBeamSpot"),
  triggerEvent = cms.InputTag("patTriggerEvent"),
  tracks = cms.InputTag("generalTracks"),
  TriggerResults = cms.InputTag("TriggerResults","","RECO"),
  TrackRefitter = cms.InputTag("TrackRefitter"),
  primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
  Traj = cms.InputTag("TrackRefitter"),
  finalStates = cms.bool(False),
  simulation = cms.bool(True),
  debug = cms.untracked.bool(False),
  runMMC = cms.bool(False)
)
process.dump=cms.EDAnalyzer('EventContentAnalyzer')

process.TFileService = cms.Service("TFileService",
  fileName = cms.string("out_ana.root")
)

process.phlt = cms.Path(process.hltfilter)
process.pDiHiggsWWBBAna = cms.Path(
  process.hltfilter*
  process.DiHiggsWWBBAna
)

process.pdump = cms.Path(process.dump)

process.schedule = cms.Schedule(process.pDiHiggsWWBBAna)