#Author: Emma Carli 
#INITIALISATION
#clear variables?
import numpy as np
import matplotlib.pyplot as plt
startlist=np.genfromtxt(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\start.txt")


# =============================================================================
#PICKING A STAR
f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    starint=int(float(star))
    print('Star',''.join(starlist), '...') #After this the stellar periods will be printed
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
    if starint in [211818581, 212093295, 211750200, 211693508, 211505372, 211754103, 211946900, 211825485, 211922975, 212006344, 211699606, 211427097]:
        LTTcoefs=np.polyfit(time,flux,2) #Find the coefficients of the LTT polynomial
        LTT=(LTTcoefs[1]*time)+(LTTcoefs[0]*(time**2))+LTTcoefs[2] #Create the LTT polynomial
        flux=flux-LTT+1 #Remove the LTT from the data to flatten it
    # =============================================================================
    
    # =============================================================================    
    #REBINNING    
    start=time[0]
    end=time[len(time)-1]
    numberofdays=end-start
    numberof6hourintervals=numberofdays/0.25
    numberofbins=np.rint(numberof6hourintervals)
    bins=np.linspace(start,end,numberofbins+1)
    newtime=np.zeros(len(bins))
    newflux=np.zeros(len(bins))
    newerror=np.zeros(len(bins))
    for i in range(len(bins)-1):
        indices=np.where((time>=bins[i]) & (time<=bins[i+1]))[0]
        newtime[i]=np.nanmedian(time[indices])
        newflux[i]=np.nanmedian(flux[indices])
        newerror[i]=np.nanmedian(error[indices])/(np.sqrt(len(indices)))
    newtime=newtime[:-1]
    newflux=newflux[:-1]
    newerror=newerror[:-1]
    newtime=newtime[~np.isnan(newflux)] #Remove timestamps corresponding to flux NaNs
    newerror=newerror[~np.isnan(newflux)] #Remove timestamps corresponding to flux NaNs
    newflux=newflux[~np.isnan(newflux)] #Remove timestamps corresponding to flux NaNs
    # =============================================================================
    
    if True in np.isnan(newtime):
        print('Nans in time')
    if True in np.isnan(newflux):
        print('Nans in flux')
    if True in np.isnan(newerror):
        print('Nans in error')
    
    # =============================================================================    
    #WRITING THE NEW LIGHT CURVE
    linklist=list(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\Downsampled_Light_Curves_Polar_C16\211814413.txt') #Take a random link to a POLAR txt file and make it a list
    newlinklist = linklist[:120] + starlist +linklist[129:] #Replace the EPIC ID in the link using the stellar ID list
    link=''.join(newlinklist) #Create the link
    file=open(link, 'w')
    file.write('time\tflux\tsflux\n')
    file.write('----\t----\t-----\n')
    for j in range(len(newtime)-1):
        file.write('%f\t%f\t%f\n' % (newtime[j],newflux[j],newerror[j]))
    file.close()
     # =============================================================================    

    plt.errorbar(newtime,newflux,newerror, linestyle='none', marker='.', color='k')
    ax1=plt.gca()
    ax1.set_xlabel('BJD-2400000.0')
    ax1.set_ylabel('Relative flux')
    ax1.ticklabel_format(useOffset=False)
    plt.tight_layout()
    filepathlist=list(r'C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Gaussian Processes\Figures') #Take a random link to a POLAR txt file and make it a list
    fig1pathlist= filepathlist + list('\\') + starlist + list('_LightCurve.png') #As before
    fig1path= ''.join(fig1pathlist)
    plt.savefig(fig1path)
    fig1=plt.gcf()
    plt.close(fig1)
    plt.plot(newtime,newerror, linestyle='none', marker='.',color='k')
    ax2=plt.gca()
    ax2.set_xlabel('BJD-2400000.0')
    ax2.set_ylabel('Flux error')
    ax2.ticklabel_format(useOffset=False)
    plt.tight_layout()
    fig2pathlist= filepathlist + list('\\') + starlist + list('_Errors.png') #As before
    fig2path= ''.join(fig2pathlist)
    plt.savefig(fig2path)   
    fig2=plt.gcf()
    plt.close(fig2)
        
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)

