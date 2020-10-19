# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 20:50:20 2020
@author: Giulio
"""

import ThesisGraph as TG

a = TG.ThesisGraph()
#a.import_as_excel()
#a.plot_P_and_EMF_vs_Ch(filetype = 'excel',Secondbatchfilename = 'Pd_test_un.xls')
#a.plot_T_T0_vs_Ch (Secondbatchfilename = 'Pd_test_un.txt')
a.plot_trend_txt(title = "Relative trasmittance of electrolite solutions vs time",filename = "Trend_KOH.txt",filename2 = "Trend_Glicerine.txt")
#a.plot_trend_txt(title = "Relative trasmittance of Glicerine electrolite solution vs time",filename = "Trend_Glicerine.txt",Date = '19_10_2020')