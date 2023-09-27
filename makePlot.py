import ROOT
from math import sqrt
from measurement import measurement
from graphs import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)

from measurementData import measurements

measurements_all = []
measurements_direct = []
measurements_indirect = []
measurements_other = []
measurements_boosted = []

for (category, channel, com, method, ref, mt, stat, sysdown, sysup) in measurements:
    m = measurement(channel+", "+method+", "+com+" TeV")
    if mt is None:
        continue
    if stat is None:
        stat = 0.
    m.setResult(mt, stat, sysdown, sysup)
    m.setReference(ref)
    if category == "direct":
        m.setColor(ROOT.kRed)
        measurements_direct.append(m)
        measurements_all.append(m)
    elif category == "indirect":
        m.setColor(ROOT.kAzure+7)
        measurements_indirect.append(m)
        measurements_all.append(m)
    elif category == "other":
        m.setColor(ROOT.kOrange-6)
        measurements_other.append(m)
        measurements_all.append(m)
    elif category == "boosted":
        m.setColor(ROOT.kOrange-6)
        measurements_boosted.append(m)
        measurements_all.append(m)

Nall = len(measurements_all)
Ndirect = len(measurements_direct)
Nindirect = len(measurements_indirect)
Nother = len(measurements_other)
Nboosted = len(measurements_boosted)

################################################################################
## Contruct results graphs and labels
g_direct_tot = ROOT.TGraphAsymmErrors(len(measurements_direct))
g_indirect_tot = ROOT.TGraphAsymmErrors(len(measurements_indirect))
g_other_tot = ROOT.TGraphAsymmErrors(len(measurements_other))
g_boosted_tot = ROOT.TGraphAsymmErrors(len(measurements_boosted))
g_direct_stat = ROOT.TGraphAsymmErrors(len(measurements_direct))
g_indirect_stat = ROOT.TGraphAsymmErrors(len(measurements_indirect))
g_other_stat = ROOT.TGraphAsymmErrors(len(measurements_other))
g_boosted_stat = ROOT.TGraphAsymmErrors(len(measurements_boosted))

t_mt_values = []
t_title = []
t_category = []
t_ref = []

index = Nall-1+9
index_max = index
index_direct_max = -1
index_direct_min = -1
index_indirect_max = -1
index_indirect_min = -1
index_other_max = -1
index_other_min = -1

t_category.append( (index, "Indirect measurements") )
index = index -1
for i, m in enumerate(measurements_indirect):
    if i==0:
        index_indirect_max = index
    if i==len(measurements_indirect)-1:
        index_indirect_min = index
    g_indirect_tot.SetPoint(i, m.mtop(), index)
    g_indirect_tot.SetPointError(i, m.uncertTotalDown(), m.uncertTotalUp(), 0.0, 0.0)
    g_indirect_stat.SetPoint(i, m.mtop(), index)
    g_indirect_stat.SetPointError(i, m.uncertStat(), m.uncertStat(), 0.0, 0.0)
    t_mt_values.append( (index, "#it{m}_{t}^{pole} = "+m.mt_string()) )
    t_title.append( (index, m.infoString()) )
    t_ref.append( (index, m.reference()) )
    index = index -1

index_line1 = index
index = index -1
t_category.append( (index, "Direct measurements") )
index = index -1
t_category.append( (index, "Full Reconstruction") )
index = index -1


for i, m in enumerate(measurements_direct):
    if i==0:
        index_direct_max = index
    if i==len(measurements_direct)-1:
        index_direct_min = index
    g_direct_tot.SetPoint(i, m.mtop(), index)
    g_direct_tot.SetPointError(i, m.uncertTotalDown(), m.uncertTotalUp(), 0.0, 0.0)
    g_direct_stat.SetPoint(i, m.mtop(), index)
    g_direct_stat.SetPointError(i, m.uncertStat(), m.uncertStat(), 0.0, 0.0)
    t_mt_values.append( (index, "#it{m}_{t}^{MC} = "+m.mt_string()) )
    t_title.append( (index, m.infoString()) )
    t_ref.append( (index, m.reference()) )
    index = index -1

index = index -1
t_category.append( (index, "Boosted measurements") )
index = index -1

for i, m in enumerate(measurements_boosted):
    if i==0:
        index_boosted_max = index
    if i==len(measurements_boosted)-1:
        index_boosted_min = index
    g_boosted_tot.SetPoint(i, m.mtop(), index)
    g_boosted_tot.SetPointError(i, m.uncertTotalDown(), m.uncertTotalUp(), 0.0, 0.0)
    g_boosted_stat.SetPoint(i, m.mtop(), index)
    g_boosted_stat.SetPointError(i, m.uncertStat(), m.uncertStat(), 0.0, 0.0)
    t_mt_values.append( (index, "#it{m}_{t}^{MC} = "+m.mt_string()) )
    t_title.append( (index, m.infoString()) )
    t_ref.append( (index, m.reference()) )
    index = index -1

