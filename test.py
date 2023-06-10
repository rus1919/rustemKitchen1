import os
import shutil
import traceback
import zipfile, os

#p = r'C:\Users\RMS\PycharmProjects'
p = r'C:\Users\RMS\Desktop\Архив'
d = os.listdir(path=p)
for i in d:
    #print(i)
    try:
        #shutil.rmtree(targ)

        print(i)
    except:
        print(traceback.format_exc())
        pass