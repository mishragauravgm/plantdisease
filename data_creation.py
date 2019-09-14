os.chdir('/content/drive/My Drive/')
!pwd
#os.mkdir('DataScience')
os.chdir('DataScience')
os.mkdir('PlantDisease')

!ls

import random
import shutil
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop, Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras import metrics
import os
SEED=123
os.listdir()
from google.colab import drive
drive.mount('/content/drive')

from google.colab import files
files.upload()

!ls -lha kaggle.json

!pip install -q kaggle

# The Kaggle API client expects this file to be in ~/.kaggle,
# so move it there.
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

# This permissions change avoids a warning on Kaggle tool startup.
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets list -s plants

!kaggle datasets download -d emmarex/plantdisease

!unzip plantdisease.zip

!pwd

#Checking length of each disease type
os.chdir('/content/drive/My Drive/DataScience/PlantVillage/')
print(len(os.listdir('Pepper__bell___Bacterial_spot')))
print(len(os.listdir('Pepper__bell___healthy')))
print(len(os.listdir('Potato___Early_blight')))
print(len(os.listdir('Potato___Late_blight')))
print(len(os.listdir('Potato___healthy')))
print(len(os.listdir('Tomato_Bacterial_spot')))
print(len(os.listdir('Tomato_Early_blight')))
print(len(os.listdir('Tomato_Late_blight')))
print(len(os.listdir('Tomato_Leaf_Mold')))
print(len(os.listdir('Tomato_Septoria_leaf_spot')))
print(len(os.listdir('Tomato_Spider_mites_Two_spotted_spider_mite')))
print(len(os.listdir('Tomato__Target_Spot')))
print(len(os.listdir('Tomato__Tomato_YellowLeaf__Curl_Virus')))
print(len(os.listdir('Tomato__Tomato_mosaic_virus')))
print(len(os.listdir('Tomato_healthy')))

base_dir='/content/drive/My Drive/DataScience/PlantVillage/'
os.chdir(base_dir)
os.mkdir('dataset')
os.mkdir('training')
os.mkdir('validation')
os.chdir('dataset')

os.chdir(base_dir)
os.listdir()
os.chdir('dataset')
os.system('scp -r ../Tom* ../Pepper* ../Potato* .')

classes = os.listdir()
for i in classes:
    tr_dir = os.path.join('/content/drive/My Drive/DataScience/PlantVillage/training',i)
    val_dir = os.path.join('/content/drive/My Drive/DataScience/PlantVillage/validation',i)

    os.mkdir(tr_dir)
    os.mkdir(val_dir)

# Checking

print(os.listdir('/content/drive/My Drive/DataScience/PlantVillage/training'))


print(os.listdir('/content/drive/My Drive/DataScience/PlantVillage/validation'))

print(classes)
import random
print(os.getcwd())
sumval=0
sumtrain=0
for item in classes:

    n_val = round(len(os.listdir(item))*.04) #counting number of validation entries
    n_train = round(len(os.listdir(item))*.2) #conuting number of training entries
    fnames = os.listdir(item)
    sumval = sumval+n_val
    sumtrain = sumtrain+n_train

    #assert(n_val+n_train == len(fnames))

    random.seed(SEED+5)
    random.shuffle(fnames)
    val_fnames = fnames[0:n_val]
    tr_fnames = fnames[n_val:n_val+n_train] #for a smaller dataset
    #tr_fnames = fnames[n_val:len(fnames)]

    #assert(len(val_fnames)+len(tr_fnames)==len(fnames))

    for i in val_fnames:
        src ='/content/drive/My Drive/DataScience/PlantVillage/dataset/{}/{}'.format(item,i)
        dest = '/content/drive/My Drive/DataScience/PlantVillage/validation/{}/'.format(item)
        shutil.copy(src,dest)

    for j in tr_fnames:
        src ='/content/drive/My Drive/DataScience/PlantVillage/dataset/{}/{}'.format(item,j)
        dest = '/content/drive/My Drive/DataScience/PlantVillage/training/{}/'.format(item)
        shutil.copy(src,dest)
print(sumval,sumtrain)

for i in classes:
    path=os.path.join('/content/drive/My Drive/DataScience/PlantVillage/training/',i)
    print('Training samples in {} is {}'.format(i,len(os.listdir(path))))

    path=os.path.join('/content/drive/My Drive/DataScience/PlantVillage/validation/',i)
    print('Validation samples in {} is {}\n'.format(i,len(os.listdir(path))))

##Removing class files from the base directory
os.system('rm -r /content/drive/My Drive/DataScience/PlantVillage/Tom* /content/drive/My Drive/DataScience/PlantVillage/Pepper* /content/PlantVillage/Potato* .')

validation_dir = '/content/drive/My Drive/DataScience/PlantVillage/validation/'
training_dir = '/content/drive/My Drive/DataScience/PlantVillage/training/'
