# −*− coding : utf−8 −*− #
import math
import numpy
import random
import csv

#### VALORI MODIFICABILI DALL'UTENTE ### #Sia G = (V,E) grafo 
nodes = 400 # |V| = nodes ( vertici ) 
ite = 5 # numero di iterazioni 
percentuale = 0.5 # percentuale degli archi modificati
#################################################
 
edges = random.sample(range(2*nodes,int(((nodes*nodes)-nodes)*0.5)),1)[0]# |E| = edges ( archi ) 
valore = int(edges*percentuale)# calcolo percentuale discretizzata 
S = 2 # inizializzazione degli Spreaders 
R = 0 # inizializzazione Refrattari 
K = 1 # Spreaders cumulativi 
C = 0 # c i c l i t o t a l i azioni compiute dagli Spreaders 
SpreaderRate = K / nodes # i l rosso nella grafica è associato agli Spreaders 
rosso = 2
verde = 1 # i l verde nella grafica è associato agli Ignorants 
bianco =0 # i l bianco nella grafica è associato agli S t i f l e r s 
RegistroColoriCoord = None
def SmeetIC() : # (I ,S,R) |− (I−1, S+1,R) 
	global I 
	global S 
	global C 
	global K 
	I=I-1 
	S=S+1
	C=C+1 # Segno in C che è avvenuta una azione di SPREAD 
	K=K+1 # Solo in SmeetIC() g l i Spreaders aumentano , quindi lo segno nel contatore K 
	print "S vs I susceptible " ,[ I ,S ,R]

def SmeetINC() : # (I ,S,R) |− (I−1, S,R+1)

	global I 
	global R 
	global C 
	global S 
	S=S 
	I=I-1
	R=R+1
	C=C+11 # Segno in C che è avvenuta una azione di SPREAD 
	print "S vs I immune" ,[ I ,S ,R]


def SmeetS() : # (I ,S,R) |− (I , S−2,R+2) , transizione Spreader incontra Spreader 
	global I 
	global S 
	global C 
	global K 
	global R 
	I=I
	S=S-2
	R=R+2 
	C=C+1
	print "S vs S : " ,[ I ,S ,R]

def SmeetR() : # (I ,S,R) |− (I , S−1,R+1) , transizione Spreader incontra S t i f l e r 
	global I 
	global S 
	global C 
	global K
	global R 
	I=I 
	S=S-1
	R=R+1 
	C=C+1
	print "S vs R : " ,[ I ,S ,R]

def RegistroColoriCoordVerdi () : # coloro tutto di verde , quindi resetto lo scenario per una nuova iterazione 
	global I 
	global R 
	global S 
	global C 
	global K 
	global nodes 
	global RegistroColoriCoord 

	RegistroColoriCoord = numpy.zeros(shape=(nodes,3)) 
	for x in range (0,nodes ) : 

		(RegistroColoriCoord[x,0]) = verde 

	S = 0 
	I = nodes 
	R = 0 
	C = 0 
	K = 1
	
def CreaScenario() : # piazza uno Spreader a random, g l i a l t r i restano verdi 
	global I 
	global S 
	global R 
	global RegistroColoriCoord 
	y = random.sample(range(0,nodes),1)[0] 
	RegistroColoriCoord[y,0]= rosso # Scelgo un rosso a caso .
	S=1
	
	
def CreaGrafoCompleto() : # crea una matrice di adiacenza per i l grafo completo . 
	global M 
	global nodes 
	M = numpy.zeros(shape=(nodes,nodes)) 
	for y1 in range (0,nodes): 
		for y2 in range (0,nodes) : 
			M[y1,y2] = M[y2,y1]=1 
			M[y1,y1]=0
			
def CreaGrafoRandom() : # crea una matrice di adiacenza randomizzata 
	global M
	global nodes 
	global edges 
	x=0 
	edges = random.sample(range(2*nodes,int((nodes*nodes-nodes)*0.5)),1)[0] # |E| = edges ( archi ) 
	M = numpy.zeros(shape=(nodes,nodes)) 
	while x<edges :
		i = random.sample(range(0,nodes),1)[0] # associo ad i un valre {0 ,... ,n−1} random 
		j = random.sample(range(0,nodes),1)[0] # associo ad j un valre {0 ,... ,n−1} random 
		if(M[i,j] == 1 ) : 
			x=x+1 
		elif( M[i,j]== 0 & i != j ) : 
			M[i,j] = M[j,i]=1 
		else : 
			M[i,i]=0 
			x=x-1 
		x=x+1
		
