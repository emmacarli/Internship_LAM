#Author: Emma Carli 
#INITIALISATION
#clear variables?
import numpy as np
import interpacf
import matplotlib.pyplot as plt
import astropy.stats
from astropy.io import fits
from brokenaxes import brokenaxes

filepathlist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Figures\Polar\C5C16Comparison") #Path to the folder containing graphs for POLAR
d2458133=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458133.5.txt")
d2458136=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458136.5.txt")
d2458164=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458164.5.txt")
startlist=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\start.txt")


    

# =============================================================================
#PICKING A STAR
f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    starlist=list(star) #Turn the star's name into a list
    starint=int(float(star))
    del starlist[9] #Remove the "return" character
    print('Star', ''.join(starlist), '...') #After this the stellar periods will be printed
    #Here we create the link to the POLAR txt file corresponding to this star
    linklist=list('https://archive.stsci.edu/hlsps/polar/c05/211800000/14413/hlsp_polar_k2_lightcurve_211814413-c05_kepler_v1_llc.fits') #Take a random link to an EVEREST FITS file and make it a list
    newlinklist = linklist[:42] + starlist[0:4] + linklist[46:52] + starlist[4:9] + linklist[57:83] + starlist +linklist[92:] #Fill in EPIC ID occurrences in the link using the stellar ID list
    link=''.join(newlinklist) #Create the link
