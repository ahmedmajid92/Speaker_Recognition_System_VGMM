import os
import cPickle
import numpy as np
from sklearn import preprocessing
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time

source   = "development_set\\"   

modelpath = "speaker_models\\"

test_file = "development_set_test.txt"        

file_paths = open(test_file,'r')


gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

models    = [cPickle.load(open(fname,'r')) for fname in gmm_files]
speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
              in gmm_files]

cc = 0
for path in file_paths:   
    
    path = path.strip()   
    sr,audio = read(source + path)
    vector   = extract_features(audio,sr)

    vector = preprocessing.normalize(vector, norm='l2')
    
    log_likelihood = np.zeros(len(models)) 
    
    for i in range(len(models)):
        gmm    = models[i]        
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
    
    winner = np.argmax(log_likelihood)
    pp = path.split('\\')[0]
    print pp, " detected as ", speakers[winner]
    if pp == speakers[winner]:
        cc = cc + 1
    time.sleep(1.0)
print "The Recognition Rate is: ", float(cc)/float(len(models)*5)*100, "%"
