#Author: Emma Carli 
import numpy as np
import matplotlib.pyplot as plt
filepathlist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Figures\PolarSFFComparison") #Path to the folder containing graphs for POLAR
import astropy.stats


f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    starint=int(float(star))
    print('Star',''.join(starlist), '...') #After this the stellar periods will be printed
    
    linklistpolar=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Polar Detrended LCs\ktwo211418016c16_lpd_LC.txt") #Take a random link to a POLAR txt file and make it a list
    newlinklistpolar = linklistpolar[:90] + starlist +linklistpolar[99:] #Replace the EPIC ID in the link using the stellar ID list
    linkpolar=''.join(newlinklistpolar) #Create the link
    datapolar=np.genfromtxt(linkpolar) #Here the column data from the POLAR txt file is retrieved
    timepolar=datapolar[:,0] #And the two colums are separated
    fluxpolar=datapolar[:,1] 
    sigmaclippolar=astropy.stats.sigma_clip(fluxpolar,3) #Perform sigma-clipping with sigma=3, value chosen arbitrarily
    maskpolar=sigmaclippolar.mask #Retrieve the boolean mask of the sigma clipping
    fluxpolar=fluxpolar[~maskpolar] #Remove the outliers from the flux
    timepolar=timepolar[~maskpolar] #Remove the timestamps corresponding to the outliers
    
    linklistsff=list('https://archive.stsci.edu/hlsps/k2sff/c16/211300000/90837/hlsp_k2sff_k2_lightcurve_211390837-c16_kepler_v1_llc-default-aper.txt') #Take a random link to an EVEREST FITS file and make it a list
    newlinklistsff = linklistsff[:42] + starlist[0:4] + linklistsff[46:52] + starlist[4:9] + linklistsff[57:83] + starlist +linklistsff[92:] #Fill in EPIC ID occurrences in the link using the stellar ID list
    linksff=''.join(newlinklistsff) #Create the link
    datasff=np.genfromtxt(linksff, skip_header=1, delimiter=',')
    timesff=datasff[:,0]
    fluxsff=datasff[:,1] 
    sigmaclipsff=astropy.stats.sigma_clip(fluxsff,3) #Perform sigma-clipping with sigma=3, value chosen arbitrarily
    masksff=sigmaclipsff.mask #Retrieve the boolean mask of the sigma clipping
    fluxsff=fluxsff[~masksff] #Remove the outliers from the flux
    timesff=timesff[~masksff] #Remove the timestamps corresponding to the outliers
    

    fig, ax = plt.subplots() #Create new figure and axes for subplots
    ax.plot(timepolar+2400000, fluxpolar, label='POLAR', color='b', marker='.', linestyle='none') #Plot photometric data
    ax.plot(timesff+2454833, fluxsff, label='K2SFF', color='r', marker='.', linestyle='none') #Plot LTT
    ax.legend()
    ax.set_title('Comparing two corrections')
    ax.set_xlabel('Time (BJD)')
    ax.set_ylabel('Relative flux')
    ax.tick_params(labelsize=15)
    ax.ticklabel_format(useOffset=False)  #Make sure matplotlib doesn't use an offset
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]):
        item.set_fontsize(20)
    plt.tight_layout()  #Make sure box doesn't overlap information
    figpathlist= filepathlist + list('\\') + starlist + list('_K2SFF_POLAR.png') #Create a list for the LTT figure path
    figpath= ''.join(figpathlist) #Turn the list into a string
    plt.savefig(figpath) #Save the figure
    plt.close(fig) #Close the figure
    
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)

