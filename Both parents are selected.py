import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import product
#----------------------------------------------------------------------------------------------------------------------------
def zero(n, d):
    return n / d if d else 0

def finddad(gen0,n):

	count_pq = gen0.count('pq')
	count_qp = gen0.count('qp')
	count_pr = gen0.count('pr')
	count_rp = gen0.count('rp')
	count_ps = gen0.count('ps')
	count_sp = gen0.count('sp')
	count_qs = gen0.count('qs')
	count_rq = gen0.count('rq')
	count_qr = gen0.count('qr')
	count_sq = gen0.count('sq')
	count_sr = gen0.count('sr')
	count_rs = gen0.count('rs')
	count_pp = gen0.count('pp')
	count_qq = gen0.count('qq')
	count_rr = gen0.count('rr')
	count_ss = gen0.count('ss')
	gen0.sort()
	probdad_pq = 0.04
	probdad_qp = 0.04
	probdad_pr = 0.04
	probdad_rp = 0.04
	probdad_ps = 0.04
	probdad_sp = 0.04
	probdad_qr = 0.04
	probdad_rq = 0.04
	probdad_qs = 0.04
	probdad_sq = 0.04
	probdad_rs = 0.04
	probdad_sr = 0.04
	probdad_pp = 0.4
	probdad_qq = 0.04
	probdad_rr = 0.04
	probdad_ss = 0.04
	probdad = [zero(probdad_pp,count_pp)]*count_pp + [zero(probdad_pq,count_pq)]*count_pq + [zero(probdad_pr,count_pr)]*count_pr + [zero(probdad_ps,count_ps)]*count_ps +[zero(probdad_qp,count_qp)]*count_qp + [zero(probdad_qq,count_qq)]*count_qq + [zero(probdad_qr,count_qr)]*count_qr + [zero(probdad_qs,count_qs)]*count_qs + [zero(probdad_rp,count_rp)]*count_rp +  [zero(probdad_rq,count_rq)]*count_rq + [zero(probdad_rr,count_rr)]*count_rr + [zero(probdad_rs,count_rs)]*count_rs + [zero(probdad_sp,count_sp)]*count_sp + [zero(probdad_sq,count_sq)]*count_sq + [zero(probdad_sr,count_sr)]*count_sr + [zero(probdad_ss,count_ss)]*count_ss
	#pdad = [ '%.3f' % elem for elem in probdad ]
	probdad = np.array(probdad)
	probdad /= probdad.sum()
	p = list(np.random.choice(gen0,n,p=probdad,replace=False))
	
	return p

def findmum(gen0,n):

	count_pq = gen0.count('pq')
	count_qp = gen0.count('qp')
	count_pr = gen0.count('pr')
	count_rp = gen0.count('rp')
	count_ps = gen0.count('ps')
	count_sp = gen0.count('sp')
	count_qs = gen0.count('qs')
	count_rq = gen0.count('rq')
	count_qr = gen0.count('qr')
	count_sq = gen0.count('sq')
	count_sr = gen0.count('sr')
	count_rs = gen0.count('rs')
	count_pp = gen0.count('pp')
	count_qq = gen0.count('qq')
	count_rr = gen0.count('rr')
	count_ss = gen0.count('ss')
	gen0.sort()
	probmum_pq = 0.04
	probmum_qp = 0.04
	probmum_pr = 0.04
	probmum_rp = 0.04
	probmum_ps = 0.2
	probmum_sp = 0.2
	probmum_qr = 0.04
	probmum_rq = 0.04
	probmum_qs = 0.04
	probmum_sq = 0.04
	probmum_rs = 0.04
	probmum_sr = 0.04
	probmum_pp = 0.04
	probmum_qq = 0.04
	probmum_rr = 0.04
	probmum_ss = 0.04
	probmum = [zero(probmum_pp,count_pp)]*count_pp + [zero(probmum_pq,count_pq)]*count_pq + [zero(probmum_pr,count_pr)]*count_pr + [zero(probmum_ps,count_ps)]*count_ps +[zero(probmum_qp,count_qp)]*count_qp + [zero(probmum_qq,count_qq)]*count_qq + [zero(probmum_qr,count_qr)]*count_qr + [zero(probmum_qs,count_qs)]*count_qs + [zero(probmum_rp,count_rp)]*count_rp +  [zero(probmum_rq,count_rq)]*count_rq + [zero(probmum_rr,count_rr)]*count_rr + [zero(probmum_rs,count_rs)]*count_rs + [zero(probmum_sp,count_sp)]*count_sp + [zero(probmum_sq,count_sq)]*count_sq + [zero(probmum_sr,count_sr)]*count_sr + [zero(probmum_ss,count_ss)]*count_ss
	#pmum = [ '%.3f' % elem for elem in pmum ]
	probmum = np.array(probmum)
	probmum /= probmum.sum()
	p = list(np.random.choice(gen0,n,p=probmum,replace=False))
	
	return p
