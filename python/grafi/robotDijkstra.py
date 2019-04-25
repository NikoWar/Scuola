import math

adj_dict={  0:[1,2],
            1:[0,5],
            2:[0,3],
            3:[2,4,5],
            4:[3,6,7],
            5:[1,3],
            6:[4,7],
            7:[4,6]}                  

def dijkstra(graph, startNode, finishNode):
    labelList = [math.inf] * len(graph) #inizializzazione delle label (moltiplico per il numero di nodi per le righe)
    labelList[startNode] = 0  #distanza dal nodo sorgente = 0
    unexploredNode = [0,1,2,3,4,5,6,7]   #nodi da esplorare

    cntPasso=0

    while len(unexploredNode)>0:
        infiniteList = [math.inf] * len(graph)
        
        for i in unexploredNode:
            infiniteList[i]=labelList[i]    #valore della labelList[i] 
        
        minimun = min(infiniteList)   #trovo il minimo

        if(minimun==math.inf):  #controllo per uscire dal ciclo
            break
        
        currentNode = infiniteList.index(minimun)  #prendo l'indice del valore minimo
        for node, weight in enumerate(graph[currentNode]):       #ciclo for con ricerca dei nodi collegati a k per indici non ancora esplorati
            if(weight!=0):   #verifico che sia collegato e che non sia se stesso
                newLabel = labelList[currentNode] + weight
                if(newLabel<labelList[node]):
                    labelList[node] = newLabel     #per ogni nuovo nodo sommo (valore label(k)+peso arco di quel nodo) il valore della sua label e controllo se sono minori così sostituisco sennò niente
        
        cntPasso=cntPasso+1
        unexploredNode.remove(currentNode)    #rimuovo l'indice visitato
        
    print("La distanza minore partendo dal nodo %s e arrivando al nodo %s è %s" % (startNode, finishNode, labelList[finishNode]))
    return labelList 

def generaMatrice(adj_dict):
    graph=[]                #inizializzo la matrice
    cntNodi=0               #inizializzo il contatore
    print("Dizionario")
    for chiave, valore in adj_dict.items():
        print("%s --> %s" % (chiave, valore))   #stampo il dizionario a video 
        cntNodi+=1                              #conto il numero di righe/colonne
    print("-------------------------------------------------------------------")
    print("Matrice di adiacenza")
    graph = [[False for x in range(cntNodi)] for y in range(cntNodi)]   #inizializzo la matrice di cntNodi*cntNodi tutta false
    
    for chiave, valore in adj_dict.items(): #scorro il dizionario chiave-valore
        for i in valore:                    #scorro la lista dei nodi collegati
            graph[chiave][i]=True           #se i nodi sono collegati a quel nodo assegno true
    
    print(graph)
    print("----------------------------------------------------------------------")
    return graph
        

print("Inserire il numero del nodo di partenza")
startNode=int(input())
print("Inserire il numero del nodo di arrivo")
finishNode=int(input())

graph=generaMatrice(adj_dict)
dijkstra(graph, startNode, finishNode)