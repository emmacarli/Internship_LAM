#Author: Emma Carli 
#INITIALISATION
#clear variables?
import numpy as np
import matplotlib.pyplot as plt
filepathlist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Figures\Polar\Detrendedornot") #Path to the folder containing graphs for POLAR
k=-1 #k will be the star number in our list (the order is not significant)
ID_and_periods=np.zeros((73,5)) #This will be a dataset with the star's EPIC ID as the first column, and the other columns are the periods (rough and regular) and their error

# =============================================================================
#PICKING A STAR
f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    period=0 #In case the more robust period measurement cannot be made, set it to 0 so you can still fill the table
    perioderror=0 #Do the same with the robust period error
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    print('Star',''.join(starlist), '...') #After this the stellar periods will be printed
    
    # =============================================================================    
    #Here we create the link to the POLAR txt file corresponding to this star
    linklist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Polar Detrended LCs\ktwo211418016c16_lpd_LC.txt") #Take a random link to a POLAR txt file and make it a list
    newlinklist = linklist[:90] + starlist +linklist[99:] #Replace the EPIC ID in the link using the stellar ID list
    link=''.join(newlinklist) #Create the link
    # =============================================================================    
  
    # =============================================================================
    #RETRIEVING THE LIGHT CURVE FROM CORRECTED POLAR
    data=np.genfromtxt(link,comments='#') #Here the column data from the POLAR txt file is retrieved
    timedet=data[:,0] #And the two colums are separated
    fluxdet=data[:,1] 
    # =============================================================================
    
    # =============================================================================    
    #Here we create the link to the POLAR txt file corresponding to this star
    linklist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Polar not detrended LCs\ktwo211418016c16_lpd_LC.txt") #Take a random link to a POLAR txt file and make it a list
    newlinklist = linklist[:94] + starlist +linklist[103:] #Replace the EPIC ID in the link using the stellar ID list
    link=''.join(newlinklist) #Create the link
    # =============================================================================    
  
    # =============================================================================
    #RETRIEVING THE LIGHT CURVE FROM CORRECTED POLAR
    data=np.genfromtxt(link,comments='#') #Here the column data from the POLAR txt file is retrieved
    timenotdet=data[:,0] #And the two colums are separated
    fluxnotdet=data[:,1] 
    # =============================================================================
    
    # =============================================================================
    #Plot the dataset overlaid with period limits.
    fig1, ax1 = plt.subplots() #Create a new figure with subplot axes.
    ax1.plot(timedet, fluxdet, label='Detrended', color='b',  marker='.', linestyle='none') #Plot the data
    ax1.plot(timenotdet,fluxnotdet, label='Not detrended', color='r', marker='.', linestyle='none' )
    ax1.legend()
    ax1.set_title('Comparing C16 POLAR data')
    ax1.set_xlabel('BJD-2400000.0')
    ax1.set_ylabel('Relative flux')
    ax1.tick_params(labelsize=15)
    ax1.ticklabel_format(useOffset=False)
    #Change font size to 20
    for item in ([ax1.title, ax1.xaxis.label, ax1.yaxis.label]):
        item.set_fontsize(20)
    plt.tight_layout()
    fig1pathlist= filepathlist + list('\\') + starlist + list('_Detrendedornot.png') #As before
    fig1path= ''.join(fig1pathlist)
    plt.savefig(fig1path)
    plt.close(fig1)
    # =============================================================================
    
    

   
    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)



