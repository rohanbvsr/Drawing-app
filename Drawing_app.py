import turtle

option = int(input('''Select any one option:
    Press 1 to draw a Circle
    Press 2 to draw a Square
    Press 3 to draw a Rectangle
    Press 4 to draw a Triangle
    Press 5 to draw a Polygon
'''))

color_choice = input('Enter color of your choice: ')

t = turtle.Turtle()
t.color(color_choice) 

if option == 1:
    
    t.begin_fill()
    t.circle(50)
    t.end_fill()

elif option == 2:
  
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()

elif option == 3:
    s1=int(input("enter value of side 1"))
    s2=int(input("enter value of side 2"))
    t.begin_fill()
    
    t.forward(s1)
    t.right(90)
    t.forward(s2)
    t.right(90)
    t.forward(s1)
    t.right(90)
    t.forward(s2)
    t.right(90)
    t.end_fill()

elif option == 4:
     
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

elif option == 5:
    num_sides = int(input("Enter the number of sides for the polygon: "))
    side_length = int(input("Enter the length of each side: "))
    angle = 360 / num_sides
    
    t.begin_fill()
    for _ in range(num_sides):
        t.forward(side_length)
        t.left(angle)
    t.end_fill()