index = index -1
t_category.append( (index, "Alternative measurements") )
index = index -1

for i, m in enumerate(measurements_other):
    if i==0:
        index_other_max = index
    if i==len(measurements_other)-1:
        index_other_min = index
    g_other_tot.SetPoint(i, m.mtop(), index)
    g_other_tot.SetPointError(i, m.uncertTotalDown(), m.uncertTotalUp(), 0.0, 0.0)
    g_other_stat.SetPoint(i, m.mtop(), index)
    g_other_stat.SetPointError(i, m.uncertStat(), m.uncertStat(), 0.0, 0.0)
    if "endpoint" in m.title():
        t_mt_values.append( (index, "#it{m}_{t}^{     } = "+m.mt_string()) )
    else:
        t_mt_values.append( (index, "#it{m}_{t}^{MC} = "+m.mt_string()) )
    t_title.append( (index, m.infoString()) )
    t_ref.append( (index, m.reference()) )
    index = index -1

color_stat = ROOT.TColor.GetColor("#2b2b2b")
color_tot = ROOT.TColor.GetColor("#2b2b2b")

setResultStyle(g_direct_tot, color_tot, color_tot)
setResultStyle(g_indirect_tot, color_tot, color_tot)
setResultStyle(g_other_tot, color_tot, color_tot)
setResultStyle(g_boosted_tot, color_tot, color_tot)

setResultStyle(g_direct_stat, color_tot, color_stat, option="stat")
setResultStyle(g_indirect_stat, color_tot, color_stat, option="stat")
setResultStyle(g_other_stat, color_tot, color_stat, option="stat")
setResultStyle(g_boosted_stat, color_tot, color_stat, option="stat")

################################################################################
## Contruct prediction graphs

# for direct and other use CMS Run1 combination
g_predict_direct_stat, g_predict_direct_tot, l_direct = getPredictionGraph(index_other_min-0.5, index_direct_max+0.5, 172.52, 0.14, 0.42, 0.42)

# for indirect use ATLAS+CMS combination
g_predict_indirect_stat, g_predict_indirect_tot, l_indirect = getPredictionGraph(index_indirect_min-0.5, index_indirect_max+0.5, 173.4, 0.0, 2.0, 1.8)

direct_inner_color = ROOT.TColor.GetColor("#5668cc")
direct_outer_color = ROOT.TColor.GetColor("#b5bff7")
direct_line_color = ROOT.TColor.GetColor("#1935d1")
indirect_outer_color = ROOT.TColor.GetColor("#d66f6f")
indirect_line_color = ROOT.TColor.GetColor("#8f2727")

setPredictionStyle(g_predict_direct_stat, direct_inner_color, direct_line_color)
setPredictionStyle(g_predict_direct_tot, direct_outer_color, direct_line_color)
setPredictionLineStyle(l_direct, direct_line_color)

# setPredictionStyle(g_predict_indirect_stat, ROOT.)
setPredictionStyle(g_predict_indirect_tot, indirect_outer_color, indirect_line_color)
setPredictionLineStyle(l_indirect, indirect_line_color)

################################################################################
# Set up the canvas and draw a dummy graph to have full control over the axes ranges
c = ROOT.TCanvas("", "", 900, 1200)
ROOT.gStyle.SetLegendBorderSize(0)
# ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetEndErrorSize(5)

margin_top = 0.01
margin_bottom = 0.07
margin_left = 0.01
margin_right = 0.01


ROOT.gPad.SetTopMargin(margin_top)
ROOT.gPad.SetBottomMargin(margin_bottom)
ROOT.gPad.SetLeftMargin(margin_left)
ROOT.gPad.SetRightMargin(margin_right)

xmin = 142
xmax = 206
ymin = -2
ymax = index_max+5

# Needed to calculate abolute positions for y
height_plot = 1-margin_top-margin_bottom
yrange = ymax-ymin
y_perindex = height_plot/yrange

# Needed to calculate abolute positions for x
width_plot = 1-margin_left-margin_right
xrange = xmax-xmin
x_perGeV = width_plot/xrange

dummy_results = getDummyGraph(xmin, xmax, -1, Nall+2)
dummy_results.Draw("AP")
dummy_results.GetXaxis().SetRangeUser(xmin, xmax)
dummy_results.GetYaxis().SetRangeUser(ymin, ymax)


