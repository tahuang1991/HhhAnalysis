import random
import ROOT
from ROOT import TFile,TChain,TH1F,TH2F,TLegend
import os
execfile("start.py")
execfile("functions.py")

#Creating folders and parameters
tree_name="DiHiggsWWBBAna/evtree"
os.system("mkdir -p Plots/C")
os.system("mkdir -p HADD")
os.system("rm -rf HADD/*txt")
Lumi=36.42#fb-1

# MC
TT_ch = ROOT.TChain(tree_name)
os.system("find /fdata/hepx/store/user/lpernie/TTTo2L2Nu_13TeV-powheg/crab_TTTo2L2Nu_13TeV-powheg/170329_225351 | grep root | grep -v failed > HADD/TT_TTTo2L2Nu13TeV-powheg.txt")
os.system("cat HADD/TT_* > HADD/TT.txt")
os.system("hadd -T -f -k /fdata/hepx/store/user/lpernie/TTTo2L2Nu_13TeV-powheg/crab_TTTo2L2Nu_13TeV-powheg.root @HADD/TT.txt")
N_tot_path_TT = "/fdata/hepx/store/user/lpernie/TTTo2L2Nu_13TeV-powheg/crab_TTTo2L2Nu_13TeV-powheg.root"
TT_file =  ROOT.TFile.Open(N_tot_path_TT,"read"); h_TT =  ROOT.TH1F(TT_file.Get("DiHiggsWWBBAna/hevent")); nTOT_TT = h_TT.GetBinContent(2);
with open("HADD/TT.txt","r") as f:
  for line in f:
    if not line.isspace():
      TT_ch.Add(str(line[:-1]))
print "TT has", TT_ch.GetEntries(), "entries."
DY_ch = ROOT.TChain(tree_name)
os.system("find /fdata/hepx/store/user/lpernie/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/170329_225403 | grep root | grep -v failed > HADD/DY_DYJetsToLLM-10to50.txt")
os.system("find /fdata/hepx/store/user/lpernie/DYToLL_0J_13TeV-amcatnloFXFX-pythia8/crab_DYToLL_0J_13TeV-amcatnloFXFX-pythia8/170329_225415 | grep root | grep -v failed > HADD/DY_DYToLL0J.txt")
os.system("find /fdata/hepx/store/user/lpernie/DYToLL_1J_13TeV-amcatnloFXFX-pythia8/crab_DYToLL_1J_13TeV-amcatnloFXFX-pythia8/170329_225427 | grep root | grep -v failed > HADD/DY_DYToLL1J.txt")
os.system("find /fdata/hepx/store/user/lpernie/DYToLL_2J_13TeV-amcatnloFXFX-pythia8/crab_DYToLL_2J_13TeV-amcatnloFXFX-pythia8/170329_225439 | grep root | grep -v failed > HADD/DY_DYToLL2J.txt")
os.system("cat HADD/DY_* > HADD/DY.txt")
os.system("hadd -T -f -k /fdata/hepx/store/user/lpernie/DYToLL_2J_13TeV-amcatnloFXFX-pythia8/crab_DYToLL_2J_13TeV-amcatnloFXFX-pythia8.root @HADD/DY.txt")
N_tot_path_DY = "/fdata/hepx/store/user/lpernie/DYToLL_2J_13TeV-amcatnloFXFX-pythia8/crab_DYToLL_2J_13TeV-amcatnloFXFX-pythia8.root"
DY_file =  ROOT.TFile.Open(N_tot_path_DY,"read"); h_DY =  ROOT.TH1F(DY_file.Get("DiHiggsWWBBAna/hevent")); nTOT_DY = h_DY.GetBinContent(2);
with open("HADD/DY.txt","r") as f:
  for line in f:
    if not line.isspace():
      DY_ch.Add(str(line[:-1]))
