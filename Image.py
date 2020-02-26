import GreyFeatures
import Shape
import RGB_Average

class image:
    def __init__(self, image,klasa):
        self.clas = klasa        
        self.image = image       
        self.getRGB()
        self.getShape()
        self.getGreyFeatures()

    def getRGB(self):
        self.R,self.G,self.B = RGB_Average.getColor(self.image)
    def getShape(self):
        self.shape=Shape.getShape(self.image)
    def getGreyFeatures(self):
        self.energy,self.corr,self.contr,self.homg = GreyFeatures.calculateFeatures(self.image)
    
    def getFeatureString(self):
        return self.clas+"," + str(self.R) +","+str(self.G) +","+str(self.B) +","+"{0:.4f}".format(round(self.shape,4))+","+"{0:.4f}".format(round(self.energy,4))+","+"{0:.4f}".format(round(self.corr,4))+","+"{0:.1f}".format(round(self.contr,1))+","+"{0:.4f}".format(round(self.homg,4))+"\n"
    def getFeatures(self):
        return self.R,self.G,self.B,round(self.shape,4),round(self.energy,4),round(self.corr,4),round(self.contr,4),round(self.homg,4)