################################################################################
# Draw "prediction" bands and results
g_predict_direct_tot.Draw("E2 SAME")
g_predict_direct_stat.Draw("E2 SAME")
l_direct.Draw("SAME")

g_predict_indirect_tot.Draw("E2 SAME")
l_indirect.Draw("SAME")

g_direct_tot.Draw("P SAME")
g_indirect_tot.Draw("P SAME")
g_boosted_tot.Draw("P SAME")
g_other_tot.Draw("P SAME")
g_direct_stat.Draw("P SAME")
g_indirect_stat.Draw("P SAME")
g_boosted_stat.Draw("P SAME")
g_other_stat.Draw("P SAME")

################################################################################
# Lines to divide the methods
line1 = ROOT.TLine(xmin, index_line1, xmax, index_line1)
for l in [line1]:
    l.SetLineColor(15)
    l.SetLineWidth(2)
    l.Draw("SAME")

################################################################################
# Format all text and put it into a list that is drawn later
allTexts = []
x_mt = 0.63
for (index, text) in t_mt_values:
    y = margin_bottom + (index-ymin)*y_perindex
    t_latex = addText(x_mt, y, text)
    allTexts.append(t_latex)

x_ref = 0.875
for (index, text) in t_ref:
    y = margin_bottom + (index-ymin)*y_perindex
    t_latex = addText(x_ref, y, text, font=43, size=10, color=15)
    allTexts.append(t_latex)

x_title = margin_left + 0.01
for (index, text) in t_title:
    y = margin_bottom + (index-ymin)*y_perindex
    t_latex = addText(x_title, y, text, font=43, size=16)
    allTexts.append(t_latex)

for (index, text) in t_category:
    y = margin_bottom + (index-ymin)*y_perindex
    x = x_title
    fontsize = 22
    if "Boosted" in text or "Alternative" in text or "Full Reconstruction" in text:
        fontsize = 18
        y -= 0.007
        # x += 0.01
    t_latex = addText(x, y+0.007, text, font=43, size=fontsize, color=16)
    allTexts.append(t_latex)
################################################################################
# CMS logo
allTexts.append(getCMS(margin_left+0.01, 1-margin_top-0.02))

################################################################################
# Legend
leg = ROOT.TLegend(.60, .89, .9, 1-margin_top-0.01)
leg.SetTextSize(0.015)
leg.AddEntry(g_predict_indirect_tot, "ATLAS+CMS combination #it{m}_{t}^{pole} = 173.4^{#plus1.8}_{#minus2.0} GeV", "fl")
leg.AddEntry(g_predict_direct_tot, "CMS 7+8 TeV comb. #it{m}_{t}^{MC} = 172.52 #pm 0.42 GeV", "fl")
leg.AddEntry(g_predict_direct_stat, "CMS 7+8 TeV comb. stat. uncertainty", "fl")
leg.Draw()

################################################################################
# Create a Marker for the legend and label stat. and tot. uncertainty bars
leg_marker_x = 173
leg_marker_y = ymax-2
leg_marker_statUncert = 2
leg_marker_totUncert = 5

legend_marker_tot = ROOT.TGraphErrors(1)
legend_marker_stat = ROOT.TGraphErrors(1)
legend_marker_tot.SetPoint(1, leg_marker_x, leg_marker_y)
legend_marker_tot.SetPointError(1, leg_marker_totUncert, 0.0)
legend_marker_stat.SetPoint(1, leg_marker_x, leg_marker_y)
legend_marker_stat.SetPointError(1, leg_marker_statUncert, 0.0)
setResultStyle(legend_marker_tot, color_tot, color_tot)
setResultStyle(legend_marker_stat, color_tot, color_stat, option="stat")
legend_marker_tot.Draw("P SAME")
legend_marker_stat.Draw("P SAME")

y_legend_marker_text = margin_bottom + (leg_marker_y-0.57-ymin)*y_perindex
x_legend_marker_text = margin_left + (leg_marker_x-xmin)*x_perGeV
x_legend_marker_text_stat = margin_left + (leg_marker_x+leg_marker_statUncert-xmin)*x_perGeV
x_legend_marker_text_tot = margin_left + (leg_marker_x+leg_marker_totUncert-xmin)*x_perGeV
allTexts.append(addText(x_legend_marker_text_stat, y_legend_marker_text, "stat.", font=43, size=14, color=13))
allTexts.append(addText(x_legend_marker_text_tot, y_legend_marker_text, "total", font=43, size=14, color=13))


################################################################################
# Finally draw all the text, redraw axes and save plot
for t in allTexts:
    t.Draw()

ROOT.gPad.RedrawAxis()
c.SaveAs("MtopResults.pdf")
