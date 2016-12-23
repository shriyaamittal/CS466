#folder='dataset'
#dataset_folder=folder

def read_motifFile(fileName):
	f_motif=open(fileName,'rb')
	first_line = f_motif.readline()
	k = int(first_line.split()[1])
	matrix = []
	for i in range(k):
		raw = f_motif.readline().split()
		raw = np.int_(raw)
		sum = np.sum(raw)
		raw = raw/sum
		matrix.append(raw)
	return matrix

def relativeS(P, Q):
	"""
	Parameters
	----------
	P : 
		Input matrix
	Q :
		Reference matrix
	output :
		The value of relative entropy	
	"""
	import numpy as np

	epsilon = 0.0001
	k = len(P)
	D = 0
	for position in range(k):
		for nuc in range(4):
			p = P[position][nuc]
			q = Q[position][nuc]
			if q == 0 :
				q = epsilon
			if p == 0 :
				p = epsilon				
			s = p * np.log(p/q)
			D = D + s
	return D

###
def main_cal_relativeS():
	import glob 
	import numpy as np
	import os
	try:
		os.mkdir('motifFinding-relativeS')
	except:
		print('Directory exists')
	
	for dataset_directory in glob.glob('motifFinding-master/dataset*'):
		motif_file = dataset_directory+'/motif.txt'
		motif = read_motifFile(motif_file)
		Q = motif
		path = 'motifFinding-relativeS/'+dataset_directory.split('/')[-1]
		os.mkdir(path)
		for i in range(1,11):
			if i == 10:
				predicted_motif_file = dataset_directory+'/gibbs_output/gibbs_10_predictedmotif.txt'
			else:
				predicted_motif_file = dataset_directory+'/gibbs_output/gibbs_0'+str(i)+'_predictedmotif.txt'
			predicted_motif = read_motifFile(predicted_motif_file)
			P = predicted_motif
			D = relativeS(P, Q)
			np.savetxt(path +'/gibbs_'+str(i), [D])


def plot1():
	import glob
	import matplotlib.pyplot as plt
	ML = '8'
	SL = '500'
	ICPCs = ['1', '1.5', '2']
	SC = '10'
	data = []
	for ICPC in ICPCs:
		row = []
		for i in range(1,11):
			for j in range(1, 11):
				fileName = 'motifFinding-relativeS/dataset_'+ICPC+'_'+ML+'_'+SL+'_'+SC+'_'+str(i)+'/gibbs_'+str(j)+'.txt'
				D = np.loadtxt(fileName)
				row.append(D)			
		data.append(row)	
	fig, axes = plt.subplots(
	axes.boxplot(data)
	ax.yaxis.grid(True)
	axes.set_xticks(ICPCs)
	plt.show()

def plot2():		
	import glob
	import matplotlib.pyplot as plt
	import numpy as np
	ML = '8'
	SL = '500'
	ICPC = '2'
	SCs = ['5','10','20']
	data = []
	for SC in SCs:
		row = []
		for i in range(1,11):
			for j in range(1, 11):
				fileName = 'motifFinding-relativeS/dataset_'+ICPC+'_'+ML+'_'+SL+'_'+SC+'_'+str(i)+'/gibbs_'+str(j)+'.txt'
				D = np.loadtxt(fileName)
				row.append(D)			
		data.append(row)	
	fig, axes = plt.subplots()
	axes.boxplot(data)
	axes.set_ylim([0,10])
	axes.yaxis.grid(True)
	#axes.set_xticks(ICPCs)
	plt.show()

def plot3():
	import glob
	import matplotlib.pyplot as plt
	import numpy as np
	MLs = ['6', '7', '8']
	SL = '500'
	ICPC = '2'
	SC = '10'
	data = []
	for ML in MLs:
		row = []
		for i in range(1,11):
			for j in range(1, 11):
				fileName = 'motifFinding-relativeS/dataset_'+ICPC+'_'+ML+'_'+SL+'_'+SC+'_'+str(i)+'/gibbs_'+str(j)+'.txt'
				D = np.loadtxt(fileName)
				row.append(D)			
		data.append(row)	
	fig, axes = plt.subplots()
	axes.boxplot(data)
	axes.set_ylim([0,10])
	axes.yaxis.grid(True)
	#axes.set_xticks(ICPCs)
	plt.show()
