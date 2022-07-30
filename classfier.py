import numpy as np 
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import image
import PIL.ImageOps

X,y=fetch_openml('mnist_784',version=1,return_X_y=True)
X=np.load('image.npz')['arr_0']
y=pd.read_csv("labels.csv")["labels"]
print(pd.Series(y).value_counts())
classes=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nclasses=len(classes)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=9,train_size=3500,test_size=500)
clf=LogisticRegression(solver='saga',multi_class='multinomial').fit(X_train_Scaled,y_train)

def get_prediction(image):
    im_pil=Image.open(image)
    image_bw=im_pil.convert('L')
    image_bw_resized=image_bw.resize((22,30),Image.ANTIALIAS)
    pixel_filter=20
    min_pixel=np.percentile(image_bw_resized,pixel_filter)
