# Tesi in Python + Equazioni Differenziali
La tesi si basa sullo studio della diffusione dei rumors in un social network.
Con un numero finito di popolazione, suddividiamo gli individui in 
# I - incontaminati
# S - spreader ( diffusori del rumor)
# R - stifler ( coloro che si rifiutano di ridiffondere il rumor )

L'algoritmo discreto, simulato in python, funziona nel seguente modo :
Sappiamo che resta costante I+S+R = N (numero di nodi del grafo)
Scelgo un S a caso tra il registro e controllo i suoi contatti tramite una matrice di adiacenza,
se 

# S contatta un I allora ho due possibilita'   
#1.   I si converte in S con probabilita' p (scelta dall'utente) ottenendo nel passaggio di stato (I,S,R) |- (I-1,S+1,R)
#2.   I si converte in R con probabilita' 1-p e otteniamo che da (I,S,R) |-  (I-1,S,R+1)

#S Contatta un R  accade che S si converte in R con il seguente risultato (I,S,R) |- (I,S-1,R+1)
#S Contatta un S accade che S si converte in R con il seguente risultato (I,S,R)  |- (I,S-2,R+2)

Questo non e' un modello definitivo, e' stato trovato in letteratura tratto da letteratura.
Si potrebbero aggiungere le probabilita' e cambiare gli esiti per qunado S incontra un R o un S.

Mentre per la parte di equazioni differenziali, viene svolto uno studio sulle derivate prime
che ci mostrano la crescita/decrescita degli I,S,R al tempo t.

