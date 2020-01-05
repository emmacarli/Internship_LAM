#Author: Emma Carli 
from PIL import Image
pathlist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Figures") 
savelist=list(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\Figures\Polar\Full_Comparison")

f = open(r"C:\Users\New\OneDrive - University of Glasgow\Work\Internship LAM\STARS.txt") #Open the list of stars considered in this project
star = f.readline() #Read the first line of the text file
while star: #Keep reading one line at a time till you get to the end of the list.
    starlist=list(star) #Turn the star's name into a list
    del starlist[9] #Remove the "return" character
    
    
    #Load images
    linkcomparison = pathlist + list('\Polar\C5C16Comparison') + list('\\') + starlist + list('_c5c16.png')
    linkcomparison= ''.join(linkcomparison)
    comparison=Image.open(linkcomparison)
    linkacfc5= pathlist + list('\Polar\C5') + list('\\') + starlist + list('_ACF.png')
    linkacfc5= ''.join(linkacfc5)
    acfc5=Image.open(linkacfc5)
    linkEMc5= pathlist + list('\Polar\C5') + list('\\') + starlist + list('_EyeMatching.png')
    linkEMc5= ''.join(linkEMc5)
    eyematchingc5=Image.open(linkEMc5)
    linkLTTc5 = pathlist + list('\Polar\C5') + list('\\') + starlist + list('_LTT.png')
    linkLTTc5= ''.join(linkLTTc5)
    LTTc5=Image.open(linkLTTc5)
    linkacfc16= pathlist + list('\Polar\C16') + list('\\') + starlist + list('_ACF.png')
    linkacfc16= ''.join(linkacfc16)
    acfc16=Image.open(linkacfc16)
    linkEMc16= pathlist + list('\Polar\C16') + list('\\') + starlist + list('_EyeMatching.png')
    linkEMc16= ''.join(linkEMc16)
    eyematchingc16=Image.open(linkEMc16)
    linkLTTc16= pathlist + list('\Polar\C16') + list('\\') + starlist + list('_LTT.png')
    linkLTTc16= ''.join(linkLTTc16)
    LTTc16=Image.open(linkLTTc16)
    
    #Create a new image
    finalfig=Image.new('RGB',(1080,1600),color=(1000,1000,1000))
    
    #Paste images in in right place
    finalfig.paste(comparison)
    finalfig.paste(acfc5,box=(20,1010))
    finalfig.paste(acfc16,box=(600,1010))
    finalfig.paste(LTTc5,box=(20,721))
    finalfig.paste(LTTc16,box=(600,721))
    finalfig.paste(eyematchingc5,box=(20,1300))
    finalfig.paste(eyematchingc16,box=(600,1300))
    
    #Save the figure
    figpathlist= savelist + list('\\') + starlist + list('_FullComparison.png') 
    figpath= ''.join(figpathlist)
    finalfig.save(figpath)

    star = f.readline() #Proceed to reading next line of text file 
f.close() #Close the file (the list of stars)