def ComputingRandomNoGUI() : # Algoritmo casuale 
	global RegistroColoriCoord 
	
	randspreadid = random.sample(numpy.where(RegistroColoriCoord[:,0]== rosso)[0],1)[0] 
	z = random.sample(numpy.where(M[randspreadid,:]==1)[0],1)[0] # Tra i contatti di randspreadid seleziono un nodo a caso connesso
	
	if RegistroColoriCoord[z,0]==verde : # Se i l nodo z−esimo selezionato è verde 
		if random.uniform(0,1)>0.50 : # Controllo se è tendenzialmente Rosso 
			RegistroColoriCoord[z,0]= rosso # In questo caso coloro i l nodo z−esimo di Rosso 
			SmeetIC() 
		else : 
			RegistroColoriCoord[z,0]= bianco 
			SmeetINC()
	elif RegistroColoriCoord[z,0]==bianco : 
		RegistroColoriCoord[randspreadid,0]= bianco # Altrimenti se i l nodo z−esimo non è contagiabile z diventa di colore bianco 
		SmeetR()
	elif RegistroColoriCoord[z,0]== rosso : # Se i l nodo z−esimo è ROSSO 
		RegistroColoriCoord[randspreadid,0]= bianco # coloro randspreadid di BIANCO 
		RegistroColoriCoord[z,0]= bianco #Coloro i l nodo z−esimo di BIANCO 
		SmeetS()




def SalvaFileStaticoNormale () :
	
	RegistroColoriCoordVerdi() 
	CreaGrafoRandom() 
	CreaScenario()

	with open('RandomStat4b.csv','w') as csvfile : 
		spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL) 
		spamwriter.writerow(['i','s','r','Azioni Totali','S−Cumulativi','|V|','|E|','Spreader−Rate'])
		for x in range (0,ite) : 
			with open('RandomFlip4b.csv','w') as csvfile : 
				spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)  
				spamwriter.writerow([I,S,R,C,K,nodes,edges,float(K)/nodes])
			print "Saving data base f i l e . . . " 
			RegistroColoriCoordVerdi() 
			CreaGrafoRandom() 
			CreaScenario() 
			
			while S>0: 
				ComputingRandomNoGUI() 


def SalvaFileGrafoCompletoStatico() : 
	
	RegistroColoriCoordVerdi() 
	CreaGrafoCompleto() 
	CreaScenario()

	with open('CompletoStat4b.csv','w') as csvfile : 
		spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL) 
		spamwriter.writerow(['i','s','r','Azioni Totali','S−Cumulativi','|V|','|E|','Spreader−Rate'])
		for x in range (0,ite) : 
			print "Saving data base f i l e . . . " 
			with open('RandomFlip4b.csv','w') as csvfile : 
				spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)  
				spamwriter.writerow([I,S,R,C,K,nodes,edges,float(K)/nodes])
			RegistroColoriCoordVerdi() 
			CreaGrafoCompleto()
			CreaScenario() 
			
			while S>0: 
				ComputingRandomNoGUI() 



def CambiaMatrice () : # Modifica la matrice di adiacenza 
	x=0 
	global M 
	while x<valore :
		i=random.sample(range(0,nodes),1)[0] 
		j=random.sample(range(0,nodes),1)[0]
		if( i != j ) : 
			if ( M[i,j]== 1) : 
				M[i,j]=M[j,i]  = 0 # se c 'è collegamento lo rompe 
			elif(M[i,j]==0): 
				M[i,j]=M[j,i]=1 # se non c 'è collegamento lo crea 
		else : 
			x=x-1 # se i=j i l contatore torna indietro di un passo 
		x=x+1
		
		
def SalvaFileVariabileNormale() : 
	RegistroColoriCoordVerdi() 
	CreaGrafoRandom() 
	CreaScenario()
	
	with open('RandomFlip4b.csv','w') as csvfile : 
		spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL) 
		spamwriter.writerow(['I','s','r','Azioni Totali','S−Cumulativi','|V|','|E|','Spreader−Rate'])
		for x in range (0,ite) : 
			print "Saving data base f i l e . . . " 
			with open('RandomFlip4b.csv','w') as csvfile : 
				spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)  
				spamwriter.writerow([I,S,R,C,K,nodes,edges,float(K)/nodes])
			RegistroColoriCoordVerdi() 
			CreaGrafoRandom() 
			CreaScenario() 
			
			while S>0: 
				if random.uniform (0,1) > 0.99 : 
					CambiaMatrice() 
				ComputingRandomNoGUI() 



def SalvaFileGrafoCompletoVariabile() : 
	RegistroColoriCoordVerdi() 
	CreaGrafoCompleto() 
	CreaScenario()
	
	with open('CompletoFlip4b.csv','w') as csvfile : 
		spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL) 
		spamwriter.writerow(['i','s','r','Azioni Totali','S−Cumulativi','|V|','|E|','Spreader−Rate'])
		for x in range (0,ite) : 
			print "Saving data base f i l e . . . " 
			with open('CompletoFlip4b.csv','w') as csvfile : 
				spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)  
				spamwriter.writerow([I,S,R,C,K,nodes,edges,float(K)/nodes])
			RegistroColoriCoordVerdi() 
			CreaGrafoCompleto()
			CreaScenario() 
			
			while S>0: 
				if random.uniform (0,1) > 0.99 : 
					CambiaMatrice() 
				ComputingRandomNoGUI() 
			

print "START RANDOM STAT" 
SalvaFileStaticoNormale() 
print "START RANDOM FLIP"
SalvaFileVariabileNormale()
print "START COMPLETE STAT" 
SalvaFileGrafoCompletoStatico()
print "START COMPLETE FLIP" 
SalvaFileGrafoCompletoVariabile()
