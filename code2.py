import sys
import random
import time
import os

def mutate(S2):
       	for i in range(0,int(L/10)):
       		mutate=random.randrange(0,len(S2),1)
       		x=random.randrange(0,2,1)
       		if (x==0):
       			#delete
       			S2.pop(mutate)
       		elif (x==1):
       			#mutate
       			choices=list(alphabet)
       			choices.pop(alphabet.index(S2[mutate]))
       			x=random.randrange(0,3,1)
       			S2[mutate]=choices[x]
       	return ''.join(S2)

if __name__ == "__main__":
       	## Command line inputs
       	L=int(sys.argv[1])
       	alphabet=['A','G','T','C']
       	random.seed(time.time())
       	## Generate S1
       	S1=[]
       	for i in range(0,L):
       		x=random.randrange(0,4,1)
       		S1.append(alphabet[x])
       	## Generate S2 and S3
       	for i in range(2,4):
       		seq=list(S1)
       		new_seq=mutate(seq)
       		filename='S'+str(i)+'.txt'
       		f=open(filename,'wb')
       		f.write(">"+filename+"\n")
       		f.write(new_seq)
       		f.close()
       	cmd="python code1.py S2.txt S3.txt subs.txt -500"
       	os.system(cmd)
