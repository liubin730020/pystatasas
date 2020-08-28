# pystatasas
Run SAS and Stata Program in python

# First you should install stata for linux   and  (SAS for linux  or  SAS for windows within wine5.0)

# After install SAS and Stata

what you need to do is 

from pythonsasstata import *

run stata

stata("your stata code", xx=DataFrameFile, fig=True or False)
#If you want to draw figure in stata, you should select fig=True,  else  select fig=False)

run Sas

sasrun()

write your sas code in vim

and output and log will display in python.