# =============================================================================    
  
    # =============================================================================
    #RETRIEVING THE LIGHT CURVE
    hdulist = fits.open(link,ignore_missing_end=True) #Open the FITS file
    arrays=hdulist[2] #Retrieve the arrays in the FITS file
    fluxc5=arrays.data['DETFLUX'] #Retrieve the flux 
    timec5=arrays.data['DETTIME'] #Retrieve the timestamps
    # =============================================================================
    
 # =============================================================================
    #RETRIEVING THE LIGHT CURVE
    if starint in [211699606, 212006344, 211427097]:
        linklist=list('https://archive.stsci.edu/hlsps/k2sff/c16/211300000/90837/hlsp_k2sff_k2_lightcurve_211390837-c16_kepler_v1_llc-default-aper.txt') #Take a random link to an EVEREST FITS file and make it a list
        newlinklist = linklist[:42] + starlist[0:4] + linklist[46:52] + starlist[4:9] + linklist[57:83] + starlist +linklist[92:] #Fill in EPIC ID occurrences in the link using the stellar ID list
        link=''.join(newlinklist) #Create the link
        data=np.genfromtxt(link, skip_header=1, delimiter=',')
        timec16=data[:,0]
        fluxc16=data[:,1] 
    else:
        #Here we create the link to the POLAR txt file corresponding to this star
        linklist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Polar Detrended LCs\ktwo211418016c16_lpd_LC.txt") #Take a random link to a POLAR txt file and make it a list
        newlinklist = linklist[:90] + starlist +linklist[99:] #Replace the EPIC ID in the link using the stellar ID list
        link=''.join(newlinklist) #Create the link
        data=np.genfromtxt(link) #Here the column data from the POLAR txt file is retrieved
        timec16=data[:,0] #And the two colums are separated
        fluxc16=data[:,1] 
    # =============================================================================
    
    # =============================================================================
    #REMOVAL OF START AND/OR END
    if starint in [211814413, 211827122, 211696686]  :
        fluxc16=fluxc16[(timec16 <= 58170)]
        timec16 = timec16[(timec16 <= 58170)]
    if starint in startlist:
        fluxc16=fluxc16[(timec16 >= 58100)]
        timec16 = timec16[(timec16 >= 58100)]
    # =============================================================================
    

    # =============================================================================
    #DATA CLEANING 
    timec5=timec5[~np.isnan(fluxc5)] #Remove timestamps corresponding to flux NaNs
    fluxc5 = fluxc5[~np.isnan(fluxc5)] #Remove NaNs in the flux
    sigmaclip=astropy.stats.sigma_clip(fluxc5,3) #Perform sigma-clipping with sigma=3, value chosen arbitrarily
    mask=sigmaclip.mask #Retrieve the boolean mask of the sigma clipping
    fluxc5=fluxc5[~mask] #Remove the outliers from the flux
    timec5=timec5[~mask] #Remove the timestamps corresponding to the outliers
    [timec5,fluxc5]=interpacf.interpolate_missing_data(timec5,fluxc5) #Interpolate data in case of non regular long cadences
    # =============================================================================
    
    # =============================================================================
    #DATA CLEANING 
    timec16=timec16[~np.isnan(fluxc16)] #Remove timestamps corresponding to flux NaNs
    fluxc16 = fluxc16[~np.isnan(fluxc16)] #Remove NaNs in the flux
    sigmaclip=astropy.stats.sigma_clip(fluxc16,3) #Perform sigma-clipping with sigma=3, value chosen arbitrarily
    mask=sigmaclip.mask #Retrieve the boolean mask of the sigma clipping
    fluxc16=fluxc16[~mask] #Remove the outliers from the flux
    timec16=timec16[~mask] #Remove the timestamps corresponding to the outliers
    [timec16,fluxc16]=interpacf.interpolate_missing_data(timec16,fluxc16) #Interpolate data in case of non regular long cadences
    # =============================================================================
    
    # =============================================================================
    #REMOVING LONG TERM TRENDS 
    #Fit a 2nd degree polynomial to find long-term trend (LTT) due to relativistic effects.
    LTTcoefs=np.polyfit(timec5,fluxc5,2) #Find the coefficients of the LTT polynomial
    LTT=(LTTcoefs[1]*timec5)+(LTTcoefs[0]*(timec5**2))+LTTcoefs[2] #Create the LTT polynomial
    fluxc5=fluxc5-LTT+1
    # =============================================================================
    
    # =============================================================================
    #REMOVING LONG TERM TRENDS 
    #Fit a 2nd degree polynomial to find long-term trend (LTT) due to relativistic effects.
    LTTcoefs=np.polyfit(timec16,fluxc16,2) #Find the coefficients of the LTT polynomial
    LTT=(LTTcoefs[1]*timec16)+(LTTcoefs[0]*(timec16**2))+LTTcoefs[2] #Create the LTT polynomial
    fluxc16=fluxc16-LTT+1
    # =============================================================================
    
    #Here define the limits of the time axis
    startofc5=np.min(timec5)
    endofc5=np.max(timec5)
    startofc16=np.min(timec16)
    endofc16=np.max(timec16)
    
    #Here concatenate the two campaigns together
    time=np.append(timec5,timec16)
    flux=np.append(fluxc5,fluxc16)
    
    
    #Create the plot with broken axes
    fig = plt.figure(figsize=(15,10))
    bax = brokenaxes(xlims=((startofc5, endofc5), (startofc16, endofc16)), d=0.005)
    bax.plot(time, flux, color='k',  marker='.', linestyle='none')
    #Label the UVES observations at three different dates
    if starint in d2458133:
        bax.axvline(58133, ls='--', color='b', linewidth=0.5, label='UVES observations') #Label the UVES observation
        bax.legend()
    if starint in d2458136:
        bax.axvline(58136, ls='--', color='b', linewidth=0.5, label='UVES observations') #Label the UVES observation
        bax.legend()
    if starint in d2458164:
        bax.axvline(58164, ls='--', color='b', linewidth=0.5, label='UVES observations') #Label the UVES observation
        bax.legend()
    #Set the labels
    bax.set_ylabel('Relative flux', labelpad=100, fontsize=25)
    bax.set_xlabel('Time (BJD - 2400000.0)', fontsize=25, labelpad=40)
    bax.ticklabel_format(useOffset=False)
    bax.tick_params(labelsize=20)
    plt.margins(0.1)
    
    #Save the figure
    figpathlist= filepathlist + list('\\') + starlist + list('_c5c16.png') #As before
    figpath= ''.join(figpathlist)
    plt.savefig(figpath)  
    plt.close(fig)
    
    
    
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)



#NOTES
#A lag is just an entry number
