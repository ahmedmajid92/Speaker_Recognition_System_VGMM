import cPickle
import numpy as np
from sklearn import preprocessing
from scipy.io.wavfile import read
from sklearn import mixture
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")

source   = "development_set\\"   

dest = "speaker_models\\"

train_file = "development_set_enroll.txt"        

file_paths = open(train_file,'r')

features = np.asarray(())

features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print path
    
    sr,audio = read(source + path)
    
    vector   = extract_features(audio,sr)

    print vector

    print "after"

    print preprocessing.scale(vector)
    break