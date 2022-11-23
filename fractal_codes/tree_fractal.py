#importing dependancies
import turtle
import tkinter

#creating a fractal tree
MIN_BRANCH_LENGTH = 5

#create a build tree function
def build_tree(t,branch_length,shorten_by,angle):
    if branch_length> MIN_BRANCH_LENGTH:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        build_tree(t,new_length,shorten_by,angle)

        t.right(angle * 2)
        build_tree(t,new_length,shorten_by,angle)

        t.left(angle)
        t.backward(branch_length)

#make turtle object
tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color("green")

build_tree(tree,50,5,30)
turtle.mainloop()

save_file = turtle.getscreen()
save_file.getcanvas().postscript(file="../Images/tree_fractal.png")



