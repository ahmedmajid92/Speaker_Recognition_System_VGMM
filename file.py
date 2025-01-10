import os

a = open("output.txt", "w")
for path, subdirs, files in os.walk(r'\Users\Silver-Hawk\Desktop\Speaker Recognition using GMM - TIMIT\hh\MZMB0\wav'):
   for filename in files:
     f = os.path.join('MZMB0\wav\\', filename)
     a.write(str(f) + os.linesep) 