#include "RiceStyle.h"

using namespace std;

void plot_SC_centrality(){

	TFile* file = new TFile("../dataPoints/PbPb_5TeV_Centrality.root");

	TGraphErrors* gr1 = (TGraphErrors*) file->Get("Graph;1");
	TGraphErrors* gr2 = (TGraphErrors*) file->Get("Graph;2");

	TCanvas* c1 = new TCanvas("c1","c1",1,1,600,600);
	gPad->SetLeftMargin(0.20);
	gPad->SetBottomMargin(0.13);
	gPad->SetTopMargin(0.06);
	gPad->SetTicks();

	TGaxis::SetMaxDigits(3);

	TH1D* base1 = makeHist("base1", "", "Centrality", "SC(m,n)", 100,0,100,kBlack);

	base1->GetYaxis()->SetRangeUser(-0.000003,0.000005);
	base1->GetXaxis()->SetRangeUser(0, 70);
	base1->GetXaxis()->SetTitleColor(kBlack);
	
	fixedFontHist1D(base1,1.1,1.25);

	base1->GetYaxis()->SetTitleOffset(1.3);
	base1->GetXaxis()->SetTitleOffset(0.95);
	base1->GetYaxis()->SetTitleSize(base1->GetYaxis()->GetTitleSize()*1.3);
	base1->GetXaxis()->SetTitleSize(base1->GetXaxis()->GetTitleSize()*1.4);
	base1->GetYaxis()->SetLabelSize(base1->GetYaxis()->GetLabelSize()*1.4);
	base1->GetXaxis()->SetLabelSize(base1->GetXaxis()->GetLabelSize()*1.4);

	base1->Draw();

	gr1->SetMarkerStyle(20);
	gr1->SetMarkerSize(1.4);
	gr1->SetMarkerColor(kBlue);
	gr1->SetLineColor(kBlue);
	gr1->Draw("Psame");

	gr2->SetMarkerStyle(21);
	gr2->SetMarkerSize(1.4);
	gr2->SetMarkerColor(kRed);
	gr2->SetLineColor(kRed);
	gr2->Draw("Psame");

	TLegend *w2 = new TLegend(0.25,0.3,0.5,0.4);
    w2->SetLineColor(kWhite);
    w2->SetFillColor(0);
    w2->SetTextSize(20);
    w2->SetTextFont(43);
    w2->AddEntry(gr2, "SC(4,2)", "P");
    w2->AddEntry(gr1, "SC(3,2)", "P");
    w2->Draw("same");

    TLatex* r3 = new TLatex(0.23, 0.87, "PbPb #sqrt{s_{NN}} = 5.02 TeV");
    r3->SetNDC();
    r3->SetTextSize(23);
    r3->SetTextFont(43);
    r3->SetTextColor(kBlack);
    r3->Draw("same");

    TLatex* r4 = new TLatex(0.23, 0.82, "0.3 #leq p_{T} < 5.0 GeV");
    r4->SetNDC();
    r4->SetTextSize(23);
    r4->SetTextFont(43);
    r4->SetTextColor(kBlack);
    r4->Draw("same");

    TLatex* r5 = new TLatex(0.23, 0.76, "|#eta| < 0.8");
    r5->SetNDC();
    r5->SetTextSize(23);
    r5->SetTextFont(43);
    r5->SetTextColor(kBlack);
    r5->Draw("same");

}