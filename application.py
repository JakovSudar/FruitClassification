import Image
import cv2
import os
import json
import datetime
from flask_cors import CORS
from flask import Flask
import imutils
import urllib.request as urllib

application = Flask(__name__)
CORS(application, support_credentials=True)

#Ova skripta se treba pozvat iz aplikacije kad korisnik unese sliku.
#ta slika se treba spremit u folder newImage podbilokojim nazivom pa ce ju ova skripta obraditi
#varijabla result sadrzi podatke slike i njih treba nekako vratiti u aplikaciju, preko json ili ih zapisati posebno u neku text datoteku
#pa da web aplikacija procita to iz te datoteke
@application.route("/test")
def test():
    return "test uspjesan, aplikacija je objavljena i rest radi"

@application.route("/getFeatures/<string:url>")
def getFeatures(url):
    currentDT = datetime.datetime.now()
    print (str(currentDT) + " REQUEST ARRIVED\n")    
    directory = "https://ruapfruitclassification.azurewebsites.net/images/"
    img = imutils.url_to_image(directory+url)    
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
    data =  {
        "Inputs": {
                "input1":
                {
                    "ColumnNames": ["Class", "R-avg", "G-avg", "B-avg", "Shape", "Energy", "Correlation", "Contrast", "Homogenity"],
                     "Values": [ [ "value", result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7] ] ]
                },        },
            "GlobalParameters": {
                    }
    }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/3381f16d57184d1e9b30dea2f1e70257/services/266c87bfb6a14e52aa3a66fbef7f5120/execute?api-version=2.0&details=true'
    api_key = '5+3eMTkiQZSMZbHJ32ggqc09WwZx3iSzDBWt4ec/mbkp5jESGWvkpgQfc79qU9MZQXwJEafpV+rT1oZhU/9Dwg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    currentDT = datetime.datetime.now()
    print (str(currentDT)+" SENDING REQUEST TO AZURE")
    req = urllib.Request(url, body, headers) 
    try:
        response = urllib.urlopen(req)
        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)
        result = response.read()
        currentDT = datetime.datetime.now()
        print (str(currentDT)+" RETURNING JSON TO CLIENT")
        return result
    except urllib.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        

        return "error"
if __name__ == "__main__":
    application.run()