print "DY has", DY_ch.GetEntries(), "entries."
VV_ch = ROOT.TChain(tree_name)
os.system("find /fdata/hepx/store/user/lpernie/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/170329_225452 | grep root | grep -v failed > HADD/VV_ZZTo2L2Q13TeV.txt")
os.system("find /fdata/hepx/store/user/lpernie/ZZTo2L2Nu_13TeV_powheg_pythia8/crab_ZZTo2L2Nu_13TeV_powheg_pythia8/170329_225504 | grep root | grep -v failed > HADD/VV_ZZTo2L2Nu13TeV.txt")
os.system("find /fdata/hepx/store/user/lpernie/ZZTo4L_13TeV_powheg_pythia8/crab_ZZTo4L_13TeV_powheg_pythia8/170329_225516 | grep root | grep -v failed > HADD/VV_ZZTo4L13TeV.txt")
os.system("find /fdata/hepx/store/user/lpernie/WWToLNuQQ_aTGC_13TeV-madgraph-pythia8/crab_WWToLNuQQ_aTGC_13TeV-madgraph-pythia8/170329_225528 | grep root | grep -v failed > HADD/VV_WWToLNuQQaTGC.txt")
os.system("find /fdata/hepx/store/user/lpernie/WWTo2L2Nu_MWW-600To800_aTGC_13TeV-amcatnloFXFX-madspin-pythia8/crab_WWTo2L2Nu_MWW-600To800_aTGC_13TeV-amcatnloFXFX-madspin-pythia8/170329_225540 | grep root | grep -v failed > HADD/VV_WWTo2L2NuMWW-600To800.txt")
os.system("find /fdata/hepx/store/user/lpernie/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/170329_225553 | grep root | grep -v failed > HADD/VV_WZTo2L2Q13TeV.txt")
os.system("find /fdata/hepx/store/user/lpernie/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/crab_WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/170329_225606 | grep root | grep -v failed > HADD/VV_WZTo1L3Nu13TeV.txt")
os.system("find /fdata/hepx/store/user/lpernie/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/170329_225618 | grep root | grep -v failed > HADD/VV_WZTo1L1Nu2Q13TeV.txt")
os.system("find /fdata/hepx/store/user/lpernie/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/crab_WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/170329_230404 | grep root | grep -v failed > HADD/VV_WZTo3LNuTuneCUETP8M1.txt")
os.system("cat HADD/VV_* > HADD/VV.txt")
os.system("hadd -T -f -k /fdata/hepx/store/user/lpernie/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/crab_WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8.root @HADD/VV.txt")
N_tot_path_VV = "/fdata/hepx/store/user/lpernie/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/crab_WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8.root"
VV_file =  ROOT.TFile.Open(N_tot_path_VV,"read"); h_VV =  ROOT.TH1F(VV_file.Get("DiHiggsWWBBAna/hevent")); nTOT_VV = h_VV.GetBinContent(2);
with open("HADD/VV.txt","r") as f:
  for line in f:
    if not line.isspace():
      VV_ch.Add(str(line[:-1]))
print "VV has", VV_ch.GetEntries(), "entries."
sT_ch = ROOT.TChain(tree_name)
os.system("find /fdata/hepx/store/user/lpernie/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/crab_ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/170329_225903 | grep root | grep -v failed > HADD/sT_STt-channel.txt")
os.system("find /fdata/hepx/store/user/lpernie/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/crab_ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/170329_225915 | grep root | grep -v failed > HADD/sT_STt-channel.txt")
os.system("find /fdata/hepx/store/user/lpernie/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/crab_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/170329_225928 | grep root | grep -v failed > HADD/sT_STs-channel.txt")
os.system("find /fdata/hepx/store/user/lpernie/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/crab_ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/170329_225940 | grep root | grep -v failed > HADD/sT_STtW.txt")
os.system("find /fdata/hepx/store/user/lpernie/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/crab_ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/170329_225952 | grep root | grep -v failed > HADD/sT_STtW.txt")
os.system("cat HADD/sT_* > HADD/sT.txt")
os.system("hadd -T -f -k /fdata/hepx/store/user/lpernie/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/crab_ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1.root @HADD/sT.txt")
N_tot_path_sT = "/fdata/hepx/store/user/lpernie/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/crab_ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1.root"
sT_file =  ROOT.TFile.Open(N_tot_path_sT,"read"); h_sT =  ROOT.TH1F(sT_file.Get("DiHiggsWWBBAna/hevent")); nTOT_sT = h_sT.GetBinContent(2);
with open("HADD/sT.txt","r") as f:
  for line in f:
    if not line.isspace():
      sT_ch.Add(str(line[:-1]))
