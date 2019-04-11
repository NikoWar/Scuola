import turtle 
import random

#Nicolò Guerra 4AROB

WIDTH=800           #inizializzazione delle variabili
HEIGHT=600
XSTART=-WIDTH/2
MAXRAND=20
GRADI=90
MOLTIPLICATORE=2       
toggle,cont=0,1

turtle.title("TURTLE RACE")

def calculateY(dist,toggle,cont):        

    origin = 0

    if toggle==0:
        y=origin + dist*cont
        toggle = 1
    else:
        y=origin - dist*cont
        toggle = 0
    
    cont+=1

    return y,toggle,cont

def forward(vettore,players):                
    cont=0
    stop=False
    while True:
        for i in vettore:
            if i.xcor() >= WIDTH//2:
                vincitore=cont
                stop=True
                i.color("red","red")
                break
            i.forward(random.randrange(0,MAXRAND+1))
            cont+=1
        
        if stop:
            break

    return (cont%int(players))


def disegnaContorni():                 #funzione per disegnare partenza e arrivo
    drawer=turtle.Turtle()
    drawer.speed(0)
    drawer.up()
    drawer.goto(XSTART,-HEIGHT/2)
    drawer.down()
    drawer.left(GRADI)
    drawer.forward(HEIGHT)
    drawer.up()
    drawer.goto(WIDTH/2,-HEIGHT/2)
    drawer.down()
    drawer.forward(HEIGHT)
    drawer.hideturtle()



number=input("inserisci il numero di partecipanti: ")
vettoreTurte = []
dist=HEIGHT//(int(number)*MOLTIPLICATORE)     #distanza delle tartarughe l'una dall'altra

disegnaContorni()

for i in range(0,int(number)):
    vettoreTurte.append(turtle.Turtle())

for i in vettoreTurte:                                        #posizionamento turtle
    i.penup()
    i.speed(10)
    y,toggle,cont = calculateY(dist,toggle,cont)
    i.goto((XSTART),y)

vincitore=forward(vettoreTurte,number)

print("ha vinto la tartaruga con indice " + str(vincitore))     

turtle.done()