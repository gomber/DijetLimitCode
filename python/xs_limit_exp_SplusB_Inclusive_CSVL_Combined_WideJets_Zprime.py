#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()


masses = array('d', [1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0])
xs_comb_0p1 = array('d', [0.4289, 0.32401400000000002, 0.240568, 0.18908900000000001, 0.15723100000000001, 0.12995399999999999, 0.099915100000000007, 0.081588300000000002, 0.063999899999999998, 0.051599899999999997, 0.049041899999999999, 0.034229900000000001, 0.031110200000000001, 0.0249704, 0.022138600000000001, 0.01754, 0.017239500000000001, 0.0123388, 0.010970199999999999, 0.0096643700000000003, 0.0078150300000000006, 0.00677715, 0.0060796000000000001, 0.0049029800000000004, 0.00416096, 0.0037323399999999998, 0.00328773, 0.0029468200000000002, 0.0025079199999999999, 0.0021405500000000002, 0.0018841800000000001])
xs_comb_1p0 = array('d', [0.230407, 0.16552, 0.14075199999999999, 0.106697, 0.092528899999999997, 0.080888000000000002, 0.073737200000000003, 0.061639699999999999, 0.054559799999999999, 0.048937399999999999, 0.041352699999999999, 0.032641799999999999, 0.0290809, 0.024971699999999999, 0.023012999999999999, 0.018338699999999999, 0.016216100000000001, 0.013420899999999999, 0.012352200000000001, 0.010660299999999999, 0.0092406299999999997, 0.0079368200000000007, 0.0069036000000000002, 0.0060510099999999999, 0.0051682899999999999, 0.0046795099999999996, 0.0042695900000000002, 0.0036036100000000001, 0.0031934200000000002, 0.0028628299999999998, 0.0024946299999999999])
xs_incl_0p1 = array('d', [0.51581500000000002, 0.32366400000000001, 0.23811199999999999, 0.19048200000000001, 0.153582, 0.121658, 0.097132099999999999, 0.081093100000000001, 0.063999399999999998, 0.057239600000000002, 0.045206000000000003, 0.037742900000000003, 0.028114699999999999, 0.024686400000000001, 0.0227049, 0.0173267, 0.014837899999999999, 0.0130229, 0.011240099999999999, 0.0095978899999999995, 0.0081266199999999993, 0.0066717800000000004, 0.0060324699999999998, 0.0048620599999999996, 0.0043463099999999999, 0.0038874700000000001, 0.0032159900000000002, 0.0028833000000000001, 0.0024427199999999998, 0.0021274000000000002, 0.0020668499999999999])
xs_incl_1p0 = array('d', [0.55163499999999999, 0.399785, 0.32835399999999998, 0.23843300000000001, 0.19237299999999999, 0.17569000000000001, 0.13170299999999999, 0.100481, 0.082810099999999998, 0.077056899999999998, 0.056060400000000003, 0.049362299999999998, 0.037326699999999997, 0.032968600000000001, 0.027611799999999999, 0.023858799999999999, 0.020653899999999999, 0.018373500000000001, 0.017529599999999999, 0.012863100000000001, 0.011343900000000001, 0.0093021700000000002, 0.0080198500000000002, 0.0066647499999999997, 0.0057494399999999998, 0.0050854999999999997, 0.0044630900000000003, 0.0038278800000000001, 0.0032757099999999998, 0.0029319799999999998, 0.0027474999999999999])

g_comb_0p1 = TGraph(len(masses),masses,xs_comb_0p1)
g_comb_0p1.SetMarkerStyle(24)
g_comb_0p1.SetMarkerColor(kRed)
g_comb_0p1.SetLineWidth(2)
g_comb_0p1.SetLineStyle(1)
g_comb_0p1.SetLineColor(kRed)
g_comb_0p1.GetXaxis().SetTitle("Resonance Mass [GeV]")
g_comb_0p1.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
g_comb_0p1.GetYaxis().SetRangeUser(1e-03,10)
g_comb_0p1.GetXaxis().SetNdivisions(1005)

g_comb_1p0 = TGraph(len(masses),masses,xs_comb_1p0)
g_comb_1p0.SetMarkerStyle(25)
g_comb_1p0.SetMarkerColor(kRed)
g_comb_1p0.SetLineWidth(2)
g_comb_1p0.SetLineStyle(2)
g_comb_1p0.SetLineColor(kRed)

g_incl_0p1 = TGraph(len(masses),masses,xs_incl_0p1)
g_incl_0p1.SetMarkerStyle(26)
g_incl_0p1.SetMarkerColor(kGreen+2)
g_incl_0p1.SetLineWidth(2)
g_incl_0p1.SetLineStyle(1)
g_incl_0p1.SetLineColor(kGreen+2)

g_incl_1p0 = TGraph(len(masses),masses,xs_incl_1p0)
g_incl_1p0.SetMarkerStyle(27)
g_incl_1p0.SetMarkerColor(kGreen+2)
g_incl_1p0.SetLineWidth(2)
g_incl_1p0.SetLineStyle(2)
g_incl_1p0.SetLineColor(kGreen+2)

c = TCanvas("c", "",800,800)
c.cd()

g_comb_0p1.Draw("ALP")
g_comb_1p0.Draw("LP")
g_incl_0p1.Draw("LP")
g_incl_1p0.Draw("LP")

legend = TLegend(.45,.60,.85,.80)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader("Exp. 95% CL Upper Limits (stat. only)")
legend.AddEntry(g_comb_0p1, "Combined b-tagged (f_{b#bar{b}} = 0.1)","lp")
legend.AddEntry(g_comb_1p0, "Combined b-tagged (f_{b#bar{b}} = 1.0)","lp")
legend.AddEntry(g_incl_0p1, "Inclusive untagged (f_{b#bar{b}} = 0.1)","lp")
legend.AddEntry(g_incl_1p0, "Inclusive untagged (f_{b#bar{b}} = 1.0)","lp")
legend.Draw()

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetNDC()
l1.SetTextSize(0.035)
l1.DrawLatex(0.70,0.52, "f_{b#bar{b}} = #frac{BR(X#rightarrowb#bar{b})}{BR(X#rightarrowjj)}")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.89, "Z'-like")
l1.SetTextSize(0.04)
l1.DrawLatex(0.18,0.43, "CMS Preliminary")
l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
l1.DrawLatex(0.18,0.20, "Wide Jets")

c.SetLogy()
c.SaveAs('SplusB_Inclusive_CSVL_Combined_limit_exp_WideJets_Zprime.eps')

