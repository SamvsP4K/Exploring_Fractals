import turtle

def koch_curve(t,iterations,length,shortening_factor,angle):
    if iterations == 0:
        flake.forward(length)
    else:
        iterations = iterations - 1
        length = length/ shortening_factor
        koch_curve(flake,iterations,length,shortening_factor,angle)
        flake.left(angle)
        koch_curve(flake,iterations,length,shortening_factor,angle)
        flake.right(angle * 2)
        koch_curve(flake,iterations,length,shortening_factor,angle)
        flake.left(angle)
        koch_curve(flake,iterations,length,shortening_factor,angle)

flake = turtle.Turtle()
flake.hideturtle()
flake.speed("fastest")

for i in range(3):
    koch_curve(flake,4,200,3,60)
    flake.right(120)

turtle.mainloop()