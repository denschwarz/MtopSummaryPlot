from math import sqrt


class measurement:
    def __init__(self, name):
        self.__title = name
        self.__mtop = None
        self.__uncertStat = None
        self.__uncertSysUp = None
        self.__uncertSysDown = None
        self.__uncertTotalUp = None
        self.__uncertTotalDown = None
        self.__ref = None
        self.__lumi = None
        self.__color = None
        self.__oneDigit = False

    def setResult(self, mtop, stat, sysuncert_down, sysuncert_up):
        self.__mtop = mtop
        self.__uncertStat = stat
        self.__uncertSysDown = sysuncert_down
        self.__uncertSysUp = sysuncert_up
        self.__uncertTotalDown = sqrt(stat*stat + sysuncert_down*sysuncert_down)
        self.__uncertTotalUp = sqrt(stat*stat + sysuncert_up*sysuncert_up)

    def useOneDigit(self):
        self.__oneDigit = True

    def setReference(self, ref):
        self.__ref = ref

    def setLumi(self, lumi):
        self.__lumi = lumi

    def title(self):
        return self.__title

    def reference(self):
        return self.__ref

    def mtop(self):
        return self.__mtop

    def uncertStat(self):
        return self.__uncertStat

    def uncertTotalUp(self):
        return self.__uncertTotalUp

    def uncertTotalDown(self):
        return self.__uncertTotalDown

    def setColor(self, color):
        self.__color = color

    def color(self):
        return self.__color

    def mt_string(self):
        # mt value
        string = "%.2f" %(self.__mtop) if not self.__oneDigit else "%.1f  " %(self.__mtop)
        # stat uncert
        if self.__uncertStat > 0.00001:
            string += " #pm %.2f (stat)" %(self.__uncertStat) if not self.__oneDigit else " #pm %.1f   (stat)" %(self.__uncertStat)
        else:
            string += ""
        # sys uncert
        if abs(self.__uncertSysUp-self.__uncertSysDown)<0.00001:
            string += " #pm %.2f (sys)"%(self.__uncertSysUp)  if not self.__oneDigit else " #pm %.1f   (sys)"%(self.__uncertSysUp)
        else:
            string += "   {}^{#plus%.2f}_{#minus%.2f}  (sys)"%(self.__uncertSysUp, self.__uncertSysDown)  if not self.__oneDigit else "   {}^{#plus%.1f  }_{#minus%.1f  }  (sys)"%(self.__uncertSysUp, self.__uncertSysDown)
        string += " GeV"
        return string

    def infoString(self):
        string = self.__title
        return string

    def reference(self):
        return "["+self.__ref+"]"
