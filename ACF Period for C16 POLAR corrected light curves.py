#Author: Emma Carli 
#INITIALISATION
#clear variables?
import numpy as np
import interpacf
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy import signal
import astropy.stats
from astropy.table import Table
##########################################
##########PATH TO CHANGE HERE#############
##########################################
filepathlist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Figures\Polar\C16") #Path to the folder containing graphs for POLAR
k=-1 #k will be the star number in our list (the order of the stars is not significant)
ID_and_periods=np.zeros((73,5)) #This will be a dataset with the star's EPIC ID as the first column, and the other columns are the periods (rough and regular) and their error
startlist=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\start.txt")

# =============================================================================
#PICKING A STAR
##########################################
##########PATH TO CHANGE HERE#############
##########################################
f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    period=0 #In case the more robust period measurement cannot be made, set it to 0 so you can still fill the table
    perioderror=0 #Do the same with the robust period error
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    starint=int(float(star))
    print('Star',''.join(starlist), '...') #After this the stellar periods will be printed

# =============================================================================    
  
 # =============================================================================
    #RETRIEVING THE LIGHT CURVE
    if starint in [211699606, 212006344, 211427097]: #The three stars for which SFF correction was picked
        linklist=list('https://archive.stsci.edu/hlsps/k2sff/c16/211300000/90837/hlsp_k2sff_k2_lightcurve_211390837-c16_kepler_v1_llc-default-aper.txt') #Take a random link to an SFF light curve and make it a list
        newlinklist = linklist[:42] + starlist[0:4] + linklist[46:52] + starlist[4:9] + linklist[57:83] + starlist +linklist[92:] #Fill in EPIC ID occurrences in the link using the stellar ID list
        link=''.join(newlinklist) #Create the link
        data=np.genfromtxt(link, skip_header=1, delimiter=',') #Retrieve the data from this light curve
        time=data[:,0]
        flux=data[:,1] 
        error=np.zeros_like(flux) #No error is provided with SFF
    else:
        #Here we create the link to the POLAR txt file corresponding to the star
