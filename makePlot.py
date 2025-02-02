import ROOT
from math import sqrt
from measurement import measurement
from graphs import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)

from measurementData import measurements

def main(combinationPublic):
    measurements_all = []
    measurements_direct = []
    measurements_indirect = []
    measurements_msbar = []
    measurements_other = []
    measurements_boosted = []

    list_oneDigit = [
        "JHEP 07 (2011) 04",
        "EPJC 72 (2012) 2202",
        "EPJC 73 (2013) 2494",
        "PLB 728 (2014) 496",
        "JHEP 08 (2016) 029",
        "JHEP 09 (2017) 051",
        "JHEP 12 (2016) 123",
        "EPJC 77 (2017) 467",
        "EPJC 79 (2019) 368",
        "EPJC 80 (2020) 658",
        "PRL 124 (2020) 202001",
        "JHEP 07 (2023) 213",
        "PRL 124 (2020) 202001",
    ]

    for (category, channel, com, method, ref, mt, stat, sysdown, sysup) in measurements:
        title = channel+" "+com+" TeV, "+method if method != "" else channel+" "+com+" TeV"
        m = measurement(title)
        if mt is None:
            continue
        if stat is None:
            stat = 0.
        m.setResult(mt, stat, sysdown, sysup)
        m.setReference(ref)
        if ref in list_oneDigit:
            if not (ref == "EPJC 79 (2019) 368" and category == "direct"):
                m.useOneDigit()
        if category == "direct":
            m.setColor(ROOT.kRed)
            measurements_direct.append(m)
            measurements_all.append(m)
        elif category == "indirect":
            m.setColor(ROOT.kAzure+7)
            measurements_indirect.append(m)
            measurements_all.append(m)
        elif category == "msbar":
            m.setColor(ROOT.kAzure+7)
            measurements_msbar.append(m)
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
    Nmsbar = len(measurements_msbar)
    Nother = len(measurements_other)
    Nboosted = len(measurements_boosted)

    ################################################################################
    ## Contruct results graphs and labels
    g_direct_tot = ROOT.TGraphAsymmErrors(len(measurements_direct))
    g_indirect_tot = ROOT.TGraphAsymmErrors(len(measurements_indirect))
    g_msbar_tot = ROOT.TGraphAsymmErrors(len(measurements_msbar))
    g_other_tot = ROOT.TGraphAsymmErrors(len(measurements_other))
    g_boosted_tot = ROOT.TGraphAsymmErrors(len(measurements_boosted))
    g_direct_stat = ROOT.TGraphAsymmErrors(len(measurements_direct))
    g_indirect_stat = ROOT.TGraphAsymmErrors(len(measurements_indirect))
    g_msbar_stat = ROOT.TGraphAsymmErrors(len(measurements_msbar))
    g_other_stat = ROOT.TGraphAsymmErrors(len(measurements_other))
    g_boosted_stat = ROOT.TGraphAsymmErrors(len(measurements_boosted))

    t_mt_values = []
    t_title = []
    t_category = []
    t_ref = []

    index = Nall-1+13
    index_max = index
    index_direct_max = -1
    index_direct_min = -1
    index_indirect_max = -1
    index_indirect_min = -1
    index_msbar_max = -1
    index_msbar_min = -1
    index_other_max = -1
    index_other_min = -1

    t_category.append( (index, "Indirect mass extractions") )
    index = index -1
    t_category.append( (index, "Pole mass from cross section") )
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
        t_mt_values.append( (index, "#it{m}_{t}^{pole} = "+m.mt_string().replace("sys", "tot")) )
        t_title.append( (index, m.infoString()) )
        t_ref.append( (index, m.reference()) )
        index = index -1

    index = index -1
    t_category.append( (index, "#bar{MS} mass from cross section") )
    index = index -1
    for i, m in enumerate(measurements_msbar):
        if i==0:
            index_msbar_max = index
        if i==len(measurements_msbar)-1:
            index_msbar_min = index
        g_msbar_tot.SetPoint(i, m.mtop(), index)
        g_msbar_tot.SetPointError(i, m.uncertTotalDown(), m.uncertTotalUp(), 0.0, 0.0)
        g_msbar_stat.SetPoint(i, m.mtop(), index)
        g_msbar_stat.SetPointError(i, m.uncertStat(), m.uncertStat(), 0.0, 0.0)
        t_mt_values.append( (index, "#it{m}_{t}(#it{m}_{t}) = "+m.mt_string().replace("sys", "tot")) )
        t_title.append( (index, m.infoString()) )
        t_ref.append( (index, m.reference()) )
        index = index -1

    index_line1 = index
    index = index -1
    index = index -1
    t_category.append( (index, "Direct measurements") )
    index = index -1
    t_category.append( (index, "Full reconstruction") )
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
    setResultStyle(g_msbar_tot, color_tot, color_tot)
    setResultStyle(g_other_tot, color_tot, color_tot)
    setResultStyle(g_boosted_tot, color_tot, color_tot)

    setResultStyle(g_direct_stat, color_tot, color_stat, option="stat")
    setResultStyle(g_indirect_stat, color_tot, color_stat, option="stat")
    setResultStyle(g_msbar_stat, color_tot, color_stat, option="stat")
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
    ymax = index_max+6

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
    g_msbar_tot.Draw("P SAME")
    g_boosted_tot.Draw("P SAME")
    g_other_tot.Draw("P SAME")
    g_direct_stat.Draw("P SAME")
    g_indirect_stat.Draw("P SAME")
    g_msbar_stat.Draw("P SAME")
    g_boosted_stat.Draw("P SAME")
    g_other_stat.Draw("P SAME")

    ################################################################################
    # Lines to divide the methods
    line1 = ROOT.TLine(xmin, index_line1, xmax, index_line1)
    for l in [line1]:
        l.SetLineColor(15)
        l.SetLineWidth(2)
        # l.Draw("SAME")

    ################################################################################
    # Format all text and put it into a list that is drawn later
    allTexts = []
    x_mt = 0.63
    for (index, text) in t_mt_values:
        x = x_mt
        # if index >= index_msbar_min and index <= index_msbar_max:
        #     x -= 0.1
        y = margin_bottom + (index-ymin)*y_perindex
        t_latex = addText(x, y, text)
        allTexts.append(t_latex)

    x_ref = 0.875
    for (index, text) in t_ref:
        col = 14
        if not combinationPublic and "TOP-22-001" in text:
            col = ROOT.kBlue
        y = margin_bottom + (index-ymin)*y_perindex
        t_latex = addText(x_ref, y, text, font=43, size=10, color=col)
        allTexts.append(t_latex)

    x_title = margin_left + 0.01
    for (index, text) in t_title:
        col = 1
        if not combinationPublic and "Combination 7+8 TeV" in text:
            col = ROOT.kBlue
        y = margin_bottom + (index-ymin)*y_perindex
        t_latex = addText(x_title, y, text, font=43, size=16, color = col)
        allTexts.append(t_latex)

    for (index, text) in t_category:
        y = margin_bottom + (index-ymin)*y_perindex
        x = x_title
        fontstyle = 43
        fontsize = 30
        if text in ["Indirect mass extractions", "Direct measurements"]:
            fontstyle = 63
        if "Boosted" in text or "Alternative" in text or "Full reconstruction" in text or "Pole mass" in text or "#bar{MS}" in text:
            fontsize = 18
            y -= 0.007
            # x += 0.01
        t_latex = addText(x, y+0.007, text, font=fontstyle, size=fontsize, color=15)
        allTexts.append(t_latex)
    ################################################################################
    # CMS logo
    allTexts.append(getCMS(margin_left+0.01, 1-margin_top-0.02, 0.65 ))

    ################################################################################
    # Legend
    leg = ROOT.TLegend(.60, .86, .9, 1-margin_top-0.04)
    leg.SetTextSize(0.015)
    leg.AddEntry(g_predict_indirect_tot, "ATLAS+CMS combination #it{m}_{t}^{pole} = 173.4^{#plus1.8}_{#minus2.0} GeV", "fl")
    leg.AddEntry(g_predict_indirect_tot, "", "") # leave room for reference
    entry1 = leg.AddEntry(g_predict_direct_tot, "CMS 7+8 TeV comb. #it{m}_{t}^{MC} = 172.52 #pm 0.42 GeV", "fl")
    entry2 = leg.AddEntry(g_predict_direct_stat, "CMS 7+8 TeV comb. stat. uncertainty", "fl")
    if not combinationPublic:
        entry1.SetTextColor(ROOT.kBlue)
        entry2.SetTextColor(ROOT.kBlue)

    leg.AddEntry(g_predict_direct_tot, "", "") # leave room for reference
    leg.Draw()

    allTexts.append(addText(.675, .925, "[JHEP 07 (2023) 213]", font=43, size=10, color=14))

    if combinationPublic:
        allTexts.append(addText(.675, .872, "[PRL 132 (2024) 261902]", font=43, size=10, color=14))
    else:
        allTexts.append(addText(.675, .872, "[TOP-22-001]", font=43, size=10, color=ROOT.kBlue))


    ################################################################################
    # Create a Marker for the legend and label stat. and tot. uncertainty bars
    leg_marker_x = 192
    leg_marker_y = ymax-1
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

if __name__ == "__main__":
    main(combinationPublic=True)
