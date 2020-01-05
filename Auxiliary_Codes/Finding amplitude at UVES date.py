#Author: Emma Carli 
#INITIALISATION
#clear variables?
import numpy as np
import interpacf
import astropy.stats
from astropy.table import Table
k=-1 #k will be the star number in our list (the order is not significant)
fluxatUVEStable=np.zeros((67,2)) #This will be a dataset with the star's EPIC ID as the first column, and the other columns are the periods (rough and regular) and their error
d2458133=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458133.5.txt")
d2458136=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458136.5.txt")
d2458164=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\2458164.5.txt")
startlist=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\start.txt")

# =============================================================================
#PICKING A STAR
f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    fluxatUVES=0
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    starint=int(float(star))
    print('Star',''.join(starlist), '...') #After this the stellar periods will be printed
 # =============================================================================
    #RETRIEVING THE LIGHT CURVE
    if starint in [211699606, 212006344, 211427097]:
        linklist=list('https://archive.stsci.edu/hlsps/k2sff/c16/211300000/90837/hlsp_k2sff_k2_lightcurve_211390837-c16_kepler_v1_llc-default-aper.txt') #Take a random link to an EVEREST FITS file and make it a list
        newlinklist = linklist[:42] + starlist[0:4] + linklist[46:52] + starlist[4:9] + linklist[57:83] + starlist +linklist[92:] #Fill in EPIC ID occurrences in the link using the stellar ID list
        link=''.join(newlinklist) #Create the link
        data=np.genfromtxt(link, skip_header=1, delimiter=',')
        time=data[:,0]
        flux=data[:,1] 
        error=np.zeros_like(flux)
    else:
        #Here we create the link to the POLAR txt file corresponding to this star
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
    #REMOVING LONG TERM TRENDS 
    #Fit a 2nd degree polynomial to find long-term trend (LTT) due to relativistic effects.
    LTTcoefs=np.polyfit(time,flux,2) #Find the coefficients of the LTT polynomial
    LTT=(LTTcoefs[1]*time)+(LTTcoefs[0]*(time**2))+LTTcoefs[2] #Create the LTT polynomial
    flux=flux-LTT #Remove the LTT from the data to flatten it
    flux=flux/(np.max(np.abs(flux)))
    # =============================================================================
    
    if starint in d2458133:
        fluxatUVES=flux[np.abs(time - 58133).argmin()]
    if starint in d2458136:
        fluxatUVES=flux[np.abs(time - 58136).argmin()]
    if starint in d2458164:
        fluxatUVES=flux[np.abs(time - 58164).argmin()]

    k=k+1 #Go to the next line in the table containing ID and periods
    #Fill in the table : ID of the star followed by the period measurements and their error
    fluxatUVEStable[k][0]=int(star)
    fluxatUVEStable[k][1]=fluxatUVES   
        
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)


UVESfluxtable=Table(fluxatUVEStable,names=['ID','Relative flux at UVES measurement date']) #Make an astropy table with the data for easy handling
UVESfluxtable.write('UVESflux.html', overwrite=True) #Retrieve the astropy table as an html table
