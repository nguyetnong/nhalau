import turtle

def hinhchunhat(t,toado,ngan,dai,mau_nen, mau_net_but):
    t.penup()
    t.goto(toado)
    t.pendown()
    t.pencolor(mau_net_but)
    t.begin_fill()
    t.fillcolor(mau_nen)
    for i in range(2):
        t.forward(ngan)
        t.right(90)
        t.forward(dai)
        t.right(90)
    t.end_fill()   
        
t=turtle.Turtle()   
t.pensize(3)

hinhchunhat(t,(0,0),90,150,"pink",'blue')
hinhchunhat(t,(30,-50),30,50,"white",'blue')

hinhchunhat(t,(90,0),90,150,"pink",'blue')
hinhchunhat(t,(120,-50),30,50,"white",'blue')

hinhchunhat(t,(90,-150),90,150,"pink",'blue')
hinhchunhat(t,(120,-200),30,50,"white",'blue')

hinhchunhat(t,(0,-150),90,150,"pink",'blue')
hinhchunhat(t,(30,-200),30,50,"white",'blue')

hinhchunhat(t,(180,-150),130,150,"gray",'blue')
hinhchunhat(t,(224,-225),22,75,"dark green",'blue')
hinhchunhat(t,(246,-225),22,75,"dark green",'blue')







        
turtle.done()