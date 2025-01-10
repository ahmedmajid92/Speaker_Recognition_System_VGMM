import os
import glob
import time
import shutil

rootdir = 'C:\Users\Silver-Hawk\Desktop\Speaker Recognition using GMM - TIMIT\hh'


f1 = open("C:\Users\Silver-Hawk\Desktop\Speaker Recognition using GMM - TIMIT\output1.txt", "a")
f2 = open("C:\Users\Silver-Hawk\Desktop\Speaker Recognition using GMM - TIMIT\output2.txt", "a")

a = [0,1,2,3,4]
c = 0
for subdir, dirs, files in os.walk(rootdir):    
    for file in files:
        if c == 10:
            c = 0
        p = os.path.split(subdir)
        s = os.path.join(os.path.basename(p[0]),p[1],file)
        if c in a:
            f1.write(s+'\n')
        else:
            f2.write(s+'\n')
        c = c + 1
        
f1.close()
f2.close()

 #for subdir, dirs, files in os.walk(rootdir):
  #  if not subdir.endswith('wav'):
   #     for file in files:
    #        s = os.path.join(subdir,file)
     #       d= os.path.join(subdir,'wav',file)
      #      shutil.move(s,d)

#for subdir, dirs, files in os.walk(rootdir):
  #  for file in files:
   #     f = os.path.join(subdir, file)
    #    os.remove(f)