##########################################
##########PATH TO CHANGE HERE#############
##########################################
        linklist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Polar Detrended LCs\ktwo211418016c16_lpd_LC.txt") #Take a random link to a POLAR txt file and make it a list
        newlinklist = linklist[:90] + starlist +linklist[99:] #Replace the EPIC ID in the link using the stellar ID list
        link=''.join(newlinklist) #Create the link
        data=np.genfromtxt(link) #Here the column data from the POLAR txt file is retrieved
        time=data[:,0] #And the two colums are separated
        flux=data[:,1] 
        error=data[:,2]
    # =============================================================================
    
    # =============================================================================
    #REMOVAL OF START AND/OR END
    if starint in [211814413, 211827122, 211696686]  :
        flux=flux[(time <= 58170)]
        time = time[(time <= 58170)]
    if starint in startlist:
        flux=flux[(time >= 58100)]
        time = time[(time >= 58100)]
    # =============================================================================
    
    # =============================================================================
    #DATA CLEANING 
    time=time[~np.isnan(flux)] #Remove timestamps corresponding to flux NaNs
    flux = flux[~np.isnan(flux)] #Remove NaNs in the flux
    sigmaclip=astropy.stats.sigma_clip(flux,3) #Perform sigma-clipping with sigma=3, value chosen arbitrarily
    mask=sigmaclip.mask #Retrieve the boolean mask of the sigma clipping
    flux=flux[~mask] #Remove the outliers from the flux
    time=time[~mask] #Remove the timestamps corresponding to the outliers
    flux=flux-(np.median(flux)) #Normalise to 0 to be able to perform ACF (McQuillan et al. 2013)
    [time,flux]=interpacf.interpolate_missing_data(time,flux) #Interpolate data in case of non regular long cadences
    # =============================================================================
    
    
    # =============================================================================    
    #REBINNING  IF NEEDED  
    #Downsample the data to 2 hours instead of 30 minutes (4 times smaller dataset)
    #end =  4 * int(len(flux)/4) 
    #flux=np.mean(flux[:end].reshape(-1, 4), 1)
    #time=np.mean(time[:end].reshape(-1, 4), 1)
    # =============================================================================
       

    
    # =============================================================================
    #REMOVING LONG TERM TRENDS 
    #Fit a 2nd degree polynomial to find long-term trend (LTT) due to relativistic effects.
    LTTcoefs=np.polyfit(time,flux,2) #Find the coefficients of the LTT polynomial
    LTT=(LTTcoefs[1]*time)+(LTTcoefs[0]*(time**2))+LTTcoefs[2] #Create the LTT polynomial
    
    #Plot the data and the LTT together for visual comparison
    flux1=flux+1 #Add 1 to have the data centred around 1
    LTT1=LTT+1
    fig, ax = plt.subplots() #Create new figure and axes for subplots
    ax.plot(time, flux1, label='Data', color='k', marker='.', linestyle='none') #Plot photometric data
    ax.plot(time, LTT1, label='LTT', color='r') #Plot LTT
    ax.legend()
    ax.set_title('Comparing LTT and data (C16)')
    ax.set_xlabel('Time (BJD-2400000.0)')
    ax.set_ylabel('Relative flux')
    ax.tick_params(labelsize=15)
    ax.ticklabel_format(useOffset=False)  #Make sure matplotlib doesn't use an offset
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]):
        item.set_fontsize(20)
    plt.tight_layout()  #Make sure box doesn't overlap information
    figpathlist= filepathlist + list('\\') + starlist + list('_LTT.png') #Create a list for the LTT figure path
    figpath= ''.join(figpathlist) #Turn the list into a string
    plt.savefig(figpath) #Save the figure
    plt.close(fig) #Close the figure
    flux=flux-LTT #Remove the LTT from the data to flatten it
    flux1=flux+1  #To show on graphs it is more common to have the data centred on 1
    # =============================================================================
    
    # =============================================================================
    #COMPUTE ACF, ROUGH PERIOD AND PLOT
    [entriestime,ACF]=interpacf.interpolated_acf(time,flux) #Compute ACF of data, and retrieve entries in units of time elapsed.
    ACF=ACF/np.max(ACF) #Normalise the ACF
    coefstime=np.polyfit(range(len(entriestime)),entriestime,1)  #Find the relationship between datapoint number (entry) and time
    
    #Smooth the ACF using McQuillan et al. 2013 parameters
    sigma = 18/2.355
    truncate = 56/sigma
    smooth_ACF = gaussian_filter(ACF, sigma, truncate=truncate)
    smooth_ACF=smooth_ACF/np.max(smooth_ACF) #Normalise the smoothed ACF
    
    # Detect first two peaks in the ACF
    relative_maxes = signal.argrelmax(smooth_ACF, order=20)[0]
    relative_maxes = relative_maxes[0:2]
    
    # Detect highest peak of the two
    absolute_max_index = relative_maxes[np.argmax(smooth_ACF[relative_maxes])]
    roughperiod = entriestime[absolute_max_index] #The rough period will be the time elapsed since the start to this peak
    
    #Plot the ACF
    fig3, ax3 = plt.subplots() #Create a new figure to plot two graphs
    ax3.plot(entriestime, ACF, label='ACF', color='k', lw=2) #Plot the ACF
    ax3.plot(entriestime, smooth_ACF, label='Smoothed ACF', ls='--', color='r') #Plot the smoothed ACF
    ax3.axvline(roughperiod, ls='--', color='b', label='Rough period') #Label the rough period
    ax3.tick_params(labelsize=15)
    ax3.legend()
    ax3.set_title('ACF (C16)')
    ax3.set_xlabel('Period (days)')
    ax3.ticklabel_format(useOffset=False)

    roughperiod_dataentry=np.where(entriestime==roughperiod) #Find the entry number corresponding to the rough period in the data
    roughperiod_dataentry=roughperiod_dataentry[0] #Make this index a number
    print("The rough period is", roughperiod)
    print("The corresponding number of entries is", roughperiod_dataentry)
    # =============================================================================
    
    # =============================================================================      
    #COMPUTE ROUGH PERIOD ERROR
    #Now find where the smoothed ACF attains its half maximum on either side of the rough period peak.
    #Set up the problem : find the half max and the range where to look (chose arbitrarily to look in half the rough period about the peak)
    halfmax=(smooth_ACF[roughperiod_dataentry])/2 #Find the half-maximum value of the rough period peak
    halfperiod_dataentry=int(np.rint(roughperiod_dataentry/2)) #Find the number of entries corresponding to half the period
    #Create two arrays of zeros with size of number of entries of half the period. 
    #These two arrays will be filled with the differences between the smoothed ACF at entry and its half max.
    differenceplus=np.zeros(halfperiod_dataentry) #Using entries on the right of the peak within half a rough period
    differenceminus=np.zeros(halfperiod_dataentry) #Using entries on the left of the peak within half a rough period
    for i in range(halfperiod_dataentry): #Look in right of peak within chosen range
       if roughperiod_dataentry+i < len(flux):
           differenceplus[i]=np.abs(smooth_ACF[roughperiod_dataentry+i]-halfmax) #Find the difference between the value in range and the half max value
    indexplus=np.argmin(differenceplus) #Find the minimum of this difference and its index, i.e. where the function attains the half max on the right of the peak.
    for j in range(halfperiod_dataentry): #Same process
        if roughperiod_dataentry-j >0:
            differenceminus[j]=np.abs(smooth_ACF[roughperiod_dataentry-j]-halfmax)
    indexminus=np.argmin(differenceminus) #Index of where the smoothed ACF attains its half max on the left of the peak.
    
    #Find the HWHM of the rough period peak.
    HWHM_dataentry=((indexplus+indexminus)/2) #Find the HWHM in units of entries.
    #Now find the HWHM in time units.
    HWHM=(coefstime[0]*HWHM_dataentry)+coefstime[1]
    print('The error on the rough period is', HWHM)
    print('The corresponding number of entries is', HWHM_dataentry)
    # =============================================================================
    
    # =============================================================================
    #COMPUTE REAL PERIOD
    #Setting possible peak locations indices, "peaksrange", within 20% of rough period multiples
    peaksrange=[] #Create an empty matrix, where the peaks range will be stored
    for n in range(2,10) : #Going through ten possible ACF peaks,i.e. ten multiples of the period as in McQuillan et al. 2013
        lowerlimit=(n*roughperiod)-(roughperiod*0.20)
        upperlimit=(n*roughperiod)+(roughperiod*0.20)
    #If this multiple of the period is included in the dataset, proceed. 
        indicesnperiod=np.where((entriestime>=lowerlimit) & (entriestime<=upperlimit))[0]
    #Otherwise, break the loop and n will be the total number of period multiples in the dataset.
        if indicesnperiod.size>0:
          peaksrange=np.append(peaksrange,indicesnperiod) #Append that to the peaks range array.
          peaksrange=peaksrange.astype(int) #Make this array into integers so that it is iterable later.
        else:
          break
      
    if n!=2: #If there is not just space for one period in the data
        #Find the peaks of periods multiples in the smoothed ACF.
        ACF_maxima=signal.argrelmax(smooth_ACF,order=50)
        peaks=roughperiod_dataentry #The first peak entry will be the one computed earlier. The others will be appended to this array.
        for i in np.nditer(ACF_maxima): #Iterate over each extremum
            if i in peaksrange: #Verify that it is in the peaks range defined earlier
                if i-(peaks[len(peaks)-1])<1.2*roughperiod_dataentry: #Verify that we are looking at consecutive peaks of the ACF
                    peaks=np.append(peaks,i) #Append to list of peaks
        
        #Now check that peaks are at least further than 30% of the rough period to each other.
        #This is to make sure that we don't have several maxes chosen for 1 peak, if smoothing didn't remove all erroneous maxes.
        #This method is from MacQuillan et al. 2013.
        dividedpeaks=peaks/roughperiod_dataentry #Find the period multiples by dividing the peak positions by the period entry
        rintdividedpeaks=np.rint(dividedpeaks) #Round these multiples -- if there are several, it means a peak has been detected twice (it has two maxes)
        goodpeaks=[] #Create an empty matrix for the good peaks to be appended to 
        for i in range(1,10): #There are a maximum of 10 peaks as said before
            whereisi=np.where(rintdividedpeaks==i) #Find where there are i-th multiples of the rough period
            dividedpeaksarei=dividedpeaks[whereisi] #Find their index in the ACF
            if dividedpeaksarei.size>0: #If this multiple is present in the ACF
                bestpeak=dividedpeaksarei[np.abs(dividedpeaksarei-i).argmin()] #Find which of the peaks in the period multiple is closest to the rough period
                goodpeaks=np.append(goodpeaks,bestpeak*roughperiod_dataentry) #Append the index of that peak in the ACF 
        peaks=goodpeaks.astype(int) #Make sure they have no .0 (integers)
        
        if len(peaks)!=1: #If there is not just one peak in the ACF that is a multiple of the period
            #Now find the robust period measurement which is the averaged difference between the peaks.
            peaksdifferences=roughperiod_dataentry
            peaksdifferences=np.append(peaksdifferences,np.diff(peaks))
            period_dataentry=(np.mean(peaksdifferences))
            period=(coefstime[0]*period_dataentry)+coefstime[1]  #Find the corresponding number of entries
            print('The more robust period measurement is', period)
            print('Which corresponds to',period_dataentry,'entries')
            
            #Plot the smoothed ACF with peaks positions overlaid.
            ymin=np.min(smooth_ACF) #Limits of dashed lines, as before
            ymax=np.max(smooth_ACF)
            ax3.vlines(entriestime[peaks], ymin, ymax, colors='g', linestyles='dashed', label='Multiples of period')
            ax3.legend()
            #Change the font size to 20
            for item in ([ax3.title, ax3.xaxis.label, ax3.yaxis.label]):
                item.set_fontsize(20)
            plt.tight_layout()
            fig3pathlist= filepathlist + list('\\') + starlist + list('_ACF.png') #As before
            fig3path= ''.join(fig3pathlist)
            plt.savefig(fig3path)
            plt.close(fig3)
            # =============================================================================
            
            # =============================================================================
            #COMPUTE REAL PERIOD ERROR
            MAD=np.median(np.abs(peaksdifferences-np.median(peaksdifferences))) #Compute the MAD of the difference in entries between each smoothed ACF peak
            perioderror_dataentries=((1.483*MAD)/(np.sqrt(len(peaks)-1))) #Compute the error of the period using the McQuillan et al. 2013 formula
            perioderror=(coefstime[0]*perioderror_dataentries)+coefstime[1] #Convert this error in time units
            if perioderror<0:  #If this happens, it's that the period error was 0 in terms of entries
                perioderror=0
            print('The period error is', perioderror)
            print('Which corresponds to', perioderror_dataentries, 'entries')
            # =============================================================================
            
            # =============================================================================
            #EYE MATCHING THE REAL PERIOD
            #Plot lines at multiples of the period on the graph.
            firstline=np.argmax(flux)  #Find the maximum of the light curve as a reference point
            firstperiod=time[firstline]-(20*period)
            lastperiod=time[firstline]+(20*period)
            periods=np.linspace(firstperiod,lastperiod,41)  #Take fourty periods as x-axis limit will not allow to plot them all
            
            #Do the same for the rough period
            firstroughperiod=time[firstline]-(20*roughperiod)
            lastroughperiod=time[firstline]+(20*roughperiod)
            roughperiods=np.linspace(firstroughperiod,lastroughperiod,41)
        
            #Plot the dataset overlaid with period limits.
            ymin=np.min(flux1) #Define where the dotted lines of the markers start and end on the graph
            ymax=np.max(flux1)
            fig1, ax1 = plt.subplots() #Create a new figure with subplot axes.
            ax1.plot(time, flux1, label='Data', color='k',  marker='.', linestyle='none') #Plot the data
            ax1.vlines(periods, ymin, ymax, colors='r', linestyles='solid', label='Periods') #Plot the period markers
            ax1.vlines(roughperiods, ymin, ymax, colors='b', linestyles='dashed', label='Rough periods') #Plot the rough period markers
            ax1.legend()
            ax1.set_title('Eye-matching the periods (C16)')
            ax1.set_xlabel('Time (BJD-2400000.0)')
            ax1.set_ylabel('Relative flux')
            ax1.set_xlim(time[0]-1,time[len(time)-1]) #Start x-axis a bit before so can see first vertical line.
            ax1.tick_params(labelsize=15)
            ax1.ticklabel_format(useOffset=False)
            #Change font size to 20
            for item in ([ax1.title, ax1.xaxis.label, ax1.yaxis.label]):
                item.set_fontsize(20)
            plt.tight_layout()
            fig1pathlist= filepathlist + list('\\') + starlist + list('_EyeMatching.png') #As before
            fig1path= ''.join(fig1pathlist)
            plt.savefig(fig1path)
            plt.close(fig1)
            # =============================================================================
    
    
    if n==2 or len(peaks)==1: #If there is space just for one period in the dataset, or if only one ACF period multiple could be found
        #Change font size to 20
        for item in ([ax3.title, ax3.xaxis.label, ax3.yaxis.label]):
            item.set_fontsize(20)
        plt.tight_layout()
        fig3pathlist= filepathlist + list('\\') + starlist + list('_ACF.png') #As before
        fig3path= ''.join(fig3pathlist)
        plt.savefig(fig3path)
        plt.close(fig3)
        #In this case we stick to the rough period only and no robust period determination will be made.
        
        # =============================================================================
        #EYE MATCHING THE ROUGH PERIOD
        #As before
        firstline=np.argmax(flux)
        firstroughperiod=time[firstline]-(20*roughperiod)
        lastroughperiod=time[firstline]+(20*roughperiod)
        roughperiods=np.linspace(firstroughperiod,lastroughperiod,41)
        
        #Plot the dataset overlaid with rough period limits.
        ymin=np.min(flux1) #Define where the dotted lines of the markers start and end on the graph
        ymax=np.max(flux1)
        fig1, ax1 = plt.subplots() #Create a new figure with subplot axes.
        ax1.plot(time, flux1, label='Data', color='k',  marker='.', linestyle='none') #Plot the data
        ax1.vlines(roughperiods, ymin, ymax, colors='b', linestyles='dashed', label='Rough periods') #Plot the rough period markers
        ax1.legend()
        ax1.set_title('Eye-matching the rough periods (C16)')
        ax1.set_xlabel('Time (BJD-2400000.0)')
        ax1.set_ylabel('Relative flux')
        ax1.set_xlim(time[0]-1,time[len(time)-1]) #Start x-axis a bit before so can see first vertical line.
        ax1.ticklabel_format(useOffset=False)
        ax1.tick_params(labelsize=15)
        for item in ([ax1.title, ax1.xaxis.label, ax1.yaxis.label]):
            item.set_fontsize(20)
        plt.tight_layout()
        fig1pathlist= filepathlist + list('\\') + starlist + list('_EyeMatching.png') #As before
        fig1path= ''.join(fig1pathlist)
        plt.savefig(fig1path)
        plt.close(fig1)
        # =============================================================================

    k=k+1 #Go to the next line in the table containing ID and periods
    #Fill in the table : ID of the star followed by the period measurements and their error
    ID_and_periods[k][0]=int(star)
    ID_and_periods[k][1]=roughperiod
    ID_and_periods[k][2]=HWHM
    ID_and_periods[k][3]=period
    ID_and_periods[k][4]=perioderror      
        
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)

#Round to reasonable values
ID_and_periods[:,1]=np.round(ID_and_periods[:,1],1)
ID_and_periods[:,2]=np.round(ID_and_periods[:,2],1)
ID_and_periods[:,3]=np.round(ID_and_periods[:,3],2)
ID_and_periods[:,4]=np.round(ID_and_periods[:,4],2)

periods_table=Table(ID_and_periods,names=['ID','Rough Period C16','Rough Period Error C16','Period C16','Period Error C16']) #Make an astropy table with the data for easy handling
periods_table.write('periods_Polar_C16.html', overwrite=True) #Retrieve the astropy table as an html table