print "sT has", sT_ch.GetEntries(), "entries."
Wjet_ch = ROOT.TChain(tree_name)
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/170329_230005 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuTuneCUETP8M1.txt")
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170329_230018 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuHT-100To200.txt")
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170329_230031 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuHT-200To400.txt")
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170329_230044 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuHT-400To600.txt")
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170329_230057 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuHT-600To800.txt")
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170329_230110 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuHT-800To1200.txt")
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170329_230123 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuHT-1200To2500.txt")
os.system("find /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170329_230136 | grep root | grep -v failed > HADD/Wjet_WJetsToLNuHT-2500ToInf.txt")
os.system("cat HADD/Wjet_* > HADD/Wjet.txt")
os.system("hadd -T -f -k /fdata/hepx/store/user/lpernie/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root @HADD/Wjet.txt")
N_tot_path_Wjet = "/fdata/hepx/store/user/lpernie/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
Wjet_file =  ROOT.TFile.Open(N_tot_path_Wjet,"read"); h_Wjet =  ROOT.TH1F(Wjet_file.Get("DiHiggsWWBBAna/hevent")); nTOT_Wjet = h_Wjet.GetBinContent(2);
with open("HADD/Wjet.txt","r") as f:
  for line in f:
    if not line.isspace():
      Wjet_ch.Add(str(line[:-1]))
print "Wjet has", Wjet_ch.GetEntries(), "entries."
ttV_ch = ROOT.TChain(tree_name)
os.system("find /fdata/hepx/store/user/lpernie/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/crab_TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/170329_230150 | grep root | grep -v failed > HADD/ttV_TTWJetsToQQTuneCUETP8M1.txt")
os.system("find /fdata/hepx/store/user/lpernie/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/crab_TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/170329_230202 | grep root | grep -v failed > HADD/ttV_TTWJetsToLNuTuneCUETP8M1.txt")
os.system("find /fdata/hepx/store/user/lpernie/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/170329_230216 | grep root | grep -v failed > HADD/ttV_TTZToQQTuneCUETP8M1.txt")
os.system("cat HADD/ttV_* > HADD/ttV.txt")
os.system("hadd -T -f -k /fdata/hepx/store/user/lpernie/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8.root @HADD/ttV.txt")
N_tot_path_ttV = "/fdata/hepx/store/user/lpernie/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8.root"
ttV_file =  ROOT.TFile.Open(N_tot_path_ttV,"read"); h_ttV =  ROOT.TH1F(ttV_file.Get("DiHiggsWWBBAna/hevent")); nTOT_ttV = h_ttV.GetBinContent(2);
with open("HADD/ttV.txt","r") as f:
  for line in f:
    if not line.isspace():
      ttV_ch.Add(str(line[:-1]))
print "ttV has", ttV_ch.GetEntries(), "entries."
os.system("find /fdata/hepx/store/user/lpernie/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/crab_TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/170329_230228 | grep root | grep -v failed > HADD/ttV_TTZToLLNuNuM-10.txt")
# Data
DATA_ch = ROOT.TChain(tree_name)
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016B-23Sep2016-v3/170329_223804 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016B-23Sep2016-v3.txt")
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016C-23Sep2016-v1/170329_223816 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016C-23Sep2016-v1.txt")
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016D-23Sep2016-v1/170329_223828 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016D-23Sep2016-v1.txt")
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016E-23Sep2016-v1/170329_223841 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016E-23Sep2016-v1.txt")
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016F-23Sep2016-v1/170329_223852 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016F-23Sep2016-v1.txt")
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016G-23Sep2016-v1/170329_223905 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016G-23Sep2016-v1.txt")
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016H-03Feb2017_ver2-v1/170330_194716 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016H-03Feb2017_ver2-v1.txt")
os.system("find /fdata/hepx/store/user/lpernie/DoubleMuon/crab_Hhh_Run2016H-03Feb2017_ver3-v1/170330_194729 | grep root | grep -v failed > HADD/DATA_Hhh_Run2016H-03Feb2017_ver3-v1.txt")

