import Image
from termcolor import colored
import cv2
import os
import json
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app, support_credentials=True)

#Ova skripta se treba pozvat iz aplikacije kad korisnik unese sliku.
#ta slika se treba spremit u folder newImage podbilokojim nazivom pa ce ju ova skripta obraditi
#varijabla result sadrzi podatke slike i njih treba nekako vratiti u aplikaciju, preko json ili ih zapisati posebno u neku text datoteku
#pa da web aplikacija procita to iz te datoteke
@app.route("/getFeatures")
def getFeatures():    
    directory = "newImage"
    for image in os.listdir(directory):           
        img = cv2.imread(directory+"\\"+image)
        cv2.imshow("img",img)
        cv2.waitKey()
        dim = (100, 100)
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        img = Image.image(resized,"-")          
        result = img.getFeatures()
        obj={
            "R-avg" : result[0],
            "G-avg" : result[1],
            "B-avg" : result[2],
            "Shape" : result[3],
            "Energy": result[4],
            "Correlation": result[5],
            "Contrast" : result[6],
            "Homogenity": result[7]
        }   
        x= json.dumps(obj)
        print(result)
    return x

if __name__ == "__main__":
    app.run()