import os
import threading
import pandas as pd
import numpy as np


def sasrun111(sen=1):
  def lj():
    cp=os.getcwd()
    cp="Z:"+cp.replace('/','\\')+"\\"
    return cp
  aa=sen
  os.system('vim axy123321.sas')
  f=open('axy123321.sas','r')
  ftxt=f.read()
  f.close()
  ftxt=ftxt.replace('axy123321',lj())
  f=open('axy123321.sas','w')
  f.write(ftxt)
  f.close()
  os.system('xvfb-run wineconsole --backend=curses ~/.wine/drive_c/Program\ Files/SAS\ Institute/SAS/V8/sas -nosplash -noicon -noterminal -nodms -nostatuswin -sysin ./axy123321.sas -nonotes -nosource -log ./axy123321.log -print ./axy123321.lst')
  try:
    os.system('cat axy123321.log')
  except:
    _=0
  try:
    os.system('cat axy123321.lst')
  except:
    _=0

def sasrun():
  #axy123321 refer to absolute path
  threadtrd(sasrun111,1)


def threadtrd(ffuc,argg):
   okt1=threading.Thread(target=ffuc,args=(argg,))
   okt1.setDaemon(True)
   okt1.start()

def stata(sen="",xx=pd.DataFrame(),fig=False):
    xx.to_stata("axy123321.dta")
    sen=sen.split(";")
    f=open('axy123321.do','w')
    f.writelines("clear all\n")
    f.writelines("use axy123321.dta,clear\n")
    for ii in sen:
        f.writelines(ii+"\n")
    if fig==True:
        f.writelines('graph export axy123321.eps, mag(500) replace\n')
    f.writelines('clear\n')
    f.writelines('exit,STATA clear\n')
    f.close()    
    cmd=["stata","do","axy123321.do"]
    sbp.call(cmd)
    if fig==True:
        os.system("convert axy123321.eps -resize 1600x1000 axy123321.pdf")
        os.system("fimgs -r 200 axy123321.pdf")
    os.system('rm axy123321.do')
    os.system('rm axy123321.eps')
    os.system('rm axy123321.dta')
