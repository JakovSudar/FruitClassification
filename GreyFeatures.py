import numpy as np
import cv2

from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops


class glcm:
    def __init__(self, image):
        distance = [1, 2, 3]
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        self.image=img_as_ubyte(image.astype('int64'))
        self.glcm_mat=greycomatrix(self.image,distances=distance,angles=angles,symmetric=True,normed=True)
        self.properties = ['correlation', 'homogeneity', 'contrast', 'energy']
            
    def correlation(self):
        return greycoprops(self.glcm_mat, 'correlation').flatten()
    
    def homogeneity(self):
        return greycoprops(self.glcm_mat, 'homogeneity').flatten()
    
    def contrast(self):
        return greycoprops(self.glcm_mat, 'contrast').flatten()
    
    def energy(self):
        return greycoprops(self.glcm_mat, 'energy').flatten()
    
    def glcm_all(self):
        return np.hstack([greycoprops(self.glcm_mat, props).ravel() for props in self.properties])
        
def calculateFeatures(img):    
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    feats = glcm(image)
    # energy
    energy = np.mean(feats.energy())
    # correlation
    corr = np.mean(feats.correlation())
    # contrast
    cont = np.mean(feats.contrast())
    # homogeneity
    homogeneity = np.mean(feats.homogeneity())
    
    return energy,corr,cont,homogeneity
   


