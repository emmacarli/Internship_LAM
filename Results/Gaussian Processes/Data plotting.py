#Author: Emma Carli 
import matplotlib.pyplot as plt
import numpy as np
import pickle
startlist=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\start.txt")
from astropy.table import Table
import math
import matplotlib
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20) 

k=-1
data1=np.zeros((66,25))
data2=np.zeros((66,25))
data3=np.zeros((66,25))
data4=np.zeros((66,25))


# =============================================================================
#PICKING A STAR
f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    star = ''.join(starlist)
    starint=int(float(star))
    print('Star',''.join(starlist), '...') #After this the stellar periods will be printed
    k=k+1
    data1[k][0]=starint  
    data2[k][0]=starint  
    data3[k][0]=starint
    data4[k][0]=starint
    # =============================================================================    
  
    
    # =============================================================================
    #FIRST RUN 
    f1=open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\Pickle files\First_run_pickle_files\K2_C16_" + star + 'CIs.p', 'rb')
    CI_dictionary1=pickle.load(f1, encoding='latin1')
    data1[k][1]=CI_dictionary1[b'GP1_c'][0]
    data1[k][2]=CI_dictionary1[b'GP1_c'][1]
    data1[k][3]=CI_dictionary1[b'GP1_c'][2]
    data1[k][4]=CI_dictionary1[b'GP1_l1'][0]
    data1[k][5]=CI_dictionary1[b'GP1_l1'][1]
    data1[k][6]=CI_dictionary1[b'GP1_l1'][2]
    data1[k][7]=CI_dictionary1[b'GP1_l2'][0]
    data1[k][8]=CI_dictionary1[b'GP1_l2'][1]
    data1[k][9]=CI_dictionary1[b'GP1_l2'][2]
    data1[k][10]=CI_dictionary1[b'GP1_per'][0]
    data1[k][11]=CI_dictionary1[b'GP1_per'][1]
    data1[k][12]=CI_dictionary1[b'GP1_per'][2]
    data1[k][13]=CI_dictionary1[b'K2_foot'][0]
    data1[k][14]=CI_dictionary1[b'K2_foot'][1]
    data1[k][15]=CI_dictionary1[b'K2_foot'][2]
    data1[k][16]=CI_dictionary1[b'K2_jitter'][0]
    data1[k][17]=CI_dictionary1[b'K2_jitter'][1]
    data1[k][18]=CI_dictionary1[b'K2_jitter'][2]
    data1[k][19]=CI_dictionary1[b'logL'][0]
    data1[k][20]=CI_dictionary1[b'logL'][1]
    data1[k][21]=CI_dictionary1[b'logL'][2]
    data1[k][22]=CI_dictionary1[b'posterior'][0]
    data1[k][23]=CI_dictionary1[b'posterior'][1]
    data1[k][24]=CI_dictionary1[b'posterior'][2]   
    f1.close()
    # =============================================================================
    
    # =============================================================================
    #SECOND RUN 
    f2=open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\Pickle files\Second_run_pickle_files\K2_C16_" + star + 'CIs.p', 'rb')
    CI_dictionary2=pickle.load(f2, encoding='latin1')
    data2[k][1]=CI_dictionary2[b'GP1_c'][0]
    data2[k][2]=CI_dictionary2[b'GP1_c'][1]
    data2[k][3]=CI_dictionary2[b'GP1_c'][2]
    data2[k][4]=CI_dictionary2[b'GP1_l1'][0]
    data2[k][5]=CI_dictionary2[b'GP1_l1'][1]
    data2[k][6]=CI_dictionary2[b'GP1_l1'][2]
    data2[k][7]=CI_dictionary2[b'GP1_l2'][0]
    data2[k][8]=CI_dictionary2[b'GP1_l2'][1]
    data2[k][9]=CI_dictionary2[b'GP1_l2'][2]
    data2[k][10]=CI_dictionary2[b'GP1_per'][0]
    data2[k][11]=CI_dictionary2[b'GP1_per'][1]
    data2[k][12]=CI_dictionary2[b'GP1_per'][2]
    data2[k][13]=CI_dictionary2[b'K2_foot'][0]
    data2[k][14]=CI_dictionary2[b'K2_foot'][1]
    data2[k][15]=CI_dictionary2[b'K2_foot'][2]
    data2[k][16]=CI_dictionary2[b'K2_jitter'][0]
    data2[k][17]=CI_dictionary2[b'K2_jitter'][1]
    data2[k][18]=CI_dictionary2[b'K2_jitter'][2]
    data2[k][19]=CI_dictionary2[b'logL'][0]
    data2[k][20]=CI_dictionary2[b'logL'][1]
    data2[k][21]=CI_dictionary2[b'logL'][2]
    data2[k][22]=CI_dictionary2[b'posterior'][0]
    data2[k][23]=CI_dictionary2[b'posterior'][1]
    data2[k][24]=CI_dictionary2[b'posterior'][2]
    f2.close()
    # =============================================================================
    
    # =============================================================================
    #THIRD RUN 
    f3=open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\Pickle files\Third_run_pickle_files\K2_C16_" + star + 'CIs.p', 'rb')
    CI_dictionary3=pickle.load(f3, encoding='latin1')
    data3[k][1]=CI_dictionary3[b'GP1_c'][0]
    data3[k][2]=CI_dictionary3[b'GP1_c'][1]
    data3[k][3]=CI_dictionary3[b'GP1_c'][2]
    data3[k][4]=CI_dictionary3[b'GP1_l1'][0]
    data3[k][5]=CI_dictionary3[b'GP1_l1'][1]
    data3[k][6]=CI_dictionary3[b'GP1_l1'][2]
    data3[k][7]=CI_dictionary3[b'GP1_l2'][0]
    data3[k][8]=CI_dictionary3[b'GP1_l2'][1]
    data3[k][9]=CI_dictionary3[b'GP1_l2'][2]
    data3[k][10]=CI_dictionary3[b'GP1_per'][0]
    data3[k][11]=CI_dictionary3[b'GP1_per'][1]
    data3[k][12]=CI_dictionary3[b'GP1_per'][2]
    data3[k][13]=CI_dictionary3[b'K2_foot'][0]
    data3[k][14]=CI_dictionary3[b'K2_foot'][1]
    data3[k][15]=CI_dictionary3[b'K2_foot'][2]
    data3[k][16]=CI_dictionary3[b'K2_jitter'][0]
    data3[k][17]=CI_dictionary3[b'K2_jitter'][1]
    data3[k][18]=CI_dictionary3[b'K2_jitter'][2]
    data3[k][19]=CI_dictionary3[b'logL'][0]
    data3[k][20]=CI_dictionary3[b'logL'][1]
    data3[k][21]=CI_dictionary3[b'logL'][2]
    data3[k][22]=CI_dictionary3[b'posterior'][0]
    data3[k][23]=CI_dictionary3[b'posterior'][1]
    data3[k][24]=CI_dictionary3[b'posterior'][2]
    f3.close()
    # =============================================================================
    
    # =============================================================================
    #FOURTH RUN 
    f4=open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\Pickle files\Fourth_Run_Pickle_Files\K2_C16_" + star + 'CIs.p', 'rb')
    CI_dictionary4=pickle.load(f4, encoding='latin1')
    data4[k][1]=CI_dictionary4[b'GP1_c'][0]
    data4[k][2]=CI_dictionary4[b'GP1_c'][1]
    data4[k][3]=CI_dictionary4[b'GP1_c'][2]
    data4[k][4]=CI_dictionary4[b'GP1_l1'][0]
    data4[k][5]=CI_dictionary4[b'GP1_l1'][1]
    data4[k][6]=CI_dictionary4[b'GP1_l1'][2]
    data4[k][7]=CI_dictionary4[b'GP1_l2'][0]
    data4[k][8]=CI_dictionary4[b'GP1_l2'][1]
    data4[k][9]=CI_dictionary4[b'GP1_l2'][2]
    data4[k][10]=CI_dictionary4[b'GP1_per'][0]
    data4[k][11]=CI_dictionary4[b'GP1_per'][1]
    data4[k][12]=CI_dictionary4[b'GP1_per'][2]
    data4[k][13]=CI_dictionary4[b'K2_foot'][0]
    data4[k][14]=CI_dictionary4[b'K2_foot'][1]
    data4[k][15]=CI_dictionary4[b'K2_foot'][2]
    data4[k][16]=CI_dictionary4[b'K2_jitter'][0]
    data4[k][17]=CI_dictionary4[b'K2_jitter'][1]
    data4[k][18]=CI_dictionary4[b'K2_jitter'][2]
    data4[k][19]=CI_dictionary4[b'logL'][0]
    data4[k][20]=CI_dictionary4[b'logL'][1]
    data4[k][21]=CI_dictionary4[b'logL'][2]
    data4[k][22]=CI_dictionary4[b'posterior'][0]
    data4[k][23]=CI_dictionary4[b'posterior'][1]
    data4[k][24]=CI_dictionary4[b'posterior'][2]
    f4.close()
    # =============================================================================
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)

