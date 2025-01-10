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

count = 1

features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print path
    
    sr,audio = read(source + path)
    
    vector   = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    # when features of 5 files of speaker are concatenated, then do model training
    if count == 5:    
        features = preprocessing.normalize(features, norm='l2')
        #gmm = mixture.GaussianMixture(n_components = 18, max_iter = 160, covariance_type='tied',n_init = 3, warm_start=True)
        gmm = mixture.BayesianGaussianMixture(n_components = 5, max_iter = 100, covariance_type='tied',n_init = 2, weight_concentration_prior_type = 'dirichlet_process', warm_start=True)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        picklefile = path.split("\\")[0]+".gmm"
        cPickle.dump(gmm,open(dest + picklefile,'w'))
        print '+ modeling completed for speaker:',picklefile," with data point = ",features.shape    
        features = np.asarray(())
        count = 0
    count = count + 1
    