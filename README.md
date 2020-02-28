

# Tesi in Python + Equazioni Differenziali
La tesi si basa sullo studio della diffusione dei rumors in un social network.
Con un numero finito di popolazione, suddividiamo gli individui in 
# I - incontaminati
# S - spreader ( diffusori del rumor)
# R - stifler ( coloro che si rifiutano di ridiffondere il rumor )

L'algoritmo discreto, simulato in python, funziona nel seguente modo :
Sappiamo che resta costante I+S+R = N (numero di nodi del grafo)
Seleziono un S a caso tra il registro e controllo i suoi contatti tramite una matrice di adiacenza,
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

Link alla tesi : https://www.mediafire.com/file/36npa0nbyxwbnu5/TESINA-Matematica-AlbertoRagagnin-2014-2015%2528FinalVersion%2529.pdf/file  (evrything in italian)

![image](graduatepythesis/graph.png)

# Python thesis + Differential equations
The thesis is based on the study of the spread of rumors in a social network.
With a finite number of population, we divide individuals into
# I - pristine
# S - spreader (noise diffusers)
# R - stifler (those who refuse to re-broadcast the rumor)

The discrete algorithm, simulated in python, works in the following way:
We know that I + S + R = N remains constant (number of nodes in the graph)
Selected a case between the register and the control of its contacts through an adjacency matrix,
SELF

# S contacts an I, we have two possibilities
# 1. I converts to S with probability p (user choice) obtaining in the change of state (I, S, R) | - (I-1, S + 1, R)
# 2. I converts to R with probability 1-p and we obtain that from (I, S, R) | - (I-1, S, R + 1)

#S Contact an R it happens that S converts to R with the following result (I, S, R) | - (I, S-1, R + 1)
#S Contact an S it happens that S converts to R with the following result (I, S, R) | - (I, S-2, R + 2)


While for the part of differential equations, a study is carried out on the first derivatives
that there is the growth / decrease of I, S, R at time t.
