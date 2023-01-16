#Point 2

from turtle import * 

# Cachez la souris
hideturtle()

#Cercle 1
begin_fill()
fillcolor("blue")
circle1 = int(input("Sélectionnez votre rayon :"))
circle(circle1)
penup()
goto(100,0)
pendown()
end_fill()

#Cercle 2
begin_fill()
fillcolor("blue")
circle2 = int(input("Sélectionnez votre rayon :"))
circle(circle2)
penup()
goto(100,100)
pendown()
end_fill()

#Cercle 3
begin_fill()
fillcolor("blue")
circle3 = int(input("Sélectionnez votre rayon :"))
circle(circle3)
penup()
goto(0,100)
pendown()
end_fill()

#Cercle 4
begin_fill()
fillcolor("blue")
circle4 = int(input("Sélectionnez votre rayon :"))
circle(circle4)
penup()
goto(100,100)
pendown()
end_fill()
exitonclick()