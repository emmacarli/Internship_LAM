#Author: Emma Carli 
#INITIALISATION
#clear variables?
import numpy as np
import interpacf
import astropy.stats
from numpy import mean, sqrt, square
from astropy.table import Table 
k=-1 #k will be the star number in our list (the order is not significant)
rmstable=np.zeros((66,2)) #This will be a dataset with the star's EPIC ID as the first column, and the other columns are the periods (rough and regular) and their error
startlist=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\start.txt")


# =============================================================================
#PICKING A STAR
f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    starint=int(float(star))
    #Here we create the link to the POLAR txt file corresponding to this star
    linklist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Polar Detrended LCs\ktwo211418016c16_lpd_LC.txt") #Take a random link to a POLAR txt file and make it a list
    newlinklist = linklist[:91] + starlist +linklist[100:] #Replace the EPIC ID in the link using the stellar ID list
    link=''.join(newlinklist) #Create the link
# =============================================================================    
  
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
    #REBINNING    
    #Downsample the data to 2 hours instead of 30 minutes (4 times smaller dataset)
    end =  4 * int(len(flux)/4) 
    flux=np.mean(flux[:end].reshape(-1, 4), 1)
    time=np.mean(time[:end].reshape(-1, 4), 1)
    # =============================================================================
    
    rms = sqrt(mean(square(flux)))
    
    k=k+1 #Go to the next line in the table containing rms
    #Fill in the table : ID of the star followed by the stellar activity rms
    rmstable[k][0]=int(star)
    rmstable[k][1]=rms
    
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)


rms_table=Table(rmstable,names=['ID','RMS']) #Make an astropy table with the data for easy handling
rms_table.write('RMS Table.html') #Retrieve the astropy table as an html table