os.system("cat HADD/DATA_* > HADD/DATA.txt")
with open("HADD/DATA.txt","r") as f:
  for line in f:
    if not line.isspace():
      DATA_ch.Add(str(line[:-1]))
print "DATA has", DATA_ch.GetEntries(), "entries."

# Dataset to plot
filelist   = [ttV_ch, Wjet_ch, sT_ch, VV_ch, DY_ch, TT_ch, DATA_ch] #If you draw a StackPlot place the smaller samples at the beginning and data as last one
benchmarks = ["ttV", "Wjet", "singTop", "VV", "DY", "TTbar", "Data"]
nTOT       = [nTOT_ttV, nTOT_Wjet, nTOT_sT, nTOT_VV, nTOT_DY, nTOT_TT, 1]
#Cuts and Ordering
cut = "met_pt>20 && b1jet_pt>30 && b2jet_pt>30 && muon1_pt>20 && muon2_pt>20"

#---Starting to plot histos here-------------------------------------------------------------------------------------------------------------------------------------
NORM=["lumi"] #NORM=["unity","lumi"]
DataOrMC="DataMC" # MC or DATA = all samples overimposed, DataMC = MC is stack, data is overimposed
LOG=["yes"]#,"no"] # You can choose if you want the plots to be log, linear or both
Format=[".pdf",".C"]
for this_LOG in LOG:
  for this_Norm in NORM:
    #GEN
    #RECO Di-Leptons
    draw1D(filelist, "muon1_pt", "(50,10,100)", "P_{T} [GeV]", cut, benchmarks, "h_MU1_pt", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "muon2_pt", "(50,10,100)", "P_{T} [GeV]", cut, benchmarks, "h_MU2_pt", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "muon1_eta", "(50,-3,3)", "#eta", cut, benchmarks, "h_MU1_eta", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "muon2_eta", "(50,-3,3)", "#eta", cut, benchmarks, "h_MU2_eta", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "mass_l1l2", "(40,20,150)", "m(l,l)", cut, benchmarks, "h_M_l1l2", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "dR_l1l2", "(50,0,5)", "#Delta R(l,l)", cut, benchmarks, "h_DR_l1l2", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    #RECO Di-Jets
    draw1D(filelist, "b1jet_pt", "(50,20,200)", "P_{T} [GeV]", cut, benchmarks, "h_J1_pt", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "b2jet_pt", "(50,20,100)", "P_{T} [GeV]", cut, benchmarks, "h_J2_pt", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "b1jet_eta", "(50,-3.,3.)", "#eta", cut, benchmarks, "h_J1_eta", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "b2jet_eta", "(50,-3.,3.)", "#eta", cut, benchmarks, "h_J2_eta", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "mass_b1b2", "(40,40,180)", "m(j,j)", cut, benchmarks, "h_M_b1b2", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "dR_b1b2", "(50,0,5)", "#Delta R(j,j)", cut, benchmarks, "h_DR_b1b2", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    #RECO MIX
    draw1D(filelist, "mass_trans", "(50,10,150)", "M_{tran} [GeV]", cut, benchmarks, "h_MT", Lumi, NORM)
    draw1D(filelist, "dR_l1l2b1b2", "(50,0,5)", "#Delta R(lljj)", cut, benchmarks, "h_dR_l1l2b1b2", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
    draw1D(filelist, "dphi_llmet", "(50,-4,4)", "#Delta #phi (ll,MET)", cut, benchmarks, "h_Dphi_llmet", Lumi, nTOT, this_Norm, DataOrMC, this_LOG, Format)
