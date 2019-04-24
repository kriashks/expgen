import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import product

gen0=[]
#A1B1=p, A2B1=q, A1B2=r, A2B2=s

# All possible genetics
l=['pq','pr','ps','qr','qs','rs','pp','rr','ss','qq'] 

#To create the parent generation randomly
for k in range(0,6):
	a = random.sample(l, 2) 
	gen0.extend([''.join(c) for c in a]) # join selections as ['','','','']
#print('gen0 initial=',gen0)

#Initialization of crucial lists
nextgen = []
all_children = []
fpq=[]; fpr=[]; fps=[]; fqr=[]; fsq=[]; frs=[]; fss=[]; frr=[]; fqq=[]; fpp=[]
fa1=[]
fa2=[]
fb1=[]
fb2=[]

for j in range(0,40): # overall loop/ The number of generations.
	for i in range(0,20):
	#This loop randomly chooses pairs from the existing generation and 
	#creates a list of possible progenies. It then creates a certain 
	#number of children. 
		
        # randomly choosing partners from gen0
		p1,p2 = np.random.choice(gen0,2,replace=False)
		#print (p1,p2)
		
		# crossing to get first filial generation #
      	# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy #
		children = product(p1, p2)
		# joining the array as ['','','',''] #
		all_children.extend([''.join(c) for c in children])
		
		# append nextgen for the next generation to cross and 
		# choose a certain number of children from every cross 
		nextgen.extend(np.random.choice(all_children,10))
		#print 'all_children=', all_children
		#print 'next generation=', nextgen
		all_children=[]
		gen0.pop(gen0.index(p1))
		gen0.pop(gen0.index(p2))
		#print 'gen0 after pop=', gen0
		if len(gen0) == 0:
			break
	# replace parent generation with filial generation
	gen0 = nextgen
	#print(gen0)
	
	leng=len(gen0)
	#test= p + q + r + s 


	#print(A1)
	#print(A1,A2,B1,B2,leng)
	fpq.append(((gen0.count('pq')+gen0.count('qp'))/leng)) 
	fpr.append(((gen0.count('pr')+gen0.count('rp'))/leng))
	fps.append(((gen0.count('ps')+gen0.count('ps'))/leng))
	frs.append(((gen0.count('rs')+gen0.count('sr'))/leng))
	fqr.append(((gen0.count('qr')+gen0.count('rq'))/leng))
	fsq.append(((gen0.count('sq')+gen0.count('qs'))/leng))
	fss.append(((gen0.count('ss')+gen0.count('ss'))/leng))
	fqq.append(((gen0.count('qq')+gen0.count('qq'))/leng))
	frr.append(((gen0.count('rr')+gen0.count('rr'))/leng))
	fpp.append(((gen0.count('pp')+gen0.count('pp'))/leng))

	A1 = gen0.count('pq') + gen0.count('qp') + gen0.count('rp') + gen0.count('pr') + gen0.count('sp') + gen0.count('sr') + gen0.count('ps') + gen0.count('rs') + gen0.count('qr') + gen0.count('rq') + gen0.count('pp') + gen0.count('rr')
	A2 = gen0.count('pq') + gen0.count('qp')  + gen0.count('qr') + gen0.count('rq')  + gen0.count('qs') + gen0.count('sq')  + gen0.count('rs') + gen0.count('sr')  + gen0.count('ps') + gen0.count('sp') + gen0.count('qq') + gen0.count('ss')     
	B1 = gen0.count('pq') + gen0.count('qp') + gen0.count('pr') + gen0.count('rp') + gen0.count('ps') + gen0.count('sp') + gen0.count('qr') + gen0.count('rq') + gen0.count('qs') + gen0.count('sq') + gen0.count('pp') + gen0.count('qq')
	B2 = gen0.count('pr') + gen0.count('rp') + gen0.count('qr') + gen0.count('rq') + gen0.count('rs') + gen0.count('sr') + gen0.count('ps') + gen0.count('sp') + gen0.count('qs') + gen0.count('sq') + gen0.count('rr') + gen0.count('ss')  
	fa1.append((A1/leng)) 
	fa2.append((A2/leng))
	fb1.append((B1/leng))
	fb2.append((B2/leng))	
	#print(len(nextgen))
#print(fa1)
# frequency of a particular gene (AA here)
#dominants = filter(lambda c: 'ps' in c, nextgen)
#print('dominants =', float(len(list(dominants))) / len(nextgen))

#.................To print the final frequency plots.................


plt.plot(fa1, label='A1')
plt.plot(fa2, label='A2')
plt.plot(fb1, label='B1')
plt.plot(fb2, label='B2')
plt.xlabel('Generations', fontsize=12)
plt.ylabel('Probability of each allele', fontsize=12)
plt.legend()
plt.savefig('Ran11.png',dpi=100)
plt.show()
