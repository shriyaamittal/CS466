# specificity (fraction of predictions matching true sites) 
# sensitivity (fraction of true sites that were recovered)

def read_siteFile(fileName):
	import numpy as np	
	f_site=open(fileName,'rb')
	lines = f_site.readlines()
	k = np.int_(lines)
	return k
  

# specificity (fraction of predictions matching true sites) 
def specificity(site, predicted_site):
	count = 0
	for i in site:
		flag = False
		for j in predicted_site:
			if i == j:
				flag = True
		if flag:
			count = count+1
	return count/len(site)

def main_specificity():
	import glob 
	import numpy as np
	import os
	
	try:
		os.mkdir('motifFinding-specificity')
	except:
		print('Directory exists')
		
	for dataset_directory in glob.glob('motifFinding-master/dataset*'):
		site_file = dataset_directory+'/sites.txt'
		site = read_siteFile(site_file)
		path = 'motifFinding-specificity/'+dataset_directory.split('/')[-1]	
		try:
			os.mkdir(path)
		except:
			print('Directory exists')
			
		for i in range(1,11):
			if i == 10:
				predicted_site_file = dataset_directory+'/gibbs_output/gibbs_10_predictedsites.txt'
			else:
				predicted_site_file = dataset_directory+'/gibbs_output/gibbs_0'+str(i)+'_predictedsites.txt'
			predicted_site = read_siteFile(predicted_site_file)
			D = specificity(site, predicted_site)

			np.savetxt(path +'/gibbs_'+str(i), [D])


			
def plot1():
	import glob
	import matplotlib.pyplot as plt
	import numpy as np
	ML = '8'
	SL = '500'
	ICPCs = ['1', '1.5', '2']
	SC = '10'
	data = []
	for ICPC in ICPCs:
		row = []
		for i in range(1,11):
			for j in range(1, 11):
				fileName = 'motifFinding-specificity/dataset_'+ICPC+'_'+ML+'_'+SL+'_'+SC+'_'+str(i)+'/gibbs_'+str(j)
				D = np.loadtxt(fileName)
				row.append(D)			
		data.append(row)	
	fig, axes = plt.subplots()
	axes.boxplot(data)
	axes.yaxis.grid(True)
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
				fileName = 'motifFinding-specificity/dataset_'+ICPC+'_'+ML+'_'+SL+'_'+SC+'_'+str(i)+'/gibbs_'+str(j)
				D = np.loadtxt(fileName)
				row.append(D)			
		data.append(row)	
	fig, axes = plt.subplots()
	axes.boxplot(data)
	axes.yaxis.grid(True)
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
				fileName = 'motifFinding-specificity/dataset_'+ICPC+'_'+ML+'_'+SL+'_'+SC+'_'+str(i)+'/gibbs_'+str(j)
				D = np.loadtxt(fileName)
				row.append(D)			
		data.append(row)	
	fig, axes = plt.subplots()
	axes.boxplot(data, meanline=True, showmeans=True)
	axes.yaxis.grid(True)
	axes.set_ylim([0,1])
	plt.show()			
			
			
"""
# sensitivity (fraction of true sites that were recovered)
def sensitivity():
	import glob 
	import numpy as np
	import os
	
	count_matchings = 0 
	count_all = 0 
	for dataset_directory in glob.glob('motifFinding-master/dataset*'):
		motif_file = dataset_directory+'/motif.txt'
		motif = read_motifFile(motif_file)
		Q = motif
		path = 'motifFinding-matchings/'+dataset_directory.split('/')[-1]
		count_all = count_all + 1
		Flag = False
		for i in range(1,11):
			if i == 10:
				predicted_motif_file = dataset_directory+'/gibbs_output/gibbs_10_predictedmotif.txt'
			else:
				predicted_motif_file = dataset_directory+'/gibbs_output/gibbs_0'+str(i)+'_predictedmotif.txt'
			predicted_motif = read_motifFile(predicted_motif_file)
			P = predicted_motif
			D = relativeS(P, Q)
			
			if D == 0 :
				print('Equal!')
				Flag = True
		if Flag:		
			count_matchings = count_matchings + 1 
			
	sensitivity = count_matchings/count_all		
	np.savetxt('/gibbs_sensitivity', [sensitivity, count_matchings, count_all])
"""	
	

