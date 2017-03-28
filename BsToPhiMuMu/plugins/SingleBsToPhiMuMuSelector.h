//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Mar 28 12:34:25 2017 by ROOT version 6.06/01
// from TTree tree/Bs->J/psi kaskey menos ntuple
// found on file: ../python/BsToPhiMuMu_2016B_10k.root
//////////////////////////////////////////////////////////

#ifndef SingleBsToPhiMuMuSelector_h
#define SingleBsToPhiMuMuSelector_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>
#include <TTreeReaderArray.h>

// Headers needed by this particular selector
#include <string>

#include <vector>



class SingleBsToPhiMuMuSelector : public TSelector {
public :
   TTreeReader     fReader;  //!the tree reader
   TTree          *fChain = 0;   //!pointer to the analyzed TTree or TChain

   // Readers to access the data (delete the ones you do not need).
   TTreeReaderValue<UInt_t> run = {fReader, "run"};
   TTreeReaderValue<UInt_t> event = {fReader, "event"};
   TTreeReaderValue<UInt_t> lumiblock = {fReader, "lumiblock"};
   TTreeReaderValue<UInt_t> nprivtx = {fReader, "nprivtx"};
   TTreeReaderArray<string> triggernames = {fReader, "triggernames"};
   TTreeReaderArray<int> triggerprescales = {fReader, "triggerprescales"};
   TTreeReaderArray<double> mumdcabs = {fReader, "mumdcabs"};
   TTreeReaderArray<double> mumdcabserr = {fReader, "mumdcabserr"};
   TTreeReaderArray<double> mumpx = {fReader, "mumpx"};
   TTreeReaderArray<double> mumpy = {fReader, "mumpy"};
   TTreeReaderArray<double> mumpz = {fReader, "mumpz"};
   TTreeReaderArray<double> mupdcabs = {fReader, "mupdcabs"};
   TTreeReaderArray<double> mupdcabserr = {fReader, "mupdcabserr"};
   TTreeReaderArray<double> muppx = {fReader, "muppx"};
   TTreeReaderArray<double> muppy = {fReader, "muppy"};
   TTreeReaderArray<double> muppz = {fReader, "muppz"};
   TTreeReaderArray<double> mumutrkr = {fReader, "mumutrkr"};
   TTreeReaderArray<double> mumutrkz = {fReader, "mumutrkz"};
   TTreeReaderArray<double> mumudca = {fReader, "mumudca"};
   TTreeReaderArray<double> mumuvtxcl = {fReader, "mumuvtxcl"};
   TTreeReaderArray<double> mumulsbs = {fReader, "mumulsbs"};
   TTreeReaderArray<double> mumulsbserr = {fReader, "mumulsbserr"};
   TTreeReaderArray<double> mumucosalphabs = {fReader, "mumucosalphabs"};
   TTreeReaderArray<double> mumucosalphabserr = {fReader, "mumucosalphabserr"};
   TTreeReaderArray<double> mumumass = {fReader, "mumumass"};
   TTreeReaderArray<double> mumumasserr = {fReader, "mumumasserr"};
   TTreeReaderValue<vector<bool>> mumisgoodmuon = {fReader, "mumisgoodmuon"};
   TTreeReaderValue<vector<bool>> mupisgoodmuon = {fReader, "mupisgoodmuon"};
   TTreeReaderArray<int> mumnpixhits = {fReader, "mumnpixhits"};
   TTreeReaderArray<int> mupnpixhits = {fReader, "mupnpixhits"};
   TTreeReaderArray<int> mumnpixlayers = {fReader, "mumnpixlayers"};
   TTreeReaderArray<int> mupnpixlayers = {fReader, "mupnpixlayers"};
   TTreeReaderArray<int> mumntrkhits = {fReader, "mumntrkhits"};
   TTreeReaderArray<int> mupntrkhits = {fReader, "mupntrkhits"};
   TTreeReaderArray<int> mumntrklayers = {fReader, "mumntrklayers"};
   TTreeReaderArray<int> mupntrklayers = {fReader, "mupntrklayers"};
   TTreeReaderArray<double> mumnormchi2 = {fReader, "mumnormchi2"};
   TTreeReaderArray<double> mupnormchi2 = {fReader, "mupnormchi2"};
   TTreeReaderArray<int> mumtrkqual = {fReader, "mumtrkqual"};
   TTreeReaderArray<int> muptrkqual = {fReader, "muptrkqual"};
   TTreeReaderArray<double> mumdxyvtx = {fReader, "mumdxyvtx"};
   TTreeReaderArray<double> mupdxyvtx = {fReader, "mupdxyvtx"};
   TTreeReaderArray<double> mumdzvtx = {fReader, "mumdzvtx"};
   TTreeReaderArray<double> mupdzvtx = {fReader, "mupdzvtx"};
   TTreeReaderArray<string> mumtriglastfilter = {fReader, "mumtriglastfilter"};
   TTreeReaderArray<string> muptriglastfilter = {fReader, "muptriglastfilter"};
   TTreeReaderArray<double> mumpt = {fReader, "mumpt"};
   TTreeReaderArray<double> muppt = {fReader, "muppt"};
   TTreeReaderArray<double> mumeta = {fReader, "mumeta"};
   TTreeReaderArray<double> mupeta = {fReader, "mupeta"};
   TTreeReaderArray<double> kptrkdcabs = {fReader, "kptrkdcabs"};
   TTreeReaderArray<double> kptrkdcabserr = {fReader, "kptrkdcabserr"};
   TTreeReaderArray<double> kmtrkdcabs = {fReader, "kmtrkdcabs"};
   TTreeReaderArray<double> kmtrkdcabserr = {fReader, "kmtrkdcabserr"};
   TTreeReaderArray<int> kpchg = {fReader, "kpchg"};
   TTreeReaderArray<double> kppx = {fReader, "kppx"};
   TTreeReaderArray<double> kppy = {fReader, "kppy"};
   TTreeReaderArray<double> kppz = {fReader, "kppz"};
   TTreeReaderArray<int> kmchg = {fReader, "kmchg"};
   TTreeReaderArray<double> kmpx = {fReader, "kmpx"};
   TTreeReaderArray<double> kmpy = {fReader, "kmpy"};
   TTreeReaderArray<double> kmpz = {fReader, "kmpz"};
   TTreeReaderArray<double> phimass = {fReader, "phimass"};
   TTreeReaderValue<Int_t> nb = {fReader, "nb"};
   TTreeReaderArray<double> bpx = {fReader, "bpx"};
   TTreeReaderArray<double> bpxerr = {fReader, "bpxerr"};
   TTreeReaderArray<double> bpy = {fReader, "bpy"};
   TTreeReaderArray<double> bpyerr = {fReader, "bpyerr"};
   TTreeReaderArray<double> bpz = {fReader, "bpz"};
   TTreeReaderArray<double> bpzerr = {fReader, "bpzerr"};
   TTreeReaderArray<double> bmass = {fReader, "bmass"};
   TTreeReaderArray<double> bmasserr = {fReader, "bmasserr"};
   TTreeReaderArray<double> bvtxcl = {fReader, "bvtxcl"};
   TTreeReaderArray<double> bvtxx = {fReader, "bvtxx"};
   TTreeReaderArray<double> bvtxxerr = {fReader, "bvtxxerr"};
   TTreeReaderArray<double> bvtxy = {fReader, "bvtxy"};
   TTreeReaderArray<double> bvtxyerr = {fReader, "bvtxyerr"};
   TTreeReaderArray<double> bvtxz = {fReader, "bvtxz"};
   TTreeReaderArray<double> bvtxzerr = {fReader, "bvtxzerr"};
   TTreeReaderArray<double> bcosalphabs = {fReader, "bcosalphabs"};
   TTreeReaderArray<double> bcosalphabserr = {fReader, "bcosalphabserr"};
   TTreeReaderArray<double> bcosalphabs2d = {fReader, "bcosalphabs2d"};
   TTreeReaderArray<double> bcosalphabs2derr = {fReader, "bcosalphabs2derr"};
   TTreeReaderArray<double> blsbs = {fReader, "blsbs"};
   TTreeReaderArray<double> blsbserr = {fReader, "blsbserr"};
   TTreeReaderArray<double> bctau = {fReader, "bctau"};
   TTreeReaderArray<double> bctauerr = {fReader, "bctauerr"};


   SingleBsToPhiMuMuSelector(TTree * /*tree*/ =0) { }
   virtual ~SingleBsToPhiMuMuSelector() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();

   ClassDef(SingleBsToPhiMuMuSelector,0);

};

#endif

#ifdef SingleBsToPhiMuMuSelector_cxx
void SingleBsToPhiMuMuSelector::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the reader is initialized.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   fReader.SetTree(tree);
}

Bool_t SingleBsToPhiMuMuSelector::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}


#endif // #ifdef SingleBsToPhiMuMuSelector_cxx
