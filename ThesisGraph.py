# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:16:03 2020
@author: Giulio
"""



import matplotlib.pylab as plt
from scipy import optimize
import numpy as np
from math import pi
import pandas as pd


F   = 96485.33625
R   = 8.3144626
U_0 = 0.176
P_0 = 1013.
T   = 300.
V_M = 14.



def Trivial_Function (x):
	return x*1

def PressureH(x):
	return P_0*np.exp((x-U_0)*(2*F)/(R*T))

class ThesisGraph:

	def __init__(self,title='',size = [10,10],Subplots = [1,1],xlabel = [],ylabel = [],label = [],marker = 'o',color = 'Red',data = [],Ch = [],EMF = [],P_H2 = [],T_T0 = [],Save = False,has2xaxis = False,has2yaxis = False,logscalex = False,logscaley = False):
		self.logscalex=logscalex
		self.logscaley=logscaley
		self.size=size
		self.Save=Save
		self.Ch  = Ch
		self.EMF = EMF
		self.P_H2= P_H2
		self.T_T0=T_T0


	def  import_as_txt(self,filename = 'Pd_test.txt',filepath = 'Results/',spl = ','):
		"""
		Parameters
		----------
		filename : name of the file txt  I mean to open
		filepath : name of the filepath.
		spl : Splitting parameter, setted on ','
		Returns
		It fills the main attributes of the class by importing from a txt file
		None.
		"""

		row = [line.strip().split(spl) for line in open(filepath + filename)]
		del(row[0])
		l  = len(row[0])
		self.data    = [[float(row[i][j])for j in range(0,l)] for i in range(len(row))]
		self.data = np.asarray (self.data)
	
		self.Ch  = self.data[:,0]
		self.EMF = self.data[:,1]
		self.P_H2 = [P_0*np.exp((U-U_0)*(2*F)/(R*T)) for U in self.EMF]

		if l>2:    
			self.T_T0= [np.log((self.data[i,2]/self.data[0,2]))for i in range(len(self.data))]
            
    
	def  import_as_excel(self,filename = 'Pd_test.xls',filepath = 'Results/'):
		"""
		Parameters
		----------
		filename : name of the file excel I mean to open
		   
		filepath : name of the filepath.
		spl : Splitting parameter, setted on ','
		Returns
		It fills the main attributes of the class by importing from a excel file
		None.
		"""
        
		self.xls            = pd.read_excel(filepath+filename) 
		b = self.xls.columns
		l = len(self.xls.columns)
        
		self.Ch,self.EMF = np.asarray(self.xls[b[0]]) , np.asarray(self.xls[b[1]]) 
		self.P_H2 = [P_0*np.exp((U-U_0)*(2*F)/(R*T)) for U in self.EMF]
        
        
		if l>2:
            
			t          = np.asarray(self.xls[b[2]])
			t0         = t[0]
			self.T_T0  = np.asarray([np.log(ti/t0) for ti in t])

	def plot_P_and_EMF_vs_Ch(self,title = 'Test',Date = '14_10_2020',logscaley = 'True',logscalex = 'False', firstlabel = 'Loading cycle',secondlabel = 'Unloading cycle', filetype = 'txt',Secondbatchfilename = ''):
		"""
		Parameters
		----------
		title : Title of the Graph.
		Date : Date of today
		logscaley : Do you want logscale on y axis
		logscalex : Do you want logscale on x axis
		firstlabel : Name of the label of the first batch
		secondlabel : Name of the label of the second batch
		filetype : Type 
		Secondbatchfilename : Name of the second batch's file'
		Returns
		-------
		None.
		"""
		Ch = self.Ch
		EMF= self.EMF
		P_H2 = self.P_H2
		#T_T0 = self.T_T0
        
        
		self.fig, self.axs= plt.subplots(1,1,figsize = self.size)
        
        
		self.axs.set_title(title)
		self.axs.scatter(Ch,EMF,marker = 'o',label = firstlabel)
        
		self.axs.set_ylabel('EMF(V)')	
		self.axs.set_xlabel('Alleged Hydrogen concentration over time pulse')
        
		if logscalex:
			self.axs.set_xscale('log')
			self.axs.set_xlim(min(Ch[1:])/10,max(Ch)*10)
        
		axs2=self.axs.twinx()
        
		if logscaley:
			axs2.set_yscale('log')
			axs2.set_ylim(min(P_H2[1:])/10,max(P_H2)*10)

		axs2.set_ylabel('P_H2(mbar)')
		if Secondbatchfilename == '':
			self.axs.legend(loc = 'best')

			self.fig.savefig(title+'_'+Date)
        
		elif Secondbatchfilename != '':
			if filetype == 'txt':
				self.import_as_txt(filename = Secondbatchfilename)
			elif filetype == 'excel':
				self.import_as_excel(filename = Secondbatchfilename)
            
			self.axs.scatter(self.Ch,self.EMF,marker = 'd',label = secondlabel)
			self.axs.legend(loc = 'best')
			self.fig.savefig('Graphs/'+title+'_'+Date)
			self.Ch = Ch
			self.Emf= EMF
			self.P_H2 = P_H2


	def plot_T_T0_vs_Ch(self,title = 'T_T0',Date = '14_10_2020',logscaley = 'False',logscalex = 'False',firstlabel = 'Loading cycle',secondlabel = 'Unloading cycle', filetype = 'txt',Secondbatchfilename = ''):
		"""
		Parameters
		----------
		title : Title of the Graph.
		Date : Date of today
		logscaley : Do you want logscale on y axis
		logscalex : Do you want logscale on x axis
		firstlabel : Name of the label of the first batch
		secondlabel : Name of the label of the second batch
		filetype : Type 
		Secondbatchfilename : Name of the second batch's file'
		Returns
		-------
		None.
		"""
		
		
		self.fig, self.axs= plt.subplots(1,1,figsize = self.size)

		Ch = self.Ch
		EMF= self.EMF
		P_H2 = self.P_H2
		T_T0 = self.T_T0

		self.axs.set_title(title)
		self.axs.scatter(Ch,T_T0, marker = 'o',label = firstlabel)
		self.axs.set_ylabel('Relative Trasmittance (a.u.)')	
		self.axs.set_xlabel('Hydrogen concentration over time pulse')
		
		if logscalex:
			self.axs.set_xscale('log')
			self.axs.set_xlim(min(Ch[1:])/10,max(Ch)*10)
        
		if Secondbatchfilename == '':

			self.axs.legend (loc = 'best')
			self.fig.savefig(title+'_'+Date)
        
		elif Secondbatchfilename != '':
			if filetype == 'txt':
				self.import_as_txt(filename = Secondbatchfilename)
			elif filetype == 'excel':
				self.import_as_excel(filename = Secondbatchfilename)
			self.axs.scatter(self.Ch,self.T_T0,marker = 'd',label = secondlabel)
			self.axs.legend(loc = 'best')
			self.fig.savefig('Graphs/'+title+'_'+Date)
			self.Ch = Ch
			self.T_T0 = T_T0
			self.EMF = EMF
			self.P_H2 = P_H2

	def plot_trend_txt(self,title = 'Trend of Relative Transmittance',Phdim = 'Relative trasmittance (u.a.)',Element1 = 'KOH',Element2 = "Glicerine",Date = '14_10_2020',spl = ',', filepath = 'Results/',filename = 'Trend.txt',filename2 = '',TT = 30, TS = 1):
		self.fig, self.axs= plt.subplots(1,1,figsize = self.size)
		data = [line.strip().split(spl) for line in open(filepath + filename)]
		del data[0]
		data = [[float(data[i][j])for j in range(2)] for i in range(len(data))]
		data = np.asarray(data)
		t = data[:,0]
		y = data[:,1]
		y = [np.log(y[i]/y[0]) for i in range (len(y))]
		self.axs.set_title(title)
		self.axs.scatter(t,y, marker = 'o',label = "Trend of "+Phdim + "_" + Element1)
		self.axs.set_ylabel(Phdim)
		self.axs.set_xlabel('Time (min.)')
		if filename2 != '':
			data = [line.strip().split(spl) for line in open(filepath + filename2)]
			del data[0]
			data = [[float(data[i][j])for j in range(2)] for i in range(len(data))]
			data = np.asarray(data)
			t = data[:,0]
			y = data[:,1]
			y = [np.log(y[i]/y[0]) for i in range (len(y))]
			self.axs.scatter(t,y, marker = 'o',label = "Trend of "+Phdim +  "_" + Element2)
		self.axs.legend(loc = 'best')

		self.fig.savefig("Graphs/"+title+'_'+Date)
