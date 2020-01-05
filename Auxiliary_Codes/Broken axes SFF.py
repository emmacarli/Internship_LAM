#Author: Emma Carli 
#INITIALISATION
#clear variables?
import numpy as np
import interpacf
import matplotlib.pyplot as plt
import astropy.stats
from brokenaxes import brokenaxes

filepathlist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Figures\SFF\C5C16Comparison") #Path to the folder containing graphs for POLAR
d2458133=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458133.5.txt")
d2458136=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458136.5.txt")
d2458164=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458164.5.txt")


    

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
    linklist=list('https://archive.stsci.edu/hlsps/k2sff/c16/211300000/90837/hlsp_k2sff_k2_lightcurve_211390837-c16_kepler_v1_llc-default-aper.txt') #Take a random link to an EVEREST FITS file and make it a list
    newlinklist = linklist[:42] + starlist[0:4] + linklist[46:52] + starlist[4:9] + linklist[57:83] + starlist +linklist[92:] #Fill in EPIC ID occurrences in the link using the stellar ID list
    link=''.join(newlinklist) #Create the link
# =============================================================================    
  
    # =============================================================================
    #RETRIEVING THE LIGHT CURVE
    datac16=np.genfromtxt(link, skip_header=1, delimiter=',')
    timec16=datac16[:,0]
    fluxc16=datac16[:,1] 
    # =============================================================================
    
    # =============================================================================
    linklist=list('https://archive.stsci.edu/hlsps/k2sff/c05/211300000/90837/hlsp_k2sff_k2_lightcurve_211390837-c05_kepler_v1_llc-default-aper.txt') #Take a random link to an EVEREST FITS file and make it a list
    newlinklist = linklist[:42] + starlist[0:4] + linklist[46:52] + starlist[4:9] + linklist[57:83] + starlist +linklist[92:] #Fill in EPIC ID occurrences in the link using the stellar ID list
    link=''.join(newlinklist) #Create the link
    # =============================================================================    
  
    # =============================================================================
    #RETRIEVING THE LIGHT CURVE
    datac05=np.genfromtxt(link,skip_header=1, delimiter=',')
    timec05=datac05[:,0]
    fluxc05=datac05[:,1] 
    # =============================================================================

    # =============================================================================
    #DATA CLEANING 
    timec05=timec05[~np.isnan(fluxc05)] #Remove timestamps corresponding to flux NaNs
    fluxc05 = fluxc05[~np.isnan(fluxc05)] #Remove NaNs in the flux
    sigmaclip=astropy.stats.sigma_clip(fluxc05,3) #Perform sigma-clipping with sigma=3, value chosen arbitrarily
    mask=sigmaclip.mask #Retrieve the boolean mask of the sigma clipping
    fluxc05=fluxc05[~mask] #Remove the outliers from the flux
    timec05=timec05[~mask] #Remove the timestamps corresponding to the outliers
    [timec05,fluxc05]=interpacf.interpolate_missing_data(timec05,fluxc05) #Interpolate data in case of non regular long cadences
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
    LTTcoefs=np.polyfit(timec05,fluxc05,2) #Find the coefficients of the LTT polynomial
    LTT=(LTTcoefs[1]*timec05)+(LTTcoefs[0]*(timec05**2))+LTTcoefs[2] #Create the LTT polynomial
    fluxc05=fluxc05-LTT+1
    # =============================================================================
    
    # =============================================================================
    #REMOVING LONG TERM TRENDS 
    #Fit a 2nd degree polynomial to find long-term trend (LTT) due to relativistic effects.
    LTTcoefs=np.polyfit(timec16,fluxc16,2) #Find the coefficients of the LTT polynomial
    LTT=(LTTcoefs[1]*timec16)+(LTTcoefs[0]*(timec16**2))+LTTcoefs[2] #Create the LTT polynomial
    fluxc16=fluxc16-LTT+1
    # =============================================================================
    
    #Here define the limits of the time axis
    startofc5=np.min(timec05)
    endofc5=np.max(timec05)
    startofc16=np.min(timec16)
    endofc16=np.max(timec16)
    
    #Here concatenate the two campaigns together
    time=np.append(timec05,timec16)
    flux=np.append(fluxc05,fluxc16)
    
    
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
    bax.set_xlabel('BJD - 2400000.0', fontsize=25, labelpad=40)
    bax.ticklabel_format(useOffset=False)
    bax.tick_params(labelsize=20)
    plt.margins(0.1)
    
    #Save the figure
    figpathlist= filepathlist + list('\\') + starlist + list('_c5c16_SFF.png') #As before
    figpath= ''.join(figpathlist)
    plt.savefig(figpath)  
    plt.close(fig)
    
    
    
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)



#NOTES
#A lag is just an entry number
