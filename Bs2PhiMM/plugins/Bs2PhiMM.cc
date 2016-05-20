// -*- C++ -*-
//
// Package:    Run2-Bs2PhiMM/Bs2PhiMM
// Class:      Bs2PhiMM
// 
/**\class Bs2PhiMM Bs2PhiMM.cc Run2-Bs2PhiMM/Bs2PhiMM/plugins/Bs2PhiMM.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//  NTUPLE CREATOR FOR RUN2 Bs --> Phi(KK) mu+ mu- ANALYSIS 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//
//    Author:  Niladribihari Sahoo 
//   Created: Fri, 20 May 2016 08:24:52 GMT
//     Email: "nsahoo@cern.ch" or "niladri.sahoo12@gmail.com"
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//
// class declaration
//

class Bs2PhiMM : public edm::EDAnalyzer {
   public:
      explicit Bs2PhiMM(const edm::ParameterSet&);
      ~Bs2PhiMM();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
Bs2PhiMM::Bs2PhiMM(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

}


Bs2PhiMM::~Bs2PhiMM()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
Bs2PhiMM::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;



#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
Bs2PhiMM::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
Bs2PhiMM::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
Bs2PhiMM::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
Bs2PhiMM::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
Bs2PhiMM::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
Bs2PhiMM::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
Bs2PhiMM::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(Bs2PhiMM);
