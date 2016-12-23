"""
       	Prints an average of which dataset took how many to terminate the program
       	Hence is a measure of which dataset tok how long to run
       	Output is redirected to file named rounds.txt
"""

import numpy as np

f_list=open('listDatasets','rb')

for line in f_list:
       	length=0
       	folder=line.strip('\n')
       	for i in range(1,11):
       		filename='./'+folder+'gibbs_output/gibbs_'+str(i).zfill(2)+'_IC.npy'
       		data=np.load(filename)
       		length+=len(data)
       	length=length/10
       	print folder, length
f_list.close()
