import ROOT

def setResultStyle(g, col, col2, option=None):
    g.SetTitle("")
    g.SetMarkerStyle(8)
    g.SetMarkerSize(1.25)
    g.SetMarkerColor(col)
    g.SetLineColor(col2)
    g.SetLineWidth(1)
    if option == "stat":
        g.SetLineWidth(3)

    # X axis
    g.GetXaxis().SetTitle("#it{m}_{t} [GeV]")
    # g.GetXaxis().SetTitleSize(0.02)
    g.GetXaxis().SetNdivisions(909)
    g.GetXaxis().SetTitleSize(40)
    g.GetXaxis().SetTitleFont(43)
    g.GetXaxis().SetTitleOffset(0.8)
    g.GetXaxis().SetLabelFont(43)
    g.GetXaxis().SetLabelSize(21)

    # Y axis
    g.GetYaxis().SetTitle("")
    g.GetYaxis().SetTitleSize(0.0)
    g.GetYaxis().SetLabelSize(0.0)
    g.GetYaxis().SetLabelSize(0.0)
    g.GetYaxis().SetTickLength(0.0)

def addText(x, y, text, font=43, size=12, color=ROOT.kBlack):
    latex = ROOT.TLatex(3.5, 24, text)
    latex.SetNDC()
    latex.SetTextAlign(12)
    latex.SetTextFont(font)
    latex.SetTextSize(size)
    latex.SetTextColor(color)
    latex.SetX(x)
    latex.SetY(y)
    return latex

def getDummyGraph(xmin, xmax, ymin, ymax):
    g = ROOT.TGraph(4)
    g.SetPoint(0, xmin, ymin)
    g.SetPoint(1, xmin, ymax)
    g.SetPoint(2, xmax, ymax)
    g.SetPoint(3, xmax, ymin)
    setResultStyle(g, ROOT.kWhite, ROOT.kWhite)
    g.SetMarkerSize(0.0)
    return g

def getCMS(x, y, factor=1.0):
    cmstext = ROOT.TLatex(3.5, 24, "CMS")
    cmstext.SetNDC()
    cmstext.SetTextAlign(13)
    cmstext.SetTextFont(62)
    cmstext.SetTextSize(0.08*factor)
    cmstext.SetX(x)
    cmstext.SetY(y)
    return cmstext

def getPrelim():
    prelim = ROOT.TLatex(3.5, 24, "Preliminary")
    prelim.SetNDC()
    prelim.SetTextAlign(13)
    prelim.SetTextFont(52)
    prelim.SetTextSize(0.06)
    prelim.SetX(0.01)
    prelim.SetY(0.91)
    return prelim

def getPredictionGraph(ymin, ymax, central, stat, totDown, totUp):
    Npoints = 101
    graph_stat = ROOT.TGraphAsymmErrors(Npoints)
    graph_tot = ROOT.TGraphAsymmErrors(Npoints)
    stepsize = (ymax - ymin)/(Npoints-1)
    for i in range(Npoints):
        y = ymin+i*stepsize
        graph_tot.SetPoint(i, central, y)
        graph_tot.SetPointError(i, totDown, totUp, stepsize, stepsize)
        graph_stat.SetPoint(i, central, y)
        graph_stat.SetPointError(i, stat, stat, stepsize, stepsize)

    line = ROOT.TLine(central, ymin, central, ymax)
    line.SetLineColor(13)
    line.SetLineStyle(2)
    return graph_stat, graph_tot, line

def setPredictionStyle(g, col, lcol):
    g.SetTitle("")
    g.SetMarkerColor(col)
    g.SetLineColor(lcol)
    g.SetLineStyle(2)
    g.SetFillColor(col)

def setPredictionLineStyle(l, col):
    l.SetLineColor(col)
    l.SetLineStyle(2)
