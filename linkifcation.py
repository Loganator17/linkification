import glob
import subprocess
import os

folders=glob.glob('./*')
cwd=os.getcwd()
for folder in folders:
    files=glob.glob(folder+'/*')
    for f in files:
        f=os.path.basename(f)
        os.chdir(folder)
        subprocess.call('rm -rf ./'+f.split('_')[1]+'.'+f.split('.')[1],shell=True)
        subprocess.call('ln -s '+f+' ./'+f.split('_')[1]+'.'+f.split('.')[1],shell=True)
        os.chdir(cwd)
