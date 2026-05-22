import turtle

#Denna har ingen felhanteringe eller liknande gjorde sista lektionen för det var lite kul

print("Detta program ritar andragradare åt dig=) med ekvationen ax^2+bx+c")
a=float(input(print("Vad ska a värdet vara?")))
b=float(input(print("vad ska B värdet vara?")))
c=float(input(print("Vad ska C värdet vara?")))
startx=-float(input(print("Vid vilken x vill du starta och rita den?")))
slutx=float(input(print("Vid vilken x vill du sluta och rita den?")))

t=turtle.Turtle()
t.penup()
t.color('red')

def yvart(a,b,c):
    x=t.xcor()
    ax=a*x**2
    bx=b*x
    y=ax+bx+c
    return(y)


try:
    x=startx
    t.setx(x)
    t.sety(yvart(a,b,c))
    t.pendown()
    while t.xcor()>=startx and t.xcor()<slutx:
        t.setx(x)
        t.sety(yvart(a,b,c)) 
        print(t.xcor(),t.ycor())
        t.setx(x)
        x+=0.1
    
    
except KeyboardInterrupt:
    print("Nu vart det fel")


turtle.done()