#----------------------------------------------------------------------------------------------------------------------------

gen0=[]
#A1B1=p, A2B1=q, A1B2=r, A2B2=s

# All possible genetics
l=['pq','pr','ps','qr','qs','rs','pp','rr','ss','qq'] 
#l={'pq','pr','ps','qr','qs','rs'}

#To create the parent generation randomly
#p = int(input('print parent generation size: '))
for k in range(0,200):
	a = random.sample(l, 1) 
	gen0.extend([''.join(c) for c in a]) 				# join selections as ['','','','']
#print ('gen0 = ',gen0)

#Initialization of crucial lists
nextgen = []
all_children = []
fpq=[]
fpr=[]
fps=[]
fqr=[]
fsq=[]
frs=[]
fss=[]
frr=[]
fqq=[]
fpp=[]
fa1=[]
fa2=[]
fb1=[]
fb2=[]

for j in range(1,500): 	# overall loop/ The number of generations.
	#print ('Generation number: ',j)
	p1 = finddad(gen0,100)
	p2 = findmum(gen0,100)

	for i in range(50):
	#This loop randomly chooses pairs from the existing generation and 
	#creates a list of possible progenies. It then creates a certain 
	#number of children. 
        	# randomly choosing partners from gen0
		dad = p1[i]
		mom = p2[i]
		
		# crossing to get first filial generation #
		children = product(dad, mom)# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy #
		
		all_children.extend([''.join(c) for c in children])	# joining the array as ['','','',''] #

		# append nextgen for the next generation to cross and 
		# choose a certain number of children from every cross 
		nextgen.extend(np.random.choice(all_children,10))
		all_children=[]
		p1.pop(p1.index(dad))
		p2.pop(p2.index(mom))
		if len(p1) == 0:
			break
		if len(p2) == 0:
			break
	# replace parent generation with filial generation
	if len(nextgen) > 1000:						# limited the sample size of the generation by 1000
		nextgen = list(np.random.choice(gen0,1000))

	gen0 = nextgen
	leng=len(gen0)

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
#.................To print the final frequency plots.................

plt.plot(fpq, label='pq', linewidth=0.7)
plt.plot(fpr, label='pr', linewidth=0.7)
plt.plot(fps, label='ps', linewidth=0.7)
plt.plot(frs, label='rs', linewidth=0.7)
plt.plot(fqr, label='qr', linewidth=0.7)
plt.plot(fsq, label='sq', linewidth=0.7)
plt.plot(fss, label='ss', linewidth=0.7)
plt.plot(fqq, label='qq', linewidth=0.7)
plt.plot(frr, label='rr', linewidth=0.7)
plt.plot(fpp, label='pp', linewidth=0.7)

'''
plt.plot(fa1, label='A1', linewidth=0.7)
plt.plot(fa2, label='A2', linewidth=0.7)
plt.plot(fb1, label='B1', linewidth=0.7)
plt.plot(fb2, label='B2', linewidth=0.7)
'''
plt.xlabel('Generations', fontsize=14)
plt.ylabel('Probability of each genotype', fontsize=14)
#plt.ylabel('Probability of each genotype')
plt.title("PP & PS are the best Male and Female")
plt.legend()
plt.savefig('bgen22.png',dpi=100)
plt.show()