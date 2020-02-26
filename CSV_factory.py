import Image
from termcolor import colored
import cv2
import os

f= open("fruits360_CSV.txt","w+")
f.write("Class,R-avg,G-avg,B-avg,Shape,Energy,Correlation,Contrast,Homogenity\n")
directory = "fruits-360\Training"
i = 0
for filename in os.listdir(directory):
    imageDir = directory + "\\"+ filename
    for image in os.listdir(imageDir):    
        i+=1   
        print(imageDir+"\\"+image+"..."+"{0:.1f}".format(round(i/60498*100,1))+"% complete")
        img = cv2.imread(imageDir+"\\"+image)
        img = Image.image(img,filename)
        f.write(img.getFeatureString())
        