data_firstrun=Table(data1,names=['Star', 'Amplitude','Err Amp +','Err Amp -','Lambda 1','Err  L1 +', 'Err L1 -', 'Lambda 2','Err  L2 +', 'Err L2 -', 'Period','Err Per +', 'Err Per -', 'Foot','Err foot +', 'Err foot -', 'Jitter','Err Jitter +', 'Err Jitter -', 'log L','Err logL +', 'Err logL -', 'Posterior','Err Post +', 'Err Post -' ])
data_secondrun=Table(data2,names=['Star','Amplitude','Err Amp +','Err Amp -','Lambda 1','Err  L1 +', 'Err L1 -', 'Lambda 2','Err L2 +', 'Err L2 -', 'Period','Err Per +', 'Err Per -', 'Foot','Err foot +', 'Err foot -', 'Jitter','Err Jitter +', 'Err Jitter -', 'log L','Err logL +', 'Err logL -', 'Posterior','Err Post +', 'Err Post -' ])
data_thirdrun=Table(data3,names=['Star','Amplitude','Err Amp +','Err Amp -','Lambda 1','Err  L1 +', 'Err L1 -', 'Lambda 2','Err L2 +', 'Err L2 -', 'Period','Err Per +', 'Err Per -', 'Foot','Err foot +', 'Err foot -', 'Jitter','Err Jitter +', 'Err Jitter -', 'log L','Err logL +', 'Err logL -', 'Posterior','Err Post +', 'Err Post -' ])
data_fourthrun=Table(data4,names=['Star','Amplitude','Err Amp +','Err Amp -','Lambda 1','Err  L1 +', 'Err L1 -', 'Lambda 2','Err L2 +', 'Err L2 -', 'Period','Err Per +', 'Err Per -', 'Foot','Err foot +', 'Err foot -', 'Jitter','Err Jitter +', 'Err Jitter -', 'log L','Err logL +', 'Err logL -', 'Posterior','Err Post +', 'Err Post -' ])
if np.array_equal(data2[:,0] , data1[:,0]) is False:
    print('Warning! GP1&2 stars may not match.')
