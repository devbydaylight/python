# Basic pong game in Python 3 for beginners
# From @tokyoedtech youtube series - https://www.youtube.com/watch?v=C6jJg9Zan7w
#
# * == look up subject later for deeper understanding

# We will use turtle graphics for this game so we need to import the appropriate modules
import turtle

# Create a window that the game will run out of
winder = turtle.Screen() # this creates window object
winder.title("Pong by devbydaylight") # creates title for the window when opened
winder.bgcolor("black") # creates background color for the window
winder.setup(width=800, height=600) # creates window size
winder.tracer(0) # stops window from updating, improves speed of the game *


# Paddle 1
paddle_1 = turtle.Turtle() # creates turtle object
paddle_1.speed(0) # sets speed of animation to max speed possible
paddle_1.shape("square") # sets paddle shape to square
paddle_1.color("white") 
paddle_1.penup() # stops turtle from drawing line as object moves *
paddle_1.goto(-350, 0)


# Paddle 2


# Ball


# Main game loop
while True:
    winder.update() # updates the screen every time the loop runs
