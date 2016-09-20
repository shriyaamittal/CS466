import sys

def zeros(shape):
       	retval = []
       	for x in range(shape[0]):
       		retval.append([])
       		for y in range(shape[1]):
       			retval[-1].append(0)
       	return retval

def func_score(a,b):
       	col=matrix[0].index(a)
       	for i in range(1,5):
       		try:
       			x=matrix[i].index(b)
       		except ValueError:
       			continue;
       		else:
       			row=i
       			break
       	return matrix[row][col]

def align(seq1,seq2):
       	m=len(seq1)
       	n=len(seq2)
       	## Score table
       	score=zeros((m+1,n+1))
       	for i in range(0,m+1):
       		score[i][0] = i*gap_penalty
       	for i in range(0,n+1):
       		score[0][i] = i*gap_penalty
       	for i in range(1,m+1):
       		for j in range(1,n+1):
       			match_diagonal=score[i-1][j-1] + int(func_score(seq1[i-1],seq2[j-1]))
       			delete_vertical=score[i-1][j] + gap_penalty
       			insert_horizontal=score[i][j-1] + gap_penalty
       			score[i][j]=max(match_diagonal,delete_vertical,insert_horizontal)
#      	print score
       	print "The optimal alignment between given sequences has score "+str(score[m][n])+'.'
       	## Traceback
       	align1,align2 ='',''
       	i=m
       	j=n
       	while (i>0 and j>0):
       		score_current=score[i][j]
       		score_diagonal=score[i-1][j-1]
       		score_vertical=score[i-1][j]
       		score_horizontal=score[i][j-1]
       		if (score_current == score_diagonal + int(func_score(seq1[i-1],seq2[j-1]))):
       			align1= align1+seq1[i-1]
       			align2= align2+seq2[j-1]
       			i=i-1
       			j=j-1
       		elif (score_current == score_horizontal + gap_penalty):
       			align1= align1+'-'
       			align2= align2+seq2[j-1]
       			j=j-1
       		elif (score_current == score_vertical + gap_penalty):
       			align1= align1+seq1[i-1]
       			align2= align2+'-'
       			i=i-1
       	print align1[::-1]
       	print align2[::-1]
       	while (i>0):
       		align1=align1+seq1[i-1]
       		align2= align2+'-'
       		i=i-1
       	while (j>0):
       		align1= align1+'-'
       		align2=align2+seq1[j-1]
       		j=j-1





if __name__ == "__main__":
       	## Command line inputs
       	f_seq1=open(sys.argv[1],'rb')
       	f_seq2=open(sys.argv[2],'rb')
       	f_sub=open(sys.argv[3],'rb')
       	gap_penalty=int(sys.argv[4])
       	## Read substitution matrix
       	matrix=zeros((5,5))
       	i=0
       	for line in f_sub:
       		matrix[i]=line.strip().split()
       		i=i+1
       	matrix[0].insert(0,'-')
       	## Read Sequence 1
       	seq1=[]
       	flag=0
       	for line in f_seq1:
       		if (flag!=0):
       			i=0
       			while (i<len(line) and line[i]!='\n'):
       				seq1.append(line[i])
       				i=i+1
       		flag=1
       	f_seq1.close()
       	## Read Sequence 2
       	seq2=[]
       	flag=0
       	for line in f_seq2:
       		if (flag!=0):
       			i=0
       			while (i<len(line) and line[i]!='\n'):
       				seq2.append(line[i])
       				i=i+1
       		flag=1
       	f_seq2.close()
       	align(seq1,seq2)