if np.array_equal(data3[:,0] , data2[:,0]) is False:
    print('Warning! GP2&3 stars may not match.')
if np.array_equal(data3[:,0] , data1[:,0]) is False:
    print('Warning! GP1&3 stars may not match.')
if np.array_equal(data4[:,0] , data1[:,0]) is False:
    print('Warning! GP1&4 stars may not match.')
if np.array_equal(data4[:,0] , data2[:,0]) is False:
    print('Warning! GP2&4 stars may not match.')
if np.array_equal(data4[:,0] , data3[:,0]) is False:
    print('Warning! GP3&4 stars may not match.')



data_firstrun.write('data_firstrun.html', overwrite=True) #Retrieve the astropy table as an html table
data_secondrun.write('data_secondrun.html', overwrite=True) #Retrieve the astropy table as an html table
data_thirdrun.write('data_thirdrun.html', overwrite=True) #Retrieve the astropy table as an html table
data_fourthrun.write('data_fourthrun.html', overwrite=True) #Retrieve the astropy table as an html table


preperiodstable=np.genfromtxt(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\stars_and_preperiods.txt')
if np.array_equal(preperiodstable[:,0] , data1[:,0]) is False:
    print('Warning! Preperiods stars may not match GP1 stars.')
preperiods=preperiodstable[:,1]


ACFtable=np.genfromtxt(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Periods C16.txt')
ACF_period=ACFtable[1:,1]
ACF_period_error=ACFtable[1:,2]
if np.array_equal(ACFtable[1:,0] , data1[:,0]) is False:
    print('Warning! ACF stars may not match GP1 stars.')


period1=data_firstrun['Period']
period_error_plus1=data_firstrun['Err Per +']
period_error_minus1=data_firstrun['Err Per -']

period2=data_secondrun['Period']
period_error_plus2=data_secondrun['Err Per +']
period_error_minus2=data_secondrun['Err Per -']

period3=data_thirdrun['Period']
period_error_plus3=data_thirdrun['Err Per +']
period_error_minus3=data_thirdrun['Err Per -']

period4=data_fourthrun['Period']
period_error_plus4=data_fourthrun['Err Per +']
period_error_minus4=data_fourthrun['Err Per -']

RMStable=np.genfromtxt(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\RMS.txt')
RMS=RMStable[1:,1]
if np.array_equal(RMStable[1:,0] , data1[:,0]) is False:
    print('Warning! RMS stars may not match GP1 stars.')

amplitude1=data_firstrun['Amplitude']
amplitude2=data_secondrun['Amplitude']
amplitude3=data_thirdrun['Amplitude']
amplitude4=data_fourthrun['Amplitude']


teffradius=np.genfromtxt(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\TeffRadius.txt')
Teff=teffradius[1:,1]
radius=teffradius[1:,2]
if np.array_equal(teffradius[1:,0] , data1[:,0]) is False:
    print('Warning! Teff & Radius stars may not match GP1 stars.')


rotationspeeds1=((2*math.pi*teffradius[1:,2])/period1)*(6.957*(10**5))/(24*3600)
rotationspeeds2=((2*math.pi*teffradius[1:,2])/period2)*(6.957*(10**5))/(24*3600)
rotationspeeds3=((2*math.pi*teffradius[1:,2])/period3)*(6.957*(10**5))/(24*3600)
rotationspeeds4=((2*math.pi*teffradius[1:,2])/period4)*(6.957*(10**5))/(24*3600)
rotationspeedsACF=((2*math.pi*teffradius[1:,2])/ACF_period)*(6.957*(10**5))/(24*3600)

FWHM=np.zeros((66,2))
FWHM[:,0]=ACFtable[1:,0]

fwhms=Table.read(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\FWHM.txt', format='ascii')
fwhmsnames=fwhms['col1']
fwhms=(fwhms['col2']+fwhms['col3'])/2

for i in range(len(fwhms)):
    index=np.where(FWHM[:,0]==fwhmsnames[i])[0]
    if index.size>0:
      FWHM[index,1]=fwhms[i]

logRHK=np.zeros((66,3))
logRHK[:,0]=ACFtable[1:,0]

logrhktable=Table.read(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\logrhk_witherror.txt', format='ascii')
logrhknames=logrhktable['col1']
logrhk=logrhktable['col2']
logrhk_error=logrhktable['col3']

for i in range(len(logrhk)):
   index=np.where(logRHK[:,0]==logrhknames[i])[0]
   if index.size>0:
      logRHK[index,1]=logrhk[i]
      logRHK[index,2]=logrhk_error[i]

#########################################################################################
#########################################################################################
#Plot histograms and various relationships
figpath=r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\Graphs'

#GP periods vs ACF periods
fig1, ax1=plt.subplots(2,2, figsize=(15,15))
ax1[0,0].scatter(ACF_period, period1)
ax1[0,0].set_xlabel('ACF Period (days)', fontsize=20)
ax1[0,0].set_ylabel('GP1 Period (days)', fontsize=20)
ax1[0,0].plot(ACF_period, ACF_period, label='y=x', linewidth=.5)
ax1[0,0].plot(ACF_period, 2*ACF_period, label='y=2x', linewidth=.5)
ax1[0,0].legend()

ax1[0,1].scatter(ACF_period, period2)
ax1[0,1].set_xlabel('ACF Period (days)', fontsize=20)
ax1[0,1].set_ylabel('GP2 Period (days)', fontsize=20)
ax1[0,1].plot(ACF_period, ACF_period, label='y=x', linewidth=.5)
ax1[0,1].plot(ACF_period, 2*ACF_period, label='y=2x', linewidth=.5)


ax1[1,0].scatter(ACF_period, period3)
ax1[1,0].set_xlabel('ACF Period (days)', fontsize=20)
ax1[1,0].set_ylabel('GP3 Period (days)', fontsize=20)
ax1[1,0].plot(ACF_period, ACF_period, label='y=x', linewidth=.5)
ax1[1,0].plot(ACF_period, 2*ACF_period, label='y=2x', linewidth=.5)


ax1[1,1].scatter(ACF_period, period4)
ax1[1,1].set_xlabel('ACF Period (days)', fontsize=20)
ax1[1,1].set_ylabel('GP4 Period (days)', fontsize=20)
ax1[1,1].plot(ACF_period, ACF_period, label='y=x', linewidth=.5)
ax1[1,1].plot(ACF_period, 2*ACF_period, label='y=2x', linewidth=.5)


plt.tight_layout()
plt.savefig(figpath + '\\' + 'Periods_Comparison.png')
plt.close(fig1)

#GP amplitudes vs RMS
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.loglog(RMS, amplitude1, label='First Run', linestyle='none', marker='o')
ax2.loglog(RMS, amplitude2, label='Second Run', linestyle='none', marker='o')
ax2.loglog(RMS, amplitude3, label='Third Run', linestyle='none', marker='o')
ax2.loglog(RMS, amplitude4, label='Fourth Run', linestyle='none', marker='o')
ax2.loglog(RMS, RMS, label='y=x', linewidth=.5)
ax2.legend()
ax2.set_xlabel('RMS variability', fontsize=20)
ax2.set_ylabel('GP Amplitudes', fontsize=20)
ax2.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_Comparison.png')
plt.close(fig2)

#GP amplitudes vs period
fig12 = plt.figure()
plt.semilogy(period1, amplitude1, linestyle='none', marker='o')
ax12=plt.gca()
ax12.set_xlabel('Period (days)', fontsize=20)
ax12.set_ylabel('Amplitude', fontsize=20)
ax12.set_title('GP Run 1', fontsize=20)
ax12.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_Period_Run1.png')
plt.close(fig12)

fig14 = plt.figure()
plt.semilogy(period2, amplitude2, linestyle='none', marker='o')
ax14=plt.gca()
ax14.set_xlabel('Period (days)', fontsize=20)
ax14.set_ylabel('Amplitude', fontsize=20)
ax14.set_title('GP Run 2', fontsize=20)
ax14.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_Period_Run2.png')
plt.close(fig14)

fig15 = plt.figure()
plt.semilogy(period3, amplitude3, linestyle='none', marker='o')
ax15=plt.gca()
ax15.set_xlabel('Period (days)', fontsize=20)
ax15.set_ylabel('Amplitude', fontsize=20)
ax15.set_title('GP Run 3', fontsize=20)
ax15.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_Period_Run3.png')
plt.close(fig15)

fig21 = plt.figure()
plt.semilogy(period4, amplitude4, linestyle='none', marker='o')
ax21=plt.gca()
ax21.set_xlabel('Period (days)', fontsize=20)
ax21.set_ylabel('Amplitude', fontsize=20)
ax21.set_title('GP Run 4', fontsize=20)
ax21.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_Period_Run4.png')
plt.close(fig21)

#Histograms : amplitude and period
ax3 = plt.axes()
fig3=plt.gcf()
plt.hist([ACF_period, period1, period2, period3, period4], label=['ACF', 'First Run', 'Second Run', 'Third Run', 'Fourth Run'])
ax3.legend()
ax3.set_xlabel('Period (days)', fontsize=20)
ax3.set_ylabel('Number of stars', fontsize=20)
ax3.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Period_Histograms.png')
plt.close(fig3)

ax4 = plt.axes()
fig4=plt.gcf()
ax4.hist([RMS, amplitude1, amplitude2, amplitude3, amplitude4], bins=np.logspace(-4.5,0,15), label=['ACF', 'First Run', 'Second Run', 'Third Run', 'Fourth Run'])
ax4.legend()
ax4.set_xlabel('Amplitude of variability', fontsize=20)
ax4.set_ylabel('Number of stars', fontsize=20)
plt.xscale('log')
ax4.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_Histogram.png')
plt.close(fig4)


ax16 = plt.axes()
fig16=plt.gcf()
ax16.hist([preperiods, period1, period2, period3, period4], bins=20, label=['Starting Point', 'First Run', 'Second Run', 'Third Run', 'Fourth Run'])
ax16.legend()
ax16.set_xlabel('Period (days)', fontsize=20)
ax16.set_ylabel('Number of stars', fontsize=20)
ax16.tick_params(labelsize=15)
plt.tight_layout()
plt.savefig(figpath + '\\' + 'Preperiods_Periods_Histogram.png')
plt.close(fig16)


#Teff vs periods
fig7, ax7=plt.subplots(2,3, figsize=(15,15))
ax7[0,0].plot(ACF_period, Teff, linestyle='none', marker='o')
ax7[0,0].set_xlabel('ACF Period (days)', fontsize=20)
ax7[0,0].set_ylabel('Teff (K)', fontsize=20)

ax7[0,1].plot(period1, Teff, linestyle='none', marker='o')
ax7[0,1].set_xlabel('Period GP1 (days)', fontsize=20)
ax7[0,1].set_ylabel('Teff (K)', fontsize=20)

ax7[0,2].plot(period2, Teff, linestyle='none', marker='o')
ax7[0,2].set_xlabel('Period GP2 (days)', fontsize=20)
ax7[0,2].set_ylabel('Teff (K)', fontsize=20)

ax7[1,0].plot(period3, Teff, linestyle='none', marker='o')
ax7[1,0].set_xlabel('Period GP3 (days)', fontsize=20)
ax7[1,0].set_ylabel('Teff (K)', fontsize=20)

ax7[1,1].plot(period4, Teff, linestyle='none', marker='o')
ax7[1,1].set_xlabel('Period GP4 (days)', fontsize=20)
ax7[1,1].set_ylabel('Teff (K)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Period_vs_Teff.png')
plt.close(fig7)


#Radius vs periods 
fig8, ax8=plt.subplots(2,3, figsize=(15,15))
ax8[0,0].plot(ACF_period, radius, linestyle='none', marker='o')
ax8[0,0].set_xlabel('ACF Period (days)', fontsize=20)
ax8[0,0].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax8[0,1].plot(period1, radius, linestyle='none', marker='o')
ax8[0,1].set_xlabel('Period GP1 (days)', fontsize=20)
ax8[0,1].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax8[0,2].plot(period2, radius, linestyle='none', marker='o')
ax8[0,2].set_xlabel('Period GP2 (days)', fontsize=20)
ax8[0,2].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax8[1,0].plot(period3, radius, linestyle='none', marker='o')
ax8[1,0].set_xlabel('Period GP3 (days)', fontsize=20)
ax8[1,0].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax8[1,1].plot(period4, radius, linestyle='none', marker='o')
ax8[1,1].set_xlabel('Period GP4 (days)', fontsize=20)
ax8[1,1].set_ylabel('Radius (Solar Radii)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Period_vs_Radius.png')
plt.close(fig8)


#Radius vs amplitude 
fig9, ax9=plt.subplots(2,3, figsize=(15,15))
ax9[0,0].semilogx(RMS, radius, linestyle='none', marker='o')
ax9[0,0].set_xlabel('RMS', fontsize=20)
ax9[0,0].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax9[0,1].semilogx(amplitude1, radius, linestyle='none', marker='o')
ax9[0,1].set_xlabel('Amplitude GP1', fontsize=20)
ax9[0,1].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax9[0,2].semilogx(amplitude2, radius, linestyle='none', marker='o')  
ax9[0,2].set_xlabel('Amplitude GP2', fontsize=20)
ax9[0,2].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax9[1,0].semilogx(amplitude3, radius, linestyle='none', marker='o')
ax9[1,0].set_xlabel('Amplitude GP3', fontsize=20)
ax9[1,0].set_ylabel('Radius (Solar Radii)', fontsize=20)

ax9[1,1].semilogx(amplitude4, radius, linestyle='none', marker='o')
ax9[1,1].set_xlabel('Amplitude GP4', fontsize=20)
ax9[1,1].set_ylabel('Radius (Solar Radii)', fontsize=20)


plt.tight_layout()
plt.savefig(figpath + '\\' + 'Radius_vs_Amplitude.png')
plt.close(fig9)

#FWHM vs Vrot 
fig10, ax10=plt.subplots(2,3, figsize=(15,15))
ax10[0,0].loglog(rotationspeedsACF, FWHM[:,1], linestyle='none', marker='o')
ax10[0,0].set_xlabel('Rotation Speed ACF (km/s)', fontsize=20)
ax10[0,0].set_ylabel('FWHM (km/s)', fontsize=20)

ax10[0,1].loglog(rotationspeeds1, FWHM[:,1], linestyle='none', marker='o')
ax10[0,1].set_xlabel('Rotation Speed GP1 (km/s)', fontsize=20)
ax10[0,1].set_ylabel('FWHM (km/s)', fontsize=20)

ax10[0,2].loglog(rotationspeeds2, FWHM[:,1], linestyle='none', marker='o')
ax10[0,2].set_xlabel('Rotation Speed GP2 (km/s)', fontsize=20)
ax10[0,2].set_ylabel('FWHM (km/s)', fontsize=20)

ax10[1,0].loglog(rotationspeeds3, FWHM[:,1], linestyle='none', marker='o')
ax10[1,0].set_xlabel('Rotation Speed GP3 (km/s)', fontsize=20)
ax10[1,0].set_ylabel('FWHM (km/s)', fontsize=20)

ax10[1,1].loglog(rotationspeeds4, FWHM[:,1], linestyle='none', marker='o')
ax10[1,1].set_xlabel('Rotation Speed GP4 (km/s)', fontsize=20)
ax10[1,1].set_ylabel('FWHM (km/s)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'FWHM_vs_Vrot.png')
plt.close(fig10)


#Teff vs Vrot
fig11, ax11=plt.subplots(2,3, figsize=(15,15))
ax11[0,0].semilogx(rotationspeedsACF, Teff, linestyle='none', marker='o')
ax11[0,0].set_xlabel('Rotation Speed ACF (km/s)', fontsize=20)
ax11[0,0].set_ylabel('Teff (K)', fontsize=20)

ax11[0,1].semilogx(rotationspeeds1, Teff, linestyle='none', marker='o')
ax11[0,1].set_xlabel('Rotation Speed GP1 (km/s)', fontsize=20)
ax11[0,1].set_ylabel('Teff (K))', fontsize=20)

ax11[0,2].semilogx(rotationspeeds2, Teff, linestyle='none', marker='o')
ax11[0,2].set_xlabel('Rotation Speed GP1 (km/s)', fontsize=20)
ax11[0,2].set_ylabel('Teff (K)', fontsize=20)

ax11[1,0].semilogx(rotationspeeds3, Teff, linestyle='none', marker='o')
ax11[1,0].set_xlabel('Rotation Speed GP3 (km/s)', fontsize=20)
ax11[1,0].set_ylabel('Teff (K)', fontsize=20)

ax11[1,1].semilogx(rotationspeeds4, Teff, linestyle='none', marker='o')
ax11[1,1].set_xlabel('Rotation Speed GP4 (km/s)', fontsize=20)
ax11[1,1].set_ylabel('Teff (K)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Teff_vs_Vrot.png')
plt.close(fig11)


#Teff vs amplitude 
fig13, ax13=plt.subplots(2,3, figsize=(15,15))
ax13[0,0].semilogx(RMS, Teff, linestyle='none', marker='o')
ax13[0,0].set_xlabel('RMS', fontsize=20)
ax13[0,0].set_ylabel('Teff (K)', fontsize=20)

ax13[0,1].semilogx(amplitude1, Teff, linestyle='none', marker='o')
ax13[0,1].set_xlabel('Amplitude GP1', fontsize=20)
ax13[0,1].set_ylabel('Teff (K)', fontsize=20)

ax13[0,2].semilogx(amplitude2, Teff, linestyle='none', marker='o') 
ax13[0,2].set_xlabel('Amplitude GP2', fontsize=20)
ax13[0,2].set_ylabel('Teff (K)', fontsize=20)

ax13[1,0].semilogx(amplitude3, Teff, linestyle='none', marker='o')
ax13[1,0].set_xlabel('Amplitude GP3', fontsize=20)
ax13[1,0].set_ylabel('Teff (K)', fontsize=20)

ax13[1,1].semilogx(amplitude4, Teff, linestyle='none', marker='o')
ax13[1,1].set_xlabel('Amplitude GP4', fontsize=20)
ax13[1,1].set_ylabel('Teff (K)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Temperature_vs_Amplitude.png')
plt.close(fig13)

#Periods vs preperiods
fig5, ax5=plt.subplots(2,3, figsize=(15,15))
ax5[0,0].plot(preperiods, ACF_period, linestyle='none', marker='o')
ax5[0,0].plot(preperiods, preperiods, label='y=x')
ax5[0,0].plot(preperiods, 2*preperiods, label='y=2x')
ax5[0,0].legend()
ax5[0,0].set_xlabel('Preperiod (days)', fontsize=20)
ax5[0,0].set_ylabel('ACF Period (days)', fontsize=20)

ax5[0,1].plot(preperiods, period1, linestyle='none', marker='o')
ax5[0,1].plot(preperiods, preperiods, label='y=x')
ax5[0,1].plot(preperiods, 2*preperiods, label='y=2x')
ax5[0,1].set_xlabel('Preperiod (days)', fontsize=20)
ax5[0,1].set_ylabel('Period GP1 (days)', fontsize=20)

ax5[0,2].plot(preperiods, period2, linestyle='none', marker='o')
ax5[0,2].plot(preperiods, preperiods, label='y=x')
ax5[0,2].plot(preperiods, 2*preperiods, label='y=2x')
ax5[0,2].set_xlabel('Preperiod (days)', fontsize=20)
ax5[0,2].set_ylabel('Period GP2 (days)', fontsize=20)

ax5[1,0].plot(preperiods, period3, linestyle='none', marker='o')
ax5[1,0].plot(preperiods, preperiods, label='y=x')
ax5[1,0].plot(preperiods, 2*preperiods, label='y=2x')
ax5[1,0].set_xlabel('Preperiod (days)', fontsize=20)
ax5[1,0].set_ylabel('Period GP3 (days)', fontsize=20)

ax5[1,1].plot(preperiods, period4, linestyle='none', marker='o')
ax5[1,1].plot(preperiods, preperiods, label='y=x')
ax5[1,1].plot(preperiods, 2*preperiods, label='y=2x')
ax5[1,1].set_xlabel('Preperiod (days)', fontsize=20)
ax5[1,1].set_ylabel('Period GP4 (days)', fontsize=20)


plt.tight_layout()
plt.savefig(figpath + '\\' + 'Periods_vs_Preperiods.png')
plt.close(fig5)

#Period vs L1
fig17, ax17=plt.subplots(2,2, figsize=(15,15))
ax17[0,0].loglog(data_firstrun['Lambda 1'], period1, linestyle='none', marker='o')
ax17[0,0].set_xlabel('Lambda 1 GP1', fontsize=20)
ax17[0,0].set_ylabel('GP1 Period (days)', fontsize=20)

ax17[0,1].loglog(data_secondrun['Lambda 1'], period2, linestyle='none', marker='o')
ax17[0,1].set_xlabel('Lambda 1 GP2', fontsize=20)
ax17[0,1].set_ylabel('Period GP2 (days)', fontsize=20)

ax17[1,0].loglog(data_thirdrun['Lambda 1'], period3, linestyle='none', marker='o')
ax17[1,0].set_xlabel('Lambda 1 GP3', fontsize=20)
ax17[1,0].set_ylabel('Period GP3 (days)', fontsize=20)

ax17[1,1].loglog(data_fourthrun['Lambda 1'], period4, linestyle='none', marker='o')
ax17[1,1].set_xlabel('Lambda 1 GP4', fontsize=20)
ax17[1,1].set_ylabel('Period GP4 (days)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Periods_vs_L1.png')
plt.close(fig17)


#Period vs L2
fig18, ax18=plt.subplots(2,2, figsize=(15,15))
ax18[0,0].plot(data_firstrun['Lambda 2'], period1, linestyle='none', marker='o')
ax18[0,0].set_xlabel('Lambda 2 GP1', fontsize=20)
ax18[0,0].set_ylabel('GP1 Period (days)', fontsize=20)

ax18[0,1].plot(data_secondrun['Lambda 2'], period2, linestyle='none', marker='o')
ax18[0,1].set_xlabel('Lambda 2 GP2', fontsize=20)
ax18[0,1].set_ylabel('Period GP2 (days)', fontsize=20)

ax18[1,0].plot(data_thirdrun['Lambda 2'], period3, linestyle='none', marker='o')
ax18[1,0].set_xlabel('Lambda 2 GP3', fontsize=20)
ax18[1,0].set_ylabel('Period GP3 (days)', fontsize=20)

ax18[1,1].plot(data_fourthrun['Lambda 2'], period4, linestyle='none', marker='o')
ax18[1,1].set_xlabel('Lambda 2 GP4', fontsize=20)
ax18[1,1].set_ylabel('Period GP4 (days)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Periods_vs_L2.png')
plt.close(fig18)

#Amplitude vs L2
fig19, ax19=plt.subplots(2,2, figsize=(15,15))
ax19[0,0].semilogy(data_firstrun['Lambda 2'], amplitude1, linestyle='none', marker='o')
ax19[0,0].set_xlabel('Lambda 2 GP1', fontsize=20)
ax19[0,0].set_ylabel('Amplitude GP1 (days)', fontsize=20)

ax19[0,1].semilogy(data_secondrun['Lambda 2'], amplitude2, linestyle='none', marker='o')
ax19[0,1].set_xlabel('Lambda 2 GP2', fontsize=20)
ax19[0,1].set_ylabel('Amplitude GP2 (days)', fontsize=20)


ax19[1,0].semilogy(data_thirdrun['Lambda 2'], amplitude3, linestyle='none', marker='o')
ax19[1,0].set_xlabel('Lambda 2 GP3', fontsize=20)
ax19[1,0].set_ylabel('Amplitude GP3 (days)', fontsize=20)

ax19[1,1].semilogy(data_fourthrun['Lambda 2'], amplitude4, linestyle='none', marker='o')
ax19[1,1].set_xlabel('Lambda 2 GP4', fontsize=20)
ax19[1,1].set_ylabel('Amplitude GP4 (days)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_vs_L2.png')
plt.close(fig19)

#Amplitude vs L1
fig20, ax20=plt.subplots(2,2, figsize=(15,15))
ax20[0,0].loglog(data_firstrun['Lambda 1'], amplitude1, linestyle='none', marker='o')
ax20[0,0].set_xlabel('Lambda 1 GP1', fontsize=20)
ax20[0,0].set_ylabel('Amplitude GP1 (days)', fontsize=20)

ax20[0,1].loglog(data_secondrun['Lambda 1'], amplitude2, linestyle='none', marker='o')
ax20[0,1].set_xlabel('Lambda 1 GP2', fontsize=20)
ax20[0,1].set_ylabel('Amplitude GP2 (days)', fontsize=20)

ax20[1,0].loglog(data_thirdrun['Lambda 1'], amplitude3, linestyle='none', marker='o')
ax20[1,0].set_xlabel('Lambda 1 GP3', fontsize=20)
ax20[1,0].set_ylabel('Amplitude GP3 (days)', fontsize=20)

ax20[1,1].loglog(data_fourthrun['Lambda 1'], amplitude4, linestyle='none', marker='o')
ax20[1,1].set_xlabel('Lambda 1 GP4', fontsize=20)
ax20[1,1].set_ylabel('Amplitude GP4 (days)', fontsize=20)

plt.tight_layout()
plt.savefig(figpath + '\\' + 'Amplitudes_vs_L1.png')
plt.close(fig20)












